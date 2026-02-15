 ## 👤 Author

Desire Sharma  
Aspiring Data Analyst | Interested in Sports Analytics and AI  

# ⚽ VAR Decision Analysis Using AI 

---

## 📌 Project Overview

This project analyzes Video Assistant Referee (VAR) decisions in football matches to identify patterns, trends, and potential bias.

Using Python-based data analysis techniques, this project:

- Extracts structured incident categories from raw match descriptions  
- Quantifies team-level VAR impact  
- Calculates a custom VAR Bias Score  
- Visualizes decision trends using data visualization  

---

## 📊 Dataset Information

The dataset contains 218 recorded VAR incidents with the following fields:

- **Team** – Team involved in the incident  
- **Opponent Team** – Opposing team  
- **Date** – Match date  
- **Site** – Home (H) or Away (A)  
- **Incident** – Text description of the VAR decision  
- **Time** – Match minute of incident  
- **VAR Used** – Whether decision was FOR or AGAINST the team  

Total incidents analyzed: **218**

---

## 🧠 Feature Engineering

The original dataset contained raw textual descriptions of incidents.

To make the dataset analysis-ready, text processing was used to categorize incidents into structured types:

- Offside  
- Penalty  
- Handball  
- Foul  
- Red Card  
- Other  

This transformation enables statistical analysis and future machine learning modeling.

---

## ⚖️ VAR Bias Score

Bias Score = VAR_FOR − VAR_AGAINST

This metric helps identify:

- Teams that benefited most from VAR  
- Teams most negatively impacted  
- Whether decisions are balanced  
- Home vs Away influence patterns  

---

## 📈 Key Insights

- Offside incidents were the most common VAR intervention.  
- VAR decisions were evenly distributed overall (109 FOR vs 109 AGAINST).  
- Some teams show measurable positive or negative bias scores.  
- Home and Away decisions were nearly balanced.  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- Matplotlib  
- VS Code  
- Git & GitHub  

---

## 🚀 Future Improvements

- Build a machine learning model to predict VAR outcomes  
- Create interactive dashboard (Streamlit or Power BI)  
- Expand dataset to multiple leagues/seasons  
- Apply advanced NLP techniques for deeper text classification  

---


