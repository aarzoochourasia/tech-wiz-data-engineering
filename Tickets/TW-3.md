Ticket: TW-003 — Data Quality Analysis

Problem:
- Identify inconsistencies in payment and engagement data
- Scenarios:
  - Duplicate payments
  - Payments without enrollments
  - Enrollments without engagement

Understanding:
- Data quality issues arise due to duplication, missing relationships, or invalid records
- Need to detect anomalies using SQL patterns
- Missing data and duplicate data are different problems

Approach:
- Use GROUP BY + HAVING to detect duplicates
- Use LEFT JOIN + NULL filtering to detect missing relationships
- Avoid NOT IN due to NULL issues
- Focus on presence/absence of rows instead of values

Queries:

Duplicate Payments:
- GROUP BY student_id, payment_date, amount
- HAVING COUNT(*) > 1

Payments Without Enrollments:
- LEFT JOIN payments with enrollments
- Filter WHERE enrollment is NULL

Enrollments Without Engagement:
- LEFT JOIN enrollments with engagement
- Filter WHERE engagement is NULL

Concepts:

Duplicate Detection:
- GROUP BY + HAVING identifies repeated records

Missing Data Detection:
- LEFT JOIN + NULL is standard pattern

NOT IN vs LEFT JOIN:
- NOT IN fails with NULL values
- LEFT JOIN is safer and preferred

NULL vs Zero:
- NULL → no data exists
- 0 → data exists but value is zero

Issues Faced:
- Confusion between missing data and zero values
- Incorrect join usage (RIGHT JOIN instead of LEFT JOIN)
- Use of NOT IN instead of safer join pattern

Root Cause:
- Lack of clarity on data presence vs value conditions
- Limited understanding of join behavior in edge cases

Fix:
- Replaced NOT IN with LEFT JOIN + NULL
- Used correct join keys (student_id + course_id)
- Switched from value filtering to missing row detection

Key Learnings:
- LEFT JOIN + NULL is core pattern for data quality checks
- GROUP BY + HAVING used for duplicate detection
- Missing data is different from zero values
- Join conditions must include correct keys

Real-World Mapping:
- Data quality checks are critical in pipelines
- Used in:
  - ETL validation
  - Monitoring systems
  - Data observability tools

Improvements:
- Add constraints to prevent duplicates
- Implement data validation in ingestion layer
- Create automated data quality checks
