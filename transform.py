import os
import pandas as pd

csv_path = os.path.expanduser("raw_survey_data.csv")
data = pd.read_csv(csv_path)

data.dropna(how="all", inplace=True)

data.columns = data.columns.str.lower()

if "timestamp" in data.columns:
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="coerce")

for i in data.columns:
    if i.__contains__("planning on switching"):
        data[i] = data[i].map({"Yes" : 1, "No" : 0, "Maybe" : 0.5})

for j in data.columns:
    if j.__contains__("experience"):
        data = data.fillna({j : 0})

column_mapping = {
    'timestamp': 'timestamp',
    'gender': 'gender',
    'school year': 'school_year',
    'program faculty': 'program_faculty',
    'residence': 'residence',
    'what device do you use the most on campus ?': 'most_used_device',
    'what do you spend the most time on when connected on campus\npreferably one.\nnot more than three': 'most_time_spent_on',
    'how much time do you spend online  per day on campus ?': 'daily_online_time_on_campus',
    'what time are you active the most ? on campus': 'most_active_time_on_campus',
    'what are your primary internet providers on campus ? ': 'primary_internet_providers',
    'what is the main factor for choosing an internet provider ? \npreferably one.\nnot more than two.': 'internet_provider_choice_factors',
    'how much on average do you spend on internet in a month ?': 'monthly_internet_spend',
    'how many gigabytes on average do you use per month': 'monthly_data_usage_gb',
    'satisfaction with internet service on campus': 'campus_internet_satisfaction',
    'frequency of internet connectivity issues on campus': 'internet_issues_frequency',
    'main issues with internet provider\npreferably one\nnot more than two': 'main_internet_issues',
    'rate your experience in afit with the following if any [mtn]': 'mtn_experience_rating',
    'rate your experience in afit with the following if any [airtel]': 'airtel_experience_rating',
    'rate your experience in afit with the following if any [glo]': 'glo_experience_rating',
    'rate your experience in afit with the following if any [9mobile]': 'nine_mobile_experience_rating',
    'rate your experience in afit with the following if any [afit cict]': 'afit_cict_experience_rating',
    'in what way have you been coping with poor service': 'poor_service_coping_methods',
    'has poor internet affected your academics significantly ?': 'academic_impact_of_poor_internet',
    'has poor internet affected your finances significantly?': 'financial_impact_of_poor_internet',
    'are you planning on switching your primary internet provider ?': 'planning_to_switch_provider',
    'do you have any suggestions for addressing the problem of unstable internet in afit ?': 'suggestions_for_improvement'
}

data = data.rename(columns=column_mapping)

transformed_csv_path = "transformed_survey_data.csv"
data.to_csv(transformed_csv_path, index=False)


print(f"Survey data transformed and saved to {transformed_csv_path}")
print(data.columns)