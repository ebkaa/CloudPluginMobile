Specification Heading
=====================
Created by sahabt on 2019-12-17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.






//AND Randevu Al sayfası kontrolü
//---------------------------------
//
//* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
//* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
//* En yakın turkcell sayfasına gir konum kapalı
//*"ankara" sehrine "Cankaya" ilcesine git
//* "randevuAl" li elementi bul ve tıkla
//* "5" saniye bekle
//* "randevuCheck" li element sayfada bulunuyor mu kontrol et




AND Enyakın Turkcell Sayfa Düzeni Kontrolü
--------------------------
* Konumkapalı olarak çalıştır AND
* En yakın turkcell sayfasına gir konum kapalı
* "SDKbaslık" elementi bulunmuyorsa "BASLIK BULUNAMADI" varsa "BASLIK BULUNDU" uyarısı verilir
* "SDKturkcellveSuperonline" elementi bulunmuyorsa "TURKCELL VE SUPERONLİNE BARI BULUNAMADI" varsa "TURKCELL VE SUPERONLİNE BARI BULUNDU" uyarısı verilir
* "SDKHaritaİşaretleyici" elementi bulunmuyorsa "HARİTA İŞARETLEYİCİ BULUNAMADI" varsa "HARİTA İŞARETLEYİCİ BULUNDU" uyarısı verilir
* "SDKharita" elementi bulunmuyorsa "HARİTA BULUNAMADI" varsa "HARİTA BULUNDU" uyarısı verilir

AND Enyakın Turkcell Harita Kontrolü
----------------------
* Konumkapalı olarak çalıştır AND
* En yakın turkcell sayfasına gir konum kapalı
* "SDKHaritaİşaretleyici" elementi bulunmuyorsa "HARİTA İŞARETLEYİCİ BULUNAMADI" varsa "HARİTA İŞARETLEYİCİ BULUNDU" uyarısı verilir
* "SDKharita" elementi bulunmuyorsa "HARİTA BULUNAMADI" varsa "HARİTA BULUNDU" uyarısı verilir

AND Enyakın Turkcell Konum Kapalı Popup-Ayarlar Kontrolü
-------------------
* Konumkapalı olarak çalıştır AND
* En yakın turkcell sayfasına gir konum kapalı

AND Enyakın Turkcell Automatic konum ile il-ilçe kontrolü
--------------------------------------------------------
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
*En yakın turkcell sayfasına gir konum acık
*"KonumAcıkEnYakınTurkcellBayi" li element sayfada bulunuyor mu kontrol et


