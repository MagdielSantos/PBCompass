import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')
max_avg = df.loc[df['Average per Movie'].idxmax()]
print (f"O ator com a maior media por filme é o(a) {max_avg['Actor']}, e a media é {max_avg['Average per Movie']}.")