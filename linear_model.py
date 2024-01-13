from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from utils_nans1 import *
import pandas as pd

global model

def print_LINE(features, labels, p_value_thresh = 0.05):
    global model

    x_with_const = sm.add_constant(features)
    is_linearity_found, p_value = linear_assumption(model, x_with_const, labels, plot=False)
    autocorrelation, dw_value = independence_of_errors_assumption(model, x_with_const, labels, plot=False)
    n_dist_type, p_value = normality_of_errors_assumption(model, x_with_const, labels, plot=False)
    e_dist_type, p_value = equal_variance_assumption(model, x_with_const, labels, plot=False)
    has_perfect_collinearity = perfect_collinearity_assumption(features, plot=False)

    print("***************************************************************")
    print("Linearity: ",is_linearity_found)
    print("Independance of errors: ", autocorrelation is None)
    print("Normality of errors: ",n_dist_type == 'normal')
    print("Equal variencce: ",e_dist_type)

    print("Perfect colinarity: ", has_perfect_collinearity)

def transform_predicted(value):
    return "shouldnt win" if value <= 0.5 else "should win"

def transform_success(predicted, actual):
    return "yes" if predicted == "should win" and actual == 1 or predicted == "shouldnt win" and actual == 0 else "no"

def transform_residuals(data_errors):
    data_errors['Succesful'] = data_errors['Predicted'].apply(transform_predicted)
    data_errors['Guessed right'] = data_errors.apply(lambda row: transform_success(row['Succesful'], row['Actual']), axis=1)
    return data_errors

def predict_winner(selected_posters):
    global model

    test_data = pd.read_csv("static\\files\\2024_candidates.csv")
    x_test = test_data.drop(['Film', 'Year', 'won_best_picture'], axis=1)
    x_test_with_const = sm.add_constant(x_test)
    test_residuals = model.predict(x_test_with_const)
    #test_residuals_df = pd.DataFrame({'Predicted': test_residuals})
    print(test_residuals[0])

def print_model_stats(features, labels):
    global model

    print(get_rsquared_adj(model, features, labels))
    print_LINE(features, labels)
    print(are_assumptions_satisfied(model, features, labels, 0.02))

    data_errors = calculate_residuals(model, features, labels)
    data_errors = transform_residuals(data_errors)
    print(data_errors)
    print(model.summary())

def make_model(print_stats = False):
    global model

    data = pd.read_csv('static\\files\\oscardata.csv')
    features = data.drop(['Film', 'Year', 'won_best_picture'], axis=1)  

    labels = data['won_best_picture']

    model = get_fitted_model(features, labels)

    if print_stats:
        print_model_stats(features, labels)
    
