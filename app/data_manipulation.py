import pandas as pd

def load_category_ratings(file_path):
    # Load the category ratings into a DataFrame
    df = pd.read_csv(file_path)
    # Convert the DataFrame to a dictionary with categories as keys and ratings as values
    # Assuming the CSV has two columns: 'Category' and 'Rating'
    category_ratings = df.set_index('Category')['Rating'].to_dict()
    return category_ratings

def load_mechanic_ratings(file_path):
    # Load the category ratings into a DataFrame
    df = pd.read_csv(file_path)
    # Convert the DataFrame to a dictionary with categories as keys and ratings as values
    # Assuming the CSV has two columns: 'Category' and 'Rating'
    mechanic_ratings = df.set_index('Mechanic')['Rating'].to_dict()
    return mechanic_ratings

def get_average_category_rating(categories_str, category_ratings):
    # Split the categories string into individual categories
    categories = categories_str.split(', ')
    # Initialize a list to store the ratings
    ratings = []
    
    # For each category, get the rating if the category is in the dictionary
    for category in categories:
        category = category.strip().title()  # Adjust case to match dictionary keys
        if category in category_ratings:
            ratings.append(category_ratings[category])
    
    # Calculate the average rating if there are any ratings
    if ratings:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = .5  #  Default value if no valid categories are found

    return average_rating

def get_average_mechanic_rating(mechanics_str, mechanic_rating):
    # Split the mechanics string into individual mechanics
    mechanics = mechanics_str.split(', ')
    # Initialize a list to store the ratings
    ratings = []
    
    # For each mechanic, get the rating if the mechanic is in the dictionary
    for mechanic in mechanics:
        mechanic = mechanic.strip().title()  # Adjust case to match dictionary keys
        if mechanic in mechanic_rating:
            ratings.append(mechanic_rating[mechanic])
    
    # Calculate the average rating if there are any ratings
    if ratings:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = .5  #  Default value if no valid mechanics are found

    return average_rating
