# House Price Prediction

A web application that predicts the price of a house in India using machine learning.

## Overview

---

This web application is an  project that used a linear regression model to predict the price of a house in India based on various features. The application is built using Flask, pandas, scikit-learn, and numpy. It provides a user interface for entering the required features and displaying the predicted price.

## Table of Contents

---

1. [Getting Started](#getting-started)
2. [Files](#Files)
3. [Prerequisites](#Prerequisites)
4. [Installing](#Installing)
5. [Usage](#Usage)
6. [Attributes](#Attributes)
7. [Model](#Model)
8. [Dataset](#Dataset)
9. [Screenshot](#Screenshot)
10. [Contributing](#contributing)
11. [License](#license)

## Getting Started

---

This application uses a linear regression model trained on a dataset of house prices in India to predict the price of a house based on various features.

### Files

- `app.py`: This file contains the main Flask application code. It defines the routes, handles form submissions, and renders the templates.
- `templates/index.html`: This file contains the HTML template for the home page of the application. It includes the form for entering house features and displaying the predicted price.
- `model.py`: This file contains the code for training the linear regression model using the dataset of house prices in India. It reads the dataset, cleans it, splits it into training and test sets, trains the model, and saves it to a pickle file.
  The `app.py` file is the entry point of the application. It defines the routes and handles the form submissions. When the user submits the form on the home page, the `predict` route is called, and the entered features are processed by the trained model to get the predicted price. The predicted price is then displayed on the home page.
- `model.pkl`: This file contains the trained model that is used to predict the price of a house based on the entered features. It is loaded from the pickle file in `app.py` when the application starts.
- `Datasets/HousePriceIndia.csv`: This file contains the dataset of house prices in India. It includes various features such as number of bedrooms, number of bathrooms, living area, built year, etc., and the corresponding house prices.
- `requirements.txt`: This file lists the Python dependencies required to run the application. It includes Flask, pandas, scikit-learn, and numpy.file lists the Python dependencies required to run the application. It includes Flask, pandas, scikit-learn, and numpy. These dependencies are installed using `pip install -r requirements.txt` command.

### Prerequisites

- Python 3.x
- Flask
- pandas
- scikit-learn
- numpy

### Installing

1. Clone the repository: `git clone https://github.com/sivabala21/House-Price-Prediction.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## Usage

---

1. Open a web browser and navigate to `http://localhost:5000`
2. Fill in the form with the required features (e.g. number of bedrooms, number of bathrooms, etc.)
3. Click the "Predict" button to get the predicted house price

## Attributes

---

- Number of bedrooms
- Number of bathrooms
- Living area (in sqft)
- Number of floors
- Number of views
- Condition of the house (0-5)
- Area of the house (excluding basement) (in sqft)
- Basement area (in sqft)
- Built year
- Postal code
- Number of schools nearby

## Model

---

The model used is a linear regression model trained on a dataset of house prices in India. The model takes in the features listed above and outputs a predicted house price. We also placed some other dataset into dataset folder for further use case but for this model is trained by HousePriceIndia.csv file.

## Dataset

---

The dataset used is a CSV file named `HousePriceIndia.csv` containing information on house prices in India. This dataset includes the following features:

- Number of bedrooms
- Number of bathrooms
- Living area (in square feet)
- Number of floors
- Number of views
- Condition of the house (0-5)
- Area of the house (excluding basement) (in square feet)
- Basement area (in square feet)
- Built year
- Postal code
- Number of schools nearby

The dataset also includes the corresponding house prices.

### Other Datasets

---

We also have other datasets in the `Datasets` folder which can be used for further use case.

## Screenshot

---

![Screenshot](https://i.imgur.com/AEDaKBT.png)

## Contributing

---

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

---

This project is licensed under the MIT License. See the LICENSE file for details.
