meme_dict = {
            "LOL": "una respuesta a algo gracioso",
            "CRINGE": "algo raro o embarazoso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
word = input("escribe una palabra moderna que no entiendas(utiliza mayusculas):")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("todabia no tenemos esta palabra")
