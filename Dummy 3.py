
import os
import urllib.request
import ssl


data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

data_dir1 = "hadoop/bin"
os.makedirs(data_dir1, exist_ok=True)

urls_and_paths = {
    "https://raw.githubusercontent.com/saiadityaus1/SparkCore1/master/test.txt": os.path.join(data_dir, "test.txt"),
    "https://github.com/saiadityaus1/SparkCore1/raw/master/winutils.exe": os.path.join(data_dir1, "winutils.exe"),
    "https://github.com/saiadityaus1/SparkCore1/raw/master/hadoop.dll": os.path.join(data_dir1, "hadoop.dll")
}

# Create an unverified SSL context
ssl_context = ssl._create_unverified_context()

for url, path in urls_and_paths.items():
    # Use the unverified context with urlopen
    with urllib.request.urlopen(url, context=ssl_context) as response, open(path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
import os, urllib.request, ssl; ssl_context = ssl._create_unverified_context(); [open(path, 'wb').write(urllib.request.urlopen(url, context=ssl_context).read()) for url, path in { "https://github.com/saiadityaus1/test1/raw/main/df.csv": "df.csv", "https://github.com/saiadityaus1/test1/raw/main/df1.csv": "df1.csv", "https://github.com/saiadityaus1/test1/raw/main/dt.txt": "dt.txt", "https://github.com/saiadityaus1/test1/raw/main/file1.txt": "file1.txt", "https://github.com/saiadityaus1/test1/raw/main/file2.txt": "file2.txt", "https://github.com/saiadityaus1/test1/raw/main/file3.txt": "file3.txt", "https://github.com/saiadityaus1/test1/raw/main/file4.json": "file4.json", "https://github.com/saiadityaus1/test1/raw/main/file5.parquet": "file5.parquet", "https://github.com/saiadityaus1/test1/raw/main/file6": "file6", "https://github.com/saiadityaus1/test1/raw/main/prod.csv": "prod.csv", "https://github.com/saiadityaus1/test1/raw/main/state.txt": "state.txt", "https://github.com/saiadityaus1/test1/raw/main/usdata.csv": "usdata.csv"}.items()]

# ======================================================================================

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import sys

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path

os.environ['JAVA_HOME'] = r''

conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host","localhost").set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.getOrCreate()

spark.read.format("csv").load("data/test.txt").toDF("Success").show(20, False)


##################🔴🔴🔴🔴🔴🔴 -> DONT TOUCH ABOVE CODE -- TYPE BELOW ####################################

print()


#############################################################################################################################




#############################################################################################################################


################################## LIST OF NUMBERS ############################################

print('################################## LIST OF NUMBERS ############################################')

print()

lst1 = [23, 36, 99, 78, 900, 1258, 3924, 759, 483, 353]

rdd = sc.parallelize(lst1)

print()
print('=====================RAW DATA =========================')
print(lst1)
print()

addlst1 = rdd.map( lambda x : x + 50000)

print()
print('=====================ADD DATA =========================')
print(addlst1.collect())
print()

sublst1 = rdd.map( lambda x : x - 50000)

print()
print('=====================SUB DATA =========================')
print(sublst1.collect())
print()

mullst1 = rdd.map( lambda x : x * 50000)

print()
print('=====================MUL DATA =========================')
print(mullst1.collect())
print()

divlst1 = rdd.map( lambda x : x / 50000)

print()
print('=====================DIV DATA =========================')
print(divlst1.collect())
print()

######################################################


filt1 = rdd.filter( lambda x : x > 1000)

print()
print('=====================FILT 1 DATA =========================')
print(filt1.collect())
print()

filt2 = rdd.filter( lambda x : x < 1000)

print()
print('=====================FILT 2 DATA =========================')
print(filt2.collect())
print()

filt3 = rdd.filter( lambda x : 500 <= x <= 1000)

print()
print('=====================FILT 3 DATA =========================')
print(filt3.collect())
print()


filt4 = rdd.filter( lambda x : x >= 500 and x <= 1000)

print()
print('=====================FILT 4 DATA =========================')
print(filt4.collect())
print()

filt5 = rdd.filter ( lambda x : x <= 500 or x>= 1000)


print()
print('=====================FILT 5 DATA =========================')
print(filt5.collect())
print()

#################################LIST OF STRINGS ################################################

print('################################## LIST OF STRINGS ############################################')

print()


lstr1 = ["ARSENAL FC" , "BARCELONA FC" , "Tottenhum FC" , "Real Madrid FC" , "EAST BENGAL FC", "Mohun Bagan Supergiants FC", "KKR", "CSK" , "MI"]

print()
print('==================== RAW DATA ==================')
print()
print(lstr1)
print()

rdd = sc.parallelize(lstr1)

con1 = rdd.map( lambda x : x + " Franchise " )

print()
print('==================== CON DATA ==================')
print()
print(con1.collect())
print()

lstrin = rdd.filter( lambda x : "FC" in x)

print()
print('==================== LIST IN DATA ==================')
print()
print(lstrin.collect())
print()

rep1 = rdd.map( lambda x : x.replace ("FC" , "Football Club"))

print()
print('==================== REP DATA ==================')
print()
print(rep1.collect())
print()

################################### MAP SPLIT ##############################################

print()
print ('################################### MAP SPLIT ##############################################')
print()

lstr2 = ["A*B~C", "B~C*D", "C~A~B", "B*D*C"]


print()
print('==================== RAW DATA ==================')
print()
print(lstr2)
print()

rdd = sc.parallelize(lstr2)

splt1 = rdd.flatMap( lambda x : x.split("~"))

print()
print('==================== SPLIT ~ DATA ==================')
print()
print(splt1.collect())
print()

"""
splt2 = rdd.flatMap( lambda x : x.split("*"))

print()
print('==================== SPLIT * DATA ==================')
print()
print(splt2.collect())
print()

"""

splt3 = splt1.flatMap( lambda x : x.split("*"))

print()
print('==================== Output DATA ==================')
print()
print(splt3.collect())
print()

######################### Scenerio 1 ##################################

# USING FOREACH PRINT

data = [
    "State->TN,City->Chennai",
    "State->UP,City->Lucknow"
]

"""
 Expected O/P - 
 
[TN ,UP]
[ Chennai , Lucknow]
 
"""

rdd = sc.parallelize(data)

print()
print('=========INPUT DATA ==============')
print()
print(data)
print()

splt4 = rdd.flatMap( lambda x : x.split(","))

print()
print('=========SPLIT DATA ==============')
print()
splt4.foreach(print)
print()

statedata = splt4.filter( lambda x : 'State' in x)
print()
print('=========STATE DATA ==============')
print()
statedata.foreach(print)
print()

citydata = splt4.filter( lambda x : 'City' in x)
print()
print('========= CITY DATA ==============')
print()
citydata.foreach(print)
print()

staterep = statedata.map( lambda x : x.replace("State->", ""))

print()
print('=========STATE DATA ==============')
print()
staterep.foreach(print)
print()

cityrep = citydata.map( lambda x : x.replace("City->", ""))

print()
print('======== CITY DATA ==============')
print()
cityrep.foreach(print)
print()


#########################################################  DATAFRAME



csvdf = spark.read.format("csv").option("header", "true").load("C:/Users/Shubhayu/Downloads/YOUTUBE/custom_large_file.csv")

csvdf.show()


from pyspark.sql.window import Window
from pyspark.sql.functions import dense_rank, col
# Create Spark session
# spark = SparkSession.builder.appName("NthHighestSalary").getOrCreate()

# Sample data
data = [
    ("Alice", 5000),
    ("Bob", 7000),
    ("Charlie", 7000),
    ("David", 6000),
    ("Eve", 8000)
]
columns = ["name", "salary"]

df = spark.createDataFrame(data, columns)

# Define Window spec ordered by salary descending
windowSpec = Window.orderBy(col("salary").desc())

# Add rank
ranked_df = df.withColumn("rank", dense_rank().over(windowSpec))

# Define N
n = 2  # Change this value to get Nth highest

# Filter Nth highest salary
nth_highest = ranked_df.filter(col("rank") == n)

nth_highest.show()


