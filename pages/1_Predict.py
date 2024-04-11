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
  page_title="HR Predictor",
  page_icon="🔮",
)

st.markdown(
  """
  # Welcome to the HR Predictor! 🤗
  
  This web application predicts the number of home runs a Major League Baseball player will hit in a season.

  You can pick the page number from the sidebar to see the player data and predict the number of home runs for the selected player.
  """
)

with st.sidebar:
  number = st.number_input('Page Number', min_value=1, step=1) 

df = pd.DataFrame(get_player_data(number))
df = df.drop(labels=['id'], axis=1)
df.insert(0, 'Select', False)

edited_df = st.data_editor(df, hide_index=True, disabled = ['Rank', 'PLAYER', 'TEAM', 'Position', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS'])

st.button("Reset", type="primary")

if st.button('Predict'):
  for i in range(len(edited_df)):
    if edited_df.iloc[i, 0]:
      player_name = edited_df.iloc[i, 2]
      player_data = edited_df.drop(['PLAYER', 'TEAM', 'Position'], axis=1).iloc[i, 1:].to_dict().values()
      player_data = list(player_data)
      for i in range(len(player_data)-4):
        player_data[i] = int(player_data[i])
      for i in range(len(player_data)-4, len(player_data)):
        player_data[i] = float(player_data[i])
      hr = predict(player_data)
      st.write(f"Predicted HR for {player_name} is {hr}")



