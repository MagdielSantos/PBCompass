import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')
max_filmes = df.loc[df['Number of Movies'].idxmax()]
print (f"O ator com mais filmes é o {max_filmes['Actor']}, e participou de {max_filmes['Number of Movies']} Filmes. " )