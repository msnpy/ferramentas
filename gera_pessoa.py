
import requests
import os

os.system('clear')


class Pessoa:

    def __init__(self, url=None, payload=None):
        self.url = 'https://www.4devs.com.br/ferramentas_online.php'

        self.payload = {'acao': 'gerar_pessoa',
                'sexo': 'I',
                'pontuacao': 'N',
                'idade': '0',
                'cep_estado': '',
                'txt_qtde': 1,
                'cep_cidade': ''}


    def solicita(self,resultado=None):
        self.resultado = requests.post(self.url, data=self.payload).json()



    def formata_saida(self):
        for chave, valor in self.resultado.items():
            print(chave, valor)




pessoa1 = Pessoa()

pessoa1.solicita()

pessoa1.formata_saida()





