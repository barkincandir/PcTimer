import os
import tkinter as tk
from tkinter import ttk


class PcTimer:
    def __init__(self, arayuz):
        self.arayuz = arayuz
        self.arayuz.title("PcTimer")
        self.arayuz.resizable(width=False, height=False)
        self.arayuz.configure(bg="#FAF0E6")

        ekran_yuk = arayuz.winfo_screenwidth()
        ekran_uzun = arayuz.winfo_screenheight()
        self.arayuz.geometry(f"225x250+{(ekran_yuk // 2) - 100}+{(ekran_uzun // 2) - 150}")

        self.font1 = ("calibri", 11)
        self.font = ("Arial", 15)

        self.saat_etiket = tk.Label(self.arayuz, text="Saat:", font=self.font1, fg="Black", bg="#C0C0C0", bd=2, relief=tk.RAISED)
        self.saat_etiket.place(x=25, y=20)

        self.saat_giris = tk.Entry(self.arayuz, font=self.font, fg="Black", bg="white", bd=1, relief=tk.RAISED, width=2)
        self.saat_giris.place(x=72, y=19)

        self.dakika_etiket = tk.Label(self.arayuz, text="Dakika:", font=self.font1, fg="Black", bg="#C0C0C0", bd=2, relief=tk.RAISED)
        self.dakika_etiket.place(x=112, y=20)

        self.dakika_giris = tk.Entry(self.arayuz, font=self.font, fg="Black", bg="white", bd=1, relief=tk.RAISED, width=2)
        self.dakika_giris.place(x=175, y=19)

        self.baslat = tk.Button(self.arayuz, text="Başlat", font=self.font1, fg="Black", bg="#C0C0C0", bd=5, relief=tk.RAISED, command=self.saat_ve_dakika_al)
        self.baslat.place(x=80, y=185)

        self.geriye_say_etiket = tk.Label(self.arayuz, text="Kalan Süre:", font=self.font1, fg="Black", bg="#C0C0C0", bd=2, relief=tk.RAISED, width=9)
        self.geriye_say_etiket.place(x=25, y=130)

        self.geriye_say_label = tk.Label(self.arayuz, text="", font=self.font1, fg="Black", bg="#808080", bd=4, relief=tk.RAISED, width=7)
        self.geriye_say_label.place(x=125, y=128)
        self.secenek_etiket = tk.Label(self.arayuz, text="İşlem:", font=self.font1, fg="Black", bg="#C0C0C0", bd=2, relief=tk.RAISED, width=5)
        self.secenek_etiket.place(x=25, y=75)

        self.secenekler = ["Seçiniz", "Yeniden Başlat", "Kapat"]
        self.secenek_combobox = ttk.Combobox(self.arayuz,values=self.secenekler, state="readonly", width=15)
        self.secenek_combobox.place(x=90, y=78)
        self.secenek_combobox.set(self.secenekler[0])
        self.secenek_combobox.bind("<<ComboboxSelected>>", self.secenek_secildi)

    def geriye_say(self, toplam_saniye):
        if toplam_saniye > 0:
            dakika, saniye = divmod(toplam_saniye, 60)
            saat, dakika = divmod(dakika, 60)
            self.geriye_say_label.config(text=f"{saat:02d}:{dakika:02d}:{saniye:02d}")
            self.arayuz.update_idletasks()
            self.arayuz.after(1000, self.geriye_say, toplam_saniye - 1)
        else:
            self.secilen_secenek()

    def secenek_secildi(self, event):
        self.secenek = self.secenek_combobox.get()

    def saat_ve_dakika_al(self):
        saat_giris_verisi = self.saat_giris.get()
        if saat_giris_verisi.isdigit():
            saat = int(saat_giris_verisi)
        dakika_giris_verisi = self.dakika_giris.get()
        if dakika_giris_verisi.isdigit():
            dakika = int(dakika_giris_verisi)
        toplam_saniye = (saat * 3600) + (dakika * 60)
        self.geriye_say(toplam_saniye)

    def secilen_secenek(self):
        if self.secenek == "Yeniden Başlat":
            os.system("shutdown /r /t 1")
        elif self.secenek == "Kapat":
            os.system("shutdown /s /t 1")

if __name__ == "__main__":
    arayuz = tk.Tk()
    app = PcTimer(arayuz)
    arayuz.mainloop()
