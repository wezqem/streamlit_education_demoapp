import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='graph', page_icon=':dog:',layout='wide')

st.title('Graph App')
st.markdown("""
#### データを可視化しよう！
"""
)

upload_file = st.sidebar.file_uploader('csvファイルをアップロードしてください',type=['csv'])
if upload_file is not None:
  df = pd.read_csv(upload_file)
  st.dataframe(df)


columns = df.columns.tolist()
x_column = st.selectbox('x軸を選択してください',columns)
y_column = st.multiselect('y軸を選択してください（複数可）',columns)
z_column = st.selectbox('z軸を選択してください',[None]+columns)
plot_type = st.radio('グラフの形式を選択してください',['scatter','line','bar'])

def create_plot(df,x_column,y_column,z_column,plot_type):
  if plot_type == 'scatter':
    if z_column :
      fig = px.scatter_3d(df,x=x_column,y=y_column[0],z=z_column)
    else:
      fig = px.scatter(df,x=x_column,y=y_column)

  elif plot_type == 'line':
    fig = px.line(df,x=x_column,y=y_column)

  elif plot_type == 'bar':
    fig = px.bar(df,x=x_column,y=y_column)

  return fig

plot = create_plot(df,x_column,y_column,z_column,plot_type)

st.plotly_chart(plot)
