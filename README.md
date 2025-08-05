# IPL Score Prediction

## Project Overview
This project focuses on predicting the final score of IPL (Indian Premier League) cricket matches using machine learning. Score prediction in cricket is crucial for strategic decision-making during matches, helping teams set realistic targets and plan their batting approach. By analyzing current match situations, the model provides accurate predictions of what the final score might be.

## Problem Statement
The goal is to predict the final score of an IPL team's first innings based on the current match situation, including factors like current runs, overs completed, wickets lost, venue characteristics, and team performance patterns.

## Dataset
The project uses comprehensive IPL match data, which includes information about:
- **Match details** (match ID, date, teams, venue, toss winner)
- **Ball-by-ball data** (runs scored, wickets taken, overs bowled)
- **Team statistics** (cumulative runs, balls faced, wickets lost)
- **Venue information** (different cricket stadiums and their characteristics)
- **Team performance** (batting team, bowling team, current run rate)

## Project Structure
```
├── IPL_Score_Prediction.ipynb                    # Main analysis notebook
├── streamlit/
│   ├── IPL_Score_Predictor.py                   # Streamlit web application
│   └── xgb_IPL_final_score_model.pkl           # Trained XGBoost model
├── Dataset/
│   ├── IPL_first_innings.csv                   # IPL 1st Innings ball by ball dataset       
└── README.md
```

## Features
- **Exploratory Data Analysis (EDA)**: Comprehensive analysis of IPL match data to identify scoring patterns and trends
- **Data Preprocessing**: Handling missing values, feature engineering, and creating meaningful predictors
- **Machine Learning Model**: XGBoost Regressor model to predict final scores with high accuracy
- **Interactive Web Application**: Streamlit-based interface for real-time score prediction during matches

## Key Insights from EDA
- Match venues significantly impact scoring patterns
- Team combinations affect final scores differently
- Current run rate and wickets remaining are strong predictors
- Runs scored in recent overs indicate momentum and final score potential
- Different teams perform differently at various venues
- Ball-by-ball progression shows clear patterns for score prediction

## Model Performance
The XGBoost Regressor model achieves excellent accuracy in predicting IPL final scores by considering multiple factors including team strength, venue characteristics, current match situation, and historical performance patterns.

## How to Run the Project

### Prerequisites
- Python 3.7+
- Required libraries: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, streamlit, joblib

### Installation
```bash
# Clone the repository (if applicable)
git clone <repository-url>

# Install required packages
pip install pandas numpy scikit-learn xgboost matplotlib seaborn streamlit joblib
```

### Running the Analysis Notebook
```bash
jupyter notebook IPL_Score_Prediction.ipynb
```

### Running the Streamlit App
```bash
cd streamlit
streamlit run IPL_Score_Predictor.py
```

## Using the Streamlit Application
1. **Select Teams**: Choose the batting and bowling teams from dropdown menus
2. **Choose Venue**: Select the cricket stadium where the match is being played
3. **Enter Match Situation**: 
   - Current team score
   - Overs completed (works for over > 5)
   - Number of wickets lost
   - Runs scored in last 5 overs
4. **Get Prediction**: Click "Predict Final Score" to see the predicted final score

The application automatically calculates:
- Balls remaining in the innings
- Wickets left
- Current run rate
- Final score prediction based on all input parameters

## Future Improvements
- Implement ensemble methods combining multiple algorithms (Random Forest, Neural Networks)
- Add player-specific analysis to consider individual batsman and bowler performance
- Incorporate weather conditions and pitch reports for more accurate predictions
- Include real-time data integration for live match predictions

