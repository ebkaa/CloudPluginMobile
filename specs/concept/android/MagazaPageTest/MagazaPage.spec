Specification Heading
=====================
Created by sahabt on 12.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Login Magaza Cihaz Kontrolu
---------------------------
 Tags:AndroidLoginMagazaCihazKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* ilk telefonu hemen al login
* "carpıButonIkı" li element sayfada bulunuyor mu kontrol et
* "carpıButonIkı" li elementi bul ve tıkla
* "2" saniye bekle
* "Dijital Mağaza" değerini sayfa üzerinde olup olmadığını kontrol et.

//pass aldı
Login Cihaz Akıllı Telefon Satın Alma
------------------------------------
Tags:AndroidLoginTelefonCihazSatinAl
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* ilk telefonu hemen al login
* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sepeteEkleBtn" li elementi bul ve tıkla
*  "krediSorgula" li elementi bul ve varsa tıkla
*  "pesinSatinAl" li elementi bul ve varsa tıkla
* Login Satın al

Login Cihaz Tablet Satın Alma
---------------------------------
Tags:AndroidLoginTabletCihazSatinAl
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tablet Bölümüne gir login
* Apple için filtrele
* Swipe times "1"
* "ilkTablet"li elementi bulana kadar "2" kere swipe yap ve elementi bul
*  "ilkTablet" li elementi bul ve tıkla
* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sepeteEkleBtn" li elementi bul ve tıkla
*  "krediSorgula" li elementi bul ve varsa tıkla
*  "pesinSatinAl" li elementi bul ve varsa tıkla
/* "2" saniye bekle
* Login Satın al


//ıdlendir me bekliyor
Login Cihaz Aksesuar Satın Alma
-----------------------------
Tags:AndroidLoginAksesuarCihazSatinAl
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "6" saniye bekle
* dijital magazaya gir
* "2" saniye bekle
* Sepeti boşalt
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* Telefon kılıfı bölümüne gir
* "80","80" oranlarından "80","30" oranlarına "5" kere swipe et
* "ilkKılıf" li elementi bul ve tıkla
* Urun stokta var mi kontrol et ikinci sıra= "ikinciKılıf" birinci element = "ilkKılıf"
* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sepeteEkleBtn" li elementi bul ve tıkla
*  "krediSorgula" li elementi bul ve varsa tıkla
* "10" saniye bekle
*  "pesinSatinAl" li elementi bul ve varsa tıkla
* "2" saniye bekle
* Login Satın al

//girişYapmadanDevamEt butonunun idsi olmadıgı için çıkartılacak
Logout Cihaz Satın Alma
------------------------
 Tags: AndroidLogoutCihazSatinAl
* Kullanıcı girişi yapılmışsa çıkış yap
//* Akıllı telefonlara gel
//* Apple için filtrele
//* "iphone11"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "iphone11" li elementi bul ve tıkla
//*"3" saniye bekle
//* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
//* "sepeteEkleBtn" elementinin koordinatlarına x="200" y="-200" degerlerini ekleyerek tıkla
//* "sepeteEkleBtn" li elementi bul ve tıkla
//* "5" saniye bekle
//* "logoutDevamEt" li elementi bul ve tıkla
//* "80","80" oranlarından "80","30" oranlarına "2" kere swipe et
//* "3" saniye bekle
//* "sıparıseDevamEt"li elementi bulana kadar "5" kere swipe yap ve elementi bul
//* "sıparıseDevamEt" elementinin koordinatlarına x="10" y="-100" degerlerini ekleyerek tıkla
//* "sıparıseDevamEt" li elementi bul ve tıkla
//* Logout Odeme Sayfası Bilgilerini Doldur

//girişYapmadanDevamEt butonunun idsi olmadıgı için çıkartılacak
Logout Tablet Satın Alma
---------------------
 Tags:AndroidLogoutTabletSatinAl
* Giriş yapılmışsa çıkış yap
//* Tablet Bölümüne gir logout
//* Urun stokta var mi kontrol et ikinci sıra= "ikinciTablet" birinci element = "ilkTablet"
//* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
//* "sepeteEkleBtn" li elementi bul ve tıkla
//* "girişYapmadanDevamEt" li elementi bul ve tıkla
//* "sıparıseDevamEt"li elementi bulana kadar "6" kere swipe yap ve elementi bul
//* "sıparıseDevamEt" elementinin koordinatlarına x="0" y="-100" degerlerini ekleyerek tıkla
//* "sıparıseDevamEt" li elementi bul ve tıkla
//* "2" saniye bekle
//* Logout Odeme Sayfası Bilgilerini Doldur




Logout Aksesuar Satın Alma
-----------------------
 Tags:AndroidLogoutAksesuarSatinAlma
* Giriş yapılmışsa çıkış yap
* "5" saniye bekle
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* Telefon kılıfı bölümüne gir
* "ilkKılıf" li elementi bul ve tıkla
* Urun stokta var mi kontrol et ikinci sıra= "ikinciKılıf" birinci element = "ilkKılıf"
* "sepeteEkleBtn"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sepeteEkleBtn" li elementi bul ve tıkla
* "girişYapmadanDevamEt" li elementi bul ve tıkla
* "sıparıseDevamEt"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "sıparıseDevamEt" elementinin koordinatlarına x="0" y="-100" degerlerini ekleyerek tıkla
* "sıparıseDevamEt" li elementi bul ve tıkla
* "2" saniye bekle
* Logout Odeme Sayfası Bilgilerini Doldur





Logout Magaza Cihaz Kontrolu
----------------------------
 Tags:AndroidLogoutMagazaCihazKontrolu

* Kullanıcı girişi yapılmışsa çıkış yap
* dijital magazaya gir
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "hemenAlButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "hemenAlButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "carpıButonIkı" li element sayfada bulunuyor mu kontrol et
* "carpıButonIkı" li elementi bul ve tıkla
* "Dijital Mağaza" değerini sayfa üzerinde olup olmadığını kontrol et.


Login Magaza Uygulama Kontrolu
------------------------------
 Tags:AndroidLoginMagazaUygulamaKontrolu

 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* dijital magazaya gir
* "2" saniye bekle
* Sepeti boşalt
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "uygulamalarTabı" li elementi bul ve tıkla
* "5" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "2" saniye bekle
* "80","70" oranlarından "80","40" oranlarına "1" kere swipe et
* "Keşfet" li elementi bul ve tıkla


Logout Magaza Uygulama Kontrolu
-------------------------------
 Tags:AndroidLogoutMagazaUygulamaKontrolu
* Giriş yapılmışsa çıkış yap
* "5" saniye bekle
* dijital magazaya gir
* "4" saniye bekle
* "uygulamalarTabı" li ve değeri "UYGULAMALAR" e eşit olan elementli bul ve tıkla
* "4" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "1" saniye bekle
* "Keşfet" değerini sayfa üzerinde olup olmadığını kontrol et.
* "Keşfet" li elementi bul ve tıkla



Login Magaza Paketler Kontrolu
------------------------------
 Tags:AndroidLoginMagazaPaketlerKontrolu
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 dijital magazaya gir
 "2" saniye bekle
* Sepeti boşalt
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* Değeri "PAKETLER" e eşit olan elementli bul ve tıkla
 "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
"50","50" oranlarından "50","30" oranlarına "1" kere swipe et* "2" saniye bekle
* "detayaGitButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "detayaGitButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "carpıButonIkı" li element sayfada bulunuyor mu kontrol et
* "carpıButonIkı" li elementi bul ve tıkla
* "5" saniye bekle
* "PAKETLER" değerini sayfa üzerinde olup olmadığını kontrol et.


Logout Magaza Paketler Kontrolu -57
-------------------------------
  Tags:AndroidLogoutMagazaPaketlerKontrolu
* Giriş yapılmışsa çıkış yap
* "5" saniye bekle
* dijital magazaya gir
* "2" saniye bekle
* "1" kere aşağıya kaydır
* Değeri "PAKETLER" e eşit olan elementli bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
* "2" saniye bekle
* "detayaGitButonu" li elementi bul ve tıkla
* "10" saniye bekle
* "carpıButonIkı" li element sayfada bulunuyor mu kontrol et
* "carpıButonIkı" li elementi bul ve tıkla
* "PAKETLER" değerini sayfa üzerinde olup olmadığını kontrol et.



AND Paketlerde Aylik Abonelik Hemen Al Kontrolleru -59
-----------------------------
Tags:ANDPaketlerdeAylikAbonelikHemenAlKontrolu
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
* "10" saniye bekle
* "tümTekliflerYeni" elementinin koordinatlarına x="5" y="250" degerlerini ekleyerek tıkla
* Swipe times "1"
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ekPaketler" li elementi bul ve tıkla
* "4" saniye bekle
* "taraftarPaketleri" li elementi bul ve tıkla
* "taraftarPaketleri" elementinin koordinatlarına x="380" y="360" degerlerini ekleyerek tıkla
/* "sarıPaket" li elementi bul ve tıkla
* "9" saniye bekle
* "hemenAlReferans" elementinin koordinatlarına x="20" y="200" degerlerini ekleyerek tıkla
* "satınAlBtn"li elementi bulana kadar "4" kere swipe yap ve elementi bul

AND Paketlerde Aylik Abonelik Seçilebildiginin Kontrolu -63
----------------------------------
 Tags:ANDPaketlerdeAylikAbonelikSecilebildigininKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "10" saniye bekle
* "tümTekliflerYeni" elementinin koordinatlarına x="5" y="250" degerlerini ekleyerek tıkla
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ekPaketler" li elementi bul ve tıkla
* "taraftarPaketleri" li elementi bul ve tıkla
* "sarıPaket" li elementi bul ve tıkla

idlendirme eksik

AND Paketlerde Yillik Abonelik seçilebildiginin kontrolu -64
-------------------------------
 Tags:ANDPaketlerdeYillikAbonelikSecilebildigininKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir

* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla

* "tümTekliflerYeni"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "10" saniye bekle
* "tümTekliflerYeni" elementinin koordinatlarına x="5" y="250" degerlerini ekleyerek tıkla
/* "tümTeklifler" elementinin koordinatlarına x="2" y="2" degerlerini ekleyerek tıkla
 "tümTeklifler" li elementi bul ve tıkla
/* "tümTeklifler" li elementi bul ve tıkla
* "hazırKarttanFaturalıyaGeçiş" li elementi bul ve tıkla
* "yıllıkAbonelik" li elementi bul ve tıkla

AND Paket satin alma isleminde email ve sozlesme ekrani kontrolu -67
-----------------------------
 Tags:ANDPaketSatinAlmaIslemindeEmailVeSozlesmeEkraniKontrolu
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
* "3" saniye bekle
* "tümTeklifler" li elementi bul ve tıkla
* Swipe times "1"
* "ekPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ekPaketler" li elementi bul ve tıkla
* "4" saniye bekle
* "taraftarPaketleri" li elementi bul ve tıkla
/* "taraftarPaketleri" elementinin koordinatlarına x="380" y="360" degerlerini ekleyerek tıkla
* "sarıPaket" li elementi bul ve tıkla
* "9" saniye bekle
* "hemenAlReferans" elementinin koordinatlarına x="20" y="200" degerlerini ekleyerek tıkla
* "satınAlBtn"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "ePostaCheck" li element sayfada bulunuyor mu kontrol et
* "onBılgılendirmeFormuKontrol" li element sayfada bulunuyor mu kontrol et

// tüm teklifler butonu düzelince devreye sokulacak
Bana Uygun Teklifler Satin Alma İsleminde Sozlesme İçerik Kontrolu -74
----------------------------------------------------------------------------------------
 Tags: ANDBanaUygunTekliflerSatinAlmaIslemindeSozlesmeIcerikKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla

//tüm teklifler elemti bulunmadıgı için plandan çıkartıldı
AND Paketlerde Yillik Abonelik Hemen Al Kontrolleri -66
-----------------------------
 Tags:ANDPaketlerdeYillikAbonelikHemenAlKontrolleri
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "paketlerTabı" li elementi bul ve tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
 "tümTeklifler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
 "tümTeklifler" li elementi bul ve tıkla
* "10" saniye bekle
* "tümTekliflerYeni" elementinin koordinatlarına x="5" y="250" degerlerini ekleyerek tıkla
* Swipe times "1"
* "tumPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tumPaketler" li elementi bul ve tıkla
* "yeniPlatinumPaketler" li elementi bul ve tıkla
* "paketIcerik" li elementi bul ve tıkla
* "paketHemenAlBtn"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "paketHemenAlBtn" li element sayfada bulunuyor mu kontrol et

Paketlerde Yillik Abonelik Secildiginde Satin Al Buton Kontrol AND
---------------------------------
Tags:paketlerdeYillikAbonelikSecildigindeSatinAlButonKontrolAND
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "5" saniye bekle
* dijital magazaya gir
 "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "10" saniye bekle
* "tümTekliflerYeni" elementinin koordinatlarına x="5" y="250" degerlerini ekleyerek tıkla
 "tümTekliflerYeni" li elementi bul ve tıkla
* "tumPaketler"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "tumPaketler" li elementi bul ve tıkla
* "yeniPlatinumPaketler" li elementi bul ve tıkla
* "paketIcerik" li elementi bul ve tıkla
* "yıllıkAbonelik"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "yıllıkAbonelik" li elementi bul ve tıkla
* "yillikAbonelikAlanıSecimi" li elementi bul ve varsa dokun
* "paketHemenAlBtn"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "paketHemenAlBtn" li elementi bul ve tıkla
* "tamamButton" li element sayfada bulunuyor mu kontrol et


Paketlerde Yillik Abonelik Secildiginde Satin Al AND
------------------------------------
 Tags:paketlerdeYillikAbonelikSecildigindeSatinAlAND
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "2" saniye bekle
* "cıhazText" elementi bulunmuyorsa "kalanKullanimlarim" varsa "MAĞAZA SAYFASI AÇILMADI" uyarısı verilir
* "paketlerTabı" li elementi bul ve tıkla
 "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "tümPaketler" li elementi bul ve tıkla
* "tümTekliflerYeni"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "10" saniye bekle
* "tümTekliflerYeni" elementinin koordinatlarına x="5" y="250" degerlerini ekleyerek tıkla
 "tümTekliflerYeni" li elementi bul ve tıkla
* "tumPaketler"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "tumPaketler" li elementi bul ve tıkla
* "yeniPlatinumPaketler" li elementi bul ve tıkla
* "paketIcerik" li elementi bul ve tıkla
* "yıllıkAbonelik"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "yıllıkAbonelik" li elementi bul ve tıkla
* "yillikAbonelikAlanıSecimi" li elementi bul ve varsa dokun
* "paketHemenAlBtn"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "paketHemenAlBtn" li elementi bul ve tıkla
* "5" saniye bekle
* "paketSatinAlemailAlani" li elementi bul ve "g@gmail.com" değerini yaz
* Klavyeyi kapat
* "paketSatinAlemailAlaniAgain" li elementi bul ve "g@gmail.com" değerini yaz
* Klavyeyi kapat
* "iptalbtn" elementinin koordinatlarına x="10" y="-90" degerlerini ekleyerek tıkla
/* "paketSatinAlSozlesmeCheckBox" li elementi bul ve tıkla
* "paketSatinAlBtn" li elementi bul ve tıkla
* "iptalbtn" elementinin koordinatlarına x="10" y="-90" degerlerini ekleyerek tıkla

/* "paketSatinAlOnBilgilendirmeCheckBox" li  telefonun  "5" ve elementin "50" kordinatına göre tıkla
* "transferSatinAl" li elementi bul ve tıkla
* "paketSatinAlTamamPopup" li element sayfada bulunuyor mu kontrol et


Dergilik AND
-----------
 Tags:DergilikAND

* Giriş yapılmışsa çıkış yap
* "5" saniye bekle
* "uygulamalarTabı" li elementi bul ve tıkla
* "dergilik"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "dergilik" elementinin koordinatlarına x="500" y="10" degerlerini ekleyerek tıkla
* "Yükle" değerini sayfa üzerinde olup olmadığını kontrol et.


15.01.2020
249
AND Uygulamalar Aç Buton Adı Kontrolü
---------------------------------------
Tags:ANDUygulamalarAcButonAdiKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "uygulamalarTabı" li elementi bul ve tıkla
* Swipe times "7"
* "btn_Ac"li elementi bulana kadar "9" kere swipe yap ve elementi bul

16.01.2020
250,252,253,255
AND Uygulamalar Keşfet Tıklandığında Store Yönlendirme Kontrolu
---------------------------------
Tags:UygulamalarKesfetTiklandigindaStoreYonlendirmeKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "uygulamalarTabı" li elementi bul ve tıkla
* "btn_Kesfet"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* Click element by "btn_Kesfet"
* "GooglePlay" istenilen sayfaya geçilip geçilmediği kontrol edilir

251,254,256
AND Uygulamalar Aç Tıklandığında Uygulamanın Açıldığının Kontrolu
---------------------------------

Tags:ANDUygulamalarAcTiklandigindaUygulamaninAcildigininKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* dijital magazaya gir
* "uygulamalarTabı" li elementi bul ve tıkla
* "btn_Ac"li elementi bulana kadar "10" kere swipe yap ve elementi bul
* Click element by "btn_Ac"
* "uygulamalarTabı" li elementi bul varsa "geçilemedi" mesajını hata olarak göster
