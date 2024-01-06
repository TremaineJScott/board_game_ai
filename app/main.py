import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

from data_manipulation import (
    load_category_ratings,
    get_average_category_rating,
    load_mechanic_ratings,
    get_average_mechanic_rating
)


# Function to predict the rating of a new game
def predict_new_game(model, scaler, category_ratings, mechanic_ratings, feature_names):
    # Get new game data from user input
    print("\nEnter details for the new game:")
    name = input("Game Name: ")
    category = input("Categories (comma-separated): ")
    mechanic = input("Mechanics (comma-separated): ")
    weight = float(input("Weight: "))

    # Calculate scores using the provided functions
    category_score = get_average_category_rating(category, category_ratings)
    mechanic_score = get_average_mechanic_rating(mechanic, mechanic_ratings)

    # Create a DataFrame for the new game
    new_game_df = pd.DataFrame([{
        'category_score': category_score, 
        'mechanic_score': mechanic_score, 
        'weight': weight
    }])[feature_names]

    # Scale the features and predict
    scaled_features = scaler.transform(new_game_df)
    predicted_rating = model.predict(scaled_features)

    print(f"\nThe predicted rating for '{name}' is: {predicted_rating[0]}")



# Load the board games data
file_path = 'app/data/bgg_db_1806_50.csv'
board_games_data = pd.read_csv(file_path)

# Load the category ratings
category_ratings = load_category_ratings('app/data/Category_Ratings.csv')

# Create a new column 'category_score' by applying the 'get_average_category_rating' function to the 'category' column
board_games_data['category_score'] = board_games_data['category'].apply(lambda x: get_average_category_rating(x, category_ratings))

# Drop the original 'category' column since it's no longer needed
board_games_data.drop('category', axis=1, inplace=True)

# Load the mechanic ratings
mechanic_ratings = load_mechanic_ratings('app/data/Mechanic_Ratings.csv')

# Create a new column 'mechanic_score' by applying the 'get_average_mechanic_rating' function to the 'mechanic' column
board_games_data['mechanic_score'] = board_games_data['mechanic'].apply(lambda x: get_average_mechanic_rating(x, mechanic_ratings))

# Drop the original 'mechanic' column since it's no longer needed
board_games_data.drop('mechanic', axis=1, inplace=True)

# Preparing the feature matrix (X) and the target vector (y)
feature_columns = [col for col in board_games_data.columns if col not in ['names', 'my_rating']]
X = board_games_data[feature_columns]
feature_names = X.columns.tolist()

y = board_games_data['my_rating']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Creating and training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Main loop for predicting new games
while True:
    predict_new_game(model, scaler, category_ratings, mechanic_ratings, feature_names)

    # Check if user wants to predict another game
    another_game = input("\nWould you like to predict another game? (yes/no): ").lower()
    if another_game != 'yes':
        break