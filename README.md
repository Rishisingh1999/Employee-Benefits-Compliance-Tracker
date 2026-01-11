# 🎯 Employee Benefits Compliance Tracker

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)

*A Python-based analytics solution for tracking and monitoring employee benefits compliance across organizations. Features SQL analytics, automated KPI calculations, and interactive dashboards for HR compliance management.*

---

## ✨ Project Overview

This HR analytics project, developed as part of a **personal portfolio initiative** in **November 2025**, demonstrates end-to-end data analytics capabilities for compliance monitoring. The project showcases expertise in:

- 📊 **SQL Analytics** with DuckDB
- 💾 **Database Design** and data modeling
- 📈 **KPI Calculation** and metrics tracking
- 🎨 **Data Visualization** with Plotly
- 🤖 **Automated Reporting** systems

### 🎯 Key Objectives

- 📉 **Track enrollment rates** across departments
- 🔍 **Monitor compliance exceptions** and resolution
- ⏱️ **Analyze deadline adherence** for timely enrollments
- 📊 **Generate automated reports** for stakeholders
- 🏆 **Benchmark department performance** against targets

---

## 🚀 Features

### 📊 Core Capabilities

- **Synthetic Data Generation**: Creates realistic employee, enrollment, eligibility, and exception data
- **SQL Analytics**: Uses DuckDB for SQL queries over pandas DataFrames (no external database required)
- **KPI Dashboard**: Calculates key compliance metrics including enrollment rates, exception resolution, and deadline adherence
- **Automated Reporting**: Generates HTML reports and interactive Plotly charts
- **Department Analysis**: Provides department-level compliance benchmarking
- **Colab-Ready**: Runs seamlessly in Google Colab for easy demonstration

### 📈 Key Metrics Tracked

| Metric | Target | Description |
|--------|--------|-------------|
| **Enrollment Rate** | >95% | Percentage of eligible employees enrolled |
| **Exception Resolution Rate** | >80% | Percentage of compliance exceptions resolved |
| **Deadline Adherence Rate** | >90% | Percentage of enrollments completed on time |
| **Overall Compliance Score** | >85% | Weighted average of all compliance metrics |

---

## 🛠️ Technical Stack

### 💻 Core Technologies

- **Language:** Python 3.8+
- **Data Analysis:** Pandas, NumPy
- **Database:** DuckDB (embedded SQL engine)
- **Visualization:** Plotly
- **Optional Dashboard:** Streamlit

### 📚 Key Libraries

| Library | Purpose |
|---------|----------|
| **Pandas** | Data manipulation and analysis |
| **DuckDB** | Embedded SQL analytics engine |
| **Plotly** | Interactive data visualizations |
| **Faker** | Synthetic data generation |
| **Streamlit** | Optional interactive web dashboard |

### 🧪 Skills Demonstrated

- ✅ Database schema design and normalization
- ✅ SQL querying and data aggregation
- ✅ Python data analysis with pandas
- ✅ KPI calculation and business metrics
- ✅ Data visualization and reporting
- ✅ ETL pipeline development
- ✅ Documentation and code organization

---

## 💻 Installation

### Local Setup

```bash
# Clone the repository
git clone https://github.com/Rishisingh1999/Employee-Benefits-Compliance-Tracker.git
cd Employee-Benefits-Compliance-Tracker

# Install dependencies
pip install -r requirements.txt

# Run the main script
python benefits_compliance_tracker.py
```

### Google Colab Setup

1. Open a new Colab notebook: [colab.research.google.com](https://colab.research.google.com/)
2. Install dependencies:

```bash
!pip install -q duckdb pandas plotly
```

3. Upload `benefits_compliance_tracker.py` or paste the code directly
4. Run the script and download outputs from `/content/output/`

---

## 🎮 Usage

### Basic Usage

```bash
# Run the complete analysis
python benefits_compliance_tracker.py
```

The script will:

1. Generate synthetic data (or load from `input/` if available)
2. Execute SQL queries for compliance analytics
3. Calculate KPIs and department metrics
4. Export CSV files to `output/data/`
5. Generate HTML report in `output/reports/`

### Interactive Dashboard (Optional)

```bash
# Run the Streamlit app
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

---

## 📈 Sample Outputs

### 📊 KPIs Generated

- **Overall Compliance Score:** 71.59%
- **Enrollment Rate:** 99.21%
- **Exception Resolution Rate:** 35.00%
- **Deadline Adherence Rate:** 80.56%
- **Pending Enrollments:** 53
- **Open Exceptions:** 13

### 📄 Reports Generated

- `compliance_report.html`: Executive summary dashboard
- `chart_enrollment_status.html`: Enrollment distribution pie chart
- `chart_dept_enrollment_rate.html`: Department comparison bar chart

### 📊 Visualizations

The project generates:

- 🥧 **Pie Charts** - Enrollment status distribution
- 📉 **Bar Charts** - Department-level comparisons
- 📊 **Line Charts** - Trends over time
- 🗃️ **Tables** - Detailed KPI breakdowns

---

## 🔍 SQL Queries Included

The project includes ready-to-use SQL queries for:

- 📊 **Enrollment status summaries**
- ⏰ **Overdue enrollment identification**
- 🏭 **Department-level compliance analysis**
- 🚫 **Exception tracking and resolution monitoring**
- ✅ **Eligibility verification reports**

### Sample SQL Query

```sql
-- Calculate department enrollment rates
SELECT 
  department,
  COUNT(DISTINCT employee_id) as total_employees,
  SUM(CASE WHEN enrollment_status = 'Enrolled' THEN 1 ELSE 0 END) as enrolled,
  ROUND(100.0 * enrolled / total_employees, 2) as enrollment_rate
FROM employees e
LEFT JOIN enrollments en ON e.employee_id = en.employee_id
GROUP BY department
ORDER BY enrollment_rate DESC;
```

---

## 💼 Business Applications

### 🎯 Use Cases

- **HR Departments:** Monitor benefits enrollment compliance
- **Compliance Officers:** Track regulatory adherence
- **C-Suite Executives:** High-level compliance dashboards
- **Benefits Administrators:** Identify enrollment issues
- **Auditors:** Generate compliance audit reports

### 📈 Value Proposition

This solution helps organizations:

- ✅ **Reduce compliance risks** and potential penalties
- ✅ **Improve employee satisfaction** through accurate benefits administration
- ✅ **Streamline HR reporting** and reduce manual workload
- ✅ **Enable data-driven decision making** for benefits management
- ✅ **Identify and resolve** compliance issues proactively
- ✅ **Benchmark performance** across departments

---

## 📁 Project Structure

```
Employee-Benefits-Compliance-Tracker/
├── benefits_compliance_tracker.py  # Main script
├── app.py                          # Streamlit dashboard (optional)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── input/                          # Input data folder (optional)
└── output/                         # Generated outputs
    ├── data/                       # Exported CSV files
    └── reports/                    # HTML reports and charts
```

---

## 🔑 Key Insights

### 📈 Analysis Highlights

Based on the synthetic data analysis, the tracker identifies:

1. **High Enrollment Rate (99.21%)**: Strong overall participation
2. **Low Exception Resolution (35%)**: Improvement needed in handling exceptions
3. **Good Deadline Adherence (80.56%)**: Most enrollments completed on time
4. **Department Variations**: Significant differences in compliance across departments

### 💡 Actionable Recommendations

- 🎯 Focus resources on resolving open compliance exceptions
- 🚫 Investigate departments with lower enrollment rates
- ⏱️ Implement reminders for deadline adherence
- 📊 Establish regular compliance review cycles

---

## 🎓 Skills Highlighted

This project demonstrates proficiency in:

- **Data Engineering:** ETL pipeline design and implementation
- **SQL Expertise:** Complex queries and aggregations
- **Python Programming:** Pandas, data manipulation
- **Analytics:** KPI calculation and metrics tracking
- **Visualization:** Plotly charts and dashboards
- **Business Acumen:** Translating data into actionable insights
- **Documentation:** Professional project presentation

---

## 🔮 Future Enhancements

- ☁️ **Cloud Integration:** AWS/Azure deployment
- 📧 **Email Alerts:** Automated notifications for compliance issues
- 🤖 **ML Predictions:** Forecast compliance risks
- 🔄 **Real-time Monitoring:** Live dashboard updates
- 📱 **Mobile App:** iOS/Android compliance tracking
- 🔗 **API Integration:** Connect with HRIS systems

---

## 📧 Contact

**Hrushikesh Singh**

- 📧 Email: hrushisingh697@gmail.com
- 💼 LinkedIn: [linkedin.com/in/hrushikesh-singh](https://www.linkedin.com/in/hrushikesh-singh-564b4035a)
- 🐙 GitHub: [@Rishisingh1999](https://github.com/Rishisingh1999)
- 🌐 Portfolio: [rishisingh1999.github.io/my-portfolio-website](https://rishisingh1999.github.io/my-portfolio-website/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Attribution appreciated** 🙏

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 🙏 Acknowledgments

Built as a portfolio project to demonstrate business analytics and data engineering capabilities for HR technology applications.

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!

**Built with ❤️ for HR Analytics & Compliance Management**

---
