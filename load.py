import sqlite3
import pandas as pd
import os

db_path = os.path.expanduser("/mnt/c/Users/Kamiye/Documents/internet-survey/survey_data.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

table_name = "survey_responses"

create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    gender TEXT,
    school_year TEXT,
    program_faculty TEXT,
    residence TEXT,
    most_used_device TEXT,
    most_time_spent_on TEXT,
    daily_online_time_on_campus TEXT,
    most_active_time_on_campus TEXT,
    primary_internet_providers TEXT,
    internet_provider_choice_factors TEXT,
    monthly_internet_spend REAL,
    monthly_data_usage_gb REAL,
    campus_internet_satisfaction INTEGER,
    internet_issues_frequency INTEGER,
    main_internet_issues TEXT,
    mtn_experience_rating INTEGER,
    airtel_experience_rating INTEGER,
    glo_experience_rating INTEGER,
    nine_mobile_experience_rating INTEGER,
    afit_cict_experience_rating INTEGER,
    poor_service_coping_methods TEXT,
    academic_impact_of_poor_internet TEXT,
    financial_impact_of_poor_internet TEXT,
    planning_to_switch_provider TEXT,
    suggestions_for_improvement TEXT
);
"""

cursor.execute(create_table_query)

transformed_csv_path = os.path.expanduser("transformed_survey_data.csv")
data = pd.read_csv(transformed_csv_path)

data.to_sql(table_name, conn, if_exists="append", index=False)

conn.commit()
conn.close()

print(f"Data successfully loaded into SQLite database in Windows and is ready for analysis")