# 🎯 Employee Benefits Compliance Tracker

A Python-based analytics solution for tracking and monitoring employee benefits compliance across organizations. This project demonstrates end-to-end data analytics capabilities including database design, SQL querying, KPI calculation, and automated reporting.

## 🚀 Features

- **Synthetic Data Generation**: Creates realistic employee, enrollment, eligibility, and exception data
- **SQL Analytics**: Uses DuckDB for SQL queries over pandas DataFrames (no external database required)
- **KPI Dashboard**: Calculates key compliance metrics including enrollment rates, exception resolution, and deadline adherence
- **Automated Reporting**: Generates HTML reports and interactive Plotly charts
- **Department Analysis**: Provides department-level compliance benchmarking
- **Colab-Ready**: Runs seamlessly in Google Colab for easy demonstration

## 📊 Key Metrics Tracked

| Metric | Target | Description |
|--------|--------|-------------|
| Enrollment Rate | >95% | Percentage of eligible employees enrolled |
| Exception Resolution Rate | >80% | Percentage of compliance exceptions resolved |
| Deadline Adherence Rate | >90% | Percentage of enrollments completed on time |
| Overall Compliance Score | >85% | Weighted average of all compliance metrics |

## 🛠️ Tech Stack

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **DuckDB**: Embedded SQL analytics engine
- **Plotly**: Interactive data visualizations
- **Streamlit** (optional): Interactive web dashboard

## 📦 Installation

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

1. Open a new Colab notebook: [colab.research.google.com](https://colab.research.google.com)
2. Install dependencies:
```python
!pip install -q duckdb pandas plotly
```
3. Upload `benefits_compliance_tracker.py` or paste the code directly
4. Run the script and download outputs from `/content/output/`

## 🎮 Usage

### Basic Usage

```python
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

## 📈 Sample Outputs

### KPIs Generated
- Overall Compliance Score: 71.59%
- Enrollment Rate: 99.21%
- Exception Resolution Rate: 35.00%
- Deadline Adherence Rate: 80.56%
- Pending Enrollments: 53
- Open Exceptions: 13

### Reports Generated
- `compliance_report.html`: Executive summary dashboard
- `chart_enrollment_status.html`: Enrollment distribution pie chart
- `chart_dept_enrollment_rate.html`: Department comparison bar chart

## 🔍 SQL Queries Included

The project includes ready-to-use SQL queries for:
- Enrollment status summaries
- Overdue enrollment identification
- Department-level compliance analysis
- Exception tracking and resolution monitoring
- Eligibility verification reports

## 💼 Business Impact

This solution helps organizations:
- ✅ Reduce compliance risks and potential penalties
- ✅ Improve employee satisfaction through accurate benefits administration
- ✅ Streamline HR reporting and reduce manual workload
- ✅ Enable data-driven decision making for benefits management
- ✅ Identify and resolve compliance issues proactively

## 🎓 Skills Demonstrated

- Database schema design and normalization
- SQL querying and data aggregation
- Python data analysis with pandas
- KPI calculation and business metrics
- Data visualization and reporting
- ETL pipeline development
- Documentation and code organization

## 📝 Case Study

For a detailed case study of this project, including problem statement, approach, and results, see the project documentation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Rishi Singh**
- LinkedIn: [linkedin.com/in/rishi-singh](https://linkedin.com/in/rishi-singh)
- GitHub: [@Rishisingh1999](https://github.com/Rishisingh1999)

## 🙏 Acknowledgments

Built as a portfolio project to demonstrate business analytics and data engineering capabilities for HR technology applications.

---

⭐ If you found this project helpful, please consider giving it a star!
