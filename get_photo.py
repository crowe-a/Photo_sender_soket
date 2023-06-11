import socket
import os,time
from PIL import Image

def get_photo_tcp():
    # Sunucu adresi ve portu
    HOST = 'localhost'
    PORT = 8000

    # Sunucu soketini oluştur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print('Sunucu çalışıyor...')
        
        # İstemci bağlantısını kabul et
        conn, addr = server_socket.accept()
        print('Bağlantı yapıldı:', addr)
        # Dosya boyutunu al
        data = conn.recv(8)
        img_size = int.from_bytes(data, byteorder='big')

       

        i=0
        while True:
            try:
                # Boyut bilgisini doğrula
                if img_size <= 0:
                    conn.sendall(b'ERR')
                    raise ValueError('Geçersiz dosya boyutu')

                # Onay mesajı gönder
                conn.sendall(b'OK')

                # Dosya verisini al
                img_data = b''
                while len(img_data) < img_size:
                    data = conn.recv(1024)
                    img_data += data
                
                # Dosyayı diske kaydet
                img_filename = 'photos/image{}.jpg'.format(i)
                with open(img_filename, 'wb') as f:
                    f.write(img_data)

                # Dosyayı görüntü olarak aç ve göster
                with Image.open(img_filename) as img:
                    img
            except:
                i+=1
            i+=1
            time.sleep(0.4)
