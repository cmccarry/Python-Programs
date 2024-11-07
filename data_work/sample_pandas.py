import pandas as pd
import matplotlib.pyplot as plt
import re

# Sample data with Unicode characters
data = pd.Series(["23.5", "🔥24.7", "18💧.3", "20.4", "🌟22.8", "NaN", "27🎉.1", "19.6", "❗23.9"])

# Function to clean each entry individually
def clean_value(value):
    # Remove non-numeric characters (except dots for decimal points)
    numeric_value = re.sub(r"[^\d.]", "", str(value))
    try:
        # Convert cleaned string to float
        return float(numeric_value)
    except ValueError:
        # Return NaN if conversion fails
        return pd.NA

# Apply the cleaning function to the series
data = data.apply(clean_value)

# Drop any NaN values that could not be converted to floats
data = data.dropna().astype(float)

# Plot the data as a boxplot
plt.boxplot(data)
plt.title("Boxplot of Cleaned Data (Pandas)")
plt.ylabel("Values")
plt.show()
