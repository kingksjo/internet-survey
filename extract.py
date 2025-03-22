import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = os.path.expanduser("gen-lang-client-0619128938-1e8e0ceb0593.json")

SHEET_ID = ""
SHEET_NAME = "Form Responses 1"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])

gc = gspread.authorize(creds)

sheet = gc.open_by_key(SHEET_ID)
worksheet = sheet.worksheet(SHEET_NAME)
data = worksheet.get_all_records()

df = pd.DataFrame(data)

# Save as CSV
csv_path = "raw_survey_data.csv"
df.to_csv(csv_path, index=False)
print(f"Survey data extracted and saved to {csv_path}")
