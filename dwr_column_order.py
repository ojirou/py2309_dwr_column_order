import pandas as pd
import subprocess
excel_file = "sample_columns_order/sample.xlsx"
new_excel_file = "sample_columns_order/sample_converted.xlsx"
column_count = 4
new_column_order=['x'+str(i//2+1) if i % 2 == 0 else 'y' +str(i//2+1) for i in range(column_count)]
df=pd.read_excel(excel_file, header=0)
new_df=df[new_column_order]
new_df.to_excel(new_excel_file, index=False)
new_df_loaded=pd.read_excel(new_excel_file)
subprocess.Popen(["start", "", new_excel_file], shell=True)