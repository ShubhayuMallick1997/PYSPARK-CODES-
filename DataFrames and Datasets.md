
---

# 📈 4. DataFrames and Datasets

---

## 🔹 What is a DataFrame?

A **DataFrame** in PySpark is a **distributed collection of data** organized into **named columns**, similar to a table in a relational database or a Pandas DataFrame.

* Built on top of **RDDs**
* Optimized using **Catalyst optimizer** and **Tungsten execution engine**
* Supports SQL queries, DSL operations, and seamless integration with multiple data formats (CSV, JSON, Parquet, etc.)

> ✅ DataFrames are the **standard abstraction** for working with structured and semi-structured data in PySpark.

---

## 🔹 Creating DataFrames

### ✅ 1. From RDD

```python
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName("DataFrameExample").getOrCreate()

rdd = spark.sparkContext.parallelize([
    Row(id=1, name="Alice"),
    Row(id=2, name="Bob")
])

df = spark.createDataFrame(rdd)
df.show()
```

---

### ✅ 2. From CSV File

```python
df = spark.read.csv("s3://bucket/customers.csv", header=True, inferSchema=True)
df.show()
```

---

### ✅ 3. From JSON File

```python
df = spark.read.json("s3://bucket/data.json")
df.printSchema()
```

---

### ✅ 4. From Parquet File

```python
df = spark.read.parquet("s3://bucket/data.parquet")
```

> PySpark automatically handles **compression** and **schema evolution** in Parquet.

---

## 🔹 Schema Inference and Manual Schema Definition

### ✅ Schema Inference

PySpark can **automatically infer schema** from data using the `inferSchema=True` option.

```python
df = spark.read.option("inferSchema", True).csv("data.csv", header=True)
```

### ✅ Manual Schema Definition

Manually defining schema gives better control and performance.

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

df = spark.read.schema(schema).csv("data.csv", header=True)
df.printSchema()
```

---

## 🔹 Selecting, Filtering, and Sorting Columns

### ✅ Selecting Columns

```python
df.select("id", "name").show()
```

### ✅ Filtering Rows

```python
df.filter(df["id"] > 1).show()
# or using SQL-like where
df.where("id > 1").show()
```

### ✅ Sorting

```python
df.orderBy("name").show()
df.orderBy(df["id"].desc()).show()
```

---

## 🔹 Common DataFrame Operations

### ✅ `select()`

Returns a new DataFrame with selected columns.

```python
df.select("name", "salary")
```

---

### ✅ `withColumn()`

Adds a new column or updates an existing one.

```python
from pyspark.sql.functions import col

df.withColumn("salary_doubled", col("salary") * 2)
```

---

### ✅ `drop()`

Drops a column.

```python
df.drop("unwanted_column")
```

---

### ✅ `distinct()` and `dropDuplicates()`

```python
df.distinct()
df.dropDuplicates(["id"])
```

---

## 🔹 Renaming and Aliasing Columns

### ✅ Renaming Columns

```python
df = df.withColumnRenamed("old_name", "new_name")
```

### ✅ Using Alias (temporary name)

```python
df.select(col("salary").alias("income")).show()
```

> 📝 Aliases are helpful in SQL joins or when creating temporary views.

---

## ✅ Summary

| Feature                  | Usage Example                            |
| ------------------------ | ---------------------------------------- |
| Creating from RDD        | `spark.createDataFrame(rdd)`             |
| Reading CSV/JSON/Parquet | `spark.read.csv/json/parquet(...)`       |
| Schema control           | `inferSchema=True` or `StructType`       |
| Filtering                | `df.filter("age > 25")`                  |
| Sorting                  | `df.orderBy("name")`                     |
| Adding columns           | `withColumn("bonus", col("salary")*0.1)` |
| Renaming                 | `withColumnRenamed("old", "new")`        |
| Aliasing                 | `select(col("amount").alias("total"))`   |

---

Ready to move on to [5. DataFrame Transformations](#)? 🔄 Let's go!

```

---

Would you like this saved as a `.md` file or embedded into your GitHub documentation structure?
```
