
---

# 📑 5. DataFrame Transformations

---

## 🔹 What are DataFrame Transformations?

Transformations in PySpark are **operations that return a new DataFrame** by modifying the original one. These operations are **lazy**, meaning they are not executed until an **action** such as `show()`, `count()`, or `write()` is triggered.

Transformations are commonly used to:

* Filter rows
* Add or modify columns
* Convert data types
* Clean, enrich, and structure data for downstream consumption

---

## ✅ 1. Filtering Rows (`filter`, `where`)

PySpark provides two equivalent functions for filtering rows:

* `filter()`
* `where()`

Both can accept expressions or column-based conditions.

**Examples:**

* Filter rows where age is greater than 30 using column expression:

  ```python
  df.filter(df["age"] > 30).show()
  ```

* Use a SQL-style string expression to apply multiple conditions:

  ```python
  df.filter("age > 30 AND gender = 'Male'").show()
  ```

* Use `where()` instead of `filter()` — it behaves the same:

  ```python
  df.where(df["salary"] > 50000).show()
  ```

> ℹ️ You can use either `filter()` or `where()`; they are interchangeable in DataFrame operations.

---

Let me know if you'd like the next sections ("withColumn", "cast", etc.) in the same format.

---

Let me know if you'd like the next sections ("withColumn", "cast", etc.) in the same format.

---

## ✅ 2. Adding or Modifying Columns (`withColumn`)

Use `withColumn()` to **add a new column** or **modify an existing column**.

```python
from pyspark.sql.functions import col

# Add new column by doubling existing one
df = df.withColumn("double_salary", col("salary") * 2)

# Modify existing column
df = df.withColumn("age", col("age") + 1)
```

---

## ✅ 3. Type Casting Columns

You can change the data type of a column using `.cast()`.

```python
df = df.withColumn("salary", col("salary").cast("float"))
df = df.withColumn("date", col("date").cast("date"))
```

Useful for ensuring correct types before writing to external systems or doing aggregations.

---

## ✅ 4. Dropping and Renaming Columns

### 🔸 Dropping Columns

```python
df = df.drop("unnecessary_column")
```

### 🔸 Renaming Columns

```python
df = df.withColumnRenamed("emp_name", "employee_name")
```

> Renaming is often needed to standardize schema or avoid naming conflicts.

---

## ✅ 5. Using `distinct()` and `dropDuplicates()`

### 🔸 `distinct()`

Removes **duplicate rows** across the entire DataFrame.

```python
df.select("department").distinct().show()
```

### 🔸 `dropDuplicates()`

Removes duplicates based on **specific column(s)**.

```python
df.dropDuplicates(["department", "salary"]).show()
```

---

## ✅ 6. String Functions

Import from `pyspark.sql.functions`.

```python
from pyspark.sql.functions import upper, lower, length, trim

df.select(upper(col("name")).alias("name_upper")).show()
df.select(length(col("email")).alias("email_length")).show()
df.select(trim(col("name"))).show()
```

Common String Functions:

* `upper()`, `lower()`
* `length()`
* `trim()`, `ltrim()`, `rtrim()`
* `concat()`, `substring()`
* `instr()`, `locate()`, `regexp_replace()`

---

## ✅ 7. Date & Time Functions

```python
from pyspark.sql.functions import current_date, datediff, to_date

df = df.withColumn("today", current_date())
df = df.withColumn("days_since_joining", datediff(current_date(), col("joining_date")))
df = df.withColumn("joining_date", to_date(col("joining_date"), "yyyy-MM-dd"))
```

Common Date Functions:

* `current_date()`, `current_timestamp()`
* `datediff()`, `add_months()`, `months_between()`
* `year()`, `month()`, `dayofmonth()`, `weekofyear()`

---

## ✅ 8. Conditional Logic (`when`, `otherwise`)

Use `when()` and `otherwise()` to implement **if-else** logic in DataFrames.

```python
from pyspark.sql.functions import when

df = df.withColumn("status", when(col("salary") > 50000, "High")
                                .otherwise("Low"))
```

Nested Conditions:

```python
df = df.withColumn("grade", 
        when(col("marks") >= 90, "A")
        .when(col("marks") >= 75, "B")
        .when(col("marks") >= 60, "C")
        .otherwise("D"))
```

---

## ✅ Summary

| Transformation Type | Function(s)                      | Example                                      |
| ------------------- | -------------------------------- | -------------------------------------------- |
| Filter rows         | `filter()`, `where()`            | `df.filter("age > 30")`                      |
| Add/Modify columns  | `withColumn()`                   | `df.withColumn("bonus", col("x")*0.1)`       |
| Change data type    | `cast()`                         | `col("x").cast("int")`                       |
| Drop/Rename columns | `drop()`, `withColumnRenamed()`  | `df.drop("x")`                               |
| Remove duplicates   | `distinct()`, `dropDuplicates()` | `df.dropDuplicates(["id"])`                  |
| String ops          | `upper()`, `length()` etc.       | `df.select(upper(col("name")))`              |
| Date ops            | `to_date()`, `datediff()`        | `df.withColumn(...)`                         |
| Conditional logic   | `when()`, `otherwise()`          | `when(col("x")>10, "high").otherwise("low")` |

---

