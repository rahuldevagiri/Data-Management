# Transaction Data Quality Audit

This project analyzes a synthetic customer transaction dataset in Python and performs a structured data quality audit.

## Project Overview
The dataset contains transaction records with fields such as transaction_id, transaction_date, customer_id, product, region, payment_method, status, amount, and channel.

## Business Use Case
This data can be used for revenue reporting, payment analysis, customer behavior analysis, and fraud screening.

## Files
- `data_quality_audit.ipynb` — notebook with the full analysis.
- `customer_transactions_sample.csv` — input dataset.
- `audit_findings.csv` — row-level issue log.
- `kpi_summary.csv` — KPI table.
- `validation_rules.csv` — automated validation rules.
- `audit_summary.csv` — audit summary grouped by issue type.

## What the Notebook Does
- Describes the dataset and business use case.
- Identifies issues across completeness, uniqueness, validity, consistency, and integrity.
- Computes KPIs such as completeness rate, duplication rate, and amount validity rate.
- Defines validation rules for automatic checks.
- Produces an audit summary and cleaning recommendations.

## KPIs
- Completeness Rate
- Duplication Rate
- Amount Validity Rate
- Date Parseability Rate

## Validation Rules
- `transaction_id` must be non-null and unique.
- `amount` must be numeric and within a valid range.
- `transaction_date` must be parseable.
- `region` must be one of the allowed values.

## Cleaning Recommendations
- Deduplicate on `transaction_id`.
- Standardize dates to ISO format.
- Normalize categorical values.
- Flag invalid amounts and missing critical fields.

## How to Run
1. Open the notebook in Jupyter or VS Code.
2. Keep the CSV file in the same folder.
3. Run all notebook cells from top to bottom.

## Requirements
- Python 3
- pandas
- numpy

## Author
Rahul Shrikant Devagiri
