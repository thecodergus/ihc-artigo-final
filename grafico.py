import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    df = pd.read_csv('Feedback_saida.csv')
    colunas = df.columns

    for i in colunas:        
        optv = df[i]
        optv_sum = optv.value_counts()
        total = df[i].count()
        optv_freq = (optv_sum / total) * 100
        
        p = optv_freq.plot.pie(y = "mass", figsize=(6, 6))
        p.plot()
        # plt.title(i)
        plt.savefig(f"imgs/{i}.png")
        
        
        plt.close()