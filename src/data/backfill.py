import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://ercot_user:secret@localhost:5433/ercot")

df = pd.read_csv("data/processed/data.csv", parse_dates=['datetime'])
df.to_sql("demand_data", engine, if_exists="replace", index=False)

print("Data loaded into Postgres.") 