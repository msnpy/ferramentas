import requests


url = 'https://www.4devs.com.br/ferramentas_online.php'

payload = {'acao': 'gerar_cnpj',
'pontuacao': 'S'}

req = requests.post(url, data = payload)

print(req.text)




