from color_data import days_colors
from collections import Counter
import psycopg2

# Step 1: Calculate color frequencies
all_colors = []
for day in days_colors.values():
    all_colors.extend(day)

color_freq = Counter(all_colors)  # Count frequencies efficiently

db_params = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

# Step 3: Connect to PostgreSQL and save the data
try:
    # Establish connection
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Create table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(50) PRIMARY KEY,
        frequency INTEGER NOT NULL
    );
    """
    cursor.execute(create_table_query)

    # Insert data
    insert_query = """
    INSERT INTO color_frequencies (color, frequency)
    VALUES (%s, %s)
    ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency;
    """
    for color, freq in color_freq.items():
        cursor.execute(insert_query, (color, freq))

    # Commit the transaction
    connection.commit()
    print("Colors and their frequencies have been saved to the database successfully!")

except psycopg2.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Database connection closed.")

