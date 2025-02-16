# Backpack Price Prediction

This project is a Streamlit application that predicts the price of backpacks based on various features. The model is trained using data from the Kaggle Playground Series - Season 5, Episode 2 competition.

## Features

- Brand
- Material
- Size
- Style
- Color
- Number of Compartments
- Laptop Compartment
- Waterproof
- Weight Capacity

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Priyanshuthapliyal2005/Backpack-Prediction.git
    ```
2. Navigate to the project directory:
    ```
    cd Backpack-Prediction
    ```
3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```
    streamlit run main.py
    ```

2. Open the web browser and go to the provided URL to interact with the app.

## Files

- `main.py`: The main application file.
- `xgboost_model.json`: The pre-trained XGBoost model.
- `backpack.ipynb`: Jupyter Notebook for data preparation and model training.

## Dependencies

- streamlit
- pandas
- numpy
- matplotlib
- xgboost
- scikit-learn
- kaggle

## Kaggle Competition

### Overview

Welcome to the 2025 Kaggle Playground Series! We plan to continue in the spirit of previous playgrounds, providing interesting and approachable datasets for our community to practice their machine learning skills, and anticipate a competition each month.

**Your Goal:** Predict the price of backpacks given various attributes.

### Evaluation

![image](https://github.com/user-attachments/assets/999185fb-107c-4de8-b4f4-626390e9a54d)


### Submission File

For each id in the test set, you must predict the price of the backpack. The file should contain a header and have the following format:

You can interact with the live application here: [Backpack Price Prediction App](https://priyanshuthapliyal.streamlit.app/)

## Rank

Currently ranked 1750 in the Kaggle competition.

## Contributing

Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
