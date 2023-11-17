from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime

#Layout
sg.theme('Reddit')

layout = [
    [sg.Text('DADOS PESSOAIS')],
    [sg.Text('Nome completo'), sg.Input()],
    [sg.Text('Data de nascimento'), sg.Input()],
    [sg.Text('CPF/CNPJ:'), sg.Input()],
    [sg.Text('Genêro'), sg.Input()],
    [sg.Text('Origem:'), sg.Input()],
    [],
    [sg.Text('CONTATO')],
    [sg.Text('Telefone/Whatsapp:'),sg.Input()],
    [sg.Text('Telefone/Whatsapp:'),sg.Input()],
    [sg.Checkbox('Aceito os termos do contrato.')],
    [],
    [sg.Text('ENDEREÇO')],
    [sg.Text('Tipo endereço:'),sg.Input()],
    [sg.Text('Cep:'),sg.Input()],
    [sg.Text('UF:'),sg.Input()],
    [sg.Text('Bairro:'),sg.Input()],
    [sg.Text('Logradouro:'),sg.Input()],
    [sg.Text('Número:'),sg.Input()],
    [sg.Text('Cidade:'),sg.Input()],
    [sg.Checkbox('Incluir segundo endereço?')],


    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Cadastro Cliente', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'isadora' and valores['senha'] == '1234':
            print('Bem vindo!')





            