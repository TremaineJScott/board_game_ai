# Board Game AI

## Project Overview
Board Game AI is a data-driven approach to predict the ratings of board games. This project leverages machine learning techniques to analyze various features of board games, such as maximum playtime, game mechanics, categories, and game complexity (weight), to estimate their overall ratings.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them:
- Python 3.x
- Pandas
- Scikit-learn

## Feature Engineering

### Category Scoring

In the process of preparing our data for machine learning, we have introduced an innovative approach to handling categorical data, particularly the various board game categories. Traditionally, categorical data can be challenging to incorporate into machine learning models due to its non-numeric nature. To overcome this, we convert the descriptive categories of board games into a quantifiable metric known as `category_score`.

#### Calculating Category Score

The `category_score` is computed by first assigning a unique rating to each category based on historical data that reflects the category's popularity or significance. This approach allows us to quantify the otherwise qualitative category data.

For each board game, we analyze its associated categories and retrieve the corresponding ratings from our pre-established category ratings array. These ratings are then averaged to produce a single `category_score`. The score encapsulates the essence of the multiple categories into one numerical value that our machine learning models can process.

This method not only simplifies the dataset by reducing the dimensionality that would result from one-hot encoding but also provides a more nuanced feature that reflects the combined weight of a board game's categories.

#### Utilization in Machine Learning

The `category_score` is used as a feature in our machine learning models to predict board game ratings. By transforming the categorical data into a numerical score, we enable the model to correlate the type of board game with its potential rating. It is an essential step that enhances the model's ability to learn from categorical attributes of the data.

We have found that this approach of category scoring not only aids in the model's predictive accuracy but also provides interpretability. Analysts can understand the impact of a game's thematic elements on its overall rating, offering valuable insights into consumer preferences and market trends.



