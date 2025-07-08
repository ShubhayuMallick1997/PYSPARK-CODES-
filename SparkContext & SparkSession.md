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

## setAppName() – Sets the name shown in the Spark UI

setMaster() – Specifies where the job runs (e.g., local, yarn, spark://...)

⚠️ In modern PySpark (2.x+), SparkContext is accessed via SparkSession. Manual initialization is rare unless using lower-level RDD APIs.

