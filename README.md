# GRIDWISE

*A machine learning project to predict short/long-tern electricity demand in the ERCOT Grid.*


## **Table of Contents**
1. Project Overview
2. Key Features
3. Data Sources
4. Tech Stack
5. Installation
6. Project Structure
7. Usage
8. Results

## Project Overview

**Goal**: Create an end to end pipeline to forecast ERCOT Electricity demand (hourly/day ahead) using historical load and weather data.

We prioritize simplicity and interpretability first, then incrementally introduce model complexity:  

*Seasonal Naive -> Exponential Smoothing -> Winter-Holts -> SARIMAX -> Prophet -> TBATS -> XGBoost -> LSTM , NBEATS*

**Selection Criteria**:  
- Performance (RMSE/MAE) > Interpretability  
- Best model will be deployed regardless of complexity.  


Ultimately, the goal is to study the intuitive connection between weather and energy demand, however the final model might exclude weather depending or not if weather effects performance.

**Deployment**


We then want to be able to deploy our model within an environment as a proof of concept; furthermore, we will create an API so insights can be directly and easily accessed.

## Key Features
**Data Pipeline**: Automated ETL for ERCOT demand + Open-Meteo weather data.

**Feature Engineering**: Lagged variables, rolling averages

**Model Comparisons**: RMSE/MAE metrics across models.

**Visualization**: Interactive Plotly dashboards or Matplotlib plots.

**Deployment**: API and APP to interface with insights and forecasting.



## Project Structure
```
├── app
│   └── main.py
├── config
│   └── airflow.cfg
├── dags
│   ├── ingest_pipeline.py
│   └── retrain_pipeline.py
├── data
│   ├── processed
│   │   └── data.csv
│   └── raw
│       ├── EIA_Demand.csv
│       ├── open_meteo.csv
│       └── test.csv
├── docker
│   ├── dockerfile.airflow
│   └── dockerfile.api
├── docker-compose.yml
├── LICENSE
├── logs
├── notebooks
│   ├── EDA.ipynb
│   └── modeling.ipynb
├── plugins
├── README.md
├── requirements.txt
├── sql
│   └── solar_schema.sql
├── src
│   ├── __init__.py
│   └── data
│       ├── __init__.py
│       └── fetch_data.py
└── utils
    ├── demand_utils.py
    └── weather_api.py

```



