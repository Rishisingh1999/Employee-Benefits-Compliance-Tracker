#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Employee Benefits Compliance Tracker — Python-Only Edition

Run entirely in Python (works in Google Colab, VS Code, or local Python) to:
- Generate or load data (CSV)
- Run SQL over DataFrames using DuckDB (embedded, no external DB)
- Compute KPIs and department analytics
- Export CSVs and an HTML report
- (Optional) Render interactive charts with Plotly and save as HTML

Quick start (Colab):
!pip -q install duckdb plotly pandas
"""

import os
import sys
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

try:
    import duckdb
except ImportError:
    raise SystemExit("Please install duckdb: pip install duckdb")

# Optional visualizations
try:
    import plotly.express as px
    HAS_PLOTLY = True
except Exception:
    HAS_PLOTLY = False

# ------------------------------
# Config
# ------------------------------
SEED = 42
np.random.seed(SEED)
OUT_DIR = os.path.abspath("./output")
DATA_DIR = os.path.join(OUT_DIR, "data")
REPORTS_DIR = os.path.join(OUT_DIR, "reports")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# Toggle synthetic generation vs. loading existing CSVs in ./input
USE_EXISTING_INPUT = False
INPUT_DIR = os.path.abspath("./input")  # Place real org CSVs here with same field names

def save_csv(df: pd.DataFrame, name: str) -> str:
    path = os.path.join(DATA_DIR, name)
    df.to_csv(path, index=False)
    return path

# ------------------------------
# Data: Generate synthetic or load real CSVs
# ------------------------------
if USE_EXISTING_INPUT and os.path.isdir(INPUT_DIR):
    employees_df = pd.read_csv(os.path.join(INPUT_DIR, 'employees_data.csv'))
    departments_df = pd.read_csv(os.path.join(INPUT_DIR, 'departments_data.csv'))
    plans_df = pd.read_csv(os.path.join(INPUT_DIR, 'plans_data.csv'))
    enrollment_df = pd.read_csv(
        os.path.join(INPUT_DIR, 'enrollment_data.csv'),
        parse_dates=["enrollment_date", "election_deadline", "plan_start_date"],
        infer_datetime_format=True
    )
    eligibility_df = pd.read_csv(
        os.path.join(INPUT_DIR, 'eligibility_data.csv'),
        parse_dates=["eligibility_start_date", "eligibility_end_date"],
        infer_datetime_format=True
    )
    exceptions_df = pd.read_csv(
        os.path.join(INPUT_DIR, 'exceptions_data.csv'),
        parse_dates=["exception_date", "resolved_date"],
        infer_datetime_format=True
    )
else:
    # Departments
    departments_df = pd.DataFrame({
        'department_id': [1, 2, 3, 4, 5],
        'department_name': ['Human Resources', 'Finance', 'Engineering', 'Sales', 'Operations']
    })

    # Employees
    n_employees = 150
    employees_df = pd.DataFrame({
        'employee_id': range(1, n_employees + 1),
        'first_name': np.random.choice(['John', 'Jane', 'Michael', 'Sarah', 'Robert', 'Emily', 'James', 'Lisa'], n_employees),
        'last_name': np.random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis'], n_employees),
        'email': [f"user{i}@example.com" for i in range(1, n_employees + 1)],
        'department_id': np.random.choice(departments_df['department_id'], n_employees),
        'hire_date': pd.date_range('2018-01-01', periods=n_employees, freq='W'),
        'employment_status': np.random.choice(['Active', 'Inactive'], n_employees, p=[0.85, 0.15])
    })

    # Plans
    plans_df = pd.DataFrame({
        'plan_id': [1, 2, 3, 4, 5],
        'plan_name': ['Basic Medical', 'Premium Medical', 'Dental Plus', 'Vision Coverage', '401k Plan'],
        'plan_type': ['Medical', 'Medical', 'Dental', 'Vision', 'Retirement'],
        'premium_cost': [300, 600, 75, 50, 150],
        'employer_contribution': [150, 400, 40, 25, 100]
    })

    # Enrollment
    records = []
    for emp_id, status in employees_df[['employee_id', 'employment_status']].itertuples(index=False):
        if status == 'Active':
            num_plans = np.random.randint(2, 5)
            for plan_id in np.random.choice(plans_df['plan_id'], num_plans, replace=False):
                enrollment_date = datetime.now() - timedelta(days=np.random.randint(30, 365))
                election_deadline = enrollment_date + timedelta(days=30)
                enrollment_status = np.random.choice(['Enrolled', 'Pending', 'Declined'], p=[0.80, 0.15, 0.05])
                records.append({
                    'enrollment_id': len(records) + 1,
                    'employee_id': emp_id,
                    'plan_id': plan_id,
                    'enrollment_date': enrollment_date,
                    'election_deadline': election_deadline,
                    'plan_start_date': enrollment_date + timedelta(days=60) if enrollment_status == 'Enrolled' else pd.NaT,
                    'enrollment_status': enrollment_status
                })
    enrollment_df = pd.DataFrame(records)

    # Eligibility
    elig_records = []
    for _, row in employees_df.iterrows():
        elig_records.append({
            'eligibility_id': row.employee_id,
            'employee_id': row.employee_id,
            'eligibility_start_date': pd.to_datetime(row.hire_date),
            'eligibility_end_date': pd.NaT if row.employment_status == 'Active' else (datetime.now() + timedelta(days=30)),
            'benefit_category': 'All_Benefits',
            'is_active': 1 if row.employment_status == 'Active' else 0
        })
    eligibility_df = pd.DataFrame(elig_records)

    # Exceptions
    exc_records = []
    for emp_id in np.random.choice(employees_df['employee_id'], 20, replace=False):
        exception_type = np.random.choice(['Missed Enrollment', 'Late Election', 'Missing Documentation', 'Incorrect Data'])
        exception_date = datetime.now() - timedelta(days=np.random.randint(0, 90))
        resolution_status = np.random.choice(['Open', 'Resolved'], p=[0.6, 0.4])
        exc_records.append({
            'exception_id': len(exc_records) + 1,
            'employee_id': emp_id,
            'exception_type': exception_type,
            'exception_date': exception_date,
            'severity_level': np.random.choice(['Critical', 'High', 'Medium', 'Low']),
            'resolution_status': resolution_status,
            'resolved_date': exception_date + timedelta(days=np.random.randint(1, 30)) if resolution_status == 'Resolved' else pd.NaT
        })
    exceptions_df = pd.DataFrame(exc_records)

# Persist CSVs for artifacts
def export_all():
    paths = {
        'employees': save_csv(employees_df, 'employees_data.csv'),
        'departments': save_csv(departments_df, 'departments_data.csv'),
        'plans': save_csv(plans_df, 'plans_data.csv'),
        'enrollment': save_csv(enrollment_df, 'enrollment_data.csv'),
        'eligibility': save_csv(eligibility_df, 'eligibility_data.csv'),
        'exceptions': save_csv(exceptions_df, 'exceptions_data.csv'),
    }
    return paths

paths = export_all()

print("Data files exported successfully!")
print(f"Total employees: {len(employees_df)}")
print(f"Total enrollments: {len(enrollment_df)}")
print(f"Total exceptions: {len(exceptions_df)}")


# ------------------------------
# SQL over DataFrames with DuckDB
# ------------------------------
con = duckdb.connect(database=':memory:')
con.register('employees', employees_df)
con.register('departments', departments_df)
con.register('benefits_plans', plans_df)
con.register('benefits_enrollment', enrollment_df)
con.register('employee_eligibility', eligibility_df)
con.register('compliance_exceptions', exceptions_df)

print("\nRunning SQL queries...")

q_enrollment_status = con.execute("""
    SELECT enrollment_status, COUNT(*) AS ct
    FROM benefits_enrollment
    GROUP BY 1
    ORDER BY 2 DESC
""").df()

q_overdue = con.execute("""
    SELECT e.employee_id, e.first_name || ' ' || e.last_name AS employee_name,
           d.department_name, be.plan_id, be.enrollment_date, be.election_deadline
    FROM employees e
    JOIN benefits_enrollment be USING(employee_id)
    JOIN departments d ON e.department_id = d.department_id
    WHERE be.election_deadline < CURRENT_DATE
      AND be.enrollment_status <> 'Enrolled'
    ORDER BY be.election_deadline
""").df()

q_dept_overview = con.execute("""
    WITH enrolled AS (
      SELECT DISTINCT employee_id
      FROM benefits_enrollment
      WHERE enrollment_status = 'Enrolled'
    )
    SELECT d.department_name,
           COUNT(DISTINCT e.employee_id) AS total_employees,
           COUNT(DISTINCT en.employee_id) AS enrolled_employees,
           ROUND(COUNT(DISTINCT en.employee_id) * 100.0 / NULLIF(COUNT(DISTINCT e.employee_id),0), 2) AS enrollment_rate,
           COUNT(DISTINCT CASE WHEN ce.resolution_status = 'Open' THEN ce.exception_id END) AS open_exceptions
    FROM departments d
    LEFT JOIN employees e ON d.department_id = e.department_id
    LEFT JOIN enrolled en ON e.employee_id = en.employee_id
    LEFT JOIN compliance_exceptions ce ON e.employee_id = ce.employee_id
    GROUP BY 1
    ORDER BY enrollment_rate DESC NULLS LAST
""").df()

print("SQL queries completed!")

# KPIs in Python
active_employees = employees_df[employees_df['employment_status'] == 'Active']['employee_id'].nunique()
enrolled_unique = enrollment_df[enrollment_df['enrollment_status'] == 'Enrolled']['employee_id'].nunique()
pendings = (enrollment_df['enrollment_status'] == 'Pending').sum()

enrollment_rate = (enrolled_unique / active_employees * 100) if active_employees else 0

overdue_count = (
    enrollment_df[
        (enrollment_df['election_deadline'].dt.date < datetime.now().date()) &
        (enrollment_df['enrollment_status'] != 'Enrolled')
    ].shape[0]
)

open_ex = (exceptions_df['resolution_status'] == 'Open').sum()
resolved_ex = (exceptions_df['resolution_status'] == 'Resolved').sum()
exception_resolution_rate = (resolved_ex / (open_ex + resolved_ex) * 100) if (open_ex + resolved_ex) else 0

deadline_adherence_rate = ((len(enrollment_df) - overdue_count) / len(enrollment_df) * 100) if len(enrollment_df) else 0
overall_compliance_score = float(np.mean([enrollment_rate, exception_resolution_rate, deadline_adherence_rate]))

kpi_df = pd.DataFrame({
    'metric': ['Enrollment Rate', 'Exception Resolution Rate', 'Deadline Adherence Rate', 'Overall Compliance Score', 'Pending Enrollments', 'Open Exceptions'],
    'value': [round(enrollment_rate,2), round(exception_resolution_rate,2), round(deadline_adherence_rate,2), round(overall_compliance_score,2), int(pendings), int(open_ex)]
})

save_csv(q_enrollment_status, 'enrollment_status_summary.csv')
save_csv(q_overdue, 'overdue_enrollments.csv')
save_csv(q_dept_overview, 'department_overview.csv')
save_csv(kpi_df, 'kpis.csv')

print("\nKPIs calculated and saved!")
print(f"Overall Compliance Score: {overall_compliance_score:.2f}%")
print(f"Enrollment Rate: {enrollment_rate:.2f}%")
print(f"Exception Resolution Rate: {exception_resolution_rate:.2f}%")
print(f"Deadline Adherence Rate: {deadline_adherence_rate:.2f}%")

# ------------------------------
# Minimal HTML report
# ------------------------------
report_html = f'''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Benefits Compliance Tracker — Report</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    h1, h2 {{ color: #0b245b; }}
    .kpi {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
    .card {{ background: #0b245b; color: #fff; padding: 16px; border-radius: 8px; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; }}
    th {{ background: #f0f2f5; text-align: left; }}
  </style>
</head>
<body>
  <h1>Employee Benefits Compliance Tracker</h1>
  <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
  <h2>Key Metrics</h2>
  <div class="kpi">
    <div class="card"><strong>Enrollment Rate</strong><br/>{enrollment_rate:.2f}%</div>
    <div class="card"><strong>Exception Resolution</strong><br/>{exception_resolution_rate:.2f}%</div>
    <div class="card"><strong>Deadline Adherence</strong><br/>{deadline_adherence_rate:.2f}%</div>
    <div class="card"><strong>Compliance Score</strong><br/>{overall_compliance_score:.2f}%</div>
    <div class="card"><strong>Pending Enrollments</strong><br/>{pendings}</div>
    <div class="card"><strong>Open Exceptions</strong><br/>{open_ex}</div>
  </div>
  <h2>Enrollment Status Summary</h2>
  {q_enrollment_status.to_html(index=False)}
  <h2>Department Overview</h2>
  {q_dept_overview.to_html(index=False)}
  <h2>Overdue Enrollments</h2>
  {q_overdue.head(25).to_html(index=False)}
</body>
</html>
'''

report_path = os.path.join(REPORTS_DIR, 'compliance_report.html')
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_html)

print(f"\nHTML report generated: {report_path}")

# ------------------------------
# Optional: Interactive Charts
# ------------------------------
if HAS_PLOTLY:
    try:
        px.pie(q_enrollment_status, names='enrollment_status', values='ct',
               title='Enrollment Status Distribution')\
          .write_html(os.path.join(REPORTS_DIR, 'chart_enrollment_status.html'))
        px.bar(q_dept_overview, x='department_name', y='enrollment_rate',
               title='Enrollment Rate by Department')\
          .write_html(os.path.join(REPORTS_DIR, 'chart_dept_enrollment_rate.html'))
        print("Interactive charts generated!")
    except Exception as e:
        print(f"Chart generation skipped: {e}")

print("\n" + "="*50)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("="*50)
print(f"\nAll outputs saved to: {OUT_DIR}")
print("\nNext steps:")
print("1. Review generated CSV files in output/data/")
print("2. Open compliance_report.html in your browser")
print("3. Run 'streamlit run app.py' for interactive dashboard (if available)")
