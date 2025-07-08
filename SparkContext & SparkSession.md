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

Sure! The issue is that your **first code block** wasn't enclosed in triple backticks (` ``` `), so Markdown interpreted the rest of the content as part of the code block.

Here is the **corrected and fully formatted** Markdown version:

---

````markdown
```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("MyApp").setMaster("local[*]")
sc = SparkContext(conf=conf)
````

### 🔹 `setAppName()` and `setMaster()`

* `setAppName()` – Sets the name of your Spark application, which will be visible in the **Spark UI** and job history server.
* `setMaster()` – Defines the **cluster manager** where the Spark job will run.
  Examples:

  * `local[*]` – Run locally with all available cores
  * `yarn` – Use YARN for cluster management
  * `spark://<master-url>` – Connect to a Spark standalone cluster

> ⚠️ In modern PySpark (2.x+), `SparkContext` is typically accessed **via `SparkSession`**. Manual initialization of `SparkContext` is rare unless you're working directly with **RDDs** or legacy Spark applications.

---

### 🔹 `SparkConf` Settings

`SparkConf` is used to **configure your Spark application** at runtime. It lets you define critical parameters such as:

* **Application Name**
* **Cluster Master URL** (e.g., local, YARN, Mesos)
* **Memory and Core Allocation** for Driver and Executors
* **Custom Configurations** like:

  * Enabling Hive support
  * Optimizing shuffle behavior
  * Setting log levels
  * Tuning SQL performance

#### 🔧 Example:

```python
from pyspark import SparkConf

conf = SparkConf()
conf.setAppName("ETL-Pipeline")
conf.setMaster("yarn")
conf.set("spark.executor.memory", "4g")
conf.set("spark.driver.memory", "2g")
conf.set("spark.sql.shuffle.partitions", "200")
```

> These configurations can be passed directly to `SparkContext`, or via `SparkSession.builder.config()` in modern PySpark applications.

```

---

