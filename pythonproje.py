class Terrorism():
    def __init__(self,location_name):
        self.location_name=location_name
    
    def degree_of_the_danger(self,danger = 0): #tehlikeyi 10 üzerinden alır.
        "Bölgenin tehlike seviyesini değişken olarak giriniz."#kırmızı yüksek tehlike seviyesini, mavi orta tehlike seviyesini, 
        if danger >= 5 and danger < 7:         # yeşil düşük tehlike seviyesini, beyaz beklenen bir tehlike olmadığını temsil eder.
            return "Mavi Bölge"
           
        if danger >= 7 and danger <= 10:
            return "Kırmızı Bölge"
           
        if danger < 5 and danger >= 3:
            return "Yeşil Bölge"
           
        if danger >= 0 and danger < 3:
            return "Beyaz Bölge"
            
        else:
            print("Lütfen belirtilen sayı aralığında değerlendirme yapın!")

    def recommended_variations(self,danger):
        "Bölgenin tehlike seviyesini değişken olarak giriniz"
        a = self.degree_of_the_danger(danger)
        if a == "Beyaz Bölge":
            return "Sadece personel öneriliyor"

        elif a == "Kırmızı Bölge":
            return"Bölgeye uygun tüm ekipman çeşitleri ve personel öneriliyor"

        elif a == "Yeşil Bölge":
            return "Personel ve o bölgeye uygun bir çeşit ekipman öneriliyor"

        elif a == "Mavi Bölge":
            return "Personel ve o bölgeye uygun iki çeşit ekipman öneriliyor"               
                                                                     

    def equipment_selection(self,iklim=0,deniz_kenari=0,engebeli=0):
        "iklim 'agir' veya 'hafif', deniz_kenari ve engebeli True/False şeklinde seçilmelidir."
                                                                     #bölgenin belirleyici özelliğine göre ekipman
        if deniz_kenari == False and iklim == "agir":                #seçimi yapılır. İklim agir/hafif şeklinde
            if engebeli == True:                                     #Deniz Kenarı True/False şeklinde
                print("Jetler / personel önerilir")                  #engebeli True/False şeklinde girilmelidir.
            if engebeli == False:
                print("Jetler / personel / tanklar önerilir")

        elif deniz_kenari == False and iklim == "hafif":
            if engebeli == True:                                           
                print("Jetler / personel / helikopterler önerilir") 
            if engebeli == False:
                print("Jetler / personel / tanklar / helikopterler önerilir")

        elif deniz_kenari == True and iklim == "hafif":
            if engebeli == True:                                           
                print("Jetler / personel / helikopterler / denizaltıları önerilir") 
            if engebeli == False:
                print("Jetler / personel / tanklar / helikopterler / denizaltıları önerilir")
        elif deniz_kenari == True and iklim == "agir":
            if engebeli == True:                                           
                print("Jetler / personel / denizaltıları önerilir") 
            if engebeli == False:
                print("Jetler / personel / tanklar / denizaltıları önerilir")
            


class silah(Terrorism): #bölgenin tehlike düzeyine,silahın taşınabileceği ağırlığa ve gerekli menziline göre silah tipini belirler
    def __init__(self,location_name):
        Terrorism.__init__(self,location_name)
        

    def silah_sec(self,weight,reach): # bu fonksiyon silahları kg cinsinden ağırlıklarına ve metre cinsinden menzillerine göre ayırır
        "silahın bölgeye uygunluğunu iyice belirlemek için ağırlığını ve menzilinidoğru girmeniz gerekir"

        self.weight=weight
        self.reach=reach
                
        if self.weight <= 1 and self.reach <= 300:
            return 'tabanca' 

        if 1< self.weight <=4 and 300< self.reach <=400:
            return 'tüfek'

        if 4< self.weight <=6 and 400< self.reach <=1000:
            return 'keskin nişancı tüfeği'

        if 6< self.weight <= 12 and 1000< self.reach <= 6800:
            return 'makineli tüfek'

    def uygunluk(self,danger): #burada zeynepten gelen koddaki bölgelere göre silahları yerleştireceğim
        "Bölgenin tehlike seviyesini 10 üzerinden değerlendirin."
        a = Terrorism.degree_of_the_danger(danger)

        if a == "Beyaz Bölge":
            print('hafif silahlar yeterlidir')
            return self.silah_sec(1,300)

        if a == "Kırmızı Bölge":
            print('yok edici silahlar gerekir')
            return self.silah_sec(12,6800)

        if a == "Mavi Bölge":
            print('güçlü silahlar gerekir')
            return self.silah_sec(6,1000)

        if a == "Yeşil Bölge":
            print('etkili silahlar gerekir')
            return self.silah_sec(4,400)

        else:
            print('böyle bir silah yoktur')



            
        
        
#location name saçma mı ilk girişte senden bölgeleri nasıl alıcam uygunluğun içine ne yazmalı
