while True:
    #tanya user mau input atau tidak
    loop_question = input("Input data VLAN baru (y/t) ")
    print("*********************************")

    if loop_question == "y" or loop_question == "Y":
        #user input untuk ID dan Nama
        id_input = input("Masukkan VLAN ID: ")
        nama_input = input("Masukkan Nama VLAN: ")
        print("---------------------------------")
        
        #buka file dan tambahkan baris baru dari input user
        with open("vlan-database.txt", "a") as file:
            file.write("VLAN ID: " + id_input +", Name: " + nama_input + "\n")

    else:
        break
#tampilkan isi file
with open("vlan-database.txt", "r") as file:
    print(file.read())