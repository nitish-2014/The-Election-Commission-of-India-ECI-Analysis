import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine('postgresql://postgres:1230@localhost:5432/social_media_db')

# Load data from database
query = "SELECT * FROM social_media_metrics;"
df = pd.read_sql(query, engine)

# Clean column names
df.columns = df.columns.str.strip()

# Display column names and first few rows for debugging
print("Columns in DataFrame:", df.columns.tolist())
print(df.head())

# Check if required columns exist
if 'Platform' in df.columns and 'Likes' in df.columns:
    # Group and calculate average likes
    avg_likes = df.groupby('Platform')['Likes'].mean()

    # Plot the results
    plt.figure(figsize=(8, 5))
    avg_likes.plot(kind='bar', color='skyblue')
    plt.title('Average Likes per Platform')
    plt.ylabel('Average Likes')
    plt.xlabel('Platform')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("❌ Required columns 'Platform' and/or 'Likes' not found in the dataset.")