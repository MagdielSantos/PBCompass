import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')

filmes = df['#1 Movie'].value_counts()
filme_max = filmes.idxmax()
filme_max_count = filmes.max()

print (f"O filme que mais aparece é o {filme_max}, e ele aparece {filme_max_count} vezes.")