# coding : utf-8
# Author : yuxiang Zeng
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # address = 'datasets/MedBIoT_csv/500s/bashlite_mal_CC_all_500s.csv'
    address = 'datasets/MedBIoT_csv/500s/bashlite_leg_500s.csv'
    df = pd.read_csv(address)
    print(df.columns)
    print(df)

    x = df[df.columns[0]]
    y = df[df.columns[-1]]
    plt.figure(dpi=150)
    plt.plot(x, y)
    plt.show()
