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
df = cnx.query("select color_or_style, '@zenas_athleisure_db/products/sweatsuits/' || file_name as stg_img_path from zenas_athleisure_db.products.catalog group by 1,2")

# st.dataframe(df)
# st.stop()

# df = sdf.to_pandas()
# st.stop()
# df = session.sql("select * from table()").to_pandas()


# cnx = st.connection("snowflake")
# session = cnx.session()
# my_dataframe = session.table("zenas_athleisure_db.products.catalog")
# # st.dataframe(data=my_dataframe, use_container_width=True)
# # st.stop()

# # Convert the Snowpark Dataframe to a Pandas Dataframe so we can use the LOC function
# df = my_dataframe.to_pandas()
# st.dataframe(data=df, use_container_width=True)
# # st.stop()

sweatsuit_picker = st.selectbox(
    'Pick a sweatsuit color or style:'
    ,df["COLOR_OR_STYLE"]
)


# st.stop()

if sweatsuit_picker:
    file_url = df.loc[df['COLOR_OR_STYLE'] == sweatsuit_picker, 'stg_img_path'].iloc[0]
    # st.write(file_url)
    st.image(file_url)
    # render_image(file_url)

st.stop()
