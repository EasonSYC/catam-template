import pandas as pd
import numpy as np

file_list: list[str] = [
]

for file_name in file_list:
    df: pd.DataFrame = pd.read_csv(f'data/{file_name}.csv', index_col = 0)
    df.to_latex(f'tex/{file_name}.tex')