| # | Biodata |
| -------- | --- |
| **Nama** | M. Hannata Zahri |
| **NIM** | 312010318 |
| **Kelas** | TI.20.A.2 |
| **Mata Kuliah** | Bahasa Pemrograman |

---

## Latihan 1
* ### Membuat **Dictionary** daftar kontak, dengan nama sebagai "key" dan nomor sebagai "value"!!
+ ![img10-1](img/img10-1.png)

* ### Menampilkan hasil output **Dictionary** `daftar_kontak`:
+ ![img10-2](img/img10-2.JPG)

* ### Menambahkan kontak baru dengan nama "Riko" dengan nomor telepon "087654544"!!
+ ![img10-3](img/img10-3.png)
* ### Hasilnya:
+ ![img10-4](img/img10-4.png)

* ### Mengubah kontak "Dina" dengan nomor baru "088999776"
+ ![img10-5](img/img10-5.png)
* ### Hasilnya:
+ ![img10-6](img/img10-6.png)

* ### Menampilkan semua nama atau semua nomor!! Di karenakan saya menggunakan perulangan `for`, maka saya hanya perlu menghapus salah satu string dari **nama** ataupun **nomor**. Syntax-nya:
+ ![img10-7](img/img10-7.png)

* ### Contoh syntax dan hasil untuk menampilkan **nomor** saja:
+ ![img10-8](img/img10-8.png)
+ ![img10-9](img/img10-9.png)

* ### Contoh syntax dan hasil untuk menampilkan **nama** saja:
+ ![img10-10](img/img10-10.png)
+ ![img10-11](img/img10-11.png)

* ### Menghapus kontaknya "Dina", dengan menggunakan syntax sebagai berikut:
+ ![img10-12](img/img10-12.png)
* ### Hasil output sebelum dihapus:
+ ![img10-6](img/img10-6.png)
* ### Hasil output sesudah dihapus:
+ ![img10-13](img/img10-13.png)

* ### Berikut semua syntax program yang saya buat:
```python
daftar_kontak = {
    "Ari" : "081267888",
    "Dina" : "087677776"
}

daftar_kontak.update({"Riko" : "087654544"})
daftar_kontak.update({"Dina" : "088999776"})
del daftar_kontak["Dina"]

print("# Nama | Nomor Telepon")
print("# {}".format("="*20))

for nama, no_telp in daftar_kontak.items():
    NAMA = nama.ljust(4)
    NOMOR = no_telp.ljust(12)

    print(f"# {NAMA} | {NOMOR}")
```
