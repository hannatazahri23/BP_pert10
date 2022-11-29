print("\n")

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

print("\n")