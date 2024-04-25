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

    def propaganda_percentaje(self):
        PP_df = pd.DataFrame()

        PP_df["tweet"] = self.df["tweetText"].to_list()
        PP_df["Fecha"] = self.df[ "createdAt"].to_list()

        texto_original = self.df['tweetText'].to_list()
        texts = translateTxtArray(texto_original, self.idioma_destino)

        prop_detector = pipeline(model="cstnz/PropagandaDetection")
        scores = []
     
        for text in texts:        
            res = prop_detector(text)
            scores.append(res[0]["score"])
        
        PP_df["Porcentaje Propaganda"] = scores
       
        return PP_df


if __name__ == "__main__":

    sys_path = os.getcwd()
    new_path = sys_path.replace("\\", "/")


    path ="/Mentefactura-Hackaton/data/TwExtract-AlvarezMaynez-20240424_130940.csv" 

    handler = candidato(new_path + path)

    PB_df = handler.propaganda_percentaje()
    PB_df.to_csv("PropagandaPorcentajeMaynez.csv")
    breakpoint()