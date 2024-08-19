import pandas as pd
import streamlit as st


def transform_dataframe(df):
    # 将 DataFrame 转置（即行列转换）
    transformed_df = df.T

    # 重置索引并删除旧的索引列
    transformed_df = transformed_df.reset_index(drop=True)

    # 将第一行设置为新的表头
    transformed_df.columns = transformed_df.iloc[0]

    # 删除第一行（因为它现在是表头）
    transformed_df = transformed_df.iloc[1:].reset_index(drop=True)

    return transformed_df

def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    else:
        st.error("不支持的文件格式。请上传 .csv 或 .xlsx 文件。")
        return None