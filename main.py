from pymongo import MongoClient
import pandas as pd
from matplotlib import pyplot as plt

cliente = MongoClient("mongodb://localhost:27017/")

banco = cliente["DataCityDB"]

viagens = banco["viagens"]

dadosViagens = list(viagens.find())

planilhaViagens = pd.DataFrame(dadosViagens)

if not planilhaViagens.empty:

    totalViagens = len(planilhaViagens)

    atrasoMedio = planilhaViagens["atraso_minutos"].mean()
    maiorAtraso = planilhaViagens["atraso_minutos"].max()
    top5 = (planilhaViagens.groupby("linha_id")["atraso_minutos"].mean().sort_values(ascending=False).head(5))
    totalPassageiros = (planilhaViagens.groupby("linha_id")["passageiros"].sum())

    plt.plot(kind="bar")
    plt.title("As cinco linhas com maiores atrasos médios")
    plt.xlabel("Linha")
    plt.ylabel("Atraso médio")
    plt.show()

    print(f"""
    Foram analisados um total de {totalViagens}, e aqui está os dados analisados:

    O atraso médio das viagens é de {atrasoMedio} minutos
    O maior atraso registrado nas viagens é de {maiorAtraso} minutos
    As cinco linhas com maiores atrasos são: {top5}
    O total de passageiros em cada linha é: {totalPassageiros}
    """)
    





