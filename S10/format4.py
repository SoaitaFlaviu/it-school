loren = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print("{:.10}".format(loren))

ticket = {
    "s_plecare": "Bucuresti Nord",
    "s_sosire": "Iasi",
    "data_plecare": "27.02.2023",
    "data_sosire": "28.02.2023",
    "ora_plecare": "19:30",
    "ora_sosire": "23:30",
    "pret": 98.458766,
    "loc": True,
    "vagon": "2",
    "scaun": "34",
}

template_tren = ("Trenul pleaca din {s_plecare} in data de {data_plecare} la ora"
                 "{ora_plecare} so ajunge la {ora_sosire} in data de {data_sosire}"
                 "la ora {ora_sosire}")

# Poti avea doua dictionare cu aceeasi structura si valori diferite
print(template_tren.format(**ticket))

