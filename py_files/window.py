import PySimpleGUI as sg
from client import Client

# layouts

class PyScreen:
    def layout_login(self):
        login = [
            [sg.Text()],
            [sg.Text('Nome', font='Helvetica 14', size=(7,1)), sg.Input(key='-NAME-')],
            [sg.Text('Senha', font='Helvetica 14', size=(7,1)), sg.Input(key='-PASSWORD-')], #, password_char='*'
            [sg.Push(), sg.Text(key='login_checking', text_color='#FF5858')],
            [sg.Push(), sg.ReadButton('Entrar'), sg.Button('Cadastrar', button_color= '#0EC1BB', key='-REGISTER-')]
        ]

        frame_login = [
            [sg.Frame('Login', login, font='Helvetica 26', size=(400,300))]
        ]

        image = [
            [sg.Image(r'D:\Rodolfo\Documents\Python\PyCharmProjects\projetos_pysimplegui\projects\images\pattern.png',
                      size=(400,600), pad=(0))]
        ]

        layout = [
            [sg.Column(image), sg.VSeparator(), sg.Column(frame_login)]
        ]

        return sg.Window('Login', layout=layout, finalize=True, size=(800,600))

    def layout_register(self):
        layout = [
            [sg.T()],
            [sg.Text('Nome:', font='Helvetica 14', size=(18,1)), sg.Input(key='-NAME-')],
            [sg.Text('Idade:', font='Helvetica 14', size=(18,1)), sg.Input(key='-AGE-')],
            [sg.Text('Documento:', font='Helvetica 14', size=(18,1)), sg.Input(key='-DOCUMENT-')],
            [sg.T()],
            [sg.T('Senha:', font='Helvetica 14', size=(18,1)), sg.Input(key='-PREV_PASSWORD-')],
            [sg.T('Confirme sua senha:', font='Helvetica 14', size=(18,1)), sg.Input(key='-CONFIRM_PASSWORD-')],
            [sg.Push(), sg.Text(key='-PASSWORD_CHECKING-', text_color='#FF5858')],
            [sg.Push(), sg.Button('Cadastrar', button_color='#0EC1BB', key='-CONFIRM_REGISTER-'), sg.Button('Voltar', key='-BACK_PAGE-')]
        ]

        frame_layout = [
            [sg.Frame('Cadastro', layout, font='Helvetica 26', size=(500,350))]
        ]

        return sg.Window('Cadastro', layout=frame_layout, finalize=True, size=(600,400), element_justification='c')

    def layout_shopping(self):
        pizza = [
            [sg.T()],
            [sg.RButton('<', key='-PREV_PIZZA-'),
             sg.Image(
                      key='-PIZZA_IMAGE-', size=(400,300)),
             sg.RButton('>', key='-NEXT_PIZZA-')],
            [sg.T('Calabresa', key='-PIZZA_NAME-')],
            [sg.T('Ingredientes', key='-PIZZA_COMPOSITION')],
            [sg.T('Preço', key='-PIZZA_PRICE-')],
            [sg.VSeparator()],
            [sg.RButton('Adicionar ao carrinho', key='-ADD_SHOPPING_CAR-')]
        ]

        output = [
            [sg.Output(key='-SHOPPING_CAR-', size=(30,20))],
            [sg.RButton('Finalizar pedido', key='-FINALIZE_ORDER-'), sg.Push(), sg.RButton('Excluir item', key='-DELETE_ITEM-')],
            [sg.T()],
            [sg.Push(), sg.RButton('Voltar')]
        ]

        layout = [
            [sg.Column(pizza, element_justification='c'), sg.HSeparator(), sg.Column(output)]
        ]

        frame_layout = [
            [sg.Frame('PIZZARIA SENAI', layout, font='Helvetica 26', size=(800,600))]
        ]

        return sg.Window('Pizzaria Senai', layout=frame_layout, finalize=True, size=(800,600))

    def start(self):

        # create windows
        window1, window2, window3 = self.layout_login(), self.layout_register(), self.layout_shopping()
        window2.hide()
        window3.hide()
        client = Client()

        # read windows
        while True:

            window, self.button, self.values = sg.read_all_windows()
            client_active = False

            # window closed
            if self.button == None:
                break

            # window login
            if window == window1:
                name = self.values['-NAME-']
                password = self.values['-PASSWORD-']
                login_checking = 'Nome ou senha não encontrado(s)'

                match self.button:
                    case 'Entrar':
                        if client.clients:
                            for c in client.clients:
                                if name == c.name:
                                    if password == c.password:
                                        window1['login_checking']('')
                                        client_active = True
                                    break
                        if not client_active:
                            window1['login_checking'](login_checking)
                        else:
                            window1.hide()
                            window3.un_hide()


                    case '-REGISTER-':
                        window1 = self.layout_login()
                        window1.hide()
                        window2.un_hide()

            # window register
            if window == window2:
                name = self.values['-NAME-']
                age = self.values['-AGE-']
                document = self.values['-DOCUMENT-']
                prev_password = self.values['-PREV_PASSWORD-']
                password = self.values['-CONFIRM_PASSWORD-']
                check = 'Confirme a mesma senha'

                match self.button:
                    case '-CONFIRM_REGISTER-':
                        if prev_password != password:
                            window['-PASSWORD_CHECKING-'](check)
                        else:
                            window['-PASSWORD_CHECKING-']('')
                            client.add_client(name, password, age, document)
                            for i in range(1000):
                                sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=(100))
                            sg.PopupAnimated(None)
                            sg.Popup('Cadastrado com sucesso!')

                    case'-BACK_PAGE-':
                        window1.un_hide()
                        window2.hide()

            if window == window3:
                pizza = 'D:\Rodolfo\Documents\Python\PyCharmProjects\projetos_pysimplegui\projects\images\Pizza.png'

                if self.button == '-NEXT_PIZZA-':
                    window3['-PIZZA_IMAGE-'](pizza)

    # to update
    #window['key'](new_value)

py = PyScreen()
py.start()
