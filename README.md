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

### Category and Mechanic Scoring

In preparing our data for machine learning, we've introduced a unique approach to handling categorical data, specifically the various board game categories and mechanics. Categorical data presents a challenge for machine learning models due to its non-numeric nature. To address this, we convert the descriptive categories and mechanics of board games into quantifiable metrics known as `category_score` and `mechanic_score`.

#### Calculating Category and Mechanic Scores

Both `category_score` and `mechanic_score` are computed by assigning a unique rating to each category and mechanic based on historical data that reflects their popularity or significance. For each board game, we analyze its associated categories and mechanics and retrieve the corresponding ratings from our pre-established category and mechanic ratings arrays. These ratings are then averaged to produce a single score for each. These scores capture the essence of the game's themes and gameplay into numerical values that our machine learning models can process.

This method simplifies the dataset by reducing the dimensionality that would result from one-hot encoding, while also providing more nuanced features that reflect the combined significance of a board game's categories and mechanics.

#### Utilization in Machine Learning

The `category_score` and `mechanic_score` are used as features in our machine learning models to predict board game ratings. By transforming the categorical data into numerical scores, we enable the model to correlate the types of board games with their potential ratings. These steps are essential in enhancing the model's ability to learn from the categorical attributes of the data.

The approach of scoring categories and mechanics not only aids in the model's predictive accuracy but also in interpretability. Analysts can understand the impact of a game's thematic elements and gameplay mechanisms on its overall rating, offering valuable insights into consumer preferences and market trends.

## Data Preparation

### Feature Matrix and Target Vector

The data is prepared for machine learning by creating a feature matrix `X` and a target vector `y`. The feature matrix includes all relevant numerical features that are expected to influence the board game ratings, which are our target variable. We exclude non-predictive columns such as 'names' from the feature set. The target vector `y` comprises the board game ratings that we aim to predict.

### Training and Testing Sets

We split our dataset into training and testing sets, with 80% of the data used for training our model and the remaining 20% for testing its predictive power. This split helps in validating the performance of our machine learning model on unseen data, ensuring its effectiveness and generalization capability.

## Model Training and Evaluation

### Linear Regression Model

A Linear Regression model is chosen for its simplicity and interpretability. It is trained on the training set to understand the relationships between the features and the target variable.

### Performance Metrics

After training, we predict the ratings on the test set and evaluate the model's performance using the Mean Squared Error (MSE) metric. MSE provides us with a single aggregate figure representing the average of the squares of the errors between the predicted and actual ratings, giving us a sense of the model's accuracy.



