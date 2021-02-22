import requests


url = 'https://www.4devs.com.br/ferramentas_online.php'

payload = {'acao': 'gerar_cpf',
'pontuacao': 'S',
'cpf_estado': ''}

req = requests.post(url, data = payload)

print(req.text)


