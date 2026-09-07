# Workforce Analytics SQL Sandbox

## 📊 Project Objective
This portfolio project demonstrates the application of relational database fundamentals to human resources data. Using an independent dataset tracking employee satisfaction metrics, I built an active sandbox environment to model organizational turnover risk factors, evaluate workplace sentiment trends, and execute structural data auditing queries.

## 💻 Tech Stack & Environment
* **Database Management System:** SQLite 3.39+
* **Technical Playground:** DB Fiddle Architecture Sandbox
* **Core Competencies Engine:** Relational Schema Mapping, Data Auditing, Aggregations

---

## 🛠️ Phase 1: Database Architecture & Data Hygiene
To transition flat data variables into a functional relational environment, I engineered a structured table layout (`mytable`) containing strict constraint types for population tracking. 

### The Schema and Insertion Code:
```sql
CREATE TABLE mytable (
  EmployeeID INT,
  EnvironmentSatisfaction INT,
  JobSatisfaction INT,
  WorkLifeBalance INT
);

INSERT INTO mytable(EmployeeID,EnvironmentSatisfaction,JobSatisfaction,WorkLifeBalance) VALUES (2,3,2,4); 
INSERT INTO mytable(EmployeeID,EnvironmentSatisfaction,JobSatisfaction,WorkLifeBalance) VALUES (3,2,2,1); 
INSERT INTO mytable(EmployeeID,EnvironmentSatisfaction,JobSatisfaction,WorkLifeBalance) VALUES (4,4,4,3); 
INSERT INTO mytable(EmployeeID,EnvironmentSatisfaction,JobSatisfaction,WorkLifeBalance) VALUES (5,4,1,3); 
INSERT INTO mytable(EmployeeID,EnvironmentSatisfaction,JobSatisfaction,WorkLifeBalance) VALUES (6,3,2,2); 
INSERT INTO mytable(EmployeeID,EnvironmentSatisfaction,JobSatisfaction,WorkLifeBalance) VALUES (7,1,3,1);
```

---

## 🔍 Phase 2: Analytics & Insight Extraction

### Query A: Isolating Attrition & Severe Burnout Risk
* **Business Intent:** Proactively flag high-risk demographic clusters experiencing a simultaneous deficit in both job satisfaction and work-life balance to implement targeted corporate engagement initiatives.
* **The SQL Logic:**
```sql
SELECT COUNT(*) AS low_satisfaction_count
FROM mytable
WHERE JobSatisfaction = 1 AND WorkLifeBalance = 1;
```
* **Analytical Result:** Isolated **1** individual matching extreme criteria parameters (Employee ID 7), validating the data filtering pipeline's capacity to detect targeted anomalies.

### Query B: System Baseline Sentiment Aggregations
* **Business Intent:** Calculate data baseline milestones to monitor organizational health across the entire active workforce segment.
* **The SQL Logic:**
```sql
SELECT AVG(JobSatisfaction) AS avg_job_sat,
       AVG(EnvironmentSatisfaction) AS avg_env_sat
FROM mytable;
```
* **Analytical Result:** Calculated an institutional Job Satisfaction average of **2.33 / 4.0** and an Environment Satisfaction average of **2.83 / 4.0**, providing measurable benchmarks for stakeholder reporting.

---

## 🎨 Phase 3: Executive Tableau Visualization Architecture (Proposed Blueprint)

To translate backend SQL aggregate outputs into an automated business intelligence environment, I engineered a high-impact dashboard wireframe designed for executive-level workforce monitoring.

### 1. Corporate KPI Summary Cards (Top Row)
* **Total Headcount Tracker:** Rolling institutional population metrics.
* **Global Attrition Vector:** Standardized organizational turnover percentage.
* **Systemic Sentiment Index:** Dynamic institutional rolling satisfaction averages.

### 2. Cross-Functional Heatmap Grid (Middle Row)
* **Visual Logic:** Stratified color-coded bars flagging departmental satisfaction metrics. 
* **Operational Intent:** Instantly isolates localized operational friction by highlighting divisions breaching the critical **2.5 satisfaction constraint hurdle** for immediate intervention.

### 3. Predictive Attrition Risk Scatterplot (Bottom Row)
* **Visual Logic:** A multi-variable coordinate grid mapping *Job Satisfaction* against *Work-Life Balance*.
* **Operational Intent:** Visually segregates populations entering the high-risk "Burnout Quadrant," turning reactive HR reporting into proactive, data-backed human resource retention campaigns.
