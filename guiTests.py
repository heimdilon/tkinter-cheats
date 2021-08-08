# kütüphaneleri ekleme
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu

#Pencere ve combobox oluşturma
window = Tk()
combo = Combobox(window)

#Pencereye başlık yazma
window.title("Deneme")

#Pencere boyutlarını belirleme
window.geometry('600x400')

def menuClick():
    #Ne istersen
    return
#Menü değişkeni oluşturma
menu = Menu(window)
menu2 = Menu(window)

#Menü oluşturma
new_item = Menu(menu, tearoff=0)
new_item2 = Menu(menu2, tearoff=0)

#Menü adını verme
menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label='View', menu=new_item2)

#Menüye seçenek oluşturma
new_item.add_command(label='New')
new_item2.add_command(label='code')

#Ayırıcı oluşturma
new_item.add_separator()

#Menüye seçenek oluşturma
new_item.add_command(label='Edit')

#Menüye seçenek oluşturma ve bu seçeneğe tıklayınca hangi fonksiyonun çalışacağını belirleme
new_item.add_command(label='Newer', command=menuClick)

#Menü penceresini ayarlama
window.config(menu=menu)

#Stil değişkeni oluşturma
style = ttk.Style()

#Stil teması seçme
style.theme_use('default')

#Progres barın renk ayarları
style.configure("black.Horizontal.TProgressbar", background='black')

#Progress bar oluşturma
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

#Progress barın değerini ayarlama
bar['value'] = 70

#Barın yerini ayarlama
bar.grid(column=0, row=6)

#Özel değerli spinbox oluşturma
#spin = Spinbox(window, values=(3, 8, 11), width=5)

#Spinbox default değer verme
#var =IntVar()
#var.set(36)
#spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

#Spinbox oluşturma
spin = Spinbox(window, from_=1900, to_=2020, width=5)

#spinbox yerini ayarlama
spin.grid(column=0, row=5)

#Mesaj kutusu fonksiyonu
def MessageClick():
    messagebox.showinfo('Baslik', 'Icerik')

#Warning ve error mesajı göstermek
#messagebox.showwarning('Message title', 'Message content')
#messagebox.showerror('Message title', 'Message content')

#Çeşitli sorular mesaj kutusu olarak
#res = messagebox.askquestion('Message title','Message content')
#res = messagebox.askyesno('Message title','Message content')
#res = messagebox.askyesnocancel('Message title','Message content')
#res = messagebox.askokcancel('Message title','Message content')
#res = messagebox.askretrycancel('Message title','Message content')

#Mesaj kutusu çıkarmak için buton oluşturma
btn3 = Button(window, text='Mesaj kutusu butonu', command=MessageClick)

#Butonun yerini ayarlama
btn3.grid(column=0, row=4)

#Radio Button için değişken oluşturma
selected = IntVar()

#Butona tıklayınca olan fonksiyon
def radClicked():
    print(selected.get())

#Radio Button oluşturma ve basılınca yapılacak fonksiyonu seçme
#rad1 = Radiobutton(window,text='First', value=1, command=radClicked)
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

#Buton oluşturma ve basılınca gerçekleşicek fonksiyonu atama
btn2 = Button(window, text="Tikla", command=radClicked)

#butonun yerini ayarlama
btn2.grid(column=3, row=3)

#Radio Button yerini ayarlama
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)


#Alternatif check button değer

#chk_state = IntVar()
#chk_state.set(0)   uncheck
#chk_state.set(1)   check

#Değişken türü True False belirleme
chk_state = BooleanVar()

#Başlangıcı true olarak belirleme
chk_state.set(True)

#Check button oluşturma ve değişken türü ayarlama
chk = Checkbutton(window, text='Sec', var=chk_state)

#Check button un yerini ayarlama
chk.grid(column=0, row=1)

#Combobox içeriğini belirleme
combo['values']= (1, 2, 3, 4, 5, "Text")

#Seçilen değeri almak başlangıç değeri
combo.current(0)

#combobox yerini ayarlama
combo.grid(column=3, row=0)

#comboboxtaki değeri almak
print(combo.get())

#Yazı yazma
lbl = Label(window, text="Merhaba")

#yazının yerini ayarlama
lbl.grid(column=0, row=0)

#Tekil metin girişi oluşturma ve genişliğini ayarlama
txt = Entry(window, width=10)

#metin girişinin yerini ayarlama
txt.grid(column=1, row=0)

#metin girişine odaklanır ve direkt yazılabilir
txt.focus()

def clicked():
    #Hosgelinin arkasına metingirişinden yazılanı ekleme
    res = "Hosgeldin " + txt.get()
    #Yazılan metini yazdırma
    lbl.configure(text= res)

#Buton oluşturma ve butona tıklanınca hangi komutun çalışacağını belirleme
btn = Button(window, text="Bana tikla", command=clicked)

#Butonun yerini ayarlama
btn.grid(column=2, row=0)

#Pencerenin döngü halinde açık kalmasını sağlar
window.mainloop()