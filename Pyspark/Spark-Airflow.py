import pyspark
from airflow import DAG
from pyspark.sql import SparkSession
from datetime import timedelta, datetime
from pyspark import SparkConf

conf = SparkConf().setAll([
    ("spark.driver.memory","2g"),
    ("spark.executor.memory","6g"),
    ("spark.executor.memoryOverhead","1g"),
    ("spark.master","local[*]"),
    ("spark.executor.cores",4),
    ("spark.executor.instances",4),
    ("spark.default.parallelism",16),
])

