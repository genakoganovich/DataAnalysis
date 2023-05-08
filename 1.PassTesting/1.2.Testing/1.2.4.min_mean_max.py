import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(filepath_or_buffer='ping.txt', sep=' ', usecols=[5], skiprows=2, header=None)
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: str(x).replace('время=', '').replace('мс', ''))
    df = df.astype('int32')
    print(df.describe())