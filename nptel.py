from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

#A=pd.read_csv('income(1).csv', na_values=[' ?'])
A=pd.read_csv('cars_sampled.csv')
print(A)
