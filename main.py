import pandas as pd
import numpy as np 
import path

# def df_pdt_params():
#     path = r"C:\Users\ssgro\OneDrive\Documents\CleanData\1.PDT_parameter.csv"
#     df = pd.read_csv(path)
#     print (df.head(17))

# def df_pdt_qc_product():
#     path = r"C:\Users\ssgro\OneDrive\Documents\CleanData\2.PDT_QC_product.csv"
#     df = pd.read_csv(path, on_bad_lines='skip', low_memory=False)
#     print (df)

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_column', 500)

# df_pdt_params()
# df_pdt_qc_product()

def read_df(path):
    df = pd.read_csv(path, on_bad_lines='skip', low_memory=False)
    return df

path_pdt_params = r".\1.PDT_parameter.csv"
path_qc_product = r".\2.PDT_QC_product.csv"
# path_feed_speed = r".\3.FeedRawMaterial_Speed.csv"
# path_feed_material = r".\4.FeedRawMaterial_Quality_Data.csv"
# path_pdt_form = r"C:\Users\ssgro\OneDrive\Documents\CleanData\5.Production cleanOnlyPDT.csv"

# print (read_df(path_qc_product).head(17))

def reshape(df):
    return 

def main():
    df = read_df(path_pdt_params)
    print(df)

if __name__ == '__main__':
    main()