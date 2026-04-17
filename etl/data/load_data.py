import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/movieflix")

pd.read_csv("data/lake/movies.csv").to_sql("movies", engine, if_exists="replace", index=False)
pd.read_csv("data/lake/users.csv").to_sql("users", engine, if_exists="replace", index=False)
pd.read_csv("data/lake/ratings.csv").to_sql("ratings", engine, if_exists="replace", index=False)

print("Carga concluída")