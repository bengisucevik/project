class silah(Terrorism): #bölgenin tehlike düzeyine,silahın taşınabileceği ağırlığa
                        #ve gerekli menziline göre silah tipini belirler
    def __init__(self,location_name,):
        Terrorism.__init__(self,location_name)
        

    def silah_sec(self,agirlik,menzil): # bu fonksiyon silahları kg cinsinden ağırlıklarına
                                        #ve metre cinsinden menzillerine göre ayırır
        "ağr<=1 mnz<300;1<ağr<=4 300<mnz<=400;4<ağr<=6 400<mnz<=1000;6<ağr<=12 1k<mnz<=6800"

        self.agirlik=agirlik
        self.menzil=menzil
                
        if self.agirlik <= 1 and self.menzil <= 300:
            return 'tabanca' 

        if 1< self.agirlik <=4 and 300< self.menzil <=400:
            return 'tüfek'

        if 4< self.agirlik <=6 and 400< self.menzil <=1000:
            return 'keskin nişancı tüfeği'

        if 6< self.agirlik <= 12 and 1000< self.menzil <= 6800:
            return 'makineli tüfek'

        else:
            print("Böyle bir silah üretilmemiştir")
            
    def uygunluk(self,danger): #Terrorism classının degree_of_the_danger fonksiyonununu
                               #çağırarak bölgelerin tehlike düzeylerine göre silah önerisinde bulunuyor.
                               #silah önerisi yaparken silah seç fonksiyonunu çağırıyor.
        "Bölgenin tehlike seviyesini 10 üzerinden değerlendirin."
        a = self.degree_of_the_danger(danger)
        
        if a == "Kırmızı Bölge":
            print('Kırmızı Bölge: yok edici silahlar gerekir')
            return self.silah_sec(12,6800)
    
        if a == "Beyaz Bölge":
            print('Beyaz Bölge: hafif silahlar yeterlidir')
            return self.silah_sec(1,300)

        if a == "Mavi Bölge":
            print('Mavi Bölge: güçlü silahlar gerekir')
            return self.silah_sec(6,1000)

        if a == "Yeşil Bölge":
            print('Yeşil Bölge: etkili silahlar gerekir')
            return self.silah_sec(4,400)
