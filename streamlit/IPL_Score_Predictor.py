import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("xgb_IPL_final_score_model.pkl")

# Title
st.title("🏏 IPL Final Score Predictor")

# List of teams for the dropdown menu
teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Sunrisers Hyderabad', 'Punjab Kings',
       'Royal Challengers Bangalore', 'Delhi Capitals',
       'Lucknow Super Giants', 'Gujarat Titans']

# List of venues for the dropdown menu
venues = ['Chinnaswamy Stadium,Bengaluru', 'PCA IS Bindra Stadium,Mohali',
       'Arun Jaitley Stadium,Delhi', 'Wankhede Stadium,Mumbai',
       'Eden Gardens,Kolkata', 'Sawai Mansingh Stadium,Jaipur',
       'Rajiv Gandhi Stadium,Hyderabad', 'MA Chidambaram Stadium,Chennai',
       'DY Patil Stadium,Navi Mumbai', 'Newlands', "St George's Park",
       'Kingsmead', 'SuperSport Park', 'Buffalo Park',
       'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium,Mumbai',
       'Narendra Modi Stadium,Ahmedabad', 'Barabati Stadium',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'HCA Stadium,Dharamsala', 'ACA-VDCA Cricket Stadium,Visakhapatnam',
       'MCA Stadium,Pune',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex',
       'Sheikh Zayed Stadium,Abu Dhabi', 'Sharjah Cricket Stadium',
       'Dubai International Cricket Stadium', 'Holkar Cricket Stadium',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Barsapara Cricket Stadium, Guwahati',
       'Maharaja Yadavindra Singh Stadium, Mullanpur']

# Team selection
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted([t for t in teams if t != batting_team]))

# Venue
venue = st.selectbox('Select Venue', sorted(venues))



# Match details input
col3, col4, col5 = st.columns(3)
with col3:
    team_runs = st.number_input('Current Team Score', min_value=0)
with col4:
    overs = st.number_input('Overs Completed (works for over>5))',min_value=6,max_value=20)
with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10)

last_five = st.number_input('Runs scored in last 5 overs')


# Prediction
if st.button('Predict Final Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    current_run_rate = team_runs/overs

    # Build input dataframe
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'venue': [venue],
        'team_runs': [team_runs],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'current_run_rate': [current_run_rate],
        'last_five': [last_five]
    })

    # Predict final score
    predicted_score = model.predict(input_df)[0]
    st.header(f"🏆 Predicted Final Score: {int(predicted_score)}")



