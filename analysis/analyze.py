"""Reproducible descriptive analysis of the public IBM HR Attrition dataset."""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
df = pd.read_excel(BASE / "data" / "IBM-HR-Employee-Attrition.xlsx")
df["Left"] = df["Attrition"].eq("Yes").astype(int)

summary = pd.DataFrame([{
    "employees": len(df),
    "employees_left": int(df["Left"].sum()),
    "employees_retained": int((1-df["Left"]).sum()),
    "attrition_rate_pct": round(100 * df["Left"].mean(), 2),
    "avg_monthly_income": round(df["MonthlyIncome"].mean(), 2)
}])
summary.to_csv(BASE / "outputs" / "summary.csv", index=False)

for col, name in [("Department", "department"), ("JobRole", "job_role"),
                  ("OverTime", "overtime"), ("JobSatisfaction", "job_satisfaction"),
                  ("WorkLifeBalance", "work_life_balance")]:
    result = (df.groupby(col, dropna=False)["Left"]
              .agg(employees="size", employees_left="sum", attrition_rate="mean")
              .reset_index())
    result["attrition_rate_pct"] = (result.pop("attrition_rate") * 100).round(2)
    result.to_csv(BASE / "outputs" / f"{name}.csv", index=False)

print(summary.to_string(index=False))
