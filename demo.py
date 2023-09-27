# デモアプリ

# 必要なライブラリのインポート
import streamlit as st
import pandas as pd
import plotly.express as px

# ページ設定
st.set_page_config(page_title='graph',layout='wide')

# ページタイトル
st.title('Graph App')
st.subheader(データを可視化しよう！)

# ファイル読み込み用ウィジェット作成
upload_file = st.sidebar.file_uploader('csvファイルをアップロードしてください',type=['csv'])
if upload_file:
  df = pd.read_csv(upload_file)
  st.dataframe(df)

# データフレームのカラムリストをリスト型に変換。下で説明。
columns = df.columns.tolist()
# 各カラムのセレクトボックスを作成
x_column = st.selectbox('x軸を選択してください',columns)
y_column = st.multiselect('y軸を選択してください（複数可）',columns)  # y軸は複数個選択可にするために'maltiselect'を使用
z_column = st.selectbox('z軸を選択してください',[None]+columns)  # [None]がリスト型で、df.columnsはpandasのシリーズ型のリスト型だから結合できないため、上述のようにリスト型に変更する必要がある。
# グラフの種類
plot_type = st.radio('グラフの形式を選択してください',['scatter','line','bar'])

# グラフを作成する関数
def create_plot(df,x_column,y_column,z_column,plot_type):
  if plot_type == 'scatter':  # 'scatter'を選択した場合、散布図を作成
    if z_column :  # z軸を選択した場合、3次元プロットを作成
      fig = px.scatter_3d(df,x=x_column,y=y_column[0],z=z_column)
    else:
      fig = px.scatter(df,x=x_column,y=y_column)

  elif plot_type == 'line':   # 'line'を選択した場合、折れ線グラフを作成
    fig = px.line(df,x=x_column,y=y_column)

  elif plot_type == 'bar':   # 'bar'を選択した場合、棒グラフを作成
    fig = px.bar(df,x=x_column,y=y_column, barmode='group')

  return fig

# グラフを表示
st.plotly_chart(create_plot(df,x_column,y_column,z_column,plot_type))
