import numpy as np
import re
import matplotlib.pyplot as plt

# Sample data with Unicode characters mixed in
data = np.array(["23.5", "🔥24.7", "18💧.3", "20.4", "🌟22.8", "NaN", "27🎉.1", "19.6", "❗23.9"])

# Function to clean up data by removing any non-numeric characters and converting to float
def clean_data(arr):
    cleaned_data = []
    for item in arr:
        # Remove non-numeric characters (except dots for decimal points)
        numeric_value = re.sub(r"[^\d.]", "", item)
        try:
            # Convert cleaned string to float
            cleaned_data.append(float(numeric_value))
        except ValueError:
            # Skip values that couldn't be converted to float (like "NaN" or empty strings)
            pass
    return np.array(cleaned_data)

# Clean the data
cleaned_data = clean_data(data)

# Plot the data as a boxplot
plt.boxplot(cleaned_data)
plt.title("Boxplot of Cleaned Data (NumPy)")
plt.ylabel("Values")
plt.show()
