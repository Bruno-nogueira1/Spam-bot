from os import close
from tkinter import *
from time import sleep
import pyautogui as auto

root = Tk()

root.title('SPAM BOT')
root.iconbitmap('icone.ico')
root.configure(background='#3be8b0')
root.geometry('400x250')
root.resizable(False,False)

def main():
    spamvaria = spam.get()
    delayvaria = float(delay.get())
    quantidadevaria  = int(quantidade.get())
    arq = open('spam.txt', 'w+',encoding='utf8')
    arq.write(spamvaria)
    for c in range(quantidadevaria):
        arq = open('spam.txt', 'r',encoding='utf8')
        for frase in arq:
            sleep(delayvaria)
            auto.typewrite(' ')
            auto.typewrite(frase)
            auto.press('enter')
    
botao = Button(text='Iniciar',command=main,width=12,height=2,background='#cd595a',font='Times,12,bold').place(x=141,y=185)

spamtext = Label(root,text='Spam',background='#3be8b0',font='Times,16,bold',width=23,justify='left').place(x=93,y=25)
spam = Entry(root,background='#ffaaaa',width=35,justify='center')
spam.place(x=93,y=50)

delaytext = Label(root,text='Delay',background='#3be8b0',font='Times,16,bold',width=23,justify='center').place(x=93,y=75)
delay = Entry(root,background='#ffaaaa',width=35,justify='center')
delay.place(x=93,y=100)

quantidadetext = Label(root,text='Quantidade',background='#3be8b0',font='Times,16,bold',width=23,justify='center').place(x=93,y=125)
quantidade = Entry(root,background='#ffaaaa',width=35,justify='center')
quantidade.place(x=93,y=150)


root.mainloop()