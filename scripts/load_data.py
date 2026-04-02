import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="techwiz_db",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

def load_csv(table, file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        cols = ",".join(df.columns)
        values = ",".join(["%s"] * len(row))
        query = f"INSERT INTO {table} ({cols}) VALUES ({values})"
        cursor.execute(query, tuple(row))
    conn.commit()

load_csv("students", "data/students.csv")
load_csv("courses", "data/courses.csv")
load_csv("enrollments", "data/enrollments.csv")
load_csv("payments", "data/payments.csv")
load_csv("engagement", "data/engagement.csv")

cursor.close()
conn.close()
