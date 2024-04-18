from pyspark.sql import SparkSession




def sample():
    spark = SparkSession.Builder.appName('Demo').getOrCreate()
    
    df=spark.read.csv('~ip_files/or.csv')

    df.show(5)





