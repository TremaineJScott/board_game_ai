import pandas as pd

from data_manipulation import load_category_ratings,get_average_category_rating

# Load the board games data
file_path = 'app/data/bgg_db_1806_50.csv'
board_games_data = pd.read_csv(file_path)

# Load the category ratings
category_ratings = load_category_ratings('app/data/Category_Ratings.csv')

# Create a new column 'category_score' by applying the 'get_average_category_rating' function to the 'category' column
board_games_data['category_score'] = board_games_data['category'].apply(lambda x: get_average_category_rating(x, category_ratings))

# Now you can drop the original 'category' column if it's no longer needed
board_games_data.drop('category', axis=1, inplace=True)

print(f"Game: {board_games_data['names']} Category Rating: {board_games_data['category_score']}")