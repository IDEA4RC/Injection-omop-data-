import redivis

iris_table = redivis.organization("Demo").dataset("Iris species").table("Iris")
df = iris_table.to_pandas_dataframe()

