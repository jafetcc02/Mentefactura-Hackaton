import pandas as pd 
from tools import extra_clean, traducir, translateTxtArray
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import os 
import tqdm
import time

class candidato():

    __slots__ = ['df', "idioma_destino"]
    def __init__(self, path) -> None:
        self.df = self.load_data(path)
        self.idioma_destino = 'en'


    def load_data(self, path):
        df = pd.read_csv(path)
        df = self.clean_data(df)
        return df

    def clean_data(self, df):

        df = df[["tweetText", "retweetCount", "likeCount", "createdAt"]]
        df["tweetText"] = df["tweetText"].apply(extra_clean)

        return df
    
    def political_bias(self):
        PB_df = pd.DataFrame()

        PB_df["tweet"] = self.df["tweetText"].tolist()
        texto_original = self.df['tweetText'].tolist()
        texts = translateTxtArray(texto_original, self.idioma_destino)

        tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

        scores0 = []
        scores1 = []
        scores2 = []

     
        for text in texts:        
            inputs = tokenizer(text, return_tensors="pt")
            labels = torch.tensor([0])
            outputs = model(**inputs, labels=labels)
            loss, logits = outputs[:2]
            scores = logits.softmax(dim=-1)[0].tolist()
            scores0.append(scores[0])
            scores1.append(scores[1])
            scores2.append(scores[2])
            time.sleep(0.1)
           
        
        PB_df["Izquierda"] = scores0
        PB_df["Centro"] = scores1
        PB_df["Derecha"] = scores2

       
        return PB_df


if __name__ == "__main__":

    sys_path = os.getcwd()
    new_path = sys_path.replace("\\", "/")


    path ="/Mentefactura-Hackaton/data/TwExtract-XochitlGalvez-20240424_133659.csv" 

    handler = candidato(new_path + path)

    PB_df = handler.political_bias()
    PB_df.to_csv("PoliticalBiasXochitl.csv")
    breakpoint()