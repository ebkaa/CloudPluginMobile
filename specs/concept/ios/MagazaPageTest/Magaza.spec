Specification Heading
=====================
Created by nurgul on 7.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Login Magaza Cihaz Kontrolu
---------------------------
 Tags:LoginMagazaCihazKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "Akıllı Telefonlar" değerini sayfa üzerinde olup olmadığını kontrol et.
* "hemenAlButonu" li elementi bulana kadar swipe et ve tıkla

///// tekrar bakılacak
Login Cihaz Akıllı Telefon Satın Alma
--------------------------------
Tags:LoginTelefonCihazSatinAl

* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* ilk telefonu hemen al login
* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sepeteEkleBtn" li elementi bul ve tıkla
*  "krediSorgula" li elementi bul ve varsa tıkla
/* "10" saniye bekle
*  "pesinSatinAl" li elementi bul ve varsa tıkla
/* "5" saniye bekle
* Login Satın al


Sepeti boşalt
 "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
 "hemenAlButonu"li elementi bulana kadar "3" kere swipe yap ve elementi bul
 "hemenAlButonu" li elementi bul ve tıkla
 "5" saniye bekle
 "yoksayBtn" li elementi bul ve varsa tıkla
 "sepeteEkleBtn"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "sepeteEkleBtn" li elementi bul ve tıkla
 "yoksayBtn" li elementi bul ve varsa tıkla
 "krediSorgula" li elementi bul ve tıkla
 "10" saniye bekle
 "pesinSatinAl" li elementi bul ve tıkla
  "2" saniye bekle
/* "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
 "sıparısSozlesmeOkudum"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "1" saniye bekle
 "sıparısSozlesmeOkudum" li elementi bul ve tıkla
 "sıparısSozlesmeOnayla" li elementi bul ve tıkla
 "sıparıseDevamEt" li elementi bul ve tıkla
 "5" saniye bekle
/* "5","70" oranlarından "5","30" oranlarına "4" kere swipe et
 "1" saniye bekle
 "odemeSozlesmeOkudum"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "odemeSozlesmeOkudum" li  telefonun  "10" ve elementin "50" kordinatına göre tıkla
 "odemeYap" li elementi bul ve tıkla
 "TCKNGuvenlıKart" li elementi bul ve "45106611958" değerini yaz
 Klavyeyi kapat
 "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
 "cvvGuvenlıKart" li elementi bul ve "936" değerini yaz
 Klavyeyi kapat
 "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
 "onaylaGuvenlıKart" li elementi bul ve tıkla
 "kartDogrulamaSayfası" li elementi bul ve tıkla
 "sepetimButonu" li elementi bul ve tıkla



Login Cihaz Tablet Satın Alma
---------------------------------
Tags:LoginTabletCihazSatinAl

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "5" saniye bekle
* dijital magazaya gir
* Sepeti boşalt
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "2" saniye bekle
* "tumuButonu" li elementi bul ve tıkla
* "5" saniye bekle
 sayfadaki "45" "75"  alana tıkla
 "5" saniye bekle
* "80","70" oranlarından "80","30" oranlarına "2" kere swipe et
* "tabletSec" elementi sayfada yer almıyor "DO" yer alıyorsa "Tablet elementi clickable değil!" mesajı verilir

 "tabletSec" üründen Random  sec
 "5" saniye bekle
 "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
 "sepeteEkleBtn" li elementi bul ve tıkla
 "krediSorgula" li elementi bul ve tıkla
 "10" saniye bekle
 "pesinSatinAl" li elementi bul ve tıkla
 "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
 "1" saniye bekle
 "sıparısSozlesmeOkudum" li elementi bul ve tıkla
 "sıparısSozlesmeOnayla" li elementi bul ve tıkla
 "sıparıseDevamEt" li elementi bul ve tıkla
 "50","70" oranlarından "50","30" oranlarına "4" kere swipe et
 "1" saniye bekle
 "odemeSozlesmeOkudum" li  telefonun  "10" ve elementin "50" kordinatına göre tıkla
 "odemeYap" li elementi bul ve tıkla
 "TCKNGuvenlıKart" li elementi bul ve "45106611958" değerini yaz
 "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
 "cvvGuvenlıKart" li elementi bul ve "936" değerini yaz
 "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
 "onaylaGuvenlıKart" li elementi bul ve tıkla
 "kartDogrulamaSayfası" li elementi bul ve tıkla
 "sepetimButonu" li elementi bul ve tıkla
 Sepeti Sil



Login Cihaz Aksesuar Satın Alma
-----------------------------
Tags:LoginAksesuarCihazSatinAl

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "sepetimButonu" li elementi bul ve tıkla
* Sepeti boşalt
* geri butonuna bas
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "2" saniye bekle
* "tumuButonu" li elementi bul ve tıkla
* "5" saniye bekle
* sayfadaki "60" "75"  alana tıkla
* "5" saniye bekle
* "80","70" oranlarından "80","30" oranlarına "2" kere swipe et
* "AksesuarSec" üründen Random  sec
* "5" saniye bekle
* "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
* "sepeteEkleBtn" li elementi bul ve tıkla
* "krediSorgula" li elementi bul ve tıkla
* "10" saniye bekle
* "pesinSatinAl" li elementi bul ve tıkla
* "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
* "1" saniye bekle
* "sıparısSozlesmeOkudum" li elementi bul ve tıkla
* "sıparısSozlesmeOnayla" li elementi bul ve tıkla
* "sıparıseDevamEt" li elementi bul ve tıkla
* "50","70" oranlarından "50","30" oranlarına "4" kere swipe et
* "1" saniye bekle
* "odemeSozlesmeOkudum" li  telefonun  "10" ve elementin "50" kordinatına göre tıkla
* "odemeYap" li elementi bul ve tıkla
* "TCKNGuvenlıKart" li elementi bul ve "45106611958" değerini yaz
* "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
* "cvvGuvenlıKart" li elementi bul ve "936" değerini yaz
* "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
* "onaylaGuvenlıKart" li elementi bul ve tıkla
* "kartDogrulamaSayfası" li elementi bul ve tıkla
* "sepetimButonu" li elementi bul ve tıkla






Logout Magaza Cihaz Kontrolu
----------------------------
 Tags:LogoutMagazaCihazKontrolu

* Kullanıcı girişi yapılmışsa çıkış yap
* dijital magazaya gir
* "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "Akıllı Telefonlar" değerini sayfa üzerinde olup olmadığını kontrol et.
* "LasthemenAlButonu" li elementi bulana kadar swipe et ve tıkla
* "2" saniye bekle
* "LasthemenAlButonu" li elementi bul varsa "tıklanamadı" mesajını hata olarak göster
 "Yorum" değerini sayfa üzerinde olup olmadığını kontrol et.




Login Magaza Uygulama Kontrolu
------------------------------
 Tags:LoginMagazaUygulamaKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "uygulamalarTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "XCUIElementTypeOther" değerini sayfa üzerinde olup olmadığını kontrol et.


Logout Magaza Uygulama Kontrolu
-------------------------------
 Tags:LogoutMagazaUygulamaKontrolu

* Kullanıcı girişi yapılmışsa çıkış yap
* dijital magazaya gir
* "2" saniye bekle
* "uygulamalarTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "XCUIElementTypeOther" değerini sayfa üzerinde olup olmadığını kontrol et.


Login Magaza Paketler Kontrolu
------------------------------
 Tags:LoginMagazaPaketlerKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "5" saniye bekle
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "incele1"li elementi bulana kadar "3" kere swipe yap ve elementi bul

Logout Magaza Paketler Kontrolu -57
-------------------------------
 Tags:LogoutMagazaPaketlerKontrolu

* Kullanıcı girişi yapılmışsa çıkış yap
* "2" saniye bekle
* dijital magazaya gir
* "2" saniye bekle
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "incele1" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "incele1" li elementi bul varsa "tıklanamadı" mesajını hata olarak göster

Logout Cihaz Satin Alma Akilli Telefon
--------------------------------------
 Tags:LogoutCihazSatinAlmaAkillitelefon

* Kullanıcı girişi yapılmışsa çıkış yap
* Akıllı telefonlara gel
* Apple için filtrele
* "iphone11"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "iphone11" li elementi bul ve tıkla
*"3" saniye bekle
* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sepeteEkleBtn" elementinin koordinatlarına x="200" y="-200" degerlerini ekleyerek tıkla
* "sepeteEkleBtn" li elementi bul ve tıkla
* "5" saniye bekle
* "logoutDevamEt" li elementi bul ve tıkla
* "80","80" oranlarından "80","30" oranlarına "2" kere swipe et
* "3" saniye bekle
* "sıparıseDevamEt"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "sıparıseDevamEt" elementinin koordinatlarına x="10" y="-100" degerlerini ekleyerek tıkla
* "sıparıseDevamEt" li elementi bul ve tıkla
* Logout Odeme Sayfası Bilgilerini Doldur






/* Kullanıcı girişi yapılmışsa çıkış yap
/* dijital magazaya gir
/ "2" saniye bekle
/* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
/* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
/* "hemenAlButonu" li elementi bulana kadar swipe et ve tıkla
/* "10" saniye bekle
/* "50","70" oranlarından "50","30" oranlarına "1" kere swipe et
/* "1" saniye bekle
/* sayfadaki "50" "60"  alana tıkla
/* sayfadaki "50" "70"  alana tıkla
/* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
/* "magazaGirisYapmadanDevamEtButonu" li elementi bul ve tıkla
/* "10" saniye bekle
/* "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
/* "sepeteEkleBtn" li elementi bul ve tıkla
/* "krediSorgula" li elementi bul ve tıkla
/* "10" saniye bekle
/* "pesinSatinAl" li elementi bul ve tıkla
/* "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
/* "1" saniye bekle
/* "sıparısSozlesmeOkudum" li elementi bul ve tıkla
/* "sıparısSozlesmeOnayla" li elementi bul ve tıkla
/* "sıparıseDevamEt" li elementi bul ve tıkla
/* "50","70" oranlarından "50","30" oranlarına "2" kere swipe et
/* "1" saniye bekle
/* "odemeSozlesmeOkudum" li  telefonun  "10" ve elementin "50" kordinatına göre tıkla
/* "odemeYap" li elementi bul ve tıkla
/* "TCKNGuvenlıKart" li elementi bul ve "45106611958" değerini yaz
/* "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
/* "cvvGuvenlıKart" li elementi bul ve "936" değerini yaz
/* "IOS-Klavye-BittiButonu" li elementi bul ve tıkla
/* "onaylaGuvenlıKart" li elementi bul ve tıkla
/* "kartDogrulamaSayfası" li elementi bul ve tıkla
/* "sepetimButonu" li elementi bul ve tıkla

Logout Tablet Satın Alma
------------------------
 Tags:LogoutTabletSatinAlma

* Kullanıcı girişi yapılmışsa çıkış yap
* dijital magazaya gir
* "3" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "tumCıhazlar" li elementi bul ve tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "80","80" oranlarından "80","30" oranlarına "1" kere swipe et
* "1" saniye bekle
* "tablet" li elementi bul ve tıkla
* "5" saniye bekle
* "80","70" oranlarından "80","30" oranlarına "1" kere swipe et
* "1" saniye bekle
* "tabletSec" üründen Random  sec
* "5" saniye bekle
* Tablet stokta var mi kontrol et
* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
* "5" saniye bekle
* "urunRenk" elementi bulunmuyorsa "haberdarEt" varsa "ÜRÜN STOKTA YOK" uyarısı verilir
* "magazaWebSatinAlButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
* "magazaGirisYapmadanDevamEtButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "50","50" oranlarından "50","30" oranlarına "3" kere swipe et
* "magazaKullaniciSozlesmesiCheckbox" li elementi bulana kadar swipe et ve tıkla
* "magazaSepetiOnaylaButonu" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* iOS Logout Odeme Sayfası Bilgilerini Doldur

Logout Aksesuar Satın Alma
------------------------
 Tags:LogoutAksesuarSatinAlma

* Kullanıcı girişi yapılmışsa çıkış yap
* dijital magazaya gir
* "3" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "tumCıhazlar" li elementi bul ve tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "80","80" oranlarından "80","30" oranlarına "1" kere swipe et
* "Aksesuar" li elementi bul ve tıkla
* "5" saniye bekle
* "80","60" oranlarından "80","30" oranlarına "2" kere swipe et
* "AksesuarTıpıSec" li elementi bul ve tıkla
* "5" saniye bekle
* "80","50" oranlarından "80","30" oranlarına "3" kere swipe et
* "AksesuarSec" üründen Random  sec
* "5" saniye bekle
* Aksesuar stokta var mi kontrol et
* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
* "5" saniye bekle
* "urunRenk" elementi bulunmuyorsa "haberdarEt" varsa "ÜRÜN STOKTA YOK" uyarısı verilir
* "magazaWebSatinAlButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
* "magazaGirisYapmadanDevamEtButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "50","50" oranlarından "50","30" oranlarına "3" kere swipe et
* "magazaKullaniciSozlesmesiCheckbox" li elementi bulana kadar swipe et ve tıkla
* "magazaSepetiOnaylaButonu" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* iOS Logout Odeme Sayfası Bilgilerini Doldur

// testfligt koşulurken aktif edilecek
Logout Tesflight Magaza Sayfa Kontrolu
------------------------------
 Tags:testFlightMagazaSayfaKontrol

* Kullanıcı girişi yapılmışsa çıkış yap
//* "2" saniye bekle
//* "testflyUygulamalar" li element sayfada bulunuyor mu kontrol et
//* "50","60" oranlarından "50","30" oranlarına "1" kere swipe et


cıkarılacak senaryo
Login Magaza Paketler Kontrolu Mavi Band
------------------------------
 Tags:LoginMagazaPaketlerKontroluMaviBand

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 dijital magazaya gir
 "2" saniye bekle
 "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
 "paketlerTabı" li elementi bul ve tıkla
"2" saniye bekle
"dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
"dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tümPaketler" li elementi bul ve tıkla
 "tümTeklifler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tümTeklifler" li elementi bul ve tıkla
 "hazırKart" li elementi bul ve tıkla
 "lifeCellPaketleri" li elementi bul ve tıkla
 "vınnİnternetPaketleri" li elementi bul ve tıkla
 "superMixPaketleri" li elementi bul ve tıkla
 "maviBant"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "maviBant" li elementi bul ve tıkla


IOS Paketlerde Aylik Abonelik Satin Al Kontrolleru
-----------------------------
Tags:IOSPaketlerdeAylikAbonelikSatinAlKontrolu
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "tümTeklifler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümTeklifler" li elementi bul ve tıkla
* "6" saniye bekle
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ekPaketler" li elementi bul ve tıkla
* "taraftarPaketleri" li elementi bul ve tıkla
* "sarıPaket" li elementi bul ve tıkla
* "HemenAlBtn" li elementi bul ve tıkla
* "satınAlBtn"li elementi bulana kadar "4" kere swipe yap ve elementi bul

/DEVIRDAİM
IOS Paketlerde Aylik Abonelik Seçilebildiginin Kontrolu -63
----------------------------------
 Tags:IOSPaketlerdeAylikAbonelikSecilebildigininKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "tümTeklifler" li elementi bul ve tıkla
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ekPaketler" li elementi bul ve tıkla
* "taraftarPaketleri" li elementi bul ve tıkla
* "sarıPaket" li elementi bul ve tıkla

cıkarılacak
IOS Paketlerde Yillik Abonelik seçilebildiginin kontrolu -63
-------------------------------
 Tags:IOSPaketlerdeYillikAbonelikSecilebildigininKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 dijital magazaya gir
 "2" saniye bekle
 "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
 "paketlerTabı" li elementi bul ve tıkla
 "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tümPaketler" li elementi bul ve tıkla
 "5" saniye bekle
 "tümTeklifler" li elementi bul ve tıkla
 "5" saniye bekle
 "hazırKarttanFaturalıyaGeçiş" li elementi bul ve tıkla
 "5" saniye bekle
 "yıllıkAbonelik" li elementi bul ve tıkla

IOS Paket satin alma isleminde email ve sozlesme ekrani kontrolu -67
-----------------------------
 Tags:IOSPaketSatinAlmaIslemindeEmailVeSozlesmeEkraniKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
*"1" saniye bekle
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "10" saniye bekle
* "yoksayBtn" li elementi bul ve varsa tıkla
* "5" saniye bekle
/* "tümTeklifler" elementinin koordinatlarına x="5" y="5" degerlerini ekleyerek tıkla
* "tümTeklifler" li elementi bul ve tıkla
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
/* "ekPaketler" elementinin koordinatlarına x="5" y="5" degerlerini ekleyerek tıkla
* "ekPaketler" li elementi bul ve tıkla
* "taraftarPaketleri" li elementi bul ve tıkla
* "sarıPaket" li elementi bul ve tıkla
* "HemenAlBtn" li elementi bul ve tıkla
* "satınAlBtn"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ePostaCheck" li element sayfada bulunuyor mu kontrol et
* "önBilgilendirmeFormuCheck"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "önBilgilendirmeFormuCheck" li element sayfada bulunuyor mu kontrol et

IOS Paketlerde Yillik Abonelik Hemen Al Kontrolleri -66
-----------------------------
 Tags:IOSPaketlerdeYillikAbonelikHemenAlKontrolleri

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "tümTeklifler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümTeklifler" li elementi bul ve tıkla
* "tumPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tumPaketler" li elementi bul ve tıkla
* "yeniPlatinumPaketler" li elementi bul ve tıkla
* "paketIcerik" li elementi bul ve tıkla
/* "yıllıkAbonelik"li elementi bulana kadar "3" kere swipe yap ve elementi bul
/* "yıllıkAbonelik" li elementi bul ve tıkla
/* "yillikAbonelikAlanıSecimi" li elementi bul ve varsa dokun
* "paketHemenAlBtn"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "paketHemenAlBtn" li element sayfada bulunuyor mu kontrol et

IOS Paketlerde Aylik Abonelik Hemen Al Kontrolleru -59
-----------------------------
Tags:IOSPaketlerdeAylikAbonelikHemenAlKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "tümTeklifler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümTeklifler" li elementi bul ve tıkla
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ekPaketler" li elementi bul ve tıkla
* "taraftarPaketleri" li elementi bul ve tıkla
* "sarıPaket" li elementi bul ve tıkla
* "paketHemenAlBtn"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "paketHemenAlBtn" li elementi bul yoksa "bulunamadı" mesajını hata olarak göster


çıkarılacak
Paketlerde Yillik Abonelik Secildiginde Satin Al IOS
------------------------------------
 Tags:paketlerdeYillikAbonelikSecildigindeSatinAlIOS

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 dijital magazaya gir
 "2" saniye bekle
 "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
 "paketlerTabı" li elementi bul ve tıkla
 "2" saniye bekle
dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
"dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tümPaketler" li elementi bul ve tıkla
 "tümTeklifler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tümTeklifler" li elementi bul ve tıkla
 "tumPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tumPaketler" li elementi bul ve tıkla
 "yeniPlatinumPaketler2" li elementi bul ve tıkla
 "paketIcerik" li elementi bul ve tıkla
 "paketHemenAlBtn"li elementi bulana kadar "5" kere swipe yap ve elementi bul
 "paketHemenAlBtn" li elementi bul ve tıkla
 "paketSatinAlemailAlani" li elementi bul, temizle ve "g@gmail.com" değerini yaz
  Hide keyboard
 "paketSatinAlemailAlaniAgain" li elementi bul, temizle ve "g@gmail.com" değerini yaz
  Hide keyboard
 "paketSatinAlSozlesmeCheckBox" li elementi bul ve tıkla
 "paketSatinAlBtn" li elementi bul ve tıkla
 "transferSatinAl"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "paketSatinAlOnBilgilendirmeCheckBox" li element varsa  "6" "50" koordinatına tıkla
 "paketSatinAlOnay" li elementi bul ve tıkla
 "paketSatinAlTamamPopup" li element sayfada bulunuyor mu kontrol et


Dergilik IOS
-----------
 Tags:DergilikIOS

* Kullanıcı girişi yapılmışsa çıkış yap
* "5" saniye bekle
* "uygulamalarTabı" li elementi bul ve tıkla
* "dergilik"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "kesfetBtnDergılık" li elementi bul ve tıkla
* "GooglePlay" li elementi bul yoksa "APP STORE GİRİLMEDİ" mesajını hata olarak göster


////////////////-----
15.01.2020
IOS Uygulamalar Aç Buton Adı Kontrolü
---------------------------------------
Tags:IOSUygulamalarAcButonAdiKontrolu
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "uygulamalarTabı" li elementi bul ve tıkla
* "btn_Ac"li elementi bulana kadar "12" kere swipe yap ve elementi bul

16.01.2020
IOS Uygulamalar Keşfet Tıklandığında Store Yönlendirme Kontrolu
---------------------------------
Tags:IOSUygulamalarKesfetTiklandigindaStoreYonlendirmeKontrolu
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "uygulamalarTabı" li elementi bul ve tıkla
* "9","500" coordinatından "9","250" coordinatına "12" kere swipe et
* "btn_Ac"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* Click element by "btn_Kesfet"
* "5" saniye bekle
* "GooglePlay" li elementi bul yoksa "AppStore açılamadı" mesajını hata olarak göster
/* "GooglePlay" istenilen sayfaya geçilip geçilmediği kontrol edilir

IOS Uygulamalar Aç Tıklandığında Uygulamanın Açıldığının Kontrolu
---------------------------------
Tags:IOSUygulamalarAcTiklandigindaUygulamaninAcildigininKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "uygulamalarTabı" li elementi bul ve tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "200","500" coordinatından "200","200" coordinatına "10" kere swipe et
* Swipe times "9"
* Click element by "btn_Ac"
* "uygulamalarTabı" li elementi bul varsa "geçilemedi" mesajını hata olarak göster

