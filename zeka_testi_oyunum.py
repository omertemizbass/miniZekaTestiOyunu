"""
Mini Zeka Testi Oyunu - Python CLI (Command Line Interface) Projesi
 
Selam! 👋
 
Bu basit konsol oyunu, klasik zeka testleri (IQ ve Mantık) sorularıyla Python öğrenme yolculuğumun ilk ciddi adımıdır. 
Kendi başıma kodlamanın çoğunu tamamladım ve kalan kısımları topluluk yardımıyla ve başka kaynaklar yoluyla daha sağlam 
hale getirdim.
Sözlükleri kullanmak satırları kısaltabilir fakat ben bu şekilde yapmayı tercih ettim. Strip ve replace metodları hakkında
da kendimi geliştirmiş oldum.
 
Projeye katkıda bulunmaktan veya yeni sorular eklemekten çekinmeyin!
 
- Eğer Soru 2'deki gibi kafa karıştırıcı bir sorunuz varsa, bekliyorum! :)
"""

game_title = "///Mini Zeka Testi Oyunu///"
print(game_title)

kullanici_ismi = input("İsminiz Nedir: ")
kullanici_ismi_basharf = kullanici_ismi.capitalize()
baslangic_mesaji = f"Merhaba, {kullanici_ismi_basharf} oyunumuza hoşgeldiniz:) Hazırsanız başlıyalım!"
print(baslangic_mesaji)


sayac = 0

soru1 = input("1. Soru: 2 üzeri 6 kaçtır?")

if soru1.strip() == "64":
    print("Tebrikler cevabınız doğru! Sıradaki soruya geçiyoruz.")
    sayac += 1
else:
    print("Malesef cevabınız yanlış, doğru cevap 64.")
    

soru2 = input("2. Soru: Bir tenis raketinin ve bir topun toplam fiyatı 1,10 liradır. Tenis raketinin fiyatı toptan 1 lira daha fazla olduğuna göre topun fiyatı ne kadardır? ")

cevap2_temiz = soru2.strip().replace(',', '.') 
 
if cevap2_temiz in ["0.05", "5 kuruş", "5 kurus"]:
    print("Tebrikler cevabınız doğru! Sıradaki soruya geçiyoruz.")
    sayac += 1
else:
    print("Malesef cevabınız yanlış, doğru cevap 0.05 (veya 5 kuruş) olacaktı.")


soru3 = input("3. Soru: 5 makine 5 ürünü 5 dakikada üretirse 100 makine 100 ürünü kaç dakikada üretir?")

if soru3.strip() in ["5 dakika", "5"]: 
    print("Tebrikler cevabınız doğru! Sıradaki soruya geçiyoruz.")
    sayac += 1
else:
    print("Malesef cevabınız yanlış, doğru cevap 5 dakika.")


soru4 = input("4. Soru: Bir gölde bir nilüfer yaprağı bulunur. Bu yaprak her gün iki katı büyüklüğe ulaşır. Yaprağın tüm gölü kaplaması 48 gün sürdüğüne göre, yaprağın gölün yarısını kaplaması kaç gün sürer?")

if soru4.strip() == "47":
    print("Tebrikler cevabınız doğru! Sıradaki soruya geçiyoruz")
    sayac += 1
else:
    print("Malesef cevabınız yanlış, doğru cevap 47.")


soru5 = input("5. Soru: Hayatta değilim ama büyüyorum; Akciğerlerim yok ama havaya ihtiyacım var; Ağzım yok ama su beni öldürüyor. Ben neyim? ")

if soru5.strip().lower() == "ateş":
    print("Tebrikler cevabınız doğru! Sıradaki soruya geçiyoruz")
    sayac += 1
else:
    print("Malesef cevabınız yanlış, doğru cevap ateş olacaktı.")

# - Sonuç -
toplam_dogru_sayisi = sayac
print("... SONUÇLAR ...")
print(f"Toplam doğru sayınız: {toplam_dogru_sayisi}")

if toplam_dogru_sayisi == 5:
    print("Tüm soruları bildiniz, sonucunuz harika! Mükemmel IQ.")
elif toplam_dogru_sayisi == 4:
    print("4 doğru 1 yanlış yaptınız, süper sonuç tebrikler...")
elif toplam_dogru_sayisi == 3:
    print("3 doğru 2 yanlış yaptınız. Skorunuz fena değil...")
elif toplam_dogru_sayisi == 2:
    print("2 doğru 3 yanlış yaptınız. Zor bir testi fakat geliştirilebilir.")
elif toplam_dogru_sayisi == 1:
    print("Sadece 1 doğru yaptınız, sonuç biraz üzücü fakat başarabilirsiniz.")
else:
    print("Doğru yanıtınız yok:(")


























































































