import pandas as pd
import numpy as np 

path_pdt_params = r".\1.PDT_parameter.csv"
path_qc_product = r".\2.PDT_QC_product.csv"
# path_feed_speed = r".\3.FeedRawMaterial_Speed.csv"
# path_feed_material = r".\4.FeedRawMaterial_Quality_Data.csv"
# path_pdt_form = r".\5.Production cleanOnlyPDT.csv"

# def read_df(path):
#     df = pd.read_csv(path, on_bad_lines='skip', low_memory=False)
#     return df

# index_df_pdt = 'DateAndTime'
# columns_df_pdt = 'TagName'
# values_df_pdt = 'Val'

# def reshape(df,index,columns,value):
#     df = df.pivot_table(index=index,columns=columns,values=value)
#     return df

# columns_drop_pdt = [r'Ballmill\Bag_Filter_Pressure']

# def drop_column(df,columns):
#     df = df.drop(columns=columns)
#     return df

# def export_excel(df):
#     file_path = r".\Output.csv"
#     export = df.to_csv(file_path)
#     print(f"DataFrame has been saved to {file_path}")
#     return export

# tolerance = pd.Timedelta(minutes=10)

# def join_df(df1,df2,left_index,right_index,tolerance,direction):
#     df = pd.merge_asof(df1,df2,left_index=left_index, right_index=right_index, tolerance=tolerance, direction=direction)
#     return df

def main():
    df_pdt_params = pd.read_csv(path_pdt_params, on_bad_lines='skip', low_memory=False)
    df_pdt_qc_products = pd.read_csv(path_qc_product, on_bad_lines='skip', low_memory=False)
    df_pivot2 = df_pdt_params.pivot_table(index='DateAndTime',columns='TagName',values='Val')
    columns_drop_pdt = [r'Ballmill\Bag_Filter_Pressure']
    df_pdt_params_clean = df_pivot2.drop(columns=columns_drop_pdt)
    column_drop_qc = ['id','DateTimeTrue']
    df_pdt_qc_products_clean = df_pdt_qc_products.drop(columns=column_drop_qc)
    new_column_names = {'DateTime': 'DateAndTime'}
    df_pdt_qc_products_clean = df_pdt_qc_products_clean.rename(columns=new_column_names)
    df_pdt_qc_products_clean['DateAndTime'] = pd.to_datetime(df_pdt_qc_products_clean['DateAndTime'], errors = 'coerce')
    df_pdt_params_clean.reset_index(inplace=True)
    df_pdt_params_clean['DateAndTime'] = pd.to_datetime(df_pdt_params_clean['DateAndTime'])
    df_pdt_params_clean.set_index('DateAndTime', inplace=True)    
    df_pdt_params_clean.sort_index(inplace=True)
    df_pdt_qc_products_clean.sort_index(inplace=True)
    df_pdt_qc_products_clean = df_pdt_qc_products_clean.dropna(subset=['DateAndTime'])
    merged_df = pd.merge_asof(df_pdt_params_clean, df_pdt_qc_products_clean.sort_values('DateAndTime'), on='DateAndTime', tolerance=pd.Timedelta(hours=8), direction='forward')
    file_path = r".merge_df_test.csv"
    merged_df.to_csv(file_path)
    print(f"DataFrame has been saved to {file_path}")

# main
if __name__ == '__main__':
    main()
    