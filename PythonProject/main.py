import requests

token = "f3cba08ea92f0d7c06e0bae2d915b3af"

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Frank_Abagnale",
    "photo": "https://dolnikov.ru/pokemons/albums/069.png"
}, headers = {"Content-Type": "application/json",
              "trainer_token" : token})
         
print(response.text)

response_name = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "11096",
    "name": "Frank",
    "photo": "https://dolnikov.ru/pokemons/albums/077.png"
}, headers = {"Content-Type": "application/json",
              "trainer_token" : token})

print (response_name.text)

response_catch = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "11096"
}, headers = {"Content-Type": "application/json",
              "trainer_token" : token})

print(response_catch.text)