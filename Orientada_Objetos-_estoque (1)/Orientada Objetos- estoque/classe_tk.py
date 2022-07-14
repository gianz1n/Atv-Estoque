from classe_bd import *
from tkinter import *
from classe_menu import *



Banco_de_dados_gian = Banco_de_Dados()

root = Tk()
root.title('Estoque')
root.geometry('1400x900')
root.resizable(False, False)

fr1 = Frame(root)
bg1 = PhotoImage(file='imagens/TELA LOGIN.png')



#tela login
tela1 = Label(fr1, image=bg1)
nome_cad = Entry(fr1, width=30, font='Barlow 20')
nome_cad.place(x=487, y=431)
senha1 = Entry(fr1, width=30, font='Barlow 20', show='*')
senha1.place(x=487, y=549)
entrar = Button(fr1,font='Barlow 20', text='ENTRAR', fg='#0f1d22', bg='white', bd=0, relief='solid', cursor='hand2', command=lambda: [fr1.forget(), fr2.pack()])
entrar.place(x=635, y=710)

fr2 = Frame()
bg2 = PhotoImage(file='imagens/TELA PRINCIPAL.png')

#tela principal
tela2 = Label(fr2, image=bg2)
#cadastros
txt1 = Button(fr2, bg='white', text='CADASTRAR FABRICANTES', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr3.pack()])
txt1.place(x=65, y=330)
txt2 = Button(fr2, bg='white', text='CADASTRAR PRODUTOS', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr4.pack()])
txt2.place(x=65, y=450)
#ações
txt3 = Button(fr2, bg='white', text='LISTAR PRODUTOS', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr5.pack()])
txt3.place(x=500, y=330)
txt3 = Button(fr2, bg='white', text='HISTÓRICO', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr6.pack()])
txt3.place(x=500, y=440)
txt4 = Button(fr2, bg='white', text='ALTERAR NOME', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr7.pack()])
txt4.place(x=500, y=570)
#negociações
txt5 = Button(fr2, bg='white', text='COMPRAR', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr8.pack()])
txt5.place(x=930, y=330)
txt6 = Button(fr2, bg='white', text='VENDER', fg='#0f1d22', font='Oswald 18 bold', width=24, borderwidth=0, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr9.pack()])
txt6.place(x=930, y=440)

#botao menu principal
bt_ntc = PhotoImage(file='imagens/ntc.png')
bt_menu = Button(fr2,image=bt_ntc, borderwidth=0, width=100, relief='solid', cursor='hand2', command=lambda: [fr2.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)


#tela cadastro fabricantes

fr3 = Frame()
bg3 = PhotoImage(file='imagens/TELA CADASTRO FABRICANTES.png')
tela3 = Label(fr3, image=bg3)
bt_menu = Button(fr3,image=bt_ntc, borderwidth=0, width=100, cursor='hand2', command=lambda: [fr3.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)

fabricante_ent = Entry(fr3, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
fabricante_ent.place(x=510, y=420)

bg_seta1 = PhotoImage(file='imagens/seta.PNG')
confirma_fab = Button(fr3, image=bg_seta1, borderwidth=1, fg='white', command=lambda: [Banco_de_dados_gian.cadastrar_fabricante(nome=fabricante_ent.get(), cod=None)])
confirma_fab.place(x=640, y=480)


#cadastrar produtos

fr4 = Frame()
bg4 = PhotoImage(file='imagens/CADASTRAR PORDUTO.png')
tela4 = Label(fr4, image=bg4)

bt_menu = Button(fr4,image=bt_ntc, borderwidth=0, width=100, relief='solid', cursor='hand2', command=lambda: [fr4.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)

nome2 = Entry(fr4, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
nome2.place(x=520, y=510)
fabricante1 = Entry(fr4, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
fabricante1.place(x=520, y=370)

bg_seta = PhotoImage(file='imagens/seta.PNG')
confirma3 = Button(fr4, image=bg_seta, borderwidth=0, relief='solid', command=lambda: [Banco_de_dados_gian.cadastrar_produto(cod=None, nome=nome2.get(), fabricante=fabricante_ent.get(), quantidade=0)])
confirma3.place(x=670, y=600)

#listar produtos
fr5 = Frame()
bg5 = PhotoImage(file='imagens/TELA LISTAR.png')
tela5 = Label(fr5, image=bg5)

bt_menu = Button(fr5,image=bt_ntc, borderwidth=0, width=100, cursor='hand2', command=lambda: [fr5.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)


txt7 = Label(fr5, font='Oswald 18 bold', bg='white',fg='#0F1D22', text='ESCREVA O COD DO PRODUTO')
txt7.place(x=500, y=350)
list = Entry(fr5, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
list.place(x=550, y=400)

#historico

fr6 = Frame()
bg6 = PhotoImage(file='imagens/TELA HISTORICO.png')
tela6 = Label(fr6, image=bg6)

bt_menu = Button(fr6,image=bt_ntc, borderwidth=0, width=100, cursor='hand2', command=lambda: [fr6.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)

bg_seta6 = PhotoImage(file='imagens/seta.PNG')
altera4 = Button(fr6, image=bg_seta6, borderwidth=1, command=lambda: [listar_historico_compra()])
altera4.place(x=645, y=320)

def listar_historico_compra():
    db = Banco_de_dados_gian.listar_historico_compra()
    for i in range(len(db.listar_historico_compra)):
        print(len(db.listar_historico_compra[i]))
        listar_historico_compra.insert(END, db.listar_historico_compra[i])
    else:
        pass

#alterar nome

fr7 = Frame()
bg7 = PhotoImage(file='imagens/ALTERA NOME.png')
tela7 = Label(fr7, image=bg7)

bt_menu = Button(fr7,image=bt_ntc, borderwidth=0, width=100, cursor='hand2', command=lambda: [fr7.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)

cod2 = Entry(fr7, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
cod2.place(x=510, y=400)

altera_nome = Entry(fr7, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
altera_nome.place(x=510, y=540)

atributo = 'nome_produto'

bg_seta4 = PhotoImage(file='imagens/seta.PNG')
altera1 = Button(fr7, image=bg_seta4, borderwidth=1, command=lambda: [Banco_de_dados_gian.alterar_nome(atributo=atributo, valor=altera_nome.get(), cod=cod2.get())])
altera1.place(x=650, y=580)

#comprar
fr8 = Frame()
bg8 = PhotoImage(file='imagens/COMPRAR.png')
tela8 = Label(fr8, image=bg8)

bt_menu = Button(fr8,image=bt_ntc, borderwidth=0, width=100, cursor='hand2', command=lambda: [fr8.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)

compra1 = Entry(fr8, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
compra1.place(x=510, y=350)
compra_qtd = Entry(fr8, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0, width=6)
compra_qtd.place(x=650, y=565)

compra = 'quantidade_produto'

bg_seta2 = PhotoImage(file='imagens/seta.PNG')
confirma5 = Button(fr8, image=bg_seta2, borderwidth=1, command=lambda: [Banco_de_dados_gian.comprar_produtos(atributo=compra,cod=compra1.get(), quantidade=compra_qtd.get())])
confirma5.place(x=645, y=615)


#vender
fr9 = Frame()
bg9 = PhotoImage(file='imagens/VENDER.png')
tela9 = Label(fr9, image=bg9)

bt_menu = Button(fr9,image=bt_ntc, borderwidth=0, width=100, cursor='hand2', command=lambda: [fr9.forget(), fr2.pack()])
bt_menu.place(x=40, y=25)

venda1 = Entry(fr9, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0)
venda1.place(x=510, y=350)
venda_qtd = Entry(fr9, font='Oswald 18 bold', bg='#d9d9d9', borderwidth=0, width=6)
venda_qtd.place(x=650, y=565)

venda = 'quantidade_produto'

bg_seta3 = PhotoImage(file='imagens/seta.PNG')
confirma7 = Button(fr9, image=bg_seta1, borderwidth=1, command=lambda: [Banco_de_dados_gian.vender_produtos(atributo=venda, cod=venda1.get(), quantidade_final=venda_qtd.get())])
confirma7.place(x=645, y=615)

fr1.pack()
tela1.pack()
tela2.pack()
tela3.pack()
tela4.pack()
tela5.pack()
tela6.pack()
tela7.pack()
tela8.pack()
tela9.pack()
root.mainloop()
