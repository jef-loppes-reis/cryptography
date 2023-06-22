# [START gae_python39_app]
# [START gae_python3_app]

from string import ascii_lowercase, ascii_uppercase, digits
from random import choice
from emoji import emojize
from flask import Flask, request
from json import dump

# Se `entrypoint` não estiver definido em app.yaml, o App Engine procurará um aplicativo
# Chamando `app` em `main.py`.
app = Flask(__name__)

def generation_key() -> str:
    key = ''.join(choice(ascii_lowercase + ascii_uppercase + digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))
    return key

def str_xor(s1:str, s2:str) -> str:
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])

@app.route("/")
def main() -> str:  
    key = generation_key()
    msg = request.args.get('str')
    if msg is None:
        return {}
    secret = str_xor(msg, key)
    recuperando_mensagem_secreta = str_xor(secret, key)
    return {
        f'{emojize(":old_key:")} key_secret(Chave Secreta)': key,
        f'{emojize(":keyboard:")} string(Palavra digitada)': msg,
        f'{emojize(":keyboard:")} -> {emojize(":locked_with_key:")} string_encrypted(Texto Cripitografado)': secret,
        f'{emojize(":keyboard:")} -> {emojize(":unlocked:")} string_decrypted(Text Descriptografado)': recuperando_mensagem_secreta
        }

@app.route('/decrypt')
def decrypt():
    encryption = request.args.get('encryption')
    key = request.args.get('key')
    if (encryption is None) or (key is None):
        return {}
    string_out = str_xor(encryption, key)
    return {'Palavra encontrada': string_out}


if __name__ == '__main__':
# Isso é usado ao executar apenas localmente. Ao implantar no Google App Engine, um processo de servidor da Web, como o Gunicorn, servirá ao aplicativo. Você pode configurar as instruções de inicialização adicionando `entrypoint` ao app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
    