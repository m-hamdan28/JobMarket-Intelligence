import pandas as pd

data = r"C:\Users\hamda\OneDrive\Desktop\OneDrive - FAST National University\Projects\JobMarket-Intelligence\data\raw\data_jobs.csv"
df = pd.read_csv(data)

def clean_data(df):
    df_clean = df.copy()
    df_clean = df_clean.drop_duplicates()
    txt_cols = df_clean.select_dtypes(include="object").columns
    for col in txt_cols:
        df_clean[col] = df_clean[col].apply(
            lambda x: x.strip() if isinstance(x, str) else x
        ) 

    return df_clean

def check_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    return missing

def handle_missing_values(df):
    df_clean = df.copy()
    df_clean = df_clean.dropna(subset=["job_title"])
    columns = ["job_location", "job_via", "job_schedule_type", "job_country", "salary_rate", "salary_year_avg", "salary_hour_avg", "company_name","job_skills", "job_type_skills"]
    for col in columns:
        df_clean[col] = df_clean[col].fillna("unknown")

    return df_clean

def clean_column_names(df):
    df_clean = df.copy()
    df_clean.columns = df_clean.columns.str.strip().str.lower().str.replace(" ", "_")

    return df_clean

def convert_data_types(df):
    df_clean = df.copy()
    s_col = ["salary_year_avg", "salary_hour_avg"]
    for col in s_col:
        df_clean[s_col] = pd.to_numeric(df_clean[col], errors="coerce")

    return df_clean

def clean_skills_data(df):
    df_clean = df.copy()

    df_clean["job_skills"] = df_clean["job_skills"].fillna("")
    df_clean["job_type_skills"] = df_clean["job_type_skills"].fillna("")

    return df_clean

def save_cleaned_data(df, file_path):
    df.to_csv(file_path, index=False)
    print("Cleaned dataset saved successfully!")