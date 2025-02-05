from fastapi import FastAPI
import snowflake.connector

app = FastAPI()

@app.get("/logs")
def get_logs():
    conn = snowflake.connector.connect(user='user', password='password', account='account')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM processed_logs LIMIT 10")
    logs = cursor.fetchall()
    return {"logs": logs}
