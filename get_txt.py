import socket,struct,time,get_photo

def get_txt():
    try:

        IP = "localhost"
        PORT = 1234

        # Soket nesnesini oluşturma
        soket_nesnesi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket_nesnesi.connect((IP, PORT))
        #print(soket_nesnesi.connect((IP, PORT)))

        i=0
        while True:
            data=soket_nesnesi.recv(1024)
            my_list = struct.unpack('!{}f'.format(len(data) // 4), data)
            print('Alınan liste:', my_list)

            assert len(my_list) is not 0
            with open("photos/liste{}.txt".format(i), "w") as file:
                for item in my_list:
                    file.write("%s," % item)
                    # file.write(",")
                #file.seek(0)
                file.write("\n")
                print("kayıt ediliyor")
                print('Alınan liste:',i)
                i+=1
            # if i==10:
        #     break
    except:
        get_photo.get_photo_tcp()

get_txt()