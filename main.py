import requests
import requests as rs

#https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json
def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()

crypto_Response = get_crypto_data()
user_input = input("Enter your crypto currency: ")

for crypto in crypto_Response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break

