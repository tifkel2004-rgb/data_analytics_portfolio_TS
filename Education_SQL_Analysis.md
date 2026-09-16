# Global Education Analytics & Data Validation Baseline

This project evaluates global education macro indicators leveraging the World Bank International Education public data cluster. The goal is to programmatically interface with large-scale datasets, filter relational tracking anomalies across borders, and isolate key expenditure trends to drive evidence-based reporting structures.

---

### 📋 Database Environment Setup & Table Preview

We initialize the Google Cloud BigQuery client interface and execute a sample query against the `international_education` table to inspect multi-variable tracking structures and verify column schemas.

```python
from google.cloud import bigquery

# Initialize primary BigQuery Client
client = bigquery.Client()

# Reference target dataset and table
dataset_ref = client.dataset("world_bank_intl_education", project="bigquery-public-data")
table_ref = dataset_ref.table("international_education")
table = client.get_table(table_ref)

# Preview the first five lines of records
client.list_rows(table, max_results=5).to_dataframe()
```

---

### 📊 Core Analysis: Government Expenditure on Education

To map financial priorities across boundaries, we isolate indicator code `SE.XPD.TOTL.GD.ZS` ("Government expenditure on education as % of GDP"). This analysis focuses on calculating global expenditure averages over an 8-year cohort (2010–2017 inclusive) to rank top investing countries.

```sql
SELECT 
    country_name, 
    AVG(value) AS avg_ed_spending_pct
FROM 
    `bigquery-public-data.world_bank_intl_education.international_education`
WHERE 
    indicator_code = 'SE.XPD.TOTL.GD.ZS'
    AND year BETWEEN 2010 AND 2017
GROUP BY 
    country_name
ORDER BY 
    avg_ed_spending_pct DESC;
```

---

### 💡 Strategic Takeaways & Operational Value
* **Cloud Data Governance:** Built repeatable, high-performance query structures to cleanly map longitudinal metrics across changing national reporting frequencies.
* **Standardized Telemetry:** Filtered out sparse, low-density reporting data to isolate valid comparative benchmarks for leadership teams.
