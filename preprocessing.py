import pandas as pd


class preprocesser():

    def __init__(self, df):
        self.df = df  # dataframe as input

    def preprocess_dataframe(self):
        self.df = self.df.dropna()  # drop rows with na

        df_len = len(self.df)

        new_df = pd.DataFrame(columns=[''])
        for i in range(df_len):
            # work with price
            self.df.iloc[i]['price'] = 'pddddd'
            # work with locali

            # work with superficie

            # work with bagni

            # work with piani

            # work with description

        return


df = pd.read_csv('data/prova.csv')
df = df.drop(['Unnamed: 0'], axis=1)

prep = preprocesser(df.head())
prep.preprocess_dataframe()

# df.dropna(inplace=True)