import pandas as pd
from sqlalchemy import create_engine

# Establish connection to SmartCity PostgreSQL database
engine = create_engine(
    "postgresql://postgres:postgres@postgres:5432/smartcity_db"
)

# Load processed Parquet data from streaming pipeline
df = pd.read_parquet("/app/data/processed/smartcity")

# Calculate aggregated KPIs per sensor
kpi = (
    df.groupby("sensor_id")
      .agg(
          avg_temperature=("temperature", "mean"),    # Average temperature reading
          avg_co2=("co2", "mean"),                    # Average CO2 level
          avg_traffic=("traffic", "mean"),            # Average traffic count
          events_count=("sensor_id", "count")         # Total number of events
      )
      .reset_index()
)

# Persist KPI metrics to PostgreSQL table
kpi.to_sql(
    "smartcity_kpi",
    engine,
    if_exists="replace",    # Replace existing table
    index=False
)

# Close database connection
engine.dispose()

print("✅ SmartCity KPIs successfully loaded into smartcity_db")