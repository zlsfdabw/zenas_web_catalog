# Import python packages
import pandas as pd
import requests
import streamlit as st
from snowflake.snowpark.functions import col

# st.stop()

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

# name_on_order = st.text_input('Name on Smoothie:')
# st.write('The name on your Smoothie will be:', name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("zenas_athleisure_db.products.catalog")
st.dataframe(data=my_dataframe, use_container_width=True)
# st.stop()

# Convert the Snowpark Dataframe to a Pandas Dataframe so we can use the LOC function
df = my_dataframe.to_pandas()
st.dataframe(df)
# st.stop()

sweatsuit_picker = st.selectbox(
    'Pick a sweatsuit color or style:'
    ,df.color_or_style
)

st.stop()
