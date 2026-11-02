# HR Attrition Analytics | Employee Retention Insights

![Python](https://img.shields.io/badge/Python-Analytics-3776AB?logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas) ![HR Analytics](https://img.shields.io/badge/Focus-Employee%20Retention-16817A)

**Author:** Mohammed Labaran Halliru  
**Portfolio focus:** Data Analytics · Business Intelligence · Workforce Analytics

## Project Overview

A reproducible exploratory analysis of employee attrition using the public IBM HR Analytics sample dataset. The project examines employee departures across departments, job roles, overtime status, job satisfaction, and work-life balance to identify patterns that could inform retention research.

> This is a sample dataset and not real IBM employee records. The analysis is descriptive; associations do not establish causal drivers of attrition.

## Dataset KPIs

| Metric | Result |
|---|---:|
| Employee records | 1,470 |
| Employees who left | 237 |
| Employees retained | 1,233 |
| Attrition rate | 16.12% |
| Retention rate | 83.88% |
| Average monthly income | $6,502.93 |

## Questions Explored

- Which departments and job roles have higher observed attrition rates?
- How do departure rates differ for employees working overtime?
- How does attrition vary by job satisfaction and work-life balance scores?
- Which patterns merit further investigation by HR leaders?

## Analysis Workflow

```mermaid
flowchart LR
    A[Public IBM HR sample workbook] --> B[Python and pandas]
    B --> C[Validate employee counts]
    C --> D[Calculate segment attrition rates]
    D --> E[CSV summaries]
    E --> F[Business interpretation]
```

## How to Run

Install Python 3.10+ and run:

```bash
pip install -r requirements.txt
python analysis/analyze.py
```

Results are written to `outputs/` as CSV files. Review the generated segment summaries to identify patterns and check sample sizes before drawing conclusions.

## Selected Findings

- 237 of 1,470 employees are labeled as having left, corresponding to a 16.12% attrition rate.
- The analysis provides group-level attrition rates by department, role, overtime, satisfaction, and work-life balance.
- Smaller groups should be interpreted cautiously; rates are descriptive and not forecasts.

## Repository Structure

```text
HR-Attrition-Analytics-Mohammed-Halliru/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── IBM-HR-Employee-Attrition.xlsx
├── analysis/
│   └── analyze.py
└── outputs/
    ├── summary.csv
    ├── department.csv
    ├── job_role.csv
    ├── overtime.csv
    ├── job_satisfaction.csv
    └── work_life_balance.csv
```

## Limitations and Responsible Use

This public sample is suitable for learning and demonstration, not employment decisions. It does not establish why any individual left, and it should not be used to make individual employment or hiring decisions. Sensitive characteristics should not be used to discriminate against employees.

## Data Credit

Dataset: [IBM HR Analytics Employee Attrition & Performance (Kaggle)](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset). Dataset ownership is not claimed. The Python analysis and this repository documentation were newly prepared for this portfolio package; third-party dashboards and notebooks supplied as references are not included.

## Contact

[LinkedIn](https://www.linkedin.com/in/mohammed-labaran-halliru/)
