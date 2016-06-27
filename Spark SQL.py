## 2. Register DataFrame as a table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
tables = sqlCtx.tableNames()
print(tables)