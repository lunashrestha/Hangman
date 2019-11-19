from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import  choice

window = Tk()
window.title("Ready to Hang!! You have 5 chances")
window.geometry("800x700")

words = choice(["CHAIRS", "PYTHON", "FRIEND", "CLOCKS", "KNIVES", "NINJAS", "PIZZAS", "PUZZLE"
                "ACTIVE", "HOOKAH", "ADJUST", "DREAMS", "SCHOOL", "RUNNER", "CEMENT"])

chances=4;
image_paths=['hang.jpg','img4.jpg','img3.jpg','img2.jpg','img1.jpg']
img = Image.open(image_paths[chances])
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=0, row=0)
answer_arr=[]
def clicked(alphabet):
    global chances
    answer= words;
    if alphabet in answer: #It checks whether the albpbet is there in the answer
        if alphabet==answer[0]:
            btn01["text"] = alphabet;
        if alphabet==answer[1]:
            btn02["text"] = alphabet;
        if alphabet==answer[2]:
            btn03["text"] = alphabet;
        if alphabet==answer[3]:
            btn04["text"] = alphabet;
        if alphabet==answer[4]:
            btn05["text"] = alphabet;
        if alphabet==answer[5]:
            btn06["text"] = alphabet;
    else:
        txt="Chances remaining "+str(chances);
        label1.configure(text=txt)
        chances = chances - 1;
        image = Image.open(image_paths[chances])
        image = image.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew

        if chances<0:
            messagebox.showinfo("Loose to guess","Hanged!!!!!")
            window.destroy()
    if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5]:
        messagebox.showinfo("congratulations", "Win the Game Great Buddy!!!!")
        window.destroy()
    print(chances)
    5


btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn01.grid(column=2, row=0)
btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn02.grid(column=3, row=0)
btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn03.grid(column=4, row=0)
btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn04.grid(column=5, row=0)
btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn05.grid(column=6, row=0)
btn06 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn06.grid(column=7, row=0)


btn1 = Button(window, text="A",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="B",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="C",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="D",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="E",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn5.grid(column=5, row=1)
btn6 = Button(window, text="F",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
btn6.grid(column=6, row=1)
btn7 = Button(window, text="G",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
btn7.grid(column=7, row=1)
btn8 = Button(window, text="H",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
btn8.grid(column=8, row=1)

btn21 = Button(window, text="I",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn21.grid(column=1, row=2)
btn9 = Button(window, text="J",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
btn9.grid(column=2, row=2)
btn10 = Button(window, text="K",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
btn10.grid(column=3, row=2)
btn11= Button(window, text="L",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn11.grid(column=4, row=2)
btn12 = Button(window, text="M",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn12.grid(column=5, row=2)
btn13 = Button(window, text="N",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn13.grid(column=6, row=2)
btn14 = Button(window, text="O",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn14.grid(column=7, row=2)
btn22 = Button(window, text="P",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn22.grid(column=8, row=2)

btn23 = Button(window, text="Q",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
btn23.grid(column=2, row=3)
btn15= Button(window, text="R",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn15.grid(column=3, row=3)
btn16 = Button(window, text="S",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn16.grid(column=4, row=3)
btn17 = Button(window, text="T",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn17.grid(column=5, row=3)
btn18 = Button(window, text="U",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn18.grid(column=6, row=3)
btn24 = Button(window, text="V",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
btn24.grid(column=7, row=3)

btn25 = Button(window, text="W",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn25.grid(column=3, row=4)
btn19 = Button(window, text="X",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn19.grid(column=4, row=4)
btn20 = Button(window, text="Y",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn20.grid(column=5, row=4)
btn26 = Button(window, text="Z",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn26.grid(column=6, row=4)

label1=Label(window,text="Total Chances are : 5")
label1.grid(row=5,column=0)
window.mainloop()
