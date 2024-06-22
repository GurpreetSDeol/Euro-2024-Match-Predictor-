import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# File paths
main_file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Euros Data\Euro_Match_Team_Stats_Difference_per_Match.csv'
prediction_files = [
    'Euro_2024_Team_Stats_Difference_per_Match.csv',
    'Euro_2024_R16_Team_Stats_Difference_per_Match.csv',
    'Euro_2024_QF_Team_Stats_Difference_per_Match.csv',
    'Euro_2024_SF_Team_Stats_Difference_per_Match.csv',
    'Euro_2024_F_Team_Stats_Difference_per_Match.csv'
]
prediction_files = [rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Euros Data\{file}' for file in prediction_files]

# Read and process main file
def read_and_process(file_path):
    df = pd.read_csv(file_path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.rename(columns=lambda x: x.replace('_difference', ''), inplace=True)
    return df

main_df = read_and_process(main_file_path)
prediction_dfs = [read_and_process(file) for file in prediction_files]

# Check for NaNs and print
nan_percentage = main_df.isna().mean() * 100
print(nan_percentage)
print(main_df)

# Compute correlations
corr_df = main_df.select_dtypes(include=[float, int])
corr_matrix = corr_df.corr()
corr_pairs = corr_matrix.unstack().drop_duplicates().sort_values(ascending=False)
filtered_corr_pairs = corr_pairs[(corr_pairs >= 0.4) & (corr_pairs <= 0.99)]
top_pairs = filtered_corr_pairs.head(50).index

# Extract top columns based on correlation
top_columns = pd.unique([pair[0] for pair in top_pairs] + [pair[1] for pair in top_pairs])
top_df = main_df[top_columns]
print(top_columns)

#sns.heatmap(top_df.corr(), annot=True, fmt='.2f')
#plt.show()

# Prepare final DataFrames
standard_columns = ['Season','home_team', 'away_team', 'home_score','away_score','result']
all_columns = standard_columns + list(top_columns)
final_df = main_df[all_columns]

prediction_dfs = [df[all_columns] for df in prediction_dfs]

# Label encoding
categorical_columns = ['Season', 'home_team', 'away_team']
label_encoders = {col: LabelEncoder() for col in categorical_columns}

for col in categorical_columns:
    final_df[f'original_{col}'] = final_df[col]
    for df in prediction_dfs:
        df[f'original_{col}'] = df[col]

for col in categorical_columns:
    final_df[col] = label_encoders[col].fit_transform(final_df[col])
    for df in prediction_dfs:
        df[col] = label_encoders[col].transform(df[col])

# Filter out Season 6 and save to CSV
final_df = final_df[final_df['Season'] != 6]
final_df.to_csv(r'Data\Algorithm_Dataset.csv', index=False)

output_files = [
    r'Data\Prediction_Data.csv',
    r'Data\R16_Pred_Data.csv',
    r'Data\QF_Pred_Data.csv',
    r'Data\SF_Pred_Data.csv',
    r'Data\F_Pred_Data.csv'
]

for df, file in zip(prediction_dfs, output_files):
    df.to_csv(file, index=False)
