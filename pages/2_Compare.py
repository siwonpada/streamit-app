import streamlit as st
import requests
import pandas as pd

NUM_PAGE = 10
BE_URL = "https://da39-34-125-154-224.ngrok-free.app/api"

def get_player_data(number: int):
  page = number - 1 
  skip = page * NUM_PAGE
  response = requests.get(f'{BE_URL}/player?skip={skip}&limit={NUM_PAGE}')
  print(f'the number is {number}')
  return response.json()["result"]

def predict(player_data):
  data = {
    "feature": player_data
  }
  response = requests.post(f'{BE_URL}/predict', json=data)
  return int(response.json())

st.set_page_config(
  page_title="HR Comparator",
  page_icon="🆚",
)

st.markdown(
  """
  # Welcome to the HR Comparator! 😊
  
  This web application predicts the number of home runs based the performance of the player and compare them.

  You can write down the player's statistics and predict the number of home runs.
  """
)

player1_df = pd.DataFrame(columns=['Rank', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS'])
player1_df.loc[0] = [1, 0,0,0,0,0,0,0,0,0,0,0,0,0.0,0.0,0.0,0.0]

player2_df = pd.DataFrame(columns=['Rank', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS'])
player2_df.loc[0] = [1, 0,0,0,0,0,0,0,0,0,0,0,0,0.0,0.0,0.0,0.0]

with st.container(border=True):
  edited_df1 = st.data_editor(player1_df, hide_index=True, key='p1')

st.write('VS')

with st.container(border=True):
  edited_df2 = st.data_editor(player2_df, hide_index=True, key='p2')

if st.button('Predict'):
  p1_data = edited_df1.iloc[0].to_dict().values()
  p1_data = list(p1_data)
  for i in range(len(p1_data)-4):
    p1_data[i] = int(p1_data[i])
  for i in range(len(p1_data)-4, len(p1_data)):
    p1_data[i] = float(p1_data[i])
  hr1 = predict(p1_data)

  p2_data = edited_df2.iloc[0].to_dict().values()
  p2_data = list(p2_data)
  for i in range(len(p2_data)-4):
    p2_data[i] = int(p2_data[i])
  for i in range(len(p2_data)-4, len(p2_data)):
    p2_data[i] = float(p2_data[i])
  hr2 = predict(p2_data)

  st.write(f"Predicted HR for Player 1 is {hr1}")
  st.write(f"Predicted HR for Player 2 is {hr2}")
  if hr1 > hr2:
    st.write('The WINNER is Player 1')
  elif hr1 < hr2:
    st.write('The WINNER is Player 2')
  else:
    st.write('Both Players are TIED!')