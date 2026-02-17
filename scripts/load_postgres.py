import argparse
import pandas as pd
from sqlalchemy import create_engine

# Parse argument for dynamic input path
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="Parquet input path")
args = parser.parse_args()

# Establish connection to SmartCity PostgreSQL database
engine = create_engine(
    "postgresql://postgres:postgres@postgres:5432/smartcity_db"
)

# Load processed Parquet data from dynamic path
df = pd.read_parquet(args.input)

# Filter dummy records generated at producer startup
df = df[df["sensor_id"] != "DUMMY-INIT"]

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
    if_exists="append",     # Append to keep historical data
    index=False
)

# Close database connection
engine.dispose()

print(f"✅ SmartCity KPIs successfully loaded from {args.input} into smartcity_db")