

from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from tkinter import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
import mysql.connector



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"image\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_msgbox(hata_kodu,mesaj_text,icon,pencere):
    mesaj = tk.Toplevel(pencere)

    mesaj.title(hata_kodu)
    mesaj.geometry("300x100")

    l1 = tk.Label(mesaj, image="::tk::icons::"+icon)
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = tk.Label(mesaj, text=mesaj_text)
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = Button(mesaj, text="Tamam", command=mesaj.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")


    mesaj.update_idletasks()
    x = pencere.winfo_rootx() + (pencere.winfo_width() - mesaj.winfo_width()) // 2
    y = pencere.winfo_rooty() + (pencere.winfo_height() - mesaj.winfo_height()) // 2
    mesaj.geometry(f"300x100+{x}+{y}")


window = Tk()

window.geometry("500x500")
window.configure(bg="#A0B2B0")
window.title("Araç Kiralama Uygulaması")






class Uygulama():
    def __init__(self):
        self.giris_paneli()


        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_araba"
    )

    def veritabani(self):

        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_araba"
            )


##################################  GİRİŞ PENCERESİ VE FONKSİYONLARI  #####################################
    def giris_paneli(self):

        self.canvas = Canvas(
            window,
            bg="#A0B2B0",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            250.0,
            250.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            33.0,
            19.0,
            anchor="nw",
            text="ARAÇ KİRALAMA UYGULAMASI",
            fill="#ECE4E4",
            font=("JetBrainsMonoRoman ExtraBold", 30 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            130.0,
            135.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            130.0,
            207.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            show="*",
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )

        self.text2=self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kullanıcı adı:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )

        self.text1=self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Sifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )


        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.hesap_olustur = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.hide,
            relief="flat"
        )
        self.hesap_olustur.place(
            x=144.0,
            y=467.0,
            width=213.0,
            height=22.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.musteri_giris ,
            relief="flat"
        )
        self.button_2.place(
            x=33.0,
            y=250.0,
            width=47.643829345703125,
            height=34.0,

        )


        window.resizable(False, False)
        window.mainloop()

    def hide(self):
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.hesap_olustur.destroy()
        self.button_2.destroy()
        self.canvas.delete(self.entry_bg_1)
        self.canvas.delete(self.entry_bg_2)
        self.canvas.delete(self.text1)
        self.canvas.delete(self.text2)

        self.email_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.email_bg = self.canvas.create_image(
            130.0,
            135.5,
            image=self.email_resim
        )
        self.email = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )



        self.numara_resim = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.numara_bg = self.canvas.create_image(
            130.0,
            207.5,
            image=self.numara_resim
        )
        self.numara = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.numara.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )


        self.sifre_resim = PhotoImage(
            file=relative_to_assets("re.png"))
        self.sifre_bg = self.canvas.create_image(
            130.0,
            276.5,
            image=self.sifre_resim
        )
        self.sifre = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sifre.place(
            x=49.0,
            y=261.0,
            width=162.0,
            height=35.0
        )
        self.email_text = self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kullanıcı adı:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.numara_text = self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Telefon numarası:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.sifre_text = self.canvas.create_text(
            33.0,
            237.0,
            anchor="nw",
            text="Sifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.kayit_buton = PhotoImage(
            file=relative_to_assets("kayitbuton.png"))
        self.kayit = Button(
            image=self.kayit_buton,
            borderwidth=0,
            highlightthickness=0,
            command=self.kayit_ol,
            relief="flat"
        )
        self.kayit.place(
            x=33.0,
            y=330.0,
            width=77.643829345703125,
            height=34.0,

        )
        self.gerigel_resim = PhotoImage(
            file=relative_to_assets("gerigel.png"))
        self.gerigel = Button(
            image=self.gerigel_resim,
            borderwidth=0,
            highlightthickness=0,
            command=self.giris_paneli,
            relief="flat"
        )
        self.gerigel.place(
            x=200.0,
            y=467.0,
            width=120.0,
            height=20.0,

        )

    def kayit_ol(self):
        self.veritabani()
        self.email_giris = self.email.get()
        self.numara_giris = self.numara.get()
        self.sifre_giris = self.sifre.get()
        self.mycursor = self.mydb.cursor()
        self.sql_kayit_kontrol = "Select id FROM kullanicilar where ad = '" + self.email_giris + "'"
        self.sql_kayit = f"INSERT INTO kullanicilar (ad, sifre, telno) VALUES ('{self.email_giris}', '{self.sifre_giris}', '{self.numara_giris}')"
        # ==INSERT INTO admins (ad, sifre) VALUES ('Cardinal', 'Tom B. Erichsen');
        ################################################
        self.mycursor.execute(self.sql_kayit_kontrol)
        self.myresult = self.mycursor.fetchone()
        self.sql_kayit_kontrol = "Select id FROM kullanicilar where ad = %s"
        self.sql_kayit = "INSERT INTO kullanicilar (ad, sifre, telno) VALUES (%s, %s, %s)"

        # Boşluk kontrolü
        if not self.email_giris.strip() or not self.numara_giris.strip() or not self.sifre_giris.strip():
            login_msgbox("HATA!", "Boşluk bırakma!", "warning",window)
        else:
            self.mycursor.execute(self.sql_kayit_kontrol, (self.email_giris,))
            self.myresult = self.mycursor.fetchone()

            if self.myresult:  # DEĞER DÖNDÜRÜYORSA
                login_msgbox("HATA!", "Kullanıcı adı zaten mevcut!", "warning",window)
            else:
                try:
                    self.mycursor.execute(self.sql_kayit, (self.email_giris, self.sifre_giris, self.numara_giris))
                    self.mydb.commit()
                    print("Kayıt Başarılı")
                    login_msgbox("Tebrikler!", "Tebrikler! Kayıt başarılı.", "information",window)
                except mysql.connector.Error as err:
                    print(err)
                    login_msgbox("Hata!", "Server hatası!", "error",window)

    def musteri_giris(self):
            self.veritabani()
            self.true_kullanici_adi = self.entry_1.get()
            self.true_sifre = self.entry_2.get()

            self.sql_giris = "Select * FROM kullanicilar where ad = '" + self.true_kullanici_adi + "'" + "and sifre = '" + self.true_sifre + "'"
            self.sql_giris_admin = "Select id FROM admins where ad = '" + self.true_kullanici_adi + "'" + "and sifre = '" + self.true_sifre + "'"
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(self.sql_giris)
            self.myresult = self.mycursor.fetchone()
            self.mycursor.execute(self.sql_giris_admin)
            self.myresult2 = self.mycursor.fetchone()


            if self.myresult != None:
                self.id = self.myresult[0]
                self.bakiye = self.myresult[4]
                self.id = str(self.id)
                print("hos geldiniz"+str(self.id)+"Bakiyeniz = "+str(self.bakiye))
                window.destroy()
                self.kullanici_pencere()


            elif self.myresult2!=None:
                print("hos geldiniz")
                window.destroy()
                self.main_pencere()

            else:
                login_msgbox("HATA!","Kullanıcı adı veya şifre yanlış! ","warning",window)

##################################  ADMİN PENCERESİ VE FONKSİYONLARI  #####################################

    def main_pencere(self):
        self.main_window = Tk()

        self.main_window.geometry("850x500")
        self.main_window.configure(bg="#FFFFFF")
        self.main_window.title("Araç kiralama")

        self.main_canvas = Canvas(
        self.main_window,
        bg = "#FFFFFF",
        height = 500,
        width = 850,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.main_canvas.place(x = 0, y = 0)
        self.main_image_image_1 = PhotoImage(
            file=relative_to_assets("main_image_1.png"))
        self.main_image_1 = self.main_canvas.create_image(
            425.0,
            250.0,
            image=self.main_image_image_1
        )

        self.main_canvas.create_text(
            182.0,
            5.0,
            anchor="nw",
            text="ARAÇ KİRALAMA UYGULAMASI",
            fill="#85FFA7",
            font=("KumarOne Regular", 25 * -1)
        )

        self.main_entry_image_1 = PhotoImage(
            file=relative_to_assets("main_entry_1.png"))
        self.main_entry_bg_1 = self.main_canvas.create_image(
            112.0,
            84.0,
            image=self.main_entry_image_1
        )
        self.main_entry_1 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_1.place(
            x=44.0,
            y=65.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            31.0,
            41.0,
            anchor="nw",
            text="Araç marka:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_2 = PhotoImage(
            file=relative_to_assets("main_entry_2.png"))
        self.main_entry_bg_2 = self.main_canvas.create_image(
            110.0,
            153.0,
            image=self.main_entry_image_2
        )
        self.main_entry_2 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_2.place(
            x=42.0,
            y=134.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            110.0,
            anchor="nw",
            text="Araç km:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_3 = PhotoImage(
            file=relative_to_assets("main_entry_3.png"))
        self.main_entry_bg_3 = self.main_canvas.create_image(
            110.0,
            222.0,
            image=self.main_entry_image_3
        )
        self.main_entry_3 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_3.place(
            x=42.0,
            y=203.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            179.0,
            anchor="nw",
            text="Araç vites:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_4 = PhotoImage(
            file=relative_to_assets("main_entry_4.png"))
        self.main_entry_bg_4 = self.main_canvas.create_image(
            110.0,
            291.0,
            image=self.main_entry_image_4
        )
        self.main_entry_4 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_4.place(
            x=42.0,
            y=272.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            31.0,
            247.0,
            anchor="nw",
            text="Saatlik ücret:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_5 = PhotoImage(
            file=relative_to_assets("main_entry_5.png"))
        self.main_entry_bg_5 = self.main_canvas.create_image(
            110.0,
            360.0,
            image=self.main_entry_image_5
        )
        self.main_entry_5 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_5.place(
            x=42.0,
            y=341.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            318.0,
            anchor="nw",
            text="Günlük ücret:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_6 = PhotoImage(
            file=relative_to_assets("main_entry_6.png"))
        self.main_entry_bg_6 = self.main_canvas.create_image(
            110.0,
            429.0,
            image=self.main_entry_image_6
        )
        self.main_entry_6 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_6.place(
            x=42.0,
            y=410.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            383.0,
            anchor="nw",
            text="Kira durumu:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_button_image_1 = PhotoImage(
            file=relative_to_assets("main_button_1.png"))
        self.main_button_1 = Button(
            image=self.main_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.tablo_kayit_button,
            relief="flat"
        )
        self.main_button_1.place(
            x=248.0,
            y=400.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_2 = PhotoImage(
            file=relative_to_assets("main_button_2.png"))
        self.main_button_2 = Button(
            image=self.main_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.guncelle_arac,
            relief="flat"
        )
        self.main_button_2.place(
            x=248.0,
            y=340.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_3 = PhotoImage(
            file=relative_to_assets("main_button_3.png"))
        self.main_button_3 = Button(
            image=self.main_button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.silme_islemi,
            relief="flat"
        )
        self.main_button_3.place(
            x=248.0,
            y=280.0,
            width=98.0,
            height=44.0
        )


        self.table_frame=Frame(self.main_window,bd=10,relief=RIDGE,bg="Green")
        self.table_frame.place(x=400,y=55,width=450,height=395)

        self.scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.scroll_y=ttk.Scrollbar(self.table_frame, orient=VERTICAL)
        self.arac_tablo=ttk.Treeview(self.table_frame,columns=("id","a_m","a_km","a_vites",
        "saatlik","haftalik","kira","kiralayan_id"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.arac_tablo.xview)
        self.scroll_y.config(command=self.arac_tablo.yview)

        self.arac_tablo.heading("id",text="Araç id",anchor=W)
        self.arac_tablo.heading("a_m", text="marka",anchor=W)
        self.arac_tablo.heading("a_km", text="km",anchor=W)
        self.arac_tablo.heading("a_vites", text="vites",anchor=W)
        self.arac_tablo.heading("saatlik", text="Saatlik ücret",anchor=W)
        self.arac_tablo.heading("haftalik", text="Günlük ücret",anchor=W)
        self.arac_tablo.heading("kira", text="Kira durumu",anchor=W)
        self.arac_tablo.heading("kiralayan_id", text="Kiralayan id", anchor=W)

        self.arac_tablo.column("id", width=50)
        self.arac_tablo.column("a_m", width=50)
        self.arac_tablo.column("a_km", width=40)
        self.arac_tablo.column("a_vites", width=40)
        self.arac_tablo.column("saatlik", width=80)
        self.arac_tablo.column("haftalik", width=90)
        self.arac_tablo.column("kira", width=80)
        self.arac_tablo.column("kiralayan_id",width=80)
        self.veri_aktarimi()

        self.arac_tablo["show"]="headings"
        self.arac_tablo.pack(fill=BOTH,expand=1)

        self.arac_tablo.bind("<ButtonRelease-1>", self.get_cursor_row)


        self.main_window.resizable(False, False)
        self.main_window.mainloop()

    def guncelle_arac(self):
        selected_item = self.arac_tablo.selection()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir araç seçin!", "warning", self.main_window)
            return

        arac_id = self.arac_tablo.item(selected_item)['values'][0]
        print("Guncelle_Arac " + str(arac_id))

        yeni_marka = self.main_entry_1.get()
        yeni_km = self.main_entry_2.get()
        yeni_vites = self.main_entry_3.get()
        yeni_saatlik_ucret = self.main_entry_4.get()
        yeni_gunluk_ucret = self.main_entry_5.get()
        yeni_kira_durumu = self.main_entry_6.get()

        guncelle_query_parts = []


        if not arac_id:  # Eğer seçilmediyse
            login_msgbox("HATA!", "Güncellenecek bir alan seçilmedi!", "error", self.main_window)
            print(yeni_marka,yeni_vites,yeni_km,yeni_kira_durumu,yeni_gunluk_ucret,yeni_saatlik_ucret)
            return

        update_query = "UPDATE arabalar_tablosu SET marka=%s , km=%s , vites=%s , saatlik=%s , gunluk=%s , kira=%s WHERE Arac_id = %s"
        #self.my_cursor.execute(update_query, (yeni_marka, yeni_km,yeni_vites,yeni_saatlik_ucret,yeni_gunluk_ucret,yeni_kira_durumu))

        print("Sorgu:", update_query)

        try:
            self.my_cursor.execute(update_query, (yeni_marka, yeni_km,yeni_vites,yeni_saatlik_ucret,yeni_gunluk_ucret,yeni_kira_durumu,arac_id))
            # self.mydb.commit()  # Eğer bağlantıyı manuel olarak başlatmadıysanız bu satırı aktifleştirin.
            print(yeni_marka, yeni_vites, yeni_km, yeni_kira_durumu, yeni_gunluk_ucret, yeni_saatlik_ucret)
            login_msgbox("BAŞARILI", "Araç bilgileri güncellendi!", "information", self.main_window)
            print("Giris1 degeri:", self.main_entry_1.get())
            # Veri tablosunu güncelle
            self.veri_aktarimi()

        except Exception as e:
            login_msgbox("HATA!", f"Araç bilgileri güncellenemedi: {e}", "error", self.main_window)

    def silme_islemi(self):

        selected_item = self.arac_tablo.selection()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir araç seçin!", "warning", self.main_window)
            return

        arac_id1 = self.arac_tablo.item(selected_item)['values'][0]


        self.sql_guncelle_delete = "DELETE from arabalar_tablosu WHERE Arac_id = %s"

        try:
            self.my_cursor.execute(self.sql_guncelle_delete, ( arac_id1,))
            self.mydb.commit()

            # Güncelleme başarılıysa Treeview'daki veriyi güncelle
            self.veri_aktarimi()

        except Exception as e:
            login_msgbox("HATA!", f"Kayıt silinemedi: {e}", "error", self.main_window)

    def tablo_kayit_button(self):
        # Veritabanı bağlantısını doğrudan oluşturun
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_araba"
        )

        # Eğer `veritabani()` fonksiyonunuz bir veritabanı bağlantısı döndürmüyorsa, bu satırı kullanabilirsiniz
        # self.mydb = self.veritabani()

        self.giris1 = self.main_entry_1.get()
        self.giris2 = self.main_entry_2.get()
        self.giris3 = self.main_entry_3.get()
        self.giris4 = self.main_entry_4.get()
        self.giris5 = self.main_entry_5.get()
        self.giris6 = self.main_entry_6.get()

        # Eğer `self.mydb` değeri `None` ise, cursor oluşturmayın
        if self.mydb:
            self.my_cursor = self.mydb.cursor()
            self.sql_tablo_veri = "INSERT INTO arabalar_tablosu (marka, km, vites, saatlik, gunluk, kira) VALUES (%s, %s, %s, %s, %s, %s)"
            if not self.giris1.strip() or not self.giris2.strip() or not self.giris3.strip() or not self.giris4.strip() or not self.giris5.strip() or not self.giris6.strip():
                login_msgbox("HATA!", "Boşluk bırakma!", "warning", self.main_window)
            else:
                self.my_cursor.execute(self.sql_tablo_veri,
                                       (self.giris1, self.giris2, self.giris3, self.giris4, self.giris5, self.giris6))
                self.mydb.commit()
                self.veri_aktarimi()
                login_msgbox("Tebrikler!","Kayıt başarılı!","information",self.main_window)
        else:
            login_msgbox("HATA!", "Veritabanı bağlantı hatası!", "error", self.main_window)

    def veri_aktarimi(self):
        self.sql_veri_aktarimi="select * from arabalar_tablosu"
        self.my_cursor = self.mydb.cursor()
        self.my_cursor.execute(self.sql_veri_aktarimi)
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.arac_tablo.delete(*self.arac_tablo.get_children())
            for i in self.rows:
                self.arac_tablo.insert("",END,values=i)
            self.mydb.commit()

    def veri_aktarimi1(self):
        self.veritabani()
        self.sql_veri_aktarimi1="select Arac_id,marka,km,vites,saatlik,gunluk,kira from arabalar_tablosu where kira='Müsait'"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.sql_veri_aktarimi1)
        self.rows1=self.my_cursor1.fetchall()
        if len(self.rows1)!=0:
            self.arac_tablo1.delete(*self.arac_tablo1.get_children())
            for i in self.rows1:
                self.arac_tablo1.insert("",END,values=i)
            self.mydb.commit()

    def get_cursor_row(self, event=""):
        cursor_row = self.arac_tablo.focus()
        content = self.arac_tablo.item(cursor_row)
        row = content["values"]

        # Entry widget'larını güncelle
        self.main_entry_1.delete(0, END)
        self.main_entry_1.insert(0, row[1] if row and len(row) > 0 else "")

        self.main_entry_2.delete(0, END)
        self.main_entry_2.insert(0, row[2] if row and len(row) > 1 else "")

        self.main_entry_3.delete(0, END)
        self.main_entry_3.insert(0, row[3] if row and len(row) > 2 else "")

        self.main_entry_4.delete(0, END)
        self.main_entry_4.insert(0, row[4] if row and len(row) > 3 else "")

        self.main_entry_5.delete(0, END)
        self.main_entry_5.insert(0, row[5] if row and len(row) > 4 else "")

        self.main_entry_6.delete(0, END)
        self.main_entry_6.insert(0, row[6] if row and len(row) > 5 else "")


##################################  KULLANICI PENCERESİ VE FONKSİYONLARI   #####################################
    def kullanici_pencere(self):

        self.kullanici_window = Tk()

        self.kullanici_window.geometry("850x500")
        self.kullanici_window.configure(bg="#FFFFFF")
        self.kullanici_window.title("Araç kiralama")

        self.kullanici_window_canvas = Canvas(
            self.kullanici_window,
            bg="#FFFFFF",
            height=500,
            width=850,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.kullanici_window_canvas.place(x=0, y=0)
        self.kullanici_photo = PhotoImage(
            file=relative_to_assets("kullanici_window.png"))
        self.kullanici_image_1 = self.kullanici_window_canvas.create_image(
                425.0,
                250.0,
                image=self.kullanici_photo
            )

        self.kullanici_window_canvas.create_text(
            182.0,
            5.0,
            anchor="nw",
            text="ARAÇ KİRALAMA UYGULAMASI",
            fill="#85FFA7",
            font=("KumarOne Regular", 25 * -1)
        )

        self.ucret_lbl=self.kullanici_window_canvas.create_text(
            50.0,
            200.0,
            anchor="nw",
            text="Bakiye: "+str(self.bakiye),
            fill="#85FFA7",
            font=("KumarOne Regular", 25 * -1)
        )



        self.table_frame1 = Frame(self.kullanici_window, bd=10, relief=RIDGE, bg="Green")
        self.table_frame1.place(x=400, y=55, width=450, height=395)

        self.scroll_x1 = ttk.Scrollbar(self.table_frame1, orient=HORIZONTAL)
        self.scroll_y1 = ttk.Scrollbar(self.table_frame1, orient=VERTICAL)
        self.arac_tablo1 = ttk.Treeview(self.table_frame1, columns=("id", "a_m", "a_km", "a_vites",
                                                                  "saatlik", "haftalik", "kira"),
                                       xscrollcommand=self.scroll_x1.set, yscrollcommand=self.scroll_y1.set)

        self.scroll_x1.pack(side=BOTTOM, fill=X)
        self.scroll_y1.pack(side=RIGHT, fill=Y)

        self.scroll_x1.config(command=self.arac_tablo1.xview)
        self.scroll_y1.config(command=self.arac_tablo1.yview)

        self.arac_tablo1.heading("id", text="Araç id", anchor=W)
        self.arac_tablo1.heading("a_m", text="marka", anchor=W)
        self.arac_tablo1.heading("a_km", text="km", anchor=W)
        self.arac_tablo1.heading("a_vites", text="vites", anchor=W)
        self.arac_tablo1.heading("saatlik", text="Saatlik ücret", anchor=W)
        self.arac_tablo1.heading("haftalik", text="Günlük ücret", anchor=W)
        self.arac_tablo1.heading("kira", text="Kira durumu", anchor=W)

        self.arac_tablo1.column("id", width=50)
        self.arac_tablo1.column("a_m", width=50)
        self.arac_tablo1.column("a_km", width=40)
        self.arac_tablo1.column("a_vites", width=40)
        self.arac_tablo1.column("saatlik", width=80)
        self.arac_tablo1.column("haftalik", width=90)
        self.arac_tablo1.column("kira", width=80)

        self.veri_aktarimi1()

        self.arac_tablo1["show"] = "headings"
        self.arac_tablo1.pack(fill=BOTH, expand=1)



        n = tk.StringVar()
        self.gunluk_saatlik_secim = ttk.Combobox(self.kullanici_window, width=30, textvariable=n, state="readonly")
        self.gunluk_saatlik_secim['values'] = ('Saatlik', 'Günlük')
        self.gunluk_saatlik_secim.grid(column=2, row=6, padx=80, pady=60)  # İlk Combobox'ın konumu

        z = tk.StringVar()
        self.sure_secim = ttk.Combobox(self.kullanici_window, width=30, textvariable=z, state="readonly")
        self.sure_secim['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        self.sure_secim.grid(column=2, row=7, padx=30, pady=0)  # İkinci Combobox'ın konumu


        self.kirala_buton_image = PhotoImage(
            file=relative_to_assets("kirala.png"))
        self.kirala_buton = Button(
            image=self.kirala_buton_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command = self.kiralama_islemi
        )
        self.kirala_buton.place(
            x=248.0,
            y=340.0,
            width=98.0,
            height=44.0
        )

        self.bilgi_image = PhotoImage(
            file=relative_to_assets("bilgi.png"))
        self.bilgi = Button(
            image=self.bilgi_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.kayit_bilgi,
            relief="flat"
        )
        self.bilgi.place(
            x=248.0,
            y=280.0,
            width=98.0,
            height=44.0
        )

        self.iptal_image_1 = PhotoImage(
            file=relative_to_assets("iptal.png"))
        self.iptal = Button(
            image=self.iptal_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.kiralama_iptal,
            relief="flat"
        )
        self.iptal.place(
            x=248.0,
            y=400.0,
            width=98.0,
            height=44.0
        )
        self.geri_image_1 = PhotoImage(
            file=relative_to_assets("geri.png"))
        self.geri = Button(
            image=self.geri_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.geri_gel,
            relief="flat"
        )

        self.kullanici_window.resizable(False, False)
        self.kullanici_window.mainloop()
    def kiralama_islemi(self):
        selected_item = self.arac_tablo1.focus()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir araç seçin!", "warning", self.kullanici_window)
            return

        cmb_2 = self.sure_secim.get()
        cmb_1=self.gunluk_saatlik_secim.get()
        gunluk_ucret = 0
        saatlik_ucret = 0
        self.total = 0
        #print(cmb_1,cmb_2)
        query_bakiye = "SELECT bakiye FROM kullanicilar WHERE id =%s"
        val = (self.id,)
        self.my_cursor1.execute(query_bakiye, val)
        self.myresult = self.my_cursor1.fetchone()
        self.bakiye = self.myresult[0]
        print(self.bakiye)


        query_gunluk = "SELECT gunluk FROM arabalar_tablosu WHERE Arac_id =%s"
        query_saatlik = "SELECT saatlik FROM arabalar_tablosu WHERE Arac_id =%s"
        query_ucret = "UPDATE arabalar_tablosu SET kira='Kiralı',kiralayan_id=%s WHERE arac_id =%s"

        #self.total=7*int(cmb_2)

        content = self.arac_tablo1.item(selected_item)
        arac_id = content["values"][0]


        if cmb_1 == "Günlük":
            print("TRUE=GÜNLÜK")
            print(arac_id)
            try:
                val = (arac_id,)
                self.my_cursor1.execute(query_gunluk, val)
                self.myresult = self.my_cursor1.fetchone()
                print(self.myresult)
                gunluk_ucret = str(self.myresult[0])
                print(gunluk_ucret)
            except Exception as e:
                print("HATA GÜNLÜK")
        elif cmb_1 == "Saatlik":
            print("TRUE=GÜNLÜK")
            print(arac_id)
            try:
                val = (arac_id,)
                self.my_cursor1.execute(query_saatlik, val)
                self.myresult = self.my_cursor1.fetchone()
                print(self.myresult)
                saatlik_ucret = str(self.myresult[0])
                print(saatlik_ucret)
            except Exception as e:
                print("HATA SAATLİK")

    ##########      UCRET KOSULU İLE ARAC KIRALAMA          ################
        if cmb_1 == "Günlük":
            self.total =int(gunluk_ucret)*int(cmb_2)
            print("Total = "+str(self.total))
            print(self.id)
            try:
                self.my_cursor1 = self.mydb.cursor()
                if self.bakiye >= self.total:
                    print("IF GEÇİLDİ")
                    sql = "UPDATE arabalar_tablosu SET kira='Kiralı',kiralayan_id=%s WHERE arac_id =%s"
                    val = (self.id,arac_id,)

                    self.my_cursor1.execute(sql, val)
                    self.mydb.commit()
                    messagebox.showinfo("Başarılı", f"Araç başarıyla kiralandı!\nÜcret: {str(self.total)}")

                    self.yeni_bakiye=self.bakiye-self.total

                    self.kullanici_window_canvas.delete(self.ucret_lbl)
                    self.ucret_lbl1 = self.kullanici_window_canvas.create_text(
                        50.0,
                        200.0,
                        anchor="nw",
                        text="Bakiye: " + (str(self.yeni_bakiye)),
                        fill="#85FFA7",
                        font=("KumarOne Regular", 25 * -1)
                    )

                    self.veri_aktarimi1()


                else:
                    login_msgbox("Hata", f"Yetersiz Bakiye! ", "error",
                                 self.kullanici_window)
            except Exception as e:
                login_msgbox("Hata", f"Kiralama işlemi sırasında bir hata oluştu: {e}","error",self.kullanici_window)


######## SAATLIK KIRALAMA #############

        elif cmb_1 == "Saatlik":
            self.total = int(saatlik_ucret) * int(cmb_2)
            print("Total = " + str(self.total))
            print(self.id)
            try:
                self.my_cursor1 = self.mydb.cursor()
                if self.bakiye >= self.total:
                    print("IF GEÇİLDİ")
                    sql = "UPDATE arabalar_tablosu SET kira='Kiralı',kiralayan_id=%s WHERE arac_id =%s"
                    val = (self.id, arac_id,)
                    self.my_cursor1.execute(sql, val)
                    self.mydb.commit()


                    sql_bakiye_fark = "UPDATE kullanicilar SET bakiye=bakiye-%s WHERE id = %s"
                    print("SQL BAKİYE GEÇTİ")
                    val = (self.total, self.id,)
                    print("VAL GEÇTİ")
                    self.my_cursor1.execute(sql_bakiye_fark, val)
                    print("EXECUTE GEÇTİ")
                    self.mydb.commit()
                    print("COMMIT GEÇTİ")
                    messagebox.showinfo("Başarılı", f"Araç başarıyla kiralandı!\nÜcret: {str(self.total)}")

                    self.yeni_bakiye = self.bakiye - self.total
                    self.kullanici_window_canvas.delete(self.ucret_lbl)
                    self.ucret_lbl1 = self.kullanici_window_canvas.create_text(
                        50.0,
                        200.0,
                        anchor="nw",
                        text="Bakiye: " + (str(self.yeni_bakiye)),
                        fill="#85FFA7",
                        font=("KumarOne Regular", 25 * -1)
                    )

                    self.veri_aktarimi1()


                else:
                    login_msgbox("Hata", f"Yetersiz Bakiye!", "error",
                                 self.kullanici_window)
            except Exception as e:
                login_msgbox("Hata", f"Kiralama işlemi sırasında bir hata oluştu: {e}", "error", self.kullanici_window)

    def kayit_bilgi(self):
########### KAYIT BİLGİLERİNİ TABLOYA GETİRTME ###########
        self.arac_tablo1.delete(*self.arac_tablo1.get_children())



        self.veritabani()
        # Veriyi güncel Treeview'a aktar
        self.kayit_sql_sorgu = "SELECT Arac_id, marka, km, vites,saatlik,gunluk,kiralayan_id FROM arabalar_tablosu WHERE kiralayan_id=%s"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.kayit_sql_sorgu, (self.id,))
        self.rows1 = self.my_cursor1.fetchall()

        if len(self.rows1) != 0:
            self.arac_tablo1.delete(*self.arac_tablo1.get_children())
            for i in self.rows1:
                self.arac_tablo1.insert("", END, values=i)
            self.mydb.commit()

        self.geri.place(
            x=130.0,
            y=400.0,
            width=98.0,
            height=44.0
        )
    def kiralama_iptal(self):



        selected_item = self.arac_tablo1.focus()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir araç seçin!", "warning", self.kullanici_window)
            return
        self.veritabani()
        self.query_iptal="Update arabalar_tablosu SET kira='Müsait',kiralayan_id=0 where Arac_id=%s"


        content = self.arac_tablo1.item(selected_item)
        arac_id = content["values"][0]
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.query_iptal, (arac_id,))
        self.mydb.commit()
        login_msgbox("Başarılı!","İptal başarılı",'information',self.kullanici_window)
        self.arac_tablo1.delete(selected_item)

    def geri_gel(self):
        self.arac_tablo1.delete(*self.arac_tablo1.get_children())
        self.veri_aktarimi1()

        self.geri.place_forget()







app=Uygulama()