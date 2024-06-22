import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset (replace 'Algorithm_Dataset.csv' with your dataset file)
df = pd.read_csv('Algorithm_Dataset.csv')

# Separate target variables
y_home = df['home_score']
y_away = df['away_score']

# Drop target variables from features
x = df.drop(columns=['home_score', 'away_score'])

# Split data into training and testing sets
X_train, X_test, y_home_train, y_home_test = train_test_split(x, y_home, test_size=0.2, random_state=42)
_, _, y_away_train, y_away_test = train_test_split(x, y_away, test_size=0.2, random_state=42)

# Check and extract columns for comparison if they exist in X_test
if 'original_Season' in X_test.columns:
    Comparison = X_test[['original_Season', 'original_home_team', 'original_away_team', 'result']]
    X_train = X_train.drop(columns=['original_Season', 'original_home_team', 'original_away_team', 'result'], errors='ignore')
    X_test = X_test.drop(columns=['original_Season', 'original_home_team', 'original_away_team', 'result'], errors='ignore')
else:
    print("Columns 'original_Season', 'original_home_team', 'original_away_team' not found in X_test.")

# Number of models (bootstrap samples)
num_models = 100
models_home = []
models_away = []

# Perform bootstrapping and train models
for i in range(num_models):
    # Generate bootstrap sample
    bootstrap_indices = np.random.choice(len(X_train), size=len(X_train), replace=False)
    X_train_bootstrap = X_train.iloc[bootstrap_indices]
    y_home_train_bootstrap = y_home_train.iloc[bootstrap_indices]
    y_away_train_bootstrap = y_away_train.iloc[bootstrap_indices]
    
    # Train model on bootstrap sample with limited max_features
    model_home = RandomForestRegressor(n_estimators=100, max_features='sqrt', random_state=42)
    model_away = RandomForestRegressor(n_estimators=100, max_features='sqrt', random_state=42)
    
    model_home.fit(X_train_bootstrap, y_home_train_bootstrap)
    model_away.fit(X_train_bootstrap, y_away_train_bootstrap)
    
    # Store models
    models_home.append(model_home)
    models_away.append(model_away)

# Predictions aggregation
y_home_preds = np.zeros(len(X_test))
y_away_preds = np.zeros(len(X_test))

for model_home, model_away in zip(models_home, models_away):
    y_home_preds += model_home.predict(X_test)
    y_away_preds += model_away.predict(X_test)

# Average predictions from all models
y_home_preds /= num_models
y_away_preds /= num_models

# Evaluate predictions (optional)
print(f"Home score RMSE: {mean_squared_error(y_home_test, y_home_preds, squared=False)}")
print(f"Away score RMSE: {mean_squared_error(y_away_test, y_away_preds, squared=False)}")

# Determine predicted winners
predicted_winners = []
actual_winners = []

for i in range(len(X_test)):
    home_team = Comparison['original_home_team'].iloc[i]
    away_team = Comparison['original_away_team'].iloc[i]
    home_score_pred = y_home_preds[i]
    away_score_pred = y_away_preds[i]
    
    if home_score_pred > away_score_pred:
        predicted_winner = home_team
    elif home_score_pred < away_score_pred:
        predicted_winner = away_team
    else:
        predicted_winner = 'draw'
    
    predicted_winners.append(predicted_winner)

    # Determine actual winners
    home_score_actual = y_home_test.iloc[i]
    away_score_actual = y_away_test.iloc[i]
    
    if home_score_actual > away_score_actual:
        actual_winner = home_team
    elif home_score_actual < away_score_actual:
        actual_winner = away_team
    else:
        actual_winner = 'draw'
    
    actual_winners.append(actual_winner)

# Calculate accuracy
correct_predictions = 0
total_matches = len(predicted_winners)

for predicted, actual in zip(predicted_winners, actual_winners):
    if predicted == actual:
        correct_predictions += 1

accuracy = (correct_predictions / total_matches) * 100
print(f"Winner Accuracy: {accuracy:.2f}%")
