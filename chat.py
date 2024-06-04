#título hashzap
#botão de iniciar chat
    #clicou no  botao:
        #popup / modal
        #título: Bem vindo ao Hashzap
        #campo: escreva seu nome
        #botão: entrar no chat
#chat
#embaixo do chat
    #campo de Digite sua mensagem
    #botão de enviar


#flet -> framework do python, com o mesmo código consegue criar um site ou aplicativo
#pip install flet

#sempre 3 passos antes de começar a desenvolver um site ou aplicativo

import flet as ft #importar

def main(pagina): #sempre cria a main e coloque como parâmetro a pagina
    texto = ft.Text("Hashzap")

    chat= ft.Column()  # o chat é uma coluna com informações

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem) #neste caso como não será acrescentado nenhum texto junto, não precisa usar o f
        chat.controls.append(texto_mensagem) #mesmo processo feito abaixo quando adiciona que a pessoa entrou no chat, append é um comando que adiciona coisas em uma lista (o chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #comando para criar um túnel de comunicação entre os usuários e nesse túnel eu quero que passe a mensagem, é pra rodar a função para todo mundo

    def enviar_mensagem(evento):

        #precisa configurar o comando de enviar a mensagem no túnel
        #quero que ao apertar o botao de enviar mensagem, vá para todo mundo
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        
        #adicionar a mensagem no chat
        
        #limpe o campo mensagem
        campo_mensagem.value = ""  #para limpar o campo mensagem depois que o usuário mandar a mensagem dele, é uma alteração no valor da variável, ela fica vazia
        pagina.update()  #sempre usa quando faz uma alteração visual.
        
    campo_mensagem= ft.TextField(label="Digite sua mensagem",on_submit=enviar_mensagem) #on_subit é o enter, quando apertar enter vai enviar a mensagem, não precisa clicar no botão de enviar
    botao_enviar = ft.ElevatedButton("Enviar ", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])  #linha com o campo de mensagem e o botão de enviar 

    def entrar_chat(evento):
        #fechar o popup
        popup.open = False
        #tirar o botão iniciar chat (da tela inicial)
        pagina.remove(botao_iniciar)
        #tirar o título hashzap
        pagina.remove(texto)
        #criar e adicionar o chat
        pagina.add(chat)
        #adicionar um campo que mostre quando uma pessoa entrou no chat
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.update()
        
        
                               
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome para o chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)


    popup = ft.AlertDialog(
        #parâmetros do alertdialog
        open=False,  #no inicio ele vai estar fechado e quando o botão ser acionado, ele vai virar true 
        modal=True,   #para ele ficar no centro
        title=titulo_popup, #título do popup
        content=nome_usuario, #o conteúdo
        actions=[botao_entrar] #actions está no plural, é obrigado passar uma lista, como só tem um botao_entrar nos []


    )

    def abrir_popup(evento):  #evento é uma variável que tem que dar para o botão, podendo ser qualquer coisa
        pagina.dialog = popup #informando que é para aparecer esse popup
        popup.open = True #mandar abrir o popup
        pagina.update() #sempre que for alterar o visual da página, precisa usar esse comando

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) #criar o aplicativo, precisa colocar para ele executar a main

