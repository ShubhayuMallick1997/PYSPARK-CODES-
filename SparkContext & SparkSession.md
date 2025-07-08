# 🗂️ 2. SparkContext & SparkSession

Understanding the foundational entry points of any PySpark application is essential. Two key components are:

- `SparkContext`: The original entry point to Spark Core
- `SparkSession`: The unified entry point to Spark SQL, DataFrames, and overall Spark functionality (introduced in Spark 2.0)

---

## 🔹 SparkContext Initialization

`SparkContext` is the **core engine** that connects your application to a Spark cluster. It represents the **connection to a Spark execution environment**.

### 🔧 Example:
```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("MyApp").setMaster("local[*]")
sc = SparkContext(conf=conf)

setAppName() – Sets the name shown in the Spark UI

setMaster() – Specifies where the job runs (e.g., local, yarn, spark://...)

⚠️ In modern PySpark (2.x+), SparkContext is accessed via SparkSession. Manual initialization is rare unless using lower-level RDD APIs.

🔹 SparkConf Settings
SparkConf is used to configure your Spark application. You define settings like:

App name

Master URL

Memory and executor settings

Custom configs (e.g., enabling Hive support)

🔧 Example:
python
Copy
Edit
conf = SparkConf()
conf.set("spark.executor.memory", "4g")
conf.set("spark.driver.memory", "2g")
conf.setAppName("ETL-Pipeline").setMaster("yarn")
You pass SparkConf to SparkContext, or indirectly to SparkSession.

🔹 SparkSession: The Unified Entry Point
Since Spark 2.0, SparkSession became the single entry point for:

Creating DataFrames

Running SQL queries

Accessing catalogs and tables

Connecting to Hive, JDBC, and external formats (CSV, JSON, Parquet, etc.)

🔧 Create a SparkSession:
python
Copy
Edit
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Customer360") \
    .config("spark.some.config.option", "value") \
    .getOrCreate()
✅ Benefits of SparkSession:
Simplifies Spark app setup

Automatically initializes an internal SparkContext (spark.sparkContext)

Ideal for both batch and streaming jobs

Enables Hive support (enableHiveSupport())

🌀 Application Lifecycle
Understanding the Spark application lifecycle helps in optimizing performance and debugging.

📦 Lifecycle Phases:
SparkSession Initialization

Configurations are applied (memory, cores, etc.)

Cluster resources are allocated

Data Processing

Jobs are submitted to the DAG Scheduler

Jobs are split into stages → tasks

Executors process tasks and return results

Execution Monitoring

Progress can be monitored in Spark UI (http://localhost:4040 for local)

Cleanup

Always stop the session when done:

python
Copy
Edit
spark.stop()
✅ Summary
Component	Role
SparkConf	Holds configuration settings
SparkContext	Interface to Spark Core engine (RDD-based access)
SparkSession	Unified entry for DataFrames, SQL, Hive, Catalog
Lifecycle	Init → Execution → Monitoring → Stop

In most modern PySpark projects, you will primarily work with SparkSession, using DataFrame and SQL APIs for all major transformations.

Ready to move on to 3. RDDs (Resilient Distributed Datasets)? 🧠 Let’s continue!

yaml
Copy
Edit

---

Let me know if you'd like:
- A **code demo notebook** for SparkSession vs SparkContext  
- A **diagram of the Spark Application Lifecycle**  
- A downloadable `.md` file or PDF version of this content



