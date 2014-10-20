from tkinter import *
from tkinter import ttk


class Roughnote:


    def __init__(self):

        self.root=Tk()
        self.root.title('RoughNOTE')
        self.root.geometry("700x450")
       

        self.ta=Text(self.root,height=250, width=250)
        self.ta.pack(fill=BOTH)


        self.lb=None

        self.fonts=None

        self.lbs=None

        self.nf=None
        self.ns=10
        self.sty='normal'
        
        m=Menu()

        self.root.config(menu=m)

        filemenu=Menu(m)

        m.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='New',command=self.newfile)
        filemenu.add_command(label='Open',command=self.openfile)
        filemenu.add_command(label='Save',command=self.savefile)
        filemenu.add_command(label='Exit',command=self.quitapp)

        formatmenu=Menu(m)

        m.add_cascade(label="Format",menu=formatmenu)
        formatmenu.add_command(label='Font',command=self.newfont)
        

        helpmenu=Menu(m)

        m.add_cascade(label="Help",menu=helpmenu)
        helpmenu.add_command(label='About RoughNOTE..',command=self.about)

        self.file=None
        self.root.mainloop()

    def quitapp(self):
        self.root.destroy()
        

    def about(self):

        messagebox.showinfo('RoughNOTE','This was developed by SENTHIL')

    def newfile(self):

        self.ta.delete(1.0,END)
        self.file= None
        
            
    def openfile(self):

        self.file=filedialog.askopenfilename(title='Select a file to open')

        if self.file == "":
            
            self.file = None
        else:
            f=open(self.file,'r')
            self.ta.insert(END,f.read())
            f.close()

    def savefile(self):

        if self.file == None:
            
            self.file=filedialog.asksaveasfilename(defaultextension='.txt')
            f=open(self.file,'w')
            f.write(self.ta.get(1.0,END))
            f.close()

        else:
            
            t=self.ta.get(1.0,END)
            f=open(self.file,'w',encoding='ascii')
            f.write(self.ta.get(1.0,END))
            f.close()

    def newfont(self):

        window=Toplevel()

        window.geometry("450x250")

        window.resizable(height=FALSE,width=FALSE)
          
        lc=ttk.Label(window,text="copyright")
        lc.grid(row=500,column=0)

        l=ttk.Label(window,text='FONT')
        l.grid(row=2,column=2,columnspan=2)

        l2=ttk.Label(window,text='SIZE')
        l2.grid(row=2,column=6,columnspan=2)

        l3=ttk.Label(window,text="STYLE")
        l3.grid(row=2,column=9,columnspan=2)

        self.fonts=('courier', 'helvitica', 'system','castellar','Forte')

        sb=ttk.Scrollbar(window)
        sb.grid(row=4,column=3,sticky='nsew')

        sb2=ttk.Scrollbar(window)
        sb2.grid(row=4,column=9,sticky='nsew')
        
       
        self.lb=Listbox(window,yscrollcommand=sb.set)
        self.lb.grid(row=4,column=2)
        
        sb.config(command=self.lb.yview)

        self.lbs=Listbox(window,yscrollcommand=sb2.set,width=6)
        self.lbs.grid(row=4,column=8)

        sb2.config(command=self.lbs.yview)


        self.lbsty=Listbox(window,height=5)
        self.lbsty.grid(row=4,column=10,sticky='n')

        self.sty=['normal','bold','italic','roman']

        for i in self.sty:
            self.lbsty.insert(END,i)
            
        for i in self.fonts:
            self.lb.insert(END,i)

            
        for i in range(2,50,2):
            self.lbs.insert(END,i)

        

        self.lb.selection_set(0)
        self.lb.bind('<<ListboxSelect>>', self.lbselection)


        self.lbs.bind('<<ListboxSelect>>',self.sizselection)

        self.lbsty.bind('<<ListboxSelect>>',self.styselection)

        b=ttk.Button(window,text='OK',command=window.destroy)
        b.grid(row=350,column=10,sticky='nsew')

    def lbselection(self,event):

        s=self.lb.curselection()
        i=s[0]
        tmp=self.ta.get(1.0,END)
        self.ta.delete(1.0,END)
        self.nf=self.fonts[i]              
        self.ta.config(font=(self.nf,self.ns))
        self.ta.insert(END,tmp)

    def sizselection(self,event):

        self.ns=self.lbs.curselection()
        i=self.ns[0]
        tmp=self.ta.get(1.0,END)
        self.ta.delete(1.0,END)
        self.ta.config(font=(self.nf,self.ns))
        self.ta.insert(END,tmp)

    def styselection(self,event):

        s=self.lbsty.curselection()
        i=s[0]            
        tmp=self.ta.get(1.0,END)
        self.ta.delete(1.0,END)
        f=self.sty[i]
        self.ta.config(font=(self.nf,self.ns,f))
        self.ta.insert(END,tmp)

   

app=Roughnote()
