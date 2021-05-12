from PySimpleGUI import PySimpleGUI as sg 

# layout
sg.theme('dark')
layout = [
    [sg.Text(' User: '), sg.Input(key='user', size=(20 , 1))],
    [sg.Text(' Senha: '), sg.Input(key='senha', password_char='*', size=(20 , 1))],
    [sg.Checkbox( 'Salvar o login? ')],
    [sg.Button('ENTRAR')]
]
# janela
janela = sg.Window('tela login', layout)
# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'ENTRAR':
        if valores ['user'] == 'Bueno' and valores  ['senha'] == '1234':
            print("Deu bomS")    
