
import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query. # Loads DB on site load
df = conn.query('SELECT * FROM your_table_name;', ttl="10m")

# Print Unique Users 
# for row in df.user.unique():
#     st.write(f"{row} is unique")

option = st.selectbox("Employee",df.user.unique(),index=None,placeholder="Select User")

st.write('You selected:', option)

# df['date2'] = pd.to_datetime(df['times']) - pd.to_timedelta(7, unit='d')
# df2 = df.groupby(['user', pd.Grouper(key='date2', freq='W-MON')])['hours'].sum().reset_index().sort_values('date2')
df2 = "hi2"

#Generate Page from selection
if option == None:
    pass
    ##Load All data
    st.write("Debug:: ALL",df2)
    
else:
    ##Load Name data
    st.write(df.loc[df['user'] == option])