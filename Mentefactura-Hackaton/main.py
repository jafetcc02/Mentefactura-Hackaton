import pandas as pd 


class candidato():

    __slots__ = ['df']
    def __init__(self, path) -> None:
        self.df = pd.read_csv(path)

    