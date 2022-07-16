from tkinter import *
import requests


def pegar_cotacoes():
  requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
  
  requisicao_dic = requisicao.json()
  cotacao_dolar = requisicao_dic['USDBRL']['bid']
  cotacao_euro = requisicao_dic['EURBRL']['bid']
  cotacao_btc = requisicao_dic['BTCBRL']['bid']
  
  texto = f'''Dólar: {cotacao_dolar}
  Euro: {cotacao_euro}
  BTC: {cotacao_btc}'''
  texto_cotacao["text"] = texto

janela = Tk()
janela.title("Cotação")


janela.geometry("600x400+400+200")
janela.resizable(True, True)

# janela.minsize(width=300, height=200)
# janela.maxsize(width=600, height=400)

# janela.state('zoomed')
# janela.state('iconic')

#janela.iconbitmap("icon.ico")

janela["bg"] = "aliceblue"

texto_instrucao = Label(janela, text="Pressione o botão para ver a cotação")
texto_instrucao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Verificar", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

