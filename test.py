import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob"],
    "Age": [30, 25],
    "City": ["New York", "Los Angeles"]
}
df = pd.DataFrame(data)

# Define a function to highlight the second row (index 1)
def highlight_second_row(row):
    return ['background-color: yellow' if row.name == 1 else '' for _ in row]

# Apply the style
styled_df = df.style.apply(highlight_second_row, axis=1)

# Save to Excel with styling
styled_df.to_excel("example.xlsx", index=False, engine='openpyxl')

df.to_csv("ex.csv", index=False)

