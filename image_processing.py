from PIL import Image
import numpy as np
import cv2


while(True): # 2 ve 3 degerlerini girince tekrar sorması için sonsuz döngü içine aldık
    print("1-Fotograf Yukleyin\n2-Fotografi siyah ve beyaz hale cevirin\n3-Fotografi yatay olarak dondurun")
    secim = int(input("seciminizi giriniz: "))
    if(secim==1): #dosya yükleme işlemi
        a=input("Fotograf dosyasinin ismini giriniz: ")
        img=cv2.imread(a) #Fotograf dosyasının adını kullanıcıdan alıyor
        print(a,"Fotografi yuklendi")
        print("1-Fotograf Yukleyin\n2-Fotografi siyah ve beyaz hale cevirin\n3-Fotografi yatay olarak dondurun")#dosya yüklendikten sonra tekrar menü soruluyor
        secim = int(input("seciminizi giriniz: ")) #kullanıcının seçimini alıyoruz
        if (secim==1): #kullanıcı tekrar 1 seçeneğini seçerse hata kontrolü yapıyoruz
            print("Zaten bir dosya seçtiniz.")
            print("1-Fotograf Yukleyin\n2-Fotografi siyah ve beyaz hale cevirin\n3-Fotografi yatay olarak dondurun")
            secim = int(input("seciminizi giriniz: "))
        if (secim==2):
            en, boy, katman = np.shape(img)#Fotografin matrisinde işlem yapıyoruz renkli olduğu için 3 boyutlu
            yeniResim = np.zeros((en, boy, katman), dtype=np.uint8) #siyah beyaz halini basmak için yeni değişken açıyoruz

            for i in range(en):
                for j in range(boy):
                    yeniResim[i:, j] = img[i, j, 0] * 0.114 + img[i, j, 1] * 0.587 + img[i, j, 2] * 0.299 #RGB değerleriyle resmi siyah beyaz yapıyoruz

            cv2.imshow("Yeni siyah beyaz fotograf", yeniResim)#siyah beyaz yeni fotografi basıyoruz
            break #program sonlanıyor
        elif(secim==3):
            en, boy, katman = np.shape(img)

            yeniResim = np.zeros((en, boy, katman), dtype=np.uint8)#döndürülmüş halini yeniResime atıyoruz

            for i in range(en - 1):
                for j in range(boy - 1):
                    for k in range(katman):
                        yeniResim[i, j, k] = img[en - i - 1, j, k]#Fotografi döndürme işlemini gerçekleştiriyoruz yatay olarak döndürülüyor

            cv2.imshow("Ters cevrilmiş fotograf", yeniResim)
            break #program sonlanıyor
    elif(secim==2):
        print("Herhangi bir dosya yuklemediginiz icin bu islem gerceklestirilemiyor") #dosya secilmedigi icin islem yapılamıyor

    else:
        print("herhangi bir dosya yuklemediginiz icin bu islem gerceklestirilemiyor") #dosya secilmedigi icin islem yapılamıyor



