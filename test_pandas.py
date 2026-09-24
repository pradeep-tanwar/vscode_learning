import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Score": [80, 90, 85]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage score:", df["Score"].mean())