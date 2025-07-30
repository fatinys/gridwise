from prophet import Prophet
import pandas as pd
import os
from datetime import datetime

def forecast(df, forecast_horizon = 12, freq='H'):
    df = df.rename(columns={'timestamp': 'ds', 'demand-mwh': 'y'})
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=forecast_horizon, freq=freq)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]