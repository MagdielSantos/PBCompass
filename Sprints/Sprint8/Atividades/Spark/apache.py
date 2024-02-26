from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand
from pyspark.sql.functions import when
import random
from pyspark.sql.functions import lit

# Iniciar sessão
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv('nomes_aleatorios.txt', header=False, inferSchema=True)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 1/3, "Fundamental")
                                           .when(rand() < 2/3, "Médio")
                                           .otherwise("Superior"))


paises_americados_sul = ["Brasil", "Argentina", "Colômbia", "Chile", "Peru", "Venezuela", "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn("Pais", 
                               when(rand() <= 0.07, paises_americados_sul[0])
                               .when((rand() > 0.07) & (rand() <= 0.1), paises_americados_sul[1])
                               .when((rand() > 0.1) & (rand() <= 0.2), paises_americados_sul[2])
                               .when((rand() > 0.2) & (rand() <= 0.3), paises_americados_sul[3])
                               .when((rand() > 0.3) & (rand() <= 0.38), paises_americados_sul[4])
                               .when((rand() > 0.38) & (rand() <= 0.4), paises_americados_sul[5])
                               .when((rand() > 0.4) & (rand() <= 0.5), paises_americados_sul[6])
                               .when((rand() > 0.5) & (rand() <= 0.6), paises_americados_sul[7])
                               .when((rand() > 0.6) & (rand() <= 0.69), paises_americados_sul[8])
                               .when((rand() > 0.69) & (rand() <= 0.7), paises_americados_sul[9])
                               .when((rand() > 0.7) & (rand() <= 0.8), paises_americados_sul[10])
                               .when(rand() > 0.8, paises_americados_sul[11])
                               .otherwise(paises_americados_sul[12]))

df_nomes = df_nomes.withColumn("AnoNascimento", (rand(seed=42) * (2010 - 1945) + 1945).cast("int"))

df_nomes.createOrReplaceTempView("pessoas")

geracao_classificacao = """
  CASE
    WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
    WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
    WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
    WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
    ELSE 'Outros'
  END
"""

consulta = """
  SELECT Pais, {0} AS Geracao, COUNT(*) AS Quantidade
  FROM pessoas
  GROUP BY Pais, {0}
  ORDER BY Pais, {0}, Quantidade
""".format(geracao_classificacao)

df_resultado = spark.sql(consulta)

df_resultado.show()


