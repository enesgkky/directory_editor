import os
import time
import shutil

## TEST DOSYA YOLU : C:\Users\Enes_\OneDrive\Masaüstü\testDosya




dosya_name = {
            "txt":".Belgeler","pdf":".Belgeler","doc":".Belgeler","docx":".Belgeler",
            "jpg":".Resimler","png":".Resimler","jpeg":".Resimler",
            "mp4":".Videolar",
            "mp3":".Sesler","waw":".Sesler",
            "lnk":".Kısayollar",
            }

###################################################################################

dosyalar = set()
def transfer():
    print("Transfer başlıyor...")
    time.sleep(1)
    liste = dizin_open(dosya_url)
    for i in liste:
        if("." in i):
            i = str(i)
            uzanti = i[i.find(".")+1:]
            adress = dosya_name[uzanti]
            shutil.move(i,adress)
    print("Transfer tamamlandı!")
    time.sleep(2)

###################################################################################

def create_dosya():
    print('Dosyalar oluşturuluyor...')
    time.sleep(1)
    for i in dosyalar:
        try:
            os.mkdir(i)
        except:
            pass
    print('Dosyalar başarıyla oluşturuldu!')
    time.sleep(1)

###################################################################################

def dosya_create(liste):
    print('Dosya taranıyor...')
    time.sleep(1)
    liste = set(liste)
    for i in liste:
        dosyalar.add(dosya_name[i])

###################################################################################

def uzanti_create(liste):
    if(liste.__len__() == 0):
        os.system('cls')
        print('''
        
                    Dosya içeriği boş veya içerikler gizlenmiş olabilir!

        ''')
        time.sleep(2)
        return 0
    else:
        uzanti_list = set()
        for i in liste:
            i = str(i)
            if("." in i):
                uzanti_list.add(i[i.find(".")+1:])
        return uzanti_list

###################################################################################

def dizin_open(dosya_url):
    os.chdir(dosya_url)
    liste = os.listdir(dosya_url)
    liste1 = list()
    for i in liste:
        if(not i.startswith(".")):
            liste1.append(i)
    return liste1

###################################################################################

def dizin_kontrol(dosya_url):
    os.system('cls')
    print("Dosya yolu kontrol ediliyor...")
    time.sleep(1)
    try:
        os.chdir(dosya_url)
        return True
    except:
        return False

###################################################################################

def main():
    global dosya_url
    while(1):
        os.system('cls')
        mainPath = os.getcwd()
        print('''
                ***********************************************
                ***           DOSYA DÜZENLEYİCİ             ***
                ***                                         ***
                ***         developer by enesgkky           ***
                ***                                         ***
                ***    Çıkış yapmak için 'exit' yazınız.    ***
                ***********************************************
        ''')
        dosya_url = str(input("Düzenlemek istediğiniz dosyanın yolunu giriniz : "))
        if(dosya_url == 'exit'):
            os.system('cls')
            print('Bye bye :)')
            time.sleep(2)
            os.system('cls')
            break
        if(dizin_kontrol(dosya_url)):
            dosya_create(uzanti_create(dizin_open(dosya_url)))
            create_dosya()
            transfer()
        else:
            os.chdir(mainPath)
            os.system('cls')
            print('Dosya yolu hatalı veya korunuyor!')
            time.sleep(1.5)
main()