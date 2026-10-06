# 🛠️ Relational Database Logic & Data Validation Sandbox

### Project Overview
Welcome to my primary data analytics repository. This workspace serves as a practical sandbox where I apply rigorous statistical methodologies to core database management tasks. Moving beyond flat spreadsheets, these projects focus on building structured relational tables, ensuring strict data hygiene, and optimizing queries to track operational performance and compliance. 

### 💼 How This Applies to HRIS & Database Operations
While this project runs in a sandbox environment, the data validation logic and schema mapping rules used here are the exact mechanics needed to manage enterprise HR databases. My main focus here is data hygiene. I built these scripts to ensure that multi-table datasets—like matching a list of employee profiles to their separate payroll files—link up cleanly without creating duplicate records or system errors.


### Core Core Capabilities Demonstrated
* **Relational Database Design (3NF):** Practiced translating flat, messy behavioral and demographic datasets into organized, multi-table relational structures adhering to Third Normal Form (3NF) to completely eliminate data duplication and entry friction.
* **Structural Query Logic & Aggregations:** Authored clean SQL scripts utilizing primary and foreign key relationships, complex `JOIN` statements, conditional filters (`HAVING`, `COUNT`), and grouping rules (`GROUP BY`) to trace specific data distribution trend lines and audit files for formatting errors.
* **Data Cleansing Pipelines:** Integrated Python script loops inside Jupyter Notebooks to parse large datasets, automatically flagging missing entry fields, resolving data anomalies, and standardizing data formatting for seamless business intelligence reporting.
* **Translating Metrics for Stakeholders:** Focused on turning technical database schemas into actionable operational insights, ensuring that raw rows of data are cleanly structured to back up executive-ready visual reporting and dashboards.

### Technical Toolkit Used
* **Languages:** SQL, Python
* **Environments & Libraries:** SQLite, Jupyter Notebooks, Pandas, NumPy
* **Methodologies:** Data Quality Auditing, Schema Mapping, Quantitative Analysis

* # Corporate Workforce Insights & Cohort Attrition Dashboard
### Platform Track: Tableau Cloud Architecture (Cross-Platform Power BI / DAX Framework Transferable)

## 🎯 Executive Project Overview
This business intelligence project houses the end-to-end data transformation pipeline and interactive visualization architecture engineered to track employee lifecycle trends, identify attrition risks, and isolate targeted burnout thresholds. The live dashboard maps and normalizes a multi-variable corporate dataset containing **1,470 records**, completely eliminating reporting friction for executive leadership and HR Operations partners.

## 🛠️ Unified Analytics Stack & Logic
* **Data Layer:** Relational SQL schema design (SQLite / Google BigQuery pipelines) with normalized structures adhering to Third Normal Form (3NF) to ensure absolute data hygiene.
* **Visualization Engine:** Tableau Cloud (Interactive parameters, calculated fields, Level of Detail (LOD) expressions, and conditional color-coded logic pipelines).
* **Cross-Platform Compatibility Architecture:** System logic mapped to mirror data-join topologies used in Microsoft Power BI environments (Power Query data modeling, star-schema table relationships, and calculated measure structures).

## 📊 Core Business Metrics Rendered
1. **Targeted Burnout Threshold Tracker:** An operational matrix filtering multi-tiered behavioral survey indicators against role tenure to signal active retention risks before separation occurs.
2. **Cohort Retention Risk Matrix:** Demographic segmentation matrices providing predictive visibility into multi-member operational units and cross-functional team turnover patterns.
3. **Data Quality Governance Log:** An internal audit dashboard mapping foreign/primary key relationships and eliminating null-value entries across incoming flat files.

## 🔀 Functional Architecture: Tableau to Power BI DAX Mapping
To ensure enterprise scaling and cross-platform flexibility, the core analytical logic engineered into this project’s interactive parameters is built on universal schema principles. The data modeling formulas mirror standard Power BI configurations:

* **Tableau Calculation (User Retention Risk Status):**
  `IF [Burnout Index] > 0.75 AND [Tenure Months] < 12 THEN "High Alert" ELSE "Stable" END`
* **Power BI DAX Equivalent Measure:**
  `Retention_Status = IF(SELECTEDVALUE('WorkforceData'[Burnout Index]) > 0.75 && SELECTEDVALUE('WorkforceData'[Tenure Months]) < 12, "High Alert", "Stable")`

---
### 🔗 Technical Repositories & Execution Files
* View Active Relational Queries: `https://github.com/tifkel2004-rgb/data_analytics_portfolio_TS`
* Access Interactive Tableau Workbook: `https://github.com/users/tifkel2004-rgb/projects/1/views/2`

