# GRIDWISE




```md
SUNWISE/
├── data/
│   ├── raw/                    # Weather + solar generation data
│   └── processed/              # Feature engineered data
├── airflow_dags/
│   └── ingest_pipeline.py      # Ingest + store pipeline
│   └── retrain_pipeline.py     # Retraining DAG
├── notebooks/
│   └── analysis_modeling.ipynb # Model exploration and training
├── app/
│   ├── main.py                 # FastAPI app to serve model
│   └── model.pkl               # Trained model
├── utils/
│   ├── weather_api.py          # Live weather data ingestion
│   ├── solar_utils.py          # Solar feature calculations
├── docker/
│   └── Dockerfile.api          # For FastAPI app
│   └── Dockerfile.airflow      # For Airflow
├── sql/
│   └── solar_schema.sql        # PostgreSQL schema
├── requirements.txt
├── docker-compose.yml
└── README.md

```
