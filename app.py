import streamlit as st
import pickle
import pandas as pd
st.write("djd")
pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
'Chennai Super Kings',
'Delhi Daredevils',
'Kings XI Punjab',
'Kolkata Knight Riders',
'Mumbai Indians',
'Rajasthan Royals',
'Royal Challengers Bangalore',
'Sunrisers Hyderabad'
]

cities = [
'Hyderabad',
'Bangalore',
'Mumbai',
'Indore',
'Kolkata',
'Delhi',
'Chandigarh',
'Jaipur',
'Chennai',
'Cape Town',
'Port Elizabeth',
'Durban',
'Centurion',
'East London',
'Johannesburg',
'Kimberley',
'Bloemfontein',
'Ahmedabad',
'Cuttack',
'Nagpur',
'Dharamsala',
'Visakhapatnam',
'Pune',
'Raipur',
'Ranchi',
'Abu Dhabi',
'Sharjah',
'Mohali',
'Bengaluru'
]

st.title("IPL Win Predictor")
col1,col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Batting Team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams))

city = st.selectbox('Host City', sorted(cities))
target = st.number_input('Target Score')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Overs Completed')

with col5:
    wickets = st.number_input('Wickets Out')

if st.button('Predict Probability'):

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets

    crr = score / overs if overs > 0 else 0

    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wickets_left],
        'crr':[crr],
        'rrr':[rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    st.header(f"{batting_team} Win Probability : {round(win*100)}%")
    st.header(f"{bowling_team} Win Probability : {round(loss*100)}%")
