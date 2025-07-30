CREATE TABLE demand_data (
    timestamp TIMESTAMP PRIMARY KEY,
    demand_mwh DOUBLE PRECISION
);

CREATE TABLE weather_forecast (
    timestamp TIMESTAMP,
    temperature_2m DOUBLE PRECISION,
    relative_humidity_2m DOUBLE PRECISION,
    rain DOUBLE PRECISION,
    showers DOUBLE PRECISION,
    snowfall DOUBLE PRECISION,
    cloud_cover DOUBLE PRECISION,
    PRIMARY KEY (timestamp)
);

