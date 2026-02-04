from pyspark import pipelines as dlt

table_name = spark.conf.get("table_name")

@dlt.table(name=table_name)
def customers():
    return spark.readStream.table("sdp.source_sch.customer")
