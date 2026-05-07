import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the number of rows
num_rows = 1000

# Generate data
data = {
    # Megapixels (8 to 200)
    'camera': np.random.randint(8, 201, size=num_rows),
    # Age in years (0 to 3)
    'age': np.random.randint(0, 4, size=num_rows),
    'ram': np.random.choice([4, 6, 8, 12, 16], size=num_rows),  # RAM in GB
    # CPU benchmark score (40 to 100)
    'cpu_score': np.random.randint(40, 101, size=num_rows),
    # SD card slot (0 = no, 1 = yes)
    'slot_sd': np.random.randint(0, 2, size=num_rows),
    # Number of SIMs
    'sims': np.random.choice([1, 2], size=num_rows),
    # Price in INR (₹8,000 to ₹70,000)
    'price': np.random.randint(8000, 70001, size=num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("smartphone_data.csv", index=False)

# Display first few rows
print(df.head())
