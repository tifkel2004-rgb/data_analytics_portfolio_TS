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
  # 📊 Workforce Analytics & SQL Optimization Sandbox

### **Project Scope**
Engineered a relational SQLite schema to transition multi-variable employee survey profiles out of flat data matrices and optimize data hygiene pipelines.

### **Technical Focus**
Executed advanced data extraction models utilizing multi-table JOIN statements, Common Table Expressions (CTEs), and aggregate metrics.

### **Business Outcome**
Isolated targeted burnout and satisfaction metrics to deliver actionable corporate insights for workforce retention strategies.


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
*Note: This data module reflects structural solutions verified by automated evaluation layers in live analytics testing parameters.*

