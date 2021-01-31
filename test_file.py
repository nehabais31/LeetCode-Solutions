import sys
from pyspark import SparkContext

# Print the script name
print("PySpark Script: ", sys.argv[0])

# Create a spark context and print some information about the context object
sc = SparkContext()
print(sc.version)
print(sc.pythonVer)
print(sc.master)

# Free the spark context object
sc.stop()
print("end")