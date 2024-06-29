import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from QuoranDb import *

class Quoran(Frame):
    def __init__(self,master):
        super(Quoran,self).__init__(master)
        self.create_widget()
        #self.setchaptersAndVerse()
    def create_widget(self):
        Label(self.master,text="Chapter ",font=("Elephant",15)).place(x=190,y=20)
        Label(self.master, text=" Verse  ", font=("Elephant", 15)).place(x=190, y=70)
        Button(self.master,text="<<",font=("Segoe Script",20),command=self.prev).place(x=40,y=20)
        Button(self.master,text=">>",font=("Segoe Script",20),command=self.next).place(x=500,y=20)
        self.contexteng=Text(self.master, height = 5, width = 35, font=("Elephant",15), relief = RAISED, state = DISABLED, wrap = WORD, selectborderwidth=5)
        self.contexteng.place(x=80, y=170)
        self.contextarb = Text(self.master, height=5, width=35, font=("Elephant", 15), relief=RAISED, state=DISABLED,wrap=WORD, selectborderwidth=5)
        self.contextarb.place(x=80, y=370)
        self.chapterbox = Combobox(self.master, width=10,font=("Elephant", 15))
        self.chapterbox.place(x=300, y=20)
        self.chapterbox.bind(sequence="<<ComboboxSelected>>", func=self.chapterchanged)
        self.chapterbox.bind(sequence="<KeyRelease>", func=self.chapterchanged)
        self.chapterbox.configure(values=[x for x in range(1,115)])
        self.versebox = Combobox(self.master, width=10, font=("Elephant", 15))
        self.versebox.place(x=300, y=70)
        self.versebox.bind(sequence="<<ComboboxSelected>>", func=self.versechanged)
        self.versebox.bind(sequence="<KeyRelease>", func=self.versechanged)

    """def setchaptersAndVerse(self):
        self.versecount = getAllVerse(1)
        self.currentchapter = self.chapterbox.get()
        self.currentverse = self.versebox.get()"""
    def chapterchanged(self,_=""):
        self.currentchapter = self.chapterbox.get()
        self.versecount = getAllVerse(self.currentchapter)
        self.versebox.set(1)
        self.versebox["values"] = [x for x in range(1,self.versecount+1)]
        self.currentverse = self.versebox.get()
        self.getcontent()
    def versechanged(self,_=""):
        self.currentverse = self.versebox.get()
        self.getcontent()
    def getcontent(self):
        self.currentchapter = self.chapterbox.get()
        self.currentverse = self.versebox.get()
        self.versecontent_eng = getEngContext( self.currentchapter , self.currentverse )
        self.contexteng.configure(state = NORMAL)
        self.contexteng.delete("1.0",END)
        self.contexteng.insert(END,self.versecontent_eng)
        self.contexteng.configure(state=DISABLED)

        self.versecontent_arb = getArbContext(self.currentchapter, self.currentverse)
        self.contextarb.configure(state=NORMAL)
        self.contextarb.delete("1.0", END)
        self.contextarb.insert(END, self.versecontent_arb)
        self.contextarb.configure(state=DISABLED)

    def prev(self):
        try:
            if int(self.versebox.get()) == 1:
                self.chapterbox.current(int(self.chapterbox.get()) - 2)
                self.chapterchanged()
            else:
                self.versebox.current(int(self.versebox.get())-2)
                self.versechanged()
        except:
            pass
    def next(self):
        try:
            if int(self.versebox.get()) == getAllVerse(self.chapterbox.get()):
                self.chapterbox.current(int(self.chapterbox.get()))
                self.chapterchanged()
            else:
                self.versebox.current(int(self.versebox.get()))
                self.versechanged()
        except:
            pass
        
def run():
    window=Tk()
    frame=Quoran(window)
    window.geometry("650x550+5+5")
    window.title("Q U O R A N")
    window.mainloop()
    
if __name__=='__main__':
    run()
    
    