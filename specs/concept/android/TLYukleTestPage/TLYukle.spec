Specification Heading
=====================
Created by sahabt on 12.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Logout TL Yukle
---------------
 Tags:AndroidLogoutTLYukle
* Kullanıcı girişi yapılmışsa çıkış yap
* TL yükle sayfasına gir
* Logout Kart Bilgilerini Gir


TL Yukle Kayitli Kart
---------------------
 Tags:AndroidTLYukleKayitliKart
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* TL yükle sayfasına gir
* Kayıtlı kart kontrol
* Kayıtlı kart bilgilerini doldur

TL Yukle Kredi Karti ile Odeme -7
------------------------------
 Tags:AndroidTLYukleKrediKartiileOdeme
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* TL yükle sayfasına gir
* Başka kart ile ödeme sayfasına gir
* Login Kart Bilgilerini Gir

Logout Hazir Kart Paket Yukle -3
-----------------------------
 Tags:AndroidLogoutHazirKartPaketYukle
* Kullanıcı girişi yapılmışsa çıkış yap
* Hazırkart paket yükle sayfasına gir
* Logout Kart Bilgilerini Gir

Hazir Kart Paket Yukle Kayitli Kart -9
-----------------------------------
 Tags:AndroidHazirKartPaketYukleKayitliKart
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Hazırkart paket yükle sayfasına gir
* Kayıtlı kart kontrol
* Kayıtlı kart bilgilerini doldur

Hazir Kart Paket Yukle Kredi Karti ile Odeme
--------------------------------------------
 Tags:AndroidHazirKartPaketYukleKrediKartiileOdeme
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Hazırkart paket yükle sayfasına gir
* Kayıtsız kredi kartı ile ödeme sayfasına gir
* Login Kart Bilgilerini Gir

Logout Cepten Internet -4
----------------------
 Tags:AndroidLogoutCeptenInternet
* Kullanıcı girişi yapılmışsa çıkış yap
* Cepten internet Sayfasına Gir
* Logout Kart Bilgilerini Gir

Cepten Internet Kayitli Kart -10
----------------------------
 Tags:AndroidCeptenInternetKayitliKart
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Cepten internet Sayfasına Gir
* Kayıtlı kart kontrol
* Kayıtlı kart bilgilerini doldur

/cepten internet kısa bir süreligine iptal oldu bu yuzden senaryo askıya alındı
Cepten Internet Kredi Karti ile Odeme
-------------------------------------
 Tags:AndroidCeptenInternetKrediKartiileOdeme
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
//* Cepten internet Sayfasına Gir
//* Başka kart ile ödeme sayfasına gir
//* Login Kart Bilgilerini Gir

Logout Bilgisayardan Internet
-----------------------------
 Tags:AndroidLogoutBilgisayardanInternet
* Kullanıcı girişi yapılmışsa çıkış yap
* Vınn internet sayfasına gir
* Logout Kart Bilgilerini Gir

Bilgisayardan Internet Kayitli Kart
-----------------------------------
 Tags:AndroidBilgisayardanInternetKayitliKart
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Vınn internet sayfasına gir
* Kayıtlı kart kontrol
* Kayıtlı kart bilgilerini doldur

Bilgisayardan Internet Kredi Karti ile Odeme
--------------------------------------------
 Tags:AndroidBilgisayardanInşifreternetKrediKartiileOdeme
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Vınn internet sayfasına gir
* Başka kart ile ödeme sayfasına gir
* Login Kart Bilgilerini Gir

Prepaid hatla loginli iken detay butonuna tıklayıp detayların açılması
---------------------------------------------------------------------------
 Tags:prepaidHatlaLoginleDetay
* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "detayPrepaid"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "detayPrepaid" li elementi bul ve tıkla
* "5" saniye bekle
* "dogrulamaKoduEkranı" li element sayfada bulunuyor mu kontrol et

TL Durumum Anasayfa TL Yukle Butonu Aktif Kontrolu Prepaid AND -17
-------------------------------------------
Tags: ANDTLDurumumAnasayfaTLYukleButonuAktifKontroluPrepaid
* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Vınn internet sayfasına gir


sadada
----
* "30" saniye bekle
* son kullanma tarihi gir

