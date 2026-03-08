import pandas as pd
data = {
    "Name":["Ram","Shyam","Tre"],
    "Age":[32,33,34]
}
d= pd.DataFrame(data)

print(d)
d.to_json("output.json", index=False)