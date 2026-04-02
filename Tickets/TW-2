Ticket: TW-002 — Course Performance Analysis

Problem:
- Analyze course-level performance
- Metrics required:
  - Number of enrollments per course
  - Total revenue per course
  - Average engagement per course
  - Identify top-performing course

Understanding:
- Data distributed across enrollments, payments, engagement, and courses tables
- Course-level metrics require grouping by course_id
- Revenue and engagement are derived from different tables

Approach:
- Use GROUP BY to aggregate data per course
- Use COUNT for enrollments
- Use SUM for revenue
- Use AVG for engagement
- Use JOINs to relate tables via student_id and course_id
- Use ORDER BY to identify top-performing course

Queries:

Enrollments per Course:
- COUNT(student_id) grouped by course_id
- Derived from enrollments table

Revenue per Course:
- JOIN enrollments with payments on student_id
- SUM(payment amount) grouped by course_id
- ORDER BY revenue DESC for ranking

Average Engagement per Course:
- AVG(minutes_watched) grouped by course_id
- ROUND used for readability

Concepts:

GROUP BY:
- Used to aggregate data per category (course_id)
- Required when using aggregation functions

Aggregation Functions:
- COUNT → number of records
- SUM → total value (revenue)
- AVG → average behavior (engagement)

JOIN Usage:
- Combines data across tables
- student_id used to link payments and enrollments
- course_id used for grouping

ORDER BY:
- Used to rank results (e.g., highest revenue course)

Issues Faced:
- No major issues during implementation
- Queries executed as expected

Root Cause:
- Prior understanding of JOIN and aggregation helped avoid issues

Fix:
- Not applicable (no blocking issues)

Key Learnings:
- GROUP BY is essential for category-level analysis
- Aggregations convert raw data into business insights
- Multiple tables must be combined to derive meaningful metrics
- ORDER BY helps in ranking and identifying top performers

Real-World Mapping:
- Course performance analysis is similar to:
  - Product performance in e-commerce
  - Content performance in streaming platforms
- Used for:
  - Revenue optimization
  - Content strategy decisions

Improvements:
- Replace RIGHT JOIN with LEFT JOIN for clarity
- Precompute metrics in ETL pipelines for performance
- Create summary tables for frequent queries
- Add indexes on join keys (student_id, course_id)
