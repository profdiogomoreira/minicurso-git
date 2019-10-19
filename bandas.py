#!/usr/local/bin/python3
# coding=UTF-8

import requests

def get_info(band):
    result = requests.get("https://www.theaudiodb.com/api/v1/json/1/search.php?s=" + band).json()
    print(result)
    print("Resultado da sua busca")
    print("Artista = %s" % result['artists'][0]['strArtist'])
    print("Biografia = %s" % result['artists'][0]['strBiographyPT'])
    print("País = %s" % result['artists'][0]['strCountry'])


if __name__ == "__main__":
    banda = input("Digite o nome da sua banda favorita: ")
    get_info(banda)
