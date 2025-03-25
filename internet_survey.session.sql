
-- @block
SELECT gender, residence FROM survey_responses WHERE residence = "Agric Quarters";

-- @block
SELECT * FROM survey_responses WHERE monthly_data_usage_gb = "10 - 20 GB";

-- @block
SELECT planning_to_switch_provider FROM survey_responses WHERE monthly_data_usage_gb = "Above 40 GB"

