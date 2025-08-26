import pandas as pd
import psycopg2

# Load CSV data
df = pd.read_csv('social_media_data.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='social_media_db',     # Replace with your DB name
    user='postgres',              # Replace with your username
    password='1230',     # Replace with your password
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS social_media_metrics (
        Post_ID SERIAL PRIMARY KEY,
        Platform VARCHAR(50),
        Date DATE,
        Content_Type VARCHAR(50),
        Likes INT,
        Comments INT,
        Shares INT,
        Reach INT,
        Engagement_Rate FLOAT
    );
""")

# Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO social_media_metrics 
        (Platform, Date, Content_Type, Likes, Comments, Shares, Reach, Engagement_Rate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """, tuple(row[1:]))

conn.commit()
cur.close()
conn.close()

print("✅ Data inserted successfully!")