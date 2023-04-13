import streamlit
import snowflake.connector
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select FILE_URL as file_URL from directory(@SUPER_MARKET_SALES.RECORDS.internal_stage_img)")
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
streamlit.write(df)


streamlit.image(
      df[0],
      width=400,
      caption= product_caption
  )


