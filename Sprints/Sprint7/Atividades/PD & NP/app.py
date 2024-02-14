import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')
media = (df['Number of Movies'].mean())
print (media)