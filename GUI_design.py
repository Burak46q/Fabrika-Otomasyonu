
from tkinter import messagebox, ttk
from tkinter import*
import customtkinter as ctk
import sqlite3
from functools import partial
import tkinter as tk

db= sqlite3.connect('data.db')
cur=db.cursor()
sayac=0



class ARAYUZ():
    
    def __init__(self,master) :
        #WİNDOW AND CONFİGURATİON
        ctk.set_appearance_mode('system')
        self.master = master
        self.geometry = master.geometry('1300x700')
        
        self.resizable= master.resizable(width=False,height=FALSE)
        self.master.title('İşletme Bilgisayar Bilgileri')

        frame=ctk.CTkFrame(master,width=1500,height=700)
        frame.place(x=0,y=0)
        #CREATE TABLE 1
        ARAYUZ.tablo_create(self,frame)
        #CREATE TABLE 2
        ARAYUZ.table_create2(self,frame)
        #CREATE BUTTONS AND ENTRYS
        ARAYUZ.buttons(self,frame)
        #TABLE 1 INSERT SQL DATA
        SCRIPTS.yazdır(self)
        #HİSTORY 
        SCRIPTS.allhistory(self)
        
        
        master.mainloop()

    
    def  theme_change(self): 
        if self.switch.get()==1:
            ctk.set_appearance_mode('dark')
            self.style.configure('Treeview',background='#363636',foreground='white',fieldbackground='black')
            self.style.configure('TreeviewHeading',background='gray',foreground='white')
            
        else:
           ctk.set_appearance_mode('light') 
           self.style.configure('Treeview',background='white',foreground='#363636')
           
    def tablo_create(self,master):
        
        self.frametable1=Frame(master,width='1290px',height='350px')
        self.frametable1.place(x=10,y=70)    
        self.table = ttk.Treeview(self.frametable1,height=12,show='headings')
        self.style = ttk.Style()
        sb=ttk.Scrollbar(self.frametable1,orient=tk.VERTICAL,command=self.table.yview)
        self.table.configure(yscrollcommand=sb.set)
      
        self.table['columns'] = ('ID','name', 'pc_name', 'pc_features', 'pc_username','printers','windowsKEY','officeKEY','phone','unit','control')
        self.table.column("#0", width=0,  stretch=YES)
        self.table.column('ID',anchor=CENTER,width=40)
        self.table.column("name",anchor=CENTER, width=160)
        self.table.column("pc_name",anchor=CENTER,width=150)
        self.table.column("pc_features",anchor=CENTER,width=150)
        self.table.column("pc_username",anchor=CENTER,width=200)
        self.table.column("printers",anchor=CENTER,width=160)
        self.table.column("windowsKEY",anchor=CENTER,width=70)
        self.table.column("officeKEY",anchor=CENTER,width=70)
        self.table.column("phone",anchor=CENTER,width=90)
        self.table.column("unit",anchor=CENTER,width=120)
        self.table.column("control",anchor=CENTER,width=60)

        self.table.heading("#0",text="\n\n",anchor=CENTER )
        self.table.heading('ID',text='ID',anchor=CENTER)
        self.table.heading("name",text="İSİM",anchor=CENTER)
        self.table.heading("pc_name",text="PC ADI",anchor=CENTER)
        self.table.heading("pc_features",text="PC ÖZELLİKLERİ",anchor=CENTER)
        self.table.heading("pc_username",text="KULLANICI ADI",anchor=CENTER)
        self.table.heading("printers",text="YAZICILAR",anchor=CENTER)
        self.table.heading("officeKEY",text="OFFİCE \n   KEY",anchor=CENTER)
        self.table.heading("windowsKEY",text="WINDOWS \n   KEY",anchor=CENTER)
        self.table.heading("phone",text="TELEFON",anchor=CENTER)
        self.table.heading("unit",text="BİRİM",anchor=CENTER)
        self.table.heading("control",text="KONTROL",anchor=CENTER)
        self.style.theme_use('alt')
        self.style.map('Treeview', font=[('selected','Arial 9 bold')], background=[('selected', 'darkblue')],foreground=[('selected','red')])
        self.table.grid(row=0,column=0,sticky='nsew')
        sb.grid(row=0,column=1,sticky='ns')
        self.table.bind('<Double-1>',self.noneselect)
        self.table.bind('<<TreeviewSelect>>',lambda event :self.item_selected(self))
     
        
    def table_create2(self,master):

        self.table2 = ttk.Treeview(master,height=11,show='headings')

        self.table2['columns'] = ('ID','pc_name', 'date', 'yapılanis')
        self.table2.column("#0", width=0,  stretch=YES)
        self.table2.column('ID',anchor=CENTER,width=200)
        self.table2.column("pc_name",anchor=CENTER, width=200)
        self.table2.column("date",anchor=CENTER,width=200)
        self.table2.column("yapılanis",anchor=CENTER,width=670)
    

        self.table2.heading("#0",text="\n\n",anchor=CENTER )
        self.table2.heading('ID',text='ID',anchor=CENTER)
        self.table2.heading("pc_name",text="PC ADI",anchor=CENTER)
        self.table2.heading("date",text="TARİH",anchor=CENTER)
        self.table2.heading("yapılanis",text="YAPILAN İŞ",anchor=CENTER)
        self.style.map('Treeview', font=[('selected','Arial 9 bold')], background=[('selected', 'darkblue')],foreground=[('selected','ORANGE')])
        self.table2.place(x=10,y=420)
    def item_selected(self,event):
        
            if self.table.selection():

                self.buton3.place(x=1050,y=370)
                self.buton6.place(x=1150,y=370)
                self.buton8.place(x=930,y=370)
                
            
    def noneselect(self,event):
        
        
            for i in self.table.selection():
                self.table.selection_remove(i)
            self.buton3.place_forget()
            self.buton6.place_forget()
            self.buton8.place_forget()
                    
    def buttons(self,master):

        self.sv = StringVar()
        self.dv = StringVar()   
        
        ctk.CTkLabel(master,text='MARİTAŞ DENİM\nİŞLETME BİLGİSAYAR BİLGİLERİ',text_font='Arial 15 bold').place(x=530,y=10)

        ctk.CTkLabel(master,text ='id ile ara ',text_font='Arial 11 ',anchor='n').place(x=0,y=20)  
        ctk.CTkLabel(master,text ='isim ile ara ',text_font='Arial 11 ').place(x=120,y=20) 

        ctk.CTkLabel(master,text='YAPILAN İŞLEMLER',text_font='Arial 18 bold').place(x=10,y=380)
         
        self.entry1= ctk.CTkEntry(master,width=100,height=24,textvariable=self.dv)
        self.entry1.place(x=10,y=40)
        self.entry2=ctk.CTkEntry(master,width=150,height=24,textvariable=self.sv)
        self.entry2.place(x=150,y=40)
        self.buton6 = ctk.CTkButton(master,width=120,height=40,text='seçilen ögenin \n geçmişi',command=partial(SCRIPTS.history,self))
        self.buton6.place(x=1150,y=370)
        self.buton3= ctk.CTkButton(master,width=45,height=40,text='seçili ögeyi \n düzenle',command=partial(SCRIPTS.edit,self))
        self.buton3.place(x=1050,y=370)
        self.buton8 = ctk.CTkButton(master,width=100,height=40,text="seçili ögeye \n işlem ekle",command=partial(ARAYUZ.historyregister,self))
        self.buton8.place(x=930,y=370)
        self.buton5 = ctk.CTkButton(master,width=45,height=40,text='yeni kayıt',command=partial(ARAYUZ.register,self))
        self.buton5.place(x=1210,y=20)
        self.switch = ctk.CTkSwitch(master,text='koyu tema',command=self.theme_change)
        self.switch.place(x=1090,y=20)
        self.buton3.place_forget()
        self.buton6.place_forget()
        self.buton8.place_forget()
        self.buton7 = ctk.CTkButton(master,width=120,height=40,text='tüm işlemler',command=partial(SCRIPTS.allhistory,self))
        self.buton7.place(x=290,y=375)
        

        self.sv.trace("w", lambda name, index, mode, sv=self.sv: SCRIPTS.callback(self,self.sv))
        self.dv.trace("w", lambda name, index, mode, dv=self.dv: SCRIPTS.callback2(self,self.dv))
    def edit_widget(self,text3,select_item):
        select_item=select_item
        root2 =Toplevel()
        root2.grab_set()
        root2.title('Kullanıcı Güncelleme')
        root2.geometry('450x500+500+100')
        root2.resizable(width=False,height=False)
        root2.config(background='gray70')
        
        Label(root2,text='ID : '+text3[0],bg='gray70',font='Arial 14 ',justify='left').place(x=1,y=20)
   
        Label(root2,text='İSİM',bg='gray70',font='Arial 8',justify='left').place(x=10,y=80)
        Label(root2,text='PC ADI',bg='gray70',font='Arial 8',justify='left').place(x=10,y=130)
        Label(root2,text='PC ÖZELLİKLERİ',bg='gray70',font='Arial 8',justify='left').place(x=10,y=180)
        Label(root2,text='KULLANICI ADI',bg='gray70',font='Arial 8',justify='left').place(x=10,y=230)
        Label(root2,text='YAZICILAR',bg='gray70',font='Arial 8',justify='left').place(x=10,y=280)
        Label(root2,text='WINDOWS KEY',bg='gray70',font='Arial 8',justify='left').place(x=10,y=330)
        Label(root2,text='OFFİCE KEY',bg='gray70',font='Arial 8',justify='left').place(x=230,y=80)
        Label(root2,text='TELEFON',bg='gray70',font='Arial 8',justify='left').place(x=230,y=130)
        Label(root2,text='BİRİM',bg='gray70',font='Arial 8',justify='left').place(x=230,y=180)
        Label(root2,text='KONTROL',bg='gray70',font='Arial 8',justify='left').place(x=230,y=230)
        self.edit_entry2=ctk.CTkEntry(root2,width=200,placeholder_text=self.text3[1])
        self.edit_entry2.place(x=10,y=100)
        self.edit_entry3=ctk.CTkEntry(root2,width=200,placeholder_text=text3[2])
        self.edit_entry3.place(x=10,y=150)
        self.edit_entry4=ctk.CTkEntry(root2,width=200,placeholder_text=text3[3])
        self.edit_entry4.place(x=10,y=200)
        self.edit_entry5=ctk.CTkEntry(root2,width=200,placeholder_text=text3[4])
        self.edit_entry5.place(x=10,y=250)
        self.edit_entry6=ctk.CTkEntry(root2,width=200,placeholder_text=text3[5])
        self.edit_entry6.place(x=10,y=300)
        self.edit_entry7=ctk.CTkEntry(root2,width=200,placeholder_text=text3[6])
        self.edit_entry7.place(x=10,y=350)
        self.edit_entry8=ctk.CTkEntry(root2,width=200,placeholder_text=text3[7])
        self.edit_entry8.place(x=230,y=100)
        self.edit_entry9=ctk.CTkEntry(root2,width=200,placeholder_text=text3[8])
        self.edit_entry9.place(x=230,y=150)
        self.edit_entry10=ctk.CTkEntry(root2,width=200,placeholder_text=text3[9])
        self.edit_entry10.place(x=230,y=200)
        self.edit_entry11=ctk.CTkEntry(root2,width=200,placeholder_text=text3[10])
        self.edit_entry11.place(x=230,y=250)

        edit_btn = ctk.CTkButton(root2,text='kaydet',width=150,height=30,command=partial(SCRIPTS.kaydet,self,select_item,text3,root2))
        edit_btn.place(x=270,y=340)

    def historyregister(self):    
        root3 =Toplevel()
        root3.title('İşlem Ekle')
        root3.grab_set()
        root3.geometry('450x500+500+100')
        root3.resizable(width=False,height=False)
        root3.config(background='gray70')
        secilenitem=self.table.selection()
        secilen =self.table.item(secilenitem)['values']
        print(secilen)
        text1=secilen[0]
        text2=secilen[2]
        Label(root3,text='İŞLEM EKLE',font='Arial 14 bold',justify='left',bg='gray70').place(x=4,y=30)
        Label(root3,text='ID',bg='gray70',font='Arial 9',justify='left').place(x=10,y=80)
        Label(root3,text='PC ADI',bg='gray70',font='Arial 9',justify='left').place(x=10,y=130)
        Label(root3,text='YAPILAN İŞ',bg='gray70',font='Arial 9',justify='left').place(x=10,y=180)
        self.sv1=StringVar()
        self.sv2=StringVar()
        self.sv3=StringVar()
        self.history_entry2=ctk.CTkEntry(root3,width=80,placeholder_text=text1,textvariable=self.sv1)
        self.history_entry2.place(x=10,y=100)
        self.history_entry3=ctk.CTkEntry(root3,width=200,placeholder_text=text2,textvariable=self.sv2)
        self.history_entry3.place(x=10,y=150)
        self.history_entry4=Text(root3,width=25,height=7,bd=0)
        self.history_entry4.place(x=10,y=200)
        print(self.sv.get(),self.sv2.get())
        history_buton=ctk.CTkButton(root3,text='kaydet',width=150,height=30,command=partial(SCRIPTS.kaydethistory,self,root3))
        history_buton.place(x=110,y=350)
        self.history_entry2.config(state='disabled')
        self.history_entry3.config(state='disabled')
    def register(self): 
   
        root2 =Toplevel()
        root2.title('Kullanıcı Ekle')
        root2.grab_set()
        root2.geometry('450x500+500+100')
        root2.resizable(width=False,height=False)
        root2.config(background='gray70')    
        
        Label(root2,text='KAYIT',bg='gray70',font='Arial 14 ',justify='left').place(x=1,y=20)
   
        Label(root2,text='İSİM',bg='gray70',font='Arial 8',justify='left').place(x=10,y=80)
        Label(root2,text='PC ADI',bg='gray70',font='Arial 8',justify='left').place(x=10,y=130)
        Label(root2,text='PC ÖZELLİKLERİ',bg='gray70',font='Arial 8',justify='left').place(x=10,y=180)
        Label(root2,text='KULLANICI ADI',bg='gray70',font='Arial 8',justify='left').place(x=10,y=230)
        Label(root2,text='YAZICILAR',bg='gray70',font='Arial 8',justify='left').place(x=10,y=280)
        Label(root2,text='WINDOWS KEY',bg='gray70',font='Arial 8',justify='left').place(x=10,y=330)
        Label(root2,text='OFFİCE KEY',bg='gray70',font='Arial 8',justify='left').place(x=230,y=80)
        Label(root2,text='TELEFON',bg='gray70',font='Arial 8',justify='left').place(x=230,y=130)
        Label(root2,text='BİRİM',bg='gray70',font='Arial 8',justify='left').place(x=230,y=180)
        Label(root2,text='KONTROL',bg='gray70',font='Arial 8',justify='left').place(x=230,y=230)
        self.edit_entry2=ctk.CTkEntry(root2,width=200)
        self.edit_entry2.place(x=10,y=100)
        self.edit_entry3=ctk.CTkEntry(root2,width=200)
        self.edit_entry3.place(x=10,y=150)
        self.edit_entry4=ctk.CTkEntry(root2,width=200)
        self.edit_entry4.place(x=10,y=200)
        self.edit_entry5=ctk.CTkEntry(root2,width=200)
        self.edit_entry5.place(x=10,y=250)
        self.edit_entry6=ctk.CTkEntry(root2,width=200)
        self.edit_entry6.place(x=10,y=300)
        self.edit_entry7=ctk.CTkEntry(root2,width=200)
        self.edit_entry7.place(x=10,y=350)
        self.edit_entry8=ctk.CTkEntry(root2,width=200)
        self.edit_entry8.place(x=230,y=100)
        self.edit_entry9=ctk.CTkEntry(root2,width=200)
        self.edit_entry9.place(x=230,y=150)
        self.edit_entry10=ctk.CTkEntry(root2,width=200)
        self.edit_entry10.place(x=230,y=200)
        self.edit_entry11=ctk.CTkEntry(root2,width=200)
        self.edit_entry11.place(x=230,y=250)

        edit_btn = ctk.CTkButton(root2,text='kayıt ekle',width=150,height=30,command=partial(SCRIPTS.kayıtekle,self,root2))
        edit_btn.place(x=270,y=340)
class SCRIPTS(): 
    
    def yazdır(self): 
        a=0 
        data ='SELECT*FROM isletme'
        data2=cur.execute(data)
         
        for i in data2:
            if 'None' or None in i:
                
                newlist=[]
                for b in range(0,11):
                    if i[b]==None :
                        newtext=''
                        
                        newlist.append(newtext)
                        continue
                    elif   i[b] =='None':
                        newtext=''
                        
                        newlist.append(newtext)
                        continue
                    else:  
                        newlist.append(i[b]) 
                
            else :
                newlist=i 
           
            if a%2==1:
                self.table.insert(parent='',index='end',text='',iid=a,tags = ('tag1',),
                values=(str(newlist[0]),str(newlist[1]),str(newlist[2]),newlist[3],newlist[4],newlist[5],newlist[6]
                ,newlist[7],newlist[8],newlist[9],newlist[10]) )
                self.table.tag_configure('tag1',background='gray50',font='Arial 9')
            if a%2==0:    
                self.table.insert(parent='',index='end',text='',iid=a,tags = ('tag2',),
                    values=((newlist[0]),str(newlist[1]),str(newlist[2]),newlist[3],newlist[4],newlist[5],newlist[6]
                ,newlist[7],newlist[8],newlist[9],newlist[10]) )
                
               
                self.table.tag_configure('tag2',background='gray70',font='Arial 9')

            a=a+1   

    
    def callback(self,sv):
            for item in self.table.get_children(): 
                    self.table.delete(item)   
            text=sv.get()
            
            
            data ='SELECT*FROM isletme'
            cur.execute(data)
            data3=cur.fetchall()
            a=0
            artısmik=0
            
            if 'i' in text:
                    val3 = text.replace('i','İ')
            
            else:
                    val3 =text   
            value3 = str(val3).upper()
            uzunluk=len(value3)
            if uzunluk == 0:
                for item in self.table.get_children(): 
                    self.table.delete(item)   
                SCRIPTS.yazdır(self)

            for list in data3:
                
                if 'None' or None in list:
                
                    newlist=[]
                    for b in range(0,11):
                            if list[b]==None :
                                newtext=''
                                
                                newlist.append(newtext)
                                continue
                            elif   list[b] =='None':
                                newtext=''
                                
                                newlist.append(newtext)
                                continue
                            else:  
                                newlist.append(list[b]) 
                    
                else :
                    newlist=list 
                
                if value3 in newlist[1]:
                    
                    values= (str(newlist[0]),newlist[1],newlist[2],newlist[3],newlist[4],newlist[5],newlist[6]
                        ,newlist[7],newlist[8],newlist[9],newlist[10])
                    self.table.insert(parent='',index='end',iid=a,text='',tags = ('tag2',),
                    values=values)
                    a=a+1
                    
                else:
                    artısmik=artısmik+1
                    continue
                    
                artısmik=artısmik+1
            
    def callback2(self,dv):
            for item in self.table.get_children(): 
                    self.table.delete(item)   
            text=dv.get()
            
            
            data ='SELECT*FROM isletme'
            cur.execute(data)
            data3=cur.fetchall()
            a=0
            artısmik=0
            
            for list in data3:
                if 'None' or None in list:
                
                    newlist=[]
                    for b in range(0,11):
                        if list[b]==None :
                            newtext=''
                            
                            newlist.append(newtext)
                            continue
                        elif   list[b] =='None':
                            newtext=''
                            
                            newlist.append(newtext)
                            continue
                        else:  
                            newlist.append(list[b]) 
                
                else :
                    newlist=list 
                value3 = text.upper()
                
                if value3 == newlist[0]:
                    
                    values= (str(newlist[0]),newlist[1],newlist[2],newlist[3],newlist[4],newlist[5],newlist[6]
                        ,newlist[7],newlist[8],newlist[9],newlist[10])
                    self.table.insert(parent='',index='end',iid=a,text='',tags = ('tag2',),
                    values=values)
                    a=a+1
                elif value3 =='':
                    
                    SCRIPTS.yazdır(self)
                elif value3 == 'A': 
                   SCRIPTS.yazdır(self)
                        
                                                 
                else:
                    artısmik=artısmik+1
                    continue
                    
            artısmik=artısmik+1
    def edit(self):

    
           
        select_item=self.table.focus()
        
        self.text3 =self.table.item(select_item)['values'] 
        if select_item =='':
            pass 
        else:
            self.newtext=['','','','','','','','','','']
            ARAYUZ.edit_widget(self,self.text3,select_item)

    def kaydethistory(self,master):
        
        if self.history_entry4.get('1.0','end-1c')=='' or None:
            messagebox.showerror('eksik veri','lütfen boş alanları doldurunuz..')
        else:
            import time
            tarih = time.strftime('%d.%m.%Y  -  %H.%M')
            id = self.sv1.get()
            data = "INSERT INTO pc_history (id,pcname,date,history) VALUES ('{}','{}','{}','{}')".format(id,self.sv2.get(),tarih,self.history_entry4.get('1.0',END))
            cur.execute(data)
            db.commit()
            messagebox.showinfo('sucessfuly.','yapılan iş başarıyla kaydedildi..')
            master.destroy()
            SCRIPTS.history(self)

    def kayıtekle(self,master): 
        newtext=['','','','','','','','','','']
        lock = 0
        if self.edit_entry2.get()=='':   
            messagebox.showerror('Eksik Veri','İSİM GİRİNİZ..')
        elif ',' in self.edit_entry2.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            if 'i' in self.edit_entry2.get():
                val3 = str(self.edit_entry2.get()).replace('i','İ')
                
            else:
                val3 =str(self.edit_entry2.get())   
            value3 = str(val3).upper()
            newtext[0]=value3
            lock = lock +1
        if self.edit_entry3.get()=='':   
            messagebox.showerror('Eksik Veri','BİLGİSAYAR ADI GİRİNİZ..')
            
        elif ',' in self.edit_entry3.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[1]=self.edit_entry3.get()
            lock = lock +1 
        
        if self.edit_entry4.get()=='':   
            newtext[2]=''
            lock = lock +1
        elif ',' in self.edit_entry4.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[2]=self.edit_entry4.get()
            lock = lock +1
        
        if self.edit_entry5.get()=='':   
            newtext[3]=''
            lock = lock +1
        elif ',' in self.edit_entry5.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[3]=self.edit_entry5.get()
            lock = lock +1
        
        if self.edit_entry6.get()=='':   
            newtext[4]=''
            lock = lock +1
        elif ',' in self.edit_entry6.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[4]=self.edit_entry6.get()
            lock = lock +1
       
        if self.edit_entry7.get()=='':   
            newtext[5]=''
            lock = lock +1
        elif ',' in self.edit_entry7.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[5]=self.edit_entry7.get()
            lock = lock +1

        if self.edit_entry8.get()=='':   
            newtext[6]=''
            lock = lock +1
        elif ',' in self.edit_entry8.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[6]=self.edit_entry8.get()
            lock = lock +1
        if self.edit_entry9.get()=='':   
            newtext[7]=''
            lock = lock +1
        elif ',' in self.edit_entry9.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[7]=self.edit_entry9.get() 
            lock = lock +1
        if self.edit_entry10.get()=='':   
            newtext[8]=''
            lock = lock +1
        elif ',' in self.edit_entry10.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[8]=self.edit_entry10.get()
            lock = lock +1
        if self.edit_entry11.get()=='':   
            newtext[9]=''
            lock = lock +1
        elif ',' in self.edit_entry11.get():
            messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
        else:
            newtext[9]=self.edit_entry11.get()
            lock = lock +1

        if lock >=10:    
            cur.execute('select*from isletme') 
            rows_dat=cur.fetchall()    
            rows=len(rows_dat)+1  
            if 'i' in newtext[0]:
               valisim= newtext[0].replace('i','İ')
            else:
                valisim=newtext[0] 
            valisim2=valisim.upper()       
            query="""INSERT INTO isletme  (id,İSİM,BİLGİSAYARADI,BİLGİSAYARÖZELLİKLERİ,KULLANICIADI,YAZICILAR,WINDOWSKEY,OFFİCEKEY,TELEFON,BİRİM,KONTROL) 
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') """.format('A'+str(rows),valisim2,newtext[1],newtext[2],newtext[3],newtext[4],newtext[5],newtext[6],newtext[7],newtext[8],newtext[9])	
            cur.execute(query)
            db.commit()
            messagebox.showinfo('kayıt','kullanıcı başarıyla kaydedildi..')
            master.destroy()
            SCRIPTS.yazdır(self) 

    def kaydet(self,select_item,text3,master):
            newtext=['','','','','','','','','',''] 
            lock = 0
            if self.edit_entry2.get()=='':   
                newtext[0]=text3[1]
                lock = lock +1
            elif ',' in self.edit_entry2.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[0]=self.edit_entry2.get()
                lock = lock +1
            if self.edit_entry3.get()=='':   
                newtext[1]=text3[2]
                lock = lock +1
            elif ',' in self.edit_entry3.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[1]=self.edit_entry3.get()
                lock = lock +1 
            
            if self.edit_entry4.get()=='':   
                newtext[2]=text3[3]
                lock = lock +1
            elif ',' in self.edit_entry4.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[2]=self.edit_entry4.get()
                lock = lock +1
            
            if self.edit_entry5.get()=='':   
                newtext[3]=text3[4]
                lock = lock +1
            elif ',' in self.edit_entry5.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[3]=self.edit_entry5.get()
                lock = lock +1
            
            if self.edit_entry6.get()=='':   
                newtext[4]=text3[5]
                lock = lock +1
            elif ',' in self.edit_entry6.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[4]=self.edit_entry6.get()
                lock = lock +1
        
            if self.edit_entry7.get()=='':   
                newtext[5]=text3[6]
                lock = lock +1
            elif ',' in self.edit_entry7.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[5]=self.edit_entry7.get()
                lock = lock +1

            if self.edit_entry8.get()=='':   
                newtext[6]=text3[7]
                lock = lock +1
            elif ',' in self.edit_entry8.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[6]=self.edit_entry8.get()
                lock = lock +1
            if self.edit_entry9.get()=='':   
                newtext[7]=text3[8]
                lock = lock +1
            elif ',' in self.edit_entry9.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[7]=self.edit_entry9.get() 
                lock = lock +1
            if self.edit_entry10.get()=='':   
                newtext[8]=text3[9]
                lock = lock +1
            elif ',' in self.edit_entry10.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[8]=self.edit_entry10.get()
                lock = lock +1
            if self.edit_entry11.get()=='':   
                newtext[9]=text3[10]
                lock = lock +1
            elif ',' in self.edit_entry11.get():
                messagebox.showerror('type error!',"virgül (',') girmeyiniz..")       
            else:
                newtext[9]=self.edit_entry11.get()
                lock = lock +1
            if lock >=10:    
                
                list2=self.table.item(select_item)['values']
                id=list2[0]
                if 'i' in newtext[0]:
                    valisim = newtext[0].replace('i','İ')
                else:
                    valisim=newtext[0] 
                valisim2=valisim.upper()       
                    
                query="""UPDATE isletme SET İSİM ='{}'	,BİLGİSAYARADI='{}',	BİLGİSAYARÖZELLİKLERİ='{}',KULLANICIADI='{}'	,YAZICILAR='{}'	,WINDOWSKEY='{}'	,OFFİCEKEY='{}'	,TELEFON='{}'	,BİRİM='{}'	,KONTROL='{}'
                        WHERE id ='{}'
                        """.format(valisim2,newtext[1],newtext[2],newtext[3],newtext[4],newtext[5],newtext[6],newtext[7],newtext[8],newtext[9],id)	
                cur.execute(query)
                db.commit()
                messagebox.showinfo('düzenleme','kullanıcı başarıyla güncellendi..') 
                
                master.destroy()
                SCRIPTS.yazdır(self)  
    def history(self):
        
        
        try:
            data=self.table.selection()
            data2=self.table.item(data)['values']
            
        
            datasql="SELECT*FROM pc_history WHERE id='{}'".format(data2[0]) 
            cur.execute(datasql)
            newdata= cur.fetchall()
            datalength=len(newdata)
            
            for item in self.table2.get_children(): 
                    self.table2.delete(item)   
            if datalength==0:
                    
                    self.table2.insert(parent='',index='end',iid=0,text='',values=(data2[0],data2[2],' ','kullanıcı geçmişi yok '))
                     
            else:
                a=0
                for i in newdata:
                    
                   
                
                    text =(i[0],i[1],i[2],i[3])
                    self.table2.insert(parent='',index='end',iid=a,text='',values=text)
                    a=a+1 
        except IndexError:
            pass 
    def allhistory(self):   
           
        datasql="SELECT*FROM pc_history"
        cur.execute(datasql)
        newdata= cur.fetchall()
        datalength=len(newdata)
        
        for item in self.table2.get_children(): 
                    self.table2.delete(item)   
        if datalength==0:

             self.table2.insert(parent='',index='end',iid=0,text='',values='geçmiş yok ')
               
        else:
            a=0
            for i in newdata:
                text =(i[0],i[1],i[2],i[3])
                self.table2.insert(parent='',index='end',iid=a,text='',values=text)
                a=a+1 
        
root=Tk()                
ARAYUZ(root)
