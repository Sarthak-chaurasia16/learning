import pandas as pd
data = {
    'Name':['Sarthak','Aman','Anant'],
    'Age':[20,21,19],
    'City':['Jabalpur', 'Indore', 'Gwalior']
}
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index = False)