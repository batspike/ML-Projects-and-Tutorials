import pandas as pd
import numpy as np

data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Sales': [100, 150, 80, 120],
    'Profit_Margin': [0.2, 0.1, 0.4, 0.25]
}

df = pd.DataFrame(data)

df['Total_Profit'] = df['Sales'] * df['Profit_Margin']

print("--- Data Analysis Test ---")
print(df)
print("\nAverage Profit:", df['Total_Profit'].mean())
