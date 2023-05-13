import streamlit as st

import pandas as pd

# Reemplaza 'archivo_excel.xlsx' con el nombre real del archivo y la ruta
file_path = 'C:/Users/Sophia/Documents/2023/CODING/streamlit/supermarkt_sales.xlsx'

# Lee el archivo Excel en un DataFrame
df = pd.read_excel(file_path,
	engine='openpyxl',
	sheet_name='Sales',
	skiprows=3,
	usecols='B:P',
	nrows=1000,
)

st.write(df)
