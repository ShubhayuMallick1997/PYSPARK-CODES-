
# 🧮 6. Aggregations and Grouping

Explained in an easy-to-read, professional format with examples and descriptions.

---

## 🔹 What Are Aggregations?

Aggregations in PySpark are operations that **summarize or combine data** across groups or rows. This is useful for reporting, analytics, and creating features in machine learning workflows. Common aggregation functions include `count()`, `sum()`, `avg()`, `min()`, and `max()`.

---

## ✅ 1. `groupBy()` and Aggregation Functions

The `groupBy()` function is used to **group rows based on the values of one or more columns**. You can apply aggregation functions to each group.

**Example:**
Group employees by department and calculate total, average, and max salary:

```python
df.groupBy("department").agg(
    count("*").alias("total_employees"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary")
).show()
```

**Common aggregation functions:**

* `count()` – Total number of rows
* `sum()` – Total sum of values
* `avg()` – Average value
* `min()` – Minimum value
* `max()` – Maximum value

---

## ✅ 2. Pivoting (Wide Format Transformation)

Pivoting is used to transform distinct values in one column into new columns.

**Example:**
Count male and female employees in each department:

```python
df.groupBy("department").pivot("gender").agg(count("*")).show()
```

This will output departments in rows and genders as columns with their respective counts.

---

## ✅ 3. Unpivoting (Long Format Transformation)

Unpivoting converts wide-format data into long format. PySpark doesn’t have a direct function for this, but it can be done using the `stack()` function.

**Example:**
Convert columns `maths` and `science` into rows:

```python
df.select("id", "name",
          expr("stack(2, 'maths', maths, 'science', science) as (subject, marks)")).show()
```

This transforms subject columns into a pair of key-value rows.

---

## ✅ 4. Grouping on Multiple Columns

You can use `groupBy()` on multiple columns to perform more detailed aggregations.

**Example:**
Group by department and gender to calculate average salary:

```python
df.groupBy("department", "gender").agg(avg("salary")).show()
```

This gives a breakdown of average salary for each gender within each department.

---

## ✅ 5. Window Functions

**Window functions** allow you to perform calculations **across rows related to the current row** without collapsing them into a single result like `groupBy()` does. They are useful for ranking, running totals, and comparing values from previous or next rows.

To use window functions, you need to define a **Window specification**.

**Common window functions:**

* `row_number()` – Gives a unique sequential number to each row in a partition
* `rank()` – Ranks rows with gaps in case of ties
* `dense_rank()` – Ranks rows without gaps
* `lag()` – Gets the value from the previous row
* `lead()` – Gets the value from the next row

---

**Example with `row_number()`**
Assign row numbers within each department ordered by salary:

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("department").orderBy("salary")
df.withColumn("row_num", row_number().over(windowSpec)).show()
```

---

**Example with `lag()` and `lead()`**
Compare each employee's salary with the previous and next one in their department:

```python
from pyspark.sql.functions import lag, lead

df.withColumn("prev_salary", lag("salary").over(windowSpec)) \
  .withColumn("next_salary", lead("salary").over(windowSpec)) \
  .show()
```

---

## ✅ Summary

| Feature               | Function(s) Used          | Description                           |
| --------------------- | ------------------------- | ------------------------------------- |
| Grouping              | `groupBy()`               | Groups rows by one or more columns    |
| Aggregations          | `count()`, `sum()`, etc.  | Calculates summary statistics         |
| Pivoting              | `pivot()`                 | Converts row values to columns        |
| Unpivoting            | `stack()` (via `expr()`)  | Converts columns to rows              |
| Multi-column grouping | `groupBy("col1", "col2")` | Groups using multiple columns         |
| Ranking rows          | `row_number()`, `rank()`  | Adds ranks within each partition      |
| Row-wise comparisons  | `lag()`, `lead()`         | Looks at previous/next rows in window |

---

