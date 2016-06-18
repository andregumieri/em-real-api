import requests, json

def get_currency():

    resp = requests.get("https://openexchangerates.org/api/latest.json?app_id=APP_ID&base=USD")
    return resp.json()

    # print(resp.text)

    # f = open('USD-BRL.json', 'w')
    # f.write(json.dumps(
    #     {
    #         'timestamp': respJson['timestamp'],
    #         'rate': respJson['rates']['BRL']
    #     }
    # ));
