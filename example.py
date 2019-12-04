from address import Address

API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
payment_password = 'your_payment_password'

client = Address(API_KEY, SECRET_KEY)
coins = client.get_coins()  # Get all available coins
client.create_wallet('btc', 'My wallet')  # Create btc wallet
wallets = {coin['coin']: client.get_wallets(coin['coin']) for coin in coins}  # Get all wallets for every coin
wallet_id = wallets['btc'][0]['id']  # Get wallet id
amount = 2  # Amount btc to send

client.send_from_wallet('btc', wallet_id, amount, 'recipient_address', payment_password)

"""{
    "result": [
        {
            "txid": "your tx id"
        }
    ],
    "errors": null
}"""
