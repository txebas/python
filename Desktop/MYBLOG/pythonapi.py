import requests

def obtener_datos_habilidad(habilidad_id):
    # URL de la API de Pokémon para obtener información sobre una habilidad
    url = f"https://pokeapi.co/api/v2/ability/{habilidad_id}/"
    
    # Realizar la solicitud GET a la API
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos = respuesta.json()
        
        # Mostrar algunos datos relevantes
        print(f"Nombre de la habilidad: {datos['name']}")
        print(f"ID de la habilidad: {datos['id']}")
        print(f"Efecto: {datos['effect_entries'][0]['effect']}")
        print(f"Pokémon que pueden tener esta habilidad:")
        for pokemon in datos['pokemon']:
            print(f" - {pokemon['pokemon']['name']}")
    else:
        print(f"Error al obtener los datos. Código de estado: {respuesta.status_code}")

# Llamar a la función para obtener los datos de la habilidad con ID 1
obtener_datos_habilidad(1)