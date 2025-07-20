import requests
import time
import pandas as pd
import openmeteo_requests
import requests_cache
from retry_requests import retry

def fetch_eia_hourly_demand(api_key, start_date, end_date, region="ERCO", max_records=30000, page_size=5000, sleep_time=1):
    """
    Fetch hourly electricity demand data from the EIA API.

    Parameters:
        api_key (str): Your EIA API key.
        start_date (str): Start date in format 'YYYY-MM-DDTHH'.
        end_date (str): End date in format 'YYYY-MM-DDTHH'.
        region (str): Region code (default 'ERCO' for ERCOT).
        max_records (int): Maximum number of records to retrieve.
        page_size (int): Number of records per API call.
        sleep_time (int): Seconds to sleep between requests to avoid rate limiting.

    Returns:
        pd.DataFrame: DataFrame of demand data.
    """
    url = "https://api.eia.gov/v2/electricity/rto/region-data/data"
    all_data = []

    for offset in range(0, max_records, page_size):
        params = {
            "api_key": api_key,
            "frequency": "hourly",
            "data[0]": "value",
            "facets[type][]": "D",
            "facets[respondent][]": region,
            "start": start_date,
            "end": end_date,
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "offset": offset,
            "length": page_size
        }

        print(f"Fetching records {offset} to {offset + page_size}...")
        response = requests.get(url, params=params)

        if response.status_code == 200:
            batch = response.json().get("response", {}).get("data", [])
            all_data.extend(batch)
            if len(batch) < page_size:
                break  # No more data to fetch
        else:
            print(f"Failed at offset {offset}")
            print(response.text)
            break

        time.sleep(sleep_time)

    print(f"Total records collected: {len(all_data)}")
    return pd.DataFrame(all_data)




def fetch_weather_data(
    latitude=29.7601,
    longitude=95.3701,
    start_date="2022-01-01",
    end_date="2024-12-31",
    variables=None,
    cache_expiry=3600,
    retries=5,
    backoff=0.2
):
    """
    Fetch hourly weather data from Open-Meteo Historical Forecast API.

    Parameters:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.
        variables (list[str]): List of hourly weather variables to request.
        cache_expiry (int): Cache expiration time in seconds.
        retries (int): Number of retry attempts for failed requests.
        backoff (float): Backoff factor between retries.

    Returns:
        pd.DataFrame: Hourly weather data as a DataFrame.
    """
    if variables is None:
        variables = [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "rain",
            "showers",
            "snowfall",
            "cloud_cover",
            "wind_speed_10m"
        ]

    # Setup Open-Meteo API client with caching and retries
    cache_session = requests_cache.CachedSession('.cache', expire_after=cache_expiry)
    retry_session = retry(cache_session, retries=retries, backoff_factor=backoff)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": variables
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]  # First location/model

    # Parse hourly data
    hourly = response.Hourly()
    timestamps = pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )

    data = {"date": timestamps}
    for i, var in enumerate(variables):
        data[var] = hourly.Variables(i).ValuesAsNumpy()

    return pd.DataFrame(data)
