import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
    df_pays['dateRep'] = pd.to_datetime(df_pays['dateRep'])
    plt.figure(figsize=(20, 15))

    # Subplot for cases
    plt.subplot(2, 1, 1)
    plt.plot(df_pays['dateRep'], df_pays['cases'], label='Cases', color='blue')
    plt.xlabel('dateRep')
    plt.ylabel('Number of cases')
    plt.title(f"COVID-19 Statistics for {countriesAndTerritories}")
    plt.xticks(rotation=45)
    locator = mdates.AutoDateLocator()
    formatter = mdates.DateFormatter('%b %Y')
    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.legend(['Cases'])

    # Subplot for deaths
    plt.subplot(2, 1, 2)
    plt.plot(df_pays['dateRep'], df_pays['deaths'], label='Deaths', color='red')
    plt.xlabel('Date')
    plt.ylabel('Number of deaths')
    plt.xticks(rotation=45)
    locator = mdates.AutoDateLocator()
    formatter = mdates.DateFormatter('%b %Y')
    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.legend(['Deaths'])

    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.4)

    # Save the graph to an image file
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Create a PIL image from the image file
    image = Image.open(img_buffer)

    return image

interface = gr.Interface(
    fn=afficher_statistiques_covid,
    inputs="text",
    outputs="image",
    title="Interactive COVID-19 Monitoring",
    description="Enter a country or region and visualize interactive COVID-19 case statistics.",
    examples=[["France"], ["Canada"], ["Mauritania"]],
)

interface.launch()
suivi_interactif_covid("France")