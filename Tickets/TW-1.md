Ticket: TW-001 — Student Conversion Analysis

Problem:
- Analyze student conversion funnel
- Metrics required:
  - Total students
  - Paying students
  - Conversion rate
  - Enrolled but not paid users

Understanding:
- Data spread across multiple normalized tables
- Payments indicate conversion
- Need joins + aggregation to derive metrics

Approach:
- Use COUNT and COUNT DISTINCT for aggregations
- Use JOINs to combine tables
- Use LEFT JOIN + NULL filtering for missing data
- Use arithmetic operations for business metrics

Queries:

Total Students:
- SELECT COUNT(*) FROM students

Paying Students:
- SELECT COUNT(DISTINCT student_id) FROM payments

Conversion Rate:
- (COUNT(DISTINCT p.student_id) * 100.0) / COUNT(DISTINCT s.student_id)
- LEFT JOIN ensures all students are included

Enrolled but Not Paid:
- JOIN students + enrollments
- LEFT JOIN payments
- WHERE payment IS NULL

Concepts:

INNER JOIN:
- Returns only matching rows
- Drops unmatched data

LEFT JOIN:
- Returns all rows from left table
- Adds NULL for unmatched right-side rows

DISTINCT:
- Prevents duplicate counting in transactional tables

NULL Filtering:
- Identifies missing relationships (e.g., unpaid users)

Aggregation:
- COUNT used for metrics
- Metrics derived using SQL logic

Issues Faced:
- Difficulty with conversion rate logic
- Confusion between JOIN types
- Unclear handling of duplicates

Root Cause:
- Limited understanding of JOIN behavior
- Lack of exposure to aggregation patterns
- Missing DISTINCT concept

Fix:
- Used LEFT JOIN correctly
- Applied DISTINCT to avoid duplication
- Used NULL filtering for anti-join logic
- Used float (100.0) to avoid integer division

Key Learnings:
- JOIN choice directly impacts result accuracy
- DISTINCT is critical in real datasets
- Business metrics require combining multiple tables
- LEFT JOIN + NULL = powerful pattern

Real-World Mapping:
- Conversion rate is a core business KPI
- Used in funnel analysis and revenue tracking
- In production → precomputed in pipelines

Improvements:
- Precompute metrics in ETL layer
- Avoid repeated joins for performance
- Use indexing on join keys
