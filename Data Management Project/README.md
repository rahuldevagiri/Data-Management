# Data Management Project using Tableau Prep Builder

## Project Overview
This project demonstrates an end-to-end **data cleaning, transformation, integration, and KPI generation workflow** built using **Tableau Prep Builder**. The workflow processes multiple datasets related to sales, products, and stores to generate business-ready output files that can be used for reporting, dashboarding, and analytical decision-making.

The project focuses on:

- Cleaning and standardizing raw data
- Handling missing values and inconsistencies
- Detecting negative sales and outliers
- Joining and unifying multiple datasets
- Creating business KPIs
- Generating analytical output files for reporting

The workflow was designed and implemented using:

- **Tableau Prep Builder**
- CSV data sources
- KPI calculations and aggregation logic

---

# Workflow Architecture

The Tableau Prep flow integrates multiple datasets and transforms them through a series of cleaning and analytical steps.

## Input Datasets

The following datasets were used as inputs in the Tableau Prep flow:

| Dataset | Purpose |
|---|---|
| `Sales_2022` | Historical sales transactions |
| `Sales_2023` | Latest sales transactions |
| `Products_Data` | Product-level information |
| `Stores_Data` | Store-level information |

---

# Major Data Preparation Steps

## 1. Cleaning and Standardization
Several cleaning nodes were used throughout the flow to improve data quality.

### Tasks Performed

- Standardized inconsistent formats
- Corrected datatype mismatches
- Removed or handled invalid records
- Unified naming conventions
- Prepared fields for joins and aggregations

### Tableau Prep Nodes Used

- `Cleaning, Standardizing`
- `City_DataType_Change`
- `Adding Common Field`

---

# Missing Value Handling

The workflow contains a dedicated step for handling null or missing values.

## Techniques Used

- Replacing missing values
- Filling incomplete records
- Improving dataset consistency before aggregation

### Tableau Prep Node

- `Filling NaN`

---

# Data Integration

The project combines multiple datasets to build a unified analytical dataset.

## Joins Performed

### Sales and Product Join

Merged sales transactions with product details.

### Previous and Store Join

Combined sales data with store-level information.

### Additional Join Operations

Additional joins were implemented to enrich the analytical dataset.

### Tableau Prep Join Nodes

- `Join (Sales,Product)`
- `Join (Previous,Store)`
- `Join 5`

---

# Union Operations

The workflow combines multiple yearly sales datasets into a single dataset.

## Purpose

- Create a consolidated sales repository
- Enable year-over-year analysis
- Simplify downstream KPI calculations

### Tableau Prep Node

- `Union of Sales Data`

---

# Data Quality Checks

The project includes validation and anomaly detection steps.

## Negative Sales Detection

A dedicated process identifies records with negative sales values.

### Purpose

- Detect return transactions
- Identify incorrect entries
- Improve reporting reliability

### Tableau Prep Node

- `Negative_Sales_ID`

---

## Outlier Detection

Outlier analysis was performed on sales price values.

### Purpose

- Detect abnormal pricing
- Identify unusual transactions
- Improve analytical accuracy

### Tableau Prep Node

- `Outlier_Sales_Price`

---

# KPI Generation

The workflow calculates multiple business KPIs and analytical measures.

## KPI Calculations Included

- Revenue calculations
- Product category analysis
- Store contribution analysis
- Revenue aggregation
- Performance indicators

### Tableau Prep Nodes

- `Calculating KPIs`
- `Overall Revenue`
- `Store Revenue`
- `Grouping Category`
- `Revenue, PM, Prod. Cat.`
- `Store_Contribution_Percentage`

---

# Output Files

The Tableau Prep flow generates **three final output files**, each serving a unique analytical purpose.

---

## Output 1: KPI Output

### Tableau Prep Output Node

- `KPI Output`

### Purpose

This output file contains the primary business KPIs generated from the transformed dataset.

### Key Use Cases

- Business performance tracking
- KPI dashboard creation
- Executive reporting
- Revenue analysis
- Operational monitoring

### Example Metrics

- Revenue KPIs
- Performance indicators
- Aggregated business measures

---

## Output 2: Product Category Revenue

### Tableau Prep Output Node

- `Product Category - Revenue`

### Purpose

This output focuses on revenue performance by product category.

### Key Use Cases

- Product category analysis
- Revenue comparison across categories
- Product portfolio performance tracking
- Sales trend analysis

### Example Insights

- High-performing categories
- Low-performing categories
- Revenue contribution by category

---

## Output 3: Store Revenue Contribution Percentage

### Tableau Prep Output Node

- `Store_Revenue_Contribution_Percent`

### Purpose

This output calculates each store’s contribution toward overall revenue.

### Key Use Cases

- Store performance evaluation
- Regional comparison
- Revenue contribution analysis
- Business expansion decisions

### Example Insights

- Top-performing stores
- Revenue share percentage
- Store-level business contribution

---

# Flow Components Summary

| Tableau Prep Node | Purpose |
|---|---|
| Cleaning, Standardizing | Data cleaning and standardization |
| Filling NaN | Missing value handling |
| Join (Sales,Product) | Merge sales and product data |
| Join (Previous,Store) | Merge store data |
| Union of Sales Data | Combine yearly sales datasets |
| Negative_Sales_ID | Detect negative sales |
| Outlier_Sales_Price | Detect pricing anomalies |
| Calculating KPIs | KPI calculations |
| Overall Revenue | Revenue aggregation |
| Store Revenue | Store-level aggregation |
| Grouping Category | Product grouping and categorization |
| Store_Contribution_Percentage | Revenue contribution analysis |

---

# Business Value of the Project

This project demonstrates practical implementation of:

- Data cleaning workflows
- ETL concepts
- Data integration techniques
- Data quality validation
- Business KPI generation
- Analytical dataset preparation
- Tableau Prep Builder workflow design

The project can be used as a foundation for:

- Business Intelligence dashboards
- Tableau visualizations
- Revenue analytics
- Store performance reporting
- Product performance analysis

---

# Skills Demonstrated

## Data Management Skills

- Data Cleaning
- Data Transformation
- Data Integration
- Data Aggregation
- Data Standardization
- Missing Value Handling
- Outlier Detection
- KPI Engineering

## Tools & Technologies

- Tableau Prep Builder
- CSV Data Processing
- Data Analytics
- Business Intelligence Concepts

---

# Repository Structure

```text
📁 Tableau-Prep-Data-Management-Project
│
├── 📄 README.md
├── 📄 Data Project_Final.tfl
│
├── 📁 input_data
│   ├── Sales_2022.csv
│   ├── Sales_2023.csv
│   ├── Products_Data.csv
│   └── Stores_Data.csv
│
├── 📁 output_data
│   ├── KPI_Output.csv
│   ├── Product_Category_Revenue.csv
│   └── Store_Revenue_Contribution_Percent.csv
│
├── 📁 python_scripts
│   ├── outlier_detection.py
│   ├── missing_value_handling.py
│   └── data_cleaning.py
│
└── 📁 screenshots
    ├── flow_overview_1.png
    ├── flow_overview_2.png
    ├── output1.png
    ├── output2.png
    └── output3.png
```

---

# How to Run the Flow

1. Open Tableau Prep Builder
2. Load the `.tfl` flow file
3. Verify the input dataset paths
4. Run the flow
5. Export the generated output files

---

# Future Improvements

Potential enhancements for this project:

- Integration with SQL databases
- Automated scheduling
- Python integration for advanced analytics
- Machine learning-based anomaly detection
- Real-time dashboard integration
- Cloud deployment

---

# Conclusion

This project demonstrates a complete data preparation and KPI generation workflow using Tableau Prep Builder. It showcases how raw business data can be transformed into meaningful analytical outputs through cleaning, integration, validation, and aggregation processes.

The generated outputs support business reporting, KPI monitoring, and strategic decision-making.

