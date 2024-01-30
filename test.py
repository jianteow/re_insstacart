# -*- coding:utf-8 -*-
import streamlit as st 
import pandas as pd
import numpy as np

def main():

# CSV 파일 경로
    csv_file_path = r'./orders.csv'

# CSV 파일 불러오기
    df_orders = pd.read_csv(csv_file_path)

# 처음 10개 행 출력
    st.write("처음 10개 행:")
    st.write(df_orders.head(10))

# 필요한 열 선택 및 처음 10개 행 출력
    cols = ['order_number', 'order_hour_of_day', 'order_dow']
    result = df_orders[cols].head(10)
    st.write("선택한 열 (order_number, order_hour_of_day, order_dow)의 처음 10개 행:")
    st.write(result)

# 랜덤 데이터 생성
    random_data = np.random.randn(20, 3)
    chart_data = pd.DataFrame(random_data, columns=["order_number", "order_hour_of_day", "order_dow"])

# 바 차트 출력
    st.bar_chart(chart_data)

if __name__ == "__main__":
    main()