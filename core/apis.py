from json import loads
from config import API_KEY_EMAIL_VALIDATOR
from requests import get

API_URL = "https://api.invertexto.com/v1/email-validator/{}"

def validar_email(email):
    headers = {
        "Authorization": f"Bearer {API_KEY_EMAIL_VALIDATOR}"
    }
    url = API_URL.format(email)
    
    response = get(url, headers=headers)

    if response.status_code == 200:
        resultado = loads(response.text)
        return resultado["valid_format"] and resultado["valid_mx"] and not resultado["disposable"]
    else:
        return False


#try:
#    email_para_validar = "seu_email@exemplo.com"
#    resultado = validar_email(email_para_validar)
#
#    if resultado:
#        print("O email é válido.")
#    else:
#        print("O email é inválido.")
#except AttributeError as e:
#    print(e)
