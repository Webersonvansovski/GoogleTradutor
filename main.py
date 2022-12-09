from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

janela = Tk()
janela.title("Google Tradutor (by w.vansovski)")
janela.geometry("1080x400")
janela.resizable(False, False)
janela.config(background="white")


def muda_label():
    c = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c2)
    janela.after(1000, muda_label)


def traduzir_agora():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trad_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trad_text = trad_text.text

    text2.delete(1.0, END)
    text2.insert(END, trad_text)


# icon
img_icon = PhotoImage(file="GT_Icon.png")
janela.iconphoto(False, img_icon)

# seta

seta_img = PhotoImage(file="arrow.png")
img_label = Label(janela, image=seta_img, width=150)
img_label.place(x=460, y=50)

idioma = googletrans.LANGUAGES
idiomav = list(idioma.values())
idio = idioma.keys()

# primeiro combox
combo1 = ttk.Combobox(janela, values=idiomav, font="Roboto 14", state='r')
combo1.place(x=110, y=20)
combo1.set("PORTUGUESE")

label1 = Label(janela, text="PORTUGUESE", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)


# segundo combox
combo2 = ttk.Combobox(janela, values=idiomav, font="Roboto 14", state='r')
combo2.place(x=730, y=20)
combo2.set("SELECIONE O IDIOMA")

label2 = Label(janela, text="PORTUGUESE", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# primeiro frame
f = Frame(janela, bg='Black', bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# segundo frame
f2 = Frame(janela, bg='Black', bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# botao de traduzir
traduzir = Button(janela, text="Traduzir", font=('Roboto', 15), activebackground="white", cursor="hand2",
                 bd=1, width=10, height=2, bg='black', fg="white", command=traduzir_agora )
traduzir.place(x=476, y=256)


muda_label()

janela.mainloop()