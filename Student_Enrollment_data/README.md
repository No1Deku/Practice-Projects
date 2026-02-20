📊 Data Cleaning & Governance Implementation for Student Enrollment Records
📌 Project Overview

This project focuses on restoring structural integrity and data governance compliance within a corrupted student enrollment dataset.

The dataset was affected by manual data entry errors, resulting in concatenated fields, inconsistent identifiers, invalid formats, and financial data contamination.

The objective was to:

Diagnose systemic data quality failures

Reconstruct corrupted records

Enforce identifier integrity

Standardize domain values

Deliver a fully analysis-ready and reporting-safe dataset

Final Result:

🔹 Improved usability from ~30% to ~95%+
🔹 100% unique student identifier coverage
🔹 Standardized financial & demographic fields

🚨 Problem Statement

Student records contained:

Multiple attributes merged into a single Student_ID field

Inconsistent identifiers across Student_ID, Names, Dates, and Payments

Structural corruption caused by irregular delimiters

Missing and incomplete student identifiers

Currency symbols embedded in numeric payment fields

Multiple date formats across enrollment records

These failures made the dataset:

❌ Unreliable for enrollment tracking

❌ Unsafe for revenue aggregation

❌ Invalid for demographic analysis

❌ Risk-prone for operational reporting

🎯 Objectives

Conduct a structured data quality audit

Restore structural integrity to student records

Standardize formats across identifiers, dates, demographics, and payments

Implement unique identifier governance

Deliver a validated, aggregation-ready dataset

Provide architectural recommendations for long-term integrity

🔎 Scope of Work
1️⃣ Diagnosis of Data Quality Failures

Identified structural and domain violations across:

Student_ID

First_Name

Last_Name

Age

Gender

Course

Enrollment_Date

Total_Payments

Structural Failures Detected:

Concatenated fields using |

Misaligned columns

Mixed data types within single attributes

Missing primary identifiers

2️⃣ Data Cleaning & Structural Reconstruction

Parsed concatenated Student_ID values into atomic attributes

Restored proper column alignment

Enforced First Normal Form (1NF) compliance

3️⃣ Domain Standardization

Converted Age to numeric type

Standardized Gender to controlled values (M, F)

Unified Enrollment_Date into ISO YYYY-MM-DD format

Standardized Course naming conventions

4️⃣ Financial Field Decoupling

Extracted currency symbols from Total_Payments

Converted payment values to numeric

Created separate Currency column

This ensured:

Aggregation-safe revenue reporting

Type consistency

Financial field integrity

5️⃣ Handling Missing & Incomplete Records

Generated temporary IDs (TEMP_) for missing identifiers

Introduced id_status tracking field

Flagged irrecoverable records for escalation

📑 Deliverables

✅ Cleaned & standardized dataset (analysis-ready)

✅ SQL-based cleaning pipeline

✅ Data Quality Report:

Missing value percentages

Identifier recovery statistics

Structural corrections applied

Governance recommendations

✅ Proposed normalized schema design

📈 Workflow (Execution Flow)
🧪 Sample Work Executed
Example 1: Structural Field Reconstruction
-- Splitting concatenated Student_ID fields
SELECT SPLIT_PART(student_id, '|', 1) AS student_id_clean
FROM raw_students;

✅ Restored atomic attributes and eliminated composite field corruption.

Example 2: Date Standardization
UPDATE students
SET enrollment_date = STRFTIME('%Y-%m-%d', enrollment_date);

✅ Unified all enrollment dates into ISO standard format.

Example 3: Financial Cleaning
df['Total_Payments'] = (
    df['Total_Payments']
    .replace('[\$,]', '', regex=True)
    .astype(float)
)

✅ Enabled safe revenue aggregation and analysis.

📊 Data Quality Report (Summary Extract)
Metric	Before	After
Analysis-Ready Records	~30%	~95%
Missing Student IDs	20%	0%
Date Format Consistency	Multiple	Unified
Financial Type	Text	Numeric
Gender Standardization	Inconsistent	Controlled (M/F)

Additional Findings:

Duplicate Records → 1.8%

Irrecoverable Records → 1.1%

Payment Missing Values → 5.2%

Recommendation:
Implement validation controls at point of entry and enforce database constraints (NOT NULL, UNIQUE, FK).

📈 Analytical Questions Now Reliably Supported

After cleaning, the dataset can accurately answer:

🎓 Enrollment Analysis

Total number of enrolled students

Enrollment distribution per course

Enrollment volume over time

Course popularity ranking

👥 Demographic Analysis

Gender distribution across students

Age distribution patterns

Average age per course

Gender representation by course

💰 Revenue Analysis

Total tuition revenue

Revenue per course

Average payment per student

Revenue distribution by enrollment period

Currency breakdown of payments

🧱 Architectural Recommendation

To prevent recurrence, a normalized structure is recommended:

students

courses

enrollments

payments

This enables:

Referential integrity

Reduced redundancy

Transaction separation

Long-term scalability

✅ Expected Outcome

A reliable, aggregation-ready enrollment dataset

A documented governance intervention

Restored trust in operational reporting

Improved long-term data capture processes
