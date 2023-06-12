import pandas as pd 
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from PIL import Image
import io
import gradio as gr

df = pd.read_excel('donnees_covid.xlsx')

def suivi_interactif_covid(countriesAndTerritories):
    df_pays = df[df['countriesAndTerritories'] == countriesAndTerritories]
    print(df)
    print(df_pays)

def afficher_statistiques_covid(countriesAndTerritories):
    df_pays = df[df['countriesAndTerritories'] == countriesAndTerritories]
    plt.figure(figsize=(10, 6))
    plt.plot(df_pays['cases'], label='cases')
    plt.plot(df_pays['deaths'], label='deaths')
    plt.ylabel("Nombre de cas")
    plt.title(f"Statistiques COVID-19 pour {countriesAndTerritories}")
    plt.legend()
    plt.xticks(rotation=45)

    # Enregistrer le graphique dans un fichier d'image
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Créer une image PIL à partir du fichier d'image
    image = Image.open(img_buffer)

    return image

interface = gr.Interface(
    fn=afficher_statistiques_covid,
    inputs="text",
    outputs="image",
    title="Suivi interactif de la COVID-19",
    description="Entrez un pays ou une région et visualisez des visualisations interactives des cas de COVID-19.",
    examples=[["France"], ["Canada"], ["Maroc"]],
)

interface.launch()

suivi_interactif_covid("France")
