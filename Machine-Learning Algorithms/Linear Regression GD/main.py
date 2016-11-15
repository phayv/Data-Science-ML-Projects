from modules.Linear_Regression_Gradient_Descent import *
import pandas as pd

points = pd.read_csv("data.csv")

count = 0

initial_m = 0
initial_b = 0 
iterations = 500
alpha = .01
errors = pd.Series()

while count < iterations:
    err = line_error(initial_m,initial_b,points)
    [initial_b,initial_m] = Gradient_Step(initial_b,initial_m,points,alpha)   
    count += 1