from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.functions import count
import pyspark.sql.functions as functions

spark = SparkSession\
    .builder\
    .appName('SamplePySparkDev')\
    .getOrCreate()
    # .config()

#esconder infos do console
spark.sparkContext.setLogLevel("ERROR")

# log4j = spark.sparkContext._jvm.org.apache.log4j
# log4j.LogManager.getRootLogger().setLevel(log4j.Level.ERROR)
#esconder infos do console
# spark.sparkContext.setLogLevel("ERROR")
# ss = SparkSession.newSession(SparkSession)
# df1 = SparkSession.createDataFrame(ss, [("teste", 1)])

schema = "VendaId INT, UserID INT, Nome STRING, Produto STRING, ProdutoID INT, Valor INT"

# dados =

df1 = spark.createDataFrame([
    (1, 10, "pedro", "Caneta", 532, 10),
    (2, 15, "maria", "Toalha", 678, 20),
    (3, 12, "jose", "Caneta", 532, 12),
    (4, 10, "pedro", "Caneta", 532, 13),
    (5, 113, "joão", "Caneta", 532, 9),
    (6, 113, "joão", "Toalha", 678, 23),
    (7, 113, "joão", "Prato", 555, 47),
    (8, 113, "eunice", "Toalha", 678, 27),
], schema)

soma = df1.groupBy("ProdutoID")\
    .agg(
        count("VendaId").alias("totalVendas"),
        sum("Valor").alias("totalValor"),
        # functions.array_distinct("Produto").alias("produto")
        # functions.col("Produto")
        # functions.count("VendaId").as("totalVendas")
    )
    # .agg(sum("Valor"))\


# df1.show()
soma.show()

# soma.select("totalVendas", functions.expr("totalValor * 0.2").alias("20%"), "Produto")\
#     .where(functions.col("totalVendas") > 3)\
#     .show()