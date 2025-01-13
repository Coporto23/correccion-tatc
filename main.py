import pandas as pd
import re

file_path = r'./input/TATC.xlsx'
output_path = r'./output/TATC.xlsx'
df = pd.read_excel(file_path, header=None)

df[0] = df[0].apply(lambda x: re.sub(r'\D', '', str(x)))

df[0] = df [0].apply(lambda x: x.zfill(12))

df[0] = df [0].apply(lambda x: f"'{x}',")

df.to_excel(output_path, index=False, header=False)


