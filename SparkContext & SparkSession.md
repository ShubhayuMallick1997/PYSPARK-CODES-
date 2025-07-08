---

````markdown
# 🗂️ 2. SparkContext & SparkSession

Understanding the foundational entry points of any PySpark application is essential. Two key components are:

- **`SparkContext`**: The original entry point to Spark Core
- **`SparkSession`**: The unified entry point to Spark SQL, DataFrames, and overall Spark functionality (introduced in Spark 2.0)

---

## 🔹 SparkContext Initialization

`SparkContext` is the **core engine** that connects your application to a Spark cluster. It represents the **connection to a Spark execution environment**.

### 🔧 Example:
```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("MyApp").setMaster("local[*]")
sc = SparkContext(conf=conf)
````

* `setAppName()` – Sets the name shown in the Spark UI
* `setMaster()` – Specifies where the job runs (e.g., `local`, `yarn`, `spark://...`)

> ⚠️ In modern PySpark (2.x+), `SparkContext` is accessed via `SparkSession`. Manual initialization is rare unless using lower-level RDD APIs.

---

## 🔹 SparkConf Settings

`SparkConf` is used to **configure your Spark application**. You define settings like:

* Application name
* Cluster master (local, YARN, etc.)
* Executor memory and cores
* Custom configurations (e.g., Hive support, Spark SQL optimizations)

### 🔧 Example:

```python
conf = SparkConf()
conf.set("spark.executor.memory", "4g")
conf.set("spark.driver.memory", "2g")
conf.setAppName("ETL-Pipeline").setMaster("yarn")
```

You pass this configuration into the `SparkContext`, or indirectly via `SparkSession.builder.config()`.

---

## 🔹 SparkSession: The Unified Entry Point

Since **Spark 2.0**, `SparkSession` is the **primary entry point** to all Spark functionality:

* Creating **DataFrames**
* Running **SQL queries**
* Accessing **Hive tables** and catalogs
* Reading/writing files (CSV, JSON, Parquet, etc.)
* Managing configuration and application context

### 🔧 Create a SparkSession:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Customer360") \
    .config("spark.some.config.option", "value") \
    .getOrCreate()
```

### ✅ Benefits of SparkSession:

| Feature               | Description                                             |
| --------------------- | ------------------------------------------------------- |
| Unified API           | Combines SQL, DataFrames, Streaming under one interface |
| Implicit SparkContext | Access via `spark.sparkContext`                         |
| Configurable          | Easily add memory/parallelism settings                  |
| Hive Support          | Enable with `.enableHiveSupport()`                      |

---

## 🌀 Spark Application Lifecycle

Understanding the Spark application lifecycle helps in **efficient development, tuning, and monitoring**.

### 📦 Lifecycle Phases:

1. **Initialization**

   * `SparkSession` and `SparkContext` are created.
   * Configuration values are applied.
   * Connection established with cluster manager (YARN/K8s/local).

2. **Data Processing**

   * Code creates **jobs**, which are broken into **stages** and **tasks**.
   * Tasks are sent to **executors** on worker nodes.
   * Data is transformed and actions are performed.

3. **Execution Monitoring**

   * Real-time tracking via **Spark UI** (e.g., `http://localhost:4040`)

4. **Shutdown**

   * Spark resources are released using:

     ```python
     spark.stop()
     ```

---

## ✅ Summary Table

| Concept          | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| `SparkConf`      | Configuration settings (memory, parallelism, etc.)   |
| `SparkContext`   | Core Spark engine interface (RDD-focused)            |
| `SparkSession`   | Unified interface for SQL, DataFrames, Hive, Catalog |
| Application Flow | Init → Process → Monitor → Shutdown                  |

> ⚠️ In most PySpark jobs today, you should use `SparkSession` as your main interface. It automatically manages `SparkContext` under the hood and is suitable for DataFrame and SQL-based workloads.

---

✅ Ready to move on to [3. RDDs (Resilient Distributed Datasets)](#)? Let’s continue! 🚀

```

---

Would you like this compiled as a downloadable `README.md` file or part of a structured GitHub project documentation?
```
