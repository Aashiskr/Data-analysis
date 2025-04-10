import pandas as pd
data = pd.read_csv("data.csv")


m5=data.head(5)
m5.to_csv("5rows.csv")


print(type(data))


specific_sym_sec = data.iloc[:, [0, 2]] # specific_sym_sec = data[["symbol", "security"]]


skip = [0, 2]  # Example: dropping the first and third columns
specific_sym_sec = data.drop(skip, axis=0)

specific_sym_sec.to_csv("specific_sym_sec.csv")

data = data.astype({"today": float})

describe = data.describe()
describe.to_csv("describe.csv")

sorted = data.sort_values(by="avg volume", ascending=False)
sorted.to_csv("sorted.csv")