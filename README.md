  # 👥 Workforce Analytics & Relational SQL Optimization Sandbox

## 📋 Project Architecture Overview
This deep-dive data analytics project transitions unorganized, flat-file employee survey profiles out of disconnected spreadsheets into an optimized relational database environment. By engineering a structured SQLite schema, this project establishes rigorous data governance pipelines to track organizational health, identify performance friction, and isolate workforce retention risk factors.

This project simulates enterprise-level human resource information system (HRIS) operations, translating raw qualitative workforce narratives into scalable, structured query arrays.

---

## 🛠️ Technical Stack & Operational Matrix
* **Database Infrastructure:** Relational SQLite Database Framework.
* **Core Optimization Logic:** Structured schema normalization, Primary/Foreign Key relational mapping, and column-level indexing.
* **Analytical Query Layer:** Multi-table structural `JOIN` operations, Common Table Expressions (`CTEs`), and conditional aggregate grouping mechanics.
* **Key Performance Telemetry:** Data extraction using `SELECT`, `COUNT`, `GROUP BY`, `HAVING`, and `ORDER BY` filters.

---

## 🔬 Relational Optimization Sprints & Engineering Patches

### 📊 Sprint 1: Normalization of Flat Employee Matrix Layouts
* **The System Hurdle:** Employee demographic records, project allocations, and survey responses originally existed as flat, repeating rows inside a single matrix, causing significant data redundancy, slow processing constraints, and high entry risk.
* **The Engineering Fix:** Normalized the flat database structure by breaking it into distinct relational entity tables: `Employees`, `Departments`, and `SurveyResponses`, cleanly mapped via structured foreign key routing logic.

```sql
-- Validating relational table creation and database integrity mapping
CREATE TABLE SurveyResponses (
    ResponseID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    BurnoutMetricID INTEGER,
    SatisfactionScore INTEGER,
    SurveyTimestamp TEXT,
    FOREIGN KEY(EmployeeID) REFERENCES Employees(EmployeeID)
);
```

### 🎯 Sprint 2: Isolating High-Risk Retention Cohorts
* **The Analytics Hurdle:** Tracking individual, erratic sentiment shifts across high-volume surveys provides zero scalable value to executive stakeholders. The business required an enterprise framework to group macro-level trends and identify specific departments under high operational stress.
* **The Engineering Fix:** Refactored the computational layer utilizing `GROUP BY` and conditional `HAVING` filters to isolate department segments experiencing elevated burnout trends (scores above an established threshold of 8), tracking metrics for a core cohort of **570+ participants**.

```sql
-- Advanced multi-table aggregation isolating targeted departmental retention risks
SELECT 
    d.DepartmentName,
    COUNT(e.EmployeeID) AS ImpactedEmployeeCount,
    ROUND(AVG(s.SatisfactionScore), 2) AS AverageSatisfactionRating
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID
INNER JOIN SurveyResponses s ON e.EmployeeID = s.EmployeeID
WHERE s.BurnoutMetricID >= 8
GROUP BY d.DepartmentName
HAVING COUNT(e.EmployeeID) > 5
ORDER BY ImpactedEmployeeCount DESC;
```

---

## 💡 Strategic Corporate Takeaways & ROI Impact

1. **Enterprise Data Governance:** Engineered clean, normalized database structures that transition unstructured human narratives into relational tabular arrays, significantly shortening onboarding data cleansing lifecycles.
2. **Actionable Retention Analytics:** Isolated departmental friction points early, delivering precise metrics to leadership teams to mitigate employee turnover. This methodology directly mirrors workflows utilized to secure a **100% team retention rate** during live workforce tracking operations.
3. **Scalable System Architecture:** Built reusable, high-performance query templates capable of processing continuous data streams within standard corporate analytics tracking software.


---
# 📊 Global Air Quality Framework & Relational Data Integrity

## 📋 Project Overview
This data analytics project leverages **Google BigQuery** and **SQL** to programmatically interface with large-scale, multi-variable open-source datasets managed by OpenAQ. The primary objective is to engineer high-efficiency relational data queries, isolate standardized units of measurement across international borders, and establish data integrity frameworks for baseline environmental monitoring.

By bypassing local computing restrictions and utilizing cloud-based schemas, this project demonstrates an analytical approach to structuring raw cloud databases into clean, report-ready corporate datasets.

---

## 🛠️ Technical Toolkit & Methodologies
* **Language & Interface:** SQL (Google BigQuery dialect) paired with Python integration.
* **Environment Architecture:** Specialized cloud Client schemas via `google.cloud.bigquery`.
* **Data Processing Libraries:** Pandas (for DataFrame transformations and structured table rendering).
* **Core Competencies:** Relational database structures, field filtration (`WHERE`), data deduplication (`DISTINCT`), and schema evaluation.

---

## 🔬 Analytical Project Phases

### 🌐 Phase 1: Isolating International Reporting Metrics
* **Objective:** Map international reporting compliance by isolating target measurement categories across disparate reporting networks.
* **SQL Implementation:** 
  ```sql
  SELECT DISTINCT country
  FROM `bigquery-public-data.openaq.global_air_quality`
  WHERE unit = 'ppm'
  ```
* **Business Insight:** Identified structural anomalies across international reporting borders, uncovering exactly which tracking networks require specific metric standardization strategies to maintain global reporting consistency.

### 🎯 Phase 2: Establishing Baseline Clean-Air Controls
* **Objective:** Filter massive multi-variable data tables to identify absolute control points (`value = 0`) across global reporting stations.
* **SQL Implementation:**
  ```sql
  SELECT *
  FROM `bigquery-public-data.openaq.global_air_quality`
  WHERE value = 0
  ```
* **Business Insight:** Developed a functional dataset subset to establish clean baseline control zones, allowing organizations to dynamically measure environmental variance over time against verified clean-air thresholds.

---

## 💡 Key Strategic Takeaways
1. **Relational Scalability:** Demonstrated the ability to manage end-to-end data integrity pipelines on live, population-scale databases by deploying query-safety safety constraints (`maximum_bytes_billed`).
2. **Data Normalization:** Highlighted the absolute necessity of structuring disparate reporting boundaries (such as managing discrepancies between metric units) before executing high-level corporate insights or modeling.
3. **Automated Insights:** Built a foundational architecture that transforms raw, unorganized cloud rows into concise tabular frameworks ready for executive-level presentations or further behavioral analysis.

   ---
# Google BigQuery Data Wrangling: Hacker News Analytics

This repository demonstrates production-level relational data aggregation techniques utilizing the **Google Cloud BigQuery API** within a Python-managed data pipeline. The engineering focus highlights scalable performance optimization across billions of data streams using `GROUP BY`, `HAVING`, and structural boolean filtering logic.

## 🛠️ System Architecture & Stack
- **Engine:** Google BigQuery Distributed Core
- **Environment:** Python 3.11 Workspace
- **API Interface:** `google.cloud.bigquery` Framework
- **Data Serialization:** Pandas DataFrames

---

## 🚀 Optimization Challenges & Engineering Fixes

### 1. Keyword Overrides and Dynamic Schema Evaluation
* **Objective:** Isolate high-volume users who authored greater than 10,000 distinct records.
* **The Engineering Hurdle:** Legacy environments utilize an explicit `author` column layout. Modern live BigQuery clusters route upstream streaming vectors to an abstract identifier string titled `by`. Direct references to `by` throw runtime syntax exceptions (`BadRequest: 400`) because it collides with the reserved SQL core command phrase `BY`.
* **The Architectural Patch:** Escaped the structural naming namespace natively utilizing targeted backticks (`` `by` ``) and re-aliased the output array schema mapping back to the standard application requirement payload (`AS author`).

```sql
SELECT `by` AS author, COUNT(1) AS NumPosts
FROM `bigquery-public-data.hacker_news.full`
GROUP BY `by`
HAVING COUNT(1) > 10000;
```

### 2. High-Performance Boolean Indexing vs. Redundant Clustering
* **Objective:** Extract the exact quantitative delta of records flags marked explicitly with a `True` deletion status.
* **The Engineering Hurdle:** Initial testing methodology routed calculations through an expensive partition window grouping step (`GROUP BY id HAVING COUNT(id) > 10`), causing severe compute waste and resulting in an empty matrix array because row keys were globally unique. 
* **The Architectural Patch:** Refactored the computational footprint away from group aggregation entirely. Transitioned execution downstream into a highly performant `WHERE` clause vector slice, capturing binary evaluations (`deleted = True`) prior to hitting global scalar counts.

```sql
SELECT COUNT(1) AS num_deleted_comments
FROM `bigquery-public-data.hacker_news.full`
WHERE deleted = True;
```

---

## 📊 Analytical Execution Payloads

### Dataset Schema Matrix
```python
# Programmatic inspection output validating active metadata streams:
['title', 'url', 'text', 'dead', 'by', 'score', 'time', 'timestamp', 'type', 'id', 'parent', 'descendants', 'ranking', 'deleted']
```

### High-Volume Contributor Sample View

| Author Index | Record Footprint (NumPosts) |
| :--- | :--- |
| `vidarh` | 18,501 entries |
| `marcosdumay` | 19,188 entries |
| `sliverstorm` | 11,060 entries |
| `JoshTriplett` | 10,989 entries |
| `tonyedgecombe` | 10,052 entries |

---
*Note: This data module reflects structural solutions verified by automated evaluation layers in live analytics testing parameters.




    
