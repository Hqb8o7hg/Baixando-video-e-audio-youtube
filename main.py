from tkinter import *
from pytube import YouTube
from tkinter import filedialog

from pytube.exceptions import RegexMatchError


def dowload_completo():
    janela_msg = Toplevel()
    janela_msg.title('AVISO')
    janela_msg.resizable(0, 0)
    janela_msg.geometry('300x200+600+200')

    text = Label(janela_msg, text='Dowload concluído.', font='arial 12 bold', pady=30)
    text.pack()

    botao_saida = Button(janela_msg, text='Ok', command=janela_msg.destroy)
    botao_saida.pack()


def mensagem_erro():
    janela_erro = Toplevel()
    janela_erro.title('ERROR')
    janela_erro.resizable(0, 0)
    janela_erro.geometry('300x200+600+200')

    text = Label(janela_erro, text='Insira um link válido.', font='arial 12 bold', pady=30)
    text.pack()

    botao_saida = Button(janela_erro, text='Ok', command=janela_erro.destroy)
    botao_saida.pack()


class Dowloader:

    def __init__(self):

        self.instrucoes_corpo1 = "Passo 01: Insira o link do arquivo que deseja baixar no campo indicado;"
        self.instrucoes_corpo2 = "Passo 02: Escolha se quer baixar, somente (audio), somente (video) ou (audio e video)"
        self.instrucoes_corpo3 = "Clique no botão ao lado para iniciar o dowload e aguarde enquanto o" \
                                 " arquivo está sendo baixado"
        self.label_carregando = None
        self.janela = Tk()
        self.janela.title('TubeTubefree')
        self.janela.resizable(0, 0)
        self.janela.geometry("1280x720+130+50")

        self.img_logo = PhotoImage(file="libfiles/Im01sf.png")

        self.audio = False
        self.video = False

        self.quadro1 = Frame(self.janela, bg="white")
        self.quadro1.pack(fill='x')

        self.label_logo = Label(self.quadro1, image=self.img_logo)
        self.label_logo.pack()

        self.quadro2 = Frame(self.janela)
        self.quadro2.pack()

        self.label_inserir_link = Label(self.quadro2, text='Inserir link: ', font='arial 12 bold')
        self.label_inserir_link.pack(side='left')

        self.link = Entry(self.quadro2, font='arial 20', width=50)
        self.link.pack(side='left')

        self.play = Button(self.quadro2, bg='red', text='>', bd=0, fg='white', width=4, height=2, command=lambda: self.
                           dowload(self.link.get())).pack()

        self.quadro3 = Frame(self.janela)
        self.quadro3.pack()

        self.radio1 = Radiobutton(self.quadro3, text='Audio', value=0, command=self.validacao_audio).pack(side='left')
        self.radio2 = Radiobutton(self.quadro3, text='Video', value=1, command=self.validacao_video).pack(side='left')
        self.radio3 = Radiobutton(self.quadro3, text='Audio e Video', value=2, command=self.validacao_video_audio) \
            .pack(side='left')

        self.quadro4 = Frame(self.janela, bd=30)
        self.quadro4.pack()

        self.titulo_instrucoes = Label(self.quadro4, text='Leia as instruções', font='arial 24 bold italic', fg='red')
        self.titulo_instrucoes.pack()

        self.quadro5 = Frame(self.janela)
        self.quadro5.pack()

        self.corpo1_instrucoes = Label(self.quadro5, text=self.instrucoes_corpo1, font='arial 16 italic',
                                       fg='blue')
        self.corpo1_instrucoes.pack()

        self.quadro6 = Frame(self.janela)
        self.quadro6.pack()

        self.corpo2_instrucoes = Label(self.quadro6, text=self.instrucoes_corpo2, font='arial 16 italic',
                                       fg='blue')
        self.corpo2_instrucoes.pack()

        self.quadro7 = Frame(self.janela)
        self.quadro7.pack()

        self.corpo3_instrucoes = Label(self.quadro7, text=self.instrucoes_corpo3, font='arial 16 italic',
                                       fg='blue')
        self.corpo3_instrucoes.pack()

        self.janela.mainloop()

    def validacao_audio(self):
        self.audio = True
        self.video = False

    def validacao_video(self):
        self.audio = False
        self.video = True

    def validacao_video_audio(self):
        self.audio = False
        self.video = False

    def dowload(self, link):
        try:
            if self.audio:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.filter(only_audio=True).first().download(pasta)
                dowload_completo()
            elif self.video:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.filter(only_video=True).first().download(pasta)
                dowload_completo()
            else:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.get_highest_resolution().download(pasta)
                dowload_completo()
        except RegexMatchError:
            mensagem_erro()


Dowloader()
