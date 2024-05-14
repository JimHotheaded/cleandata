import pandas as pd
import numpy as np 
import path

path_pdt_params = r".\1.PDT_parameter.csv"
path_qc_product = r".\2.PDT_QC_product.csv"
# path_feed_speed = r".\3.FeedRawMaterial_Speed.csv"
# path_feed_material = r".\4.FeedRawMaterial_Quality_Data.csv"
# path_pdt_form = r".\5.Production cleanOnlyPDT.csv"

def read_df(path):
    df = pd.read_csv(path, on_bad_lines='skip', low_memory=False)
    return df

index_df_pdt = 'DateAndTime'
columns_df_pdt = 'TagName'
values_df_pdt = 'Val'

def reshape(df,index,columns,value):
    df = df.pivot_table(index=index,columns=columns,values=value)
    return df

columns_drop_pdt = [r'Ballmill\Bag_Filter_Pressure']

def drop_column(df,columns):
    df = df.drop(columns=columns)
    return df

def export_excel(df):
    file_path = r".\Output.csv"
    export = df.to_csv(file_path)
    print(f"DataFrame has been saved to {file_path}")
    return export

tolerance = pd.Timedelta(minutes=10)

def join_df(df1,df2,left_index,right_index,tolerance,direction):
    df = pd.merge_asof(df1,df2,left_index=left_index, right_index=right_index, tolerance=tolerance, direction=direction)
    return df

def main():
    df1 = read_df(path_pdt_params)
    df2 = read_df(path_qc_product)
    df1 = reshape(df1,index_df_pdt,columns_df_pdt,values_df_pdt)
    df1 = drop_column(df1,columns_drop_pdt)
    # df = join_df(df1,df2,True,True,tolerance,'nearest')
    # export_excel(df)
    print(df1.dtypes)

# main
if __name__ == '__main__':
    main()
    