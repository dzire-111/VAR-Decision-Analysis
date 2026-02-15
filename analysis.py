import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("data/VAR_Incidents_Stats.csv")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("Dataset Loaded Successfully!\n")

print("Shape of dataset:", df.shape)

print("\nColumns:\n", df.columns)

print("\nTotal VAR Incidents:", len(df))

print("\nIncident Types:\n")
print(df['incident'].value_counts())

print("\nHome vs Away Distribution:\n")
print(df['site'].value_counts())

print("\nVAR Used Distribution:\n")
print(df['var_used'].value_counts())


# Create incident type category
def categorize_incident(text):
    text = text.lower()
    
    if "offside" in text:
        return "Offside"
    elif "penalty" in text:
        return "Penalty"
    elif "handball" in text:
        return "Handball"
    elif "red card" in text:
        return "Red Card"
    elif "foul" in text:
        return "Foul"
    else:
        return "Other"

df['incident_type'] = df['incident'].apply(categorize_incident)

print("\nIncident Type Distribution:\n")
print(df['incident_type'].value_counts())


# Group by team and VAR outcome
team_var_summary = df.groupby(['team', 'var_used']).size().unstack(fill_value=0)

# Create Bias Score (FOR - AGAINST)
team_var_summary['bias_score'] = team_var_summary['FOR'] - team_var_summary['AGAINST']

# Sort by bias score
team_var_summary = team_var_summary.sort_values(by='bias_score', ascending=False)

print("\nTeam VAR Bias Score:\n")
print(team_var_summary)

# Plot Bias Score
plt.figure()
team_var_summary['bias_score'].plot(kind='bar')
plt.title("VAR Bias Score by Team")
plt.xlabel("Team")
plt.ylabel("Bias Score (FOR - AGAINST)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

df.to_csv("data/cleaned_var_data.csv", index=False)

# Home vs Away VAR advantage
home_away_bias = df.groupby(['site', 'var_used']).size().unstack(fill_value=0)

home_away_bias['bias_score'] = home_away_bias['FOR'] - home_away_bias['AGAINST']

print("\nHome vs Away Bias:\n")
print(home_away_bias)

incident_bias = df.groupby(['incident_type', 'var_used']).size().unstack(fill_value=0)

incident_bias['bias_score'] = incident_bias['FOR'] - incident_bias['AGAINST']

print("\nIncident Type Bias:\n")
print(incident_bias)
