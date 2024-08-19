print('Taş kağıt makas oyununa hoşgeldin')
oyun='taş,kağıt,makas'
tur=0
oyun_sayısı=0
pc_win=0
oyuncu_win=0
yeni_oyun='evet,hayır'

import random

while(tur!=2):
    x=(random.choice(oyun))
    pc_hamle=x
    print('pc hamle=',pc_hamle)
    oyuncu_hamle=input("taş,kağıt,makas?\n")
    if(pc_hamle==oyuncu_hamle):
      print('Beraberlik!')
      tur+=1
      oyuncu_win==oyuncu_win
      pc_win==pc_win
      print('tur=',tur,'oyuncu galibiyet=',oyuncu_win,'pc galibiyet=',pc_win)
    elif (oyuncu_hamle=="taş"):
         if(pc_hamle) == "kağıt)": 
            pc_win+=1
            print("Kaybettiniz")
            tur+=1
            print('tur=',tur,'oyuncu galibiyet=',oyuncu_win,'pc galibiyet=',pc_win)
         else:  
             oyuncu_win+=1
             print('Şanslıydın,kazandın')
             tur+=1
             print('tur=',tur,'oyuncu galibiyet=',oyuncu_win,'pc galibiyet=',pc_win)
    elif(oyuncu_hamle == "kağıt"):
        if(pc_hamle) == "makas)": 
         pc_win+=1
         print("Kaybettiniz")
         tur+=1
         print(tur)
        else:  
             oyuncu_win+=1
             print('Şanslıydın,kazandın')
             tur+=1
             print(tur)
    elif(oyuncu_hamle== "makas"):
        if(pc_hamle) == "taş)": 
         pc_win+=1
         print("Kaybettiniz")
         tur+=1
         print('tur=',tur,'oyuncu galibiyet=',oyuncu_win,'pc galibiyet=',pc_win)
        else:  
            oyuncu_win+=1 
            print('Şanslıydın,kazandın')
            tur+=1
            print('tur=',tur,'oyuncu galibiyet=',oyuncu_win,'pc galibiyet=',pc_win)

while True:
 oyuncu_karar=input('Tekrardan oynamak ister misin?\n').lower()
 y=random.choice(yeni_oyun)
 pc_karar=(y)
 if oyuncu_karar=="evet" and pc_karar=="evet":
    oyun_sayısı+=1
    print('yeni oyun başlıyor','oyun sayısı', oyun_sayısı)
    continue
while False: 
    print('oyun bitti. yeni oyunlarda görüşmek üzere')
    break




