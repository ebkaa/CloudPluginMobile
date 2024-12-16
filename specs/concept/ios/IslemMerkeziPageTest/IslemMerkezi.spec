Specification Heading
=====================
Created by nurgul on 8.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

382
Islemlerim Karti Kontrolu
-------------------------
 Tags:IslemlerimKartiKontrolu
* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Dinamik kartları kapat
* "tumIslemlerim" li elementi bulana kadar swipe et
* "tumIslemlerim" li elementi bul ve tıkla
* "yurtDısıIslemleri" li elementi bulana kadar swipe et
* "yurtDısıIslemleri" li elementi bul yoksa "Yurtdışı işlemleri bulunamadı" mesajını hata olarak göster
 "yurtDısıIslemleri"li elementi bulana kadar "5" kere swipe yap ve elementi bul
 "10" saniye bekle

383
Islemlerim Karti Tum Islemlerim Kontrolu
----------------------------------------
 Tags:IslemlerimKartiTumIslemlerimKontrolu
 Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "tumIslemlerim"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "tumIslemlerimBackButton" li elementi bul yoksa "TUM ISLEMLERİM SAYFASINA GİRİLEMEDİ" mesajını hata olarak göster

386
IOS Islemlerim Karti Hat Islemleri Kontrolu
----------------------------------------
 Tags:IOSIslemlerimKartiHatIslemleriKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "hatIslemleri"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "hatIslemleri" li elementi bul ve tıkla
* "10" saniye bekle
* "HatAyarlarımText" li elementi bul yoksa "HAT AYARLARIM SAYFASINA GİRİLEMEDİ" mesajını hata olarak göster

385
Islemlerim Karti Cagri Ayarlarim Kontrolu
-----------------------------------------
 Tags:IslemlerimKartiCagriAyarlarimKontrolu

* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "tumIslemlerim" li elementi bulana kadar swipe et
* "tumIslemlerim" li elementi bul ve tıkla
* "cagriAyarlari" li elementi bulana kadar swipe et
* "cagriAyarlari" li elementi bul ve tıkla
* "cagriAyarlariText" li elementi bul yoksa "ÇAGRI AYARLARIM SAYFASINA GİRİLEMEDİ" mesajını hata olarak göster

kapsam dahilinde
Islemlerim Karti Yurt Disi Islemleri Kontrolu
---------------------------------------------
 Tags:IslemlerimKartiYurtDisiIslemleriKontrolu
* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim" li elementi bulana kadar swipe et
* "tumIslemlerim" li elementi bul ve tıkla
* "yurtDısıIslemleri" li elementi bulana kadar swipe et
* "yurtDısıIslemleri" li elementi bul ve tıkla
* "YurtDışıAyarlarımText" li elementi bul yoksa "YURTDIŞI AYARLARIM SAYFASINA GİRİLEMEDİ" mesajını hata olarak göster

471
Islemlerim Karti Ek Paket Islemleri Kontrolu
--------------------------------------------
 Tags:IslemlerimKartiEkPaketIslemleriKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "ekPaketIslemlerı"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "ekPaketIslemlerı" li elementi bul ve tıkla
* "8" saniye bekle
* "internetEkPaketleriText" li elementi bul yoksa "EKPAKET İŞLEMLERİ SAYFASINA GİRİLMEDİ" mesajını hata olarak göster

Islemlerim Karti Siparislerim Kontrolu -472
--------------------------------------
 Tags:IslemlerimKartiSiparislerimKontrolu

* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tum işlemlerim sayfasına git
 "siparislerim"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "siparislerim" li elementi bulana kadar swipe et
* "siparislerim" li elementi bul ve tıkla
* "3" saniye bekle
* "siparişlerimText" li elementi bul yoksa "SİPARİŞLERİM SAYFASINA GİREMEDİ" mesajını hata olarak göster

389
Islemlerim Karti Paycell ve Kayitli Kartlarim Kontrolu
------------------------------------------------------
 Tags:IslemlerimKartiPaycellveKayitliKartlarimKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tum işlemlerim sayfasına git
* "tumIslemlerım-PaycellveKayıtlıKartlarım"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "9" saniye bekle
* "paycellVeKayıtlıKartlarımText" li elementi bul yoksa "PAYCELL VE KAYITLI KARTLARIM SAYFASINA GİREMEDİ" mesajını hata olarak göster

388
Islemlerim Karti Fatura Islemlerim Kontrolu
-------------------------------------------
 Tags:IslemlerimKartiFaturaIslemlerimKontrolu

* Numara:"Faturalı" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tum işlemlerim sayfasına git
* "faturaIslemlerım" li elementi bulana kadar swipe et
* "faturaIslemlerım" li elementi bul ve tıkla
* "4" saniye bekle
* "faturaAyarlarıText" li elementi bul yoksa "FATURA AYARLARI SAYFASINA GİREMEDİ" mesajını hata olarak göster

Islemlerim Puk Kodu Kontrolu
----------------------------
 Tags:IslemlerimPUKKoduKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tum işlemlerim sayfasına git
* "hatIslemleri" li elementi bul ve tıkla
* "pukKodu" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "PUK" değerini sayfa üzerinde olup olmadığını kontrol et.

390
Islemlerim Karti Salla Kazan Kontrolu
-------------------------------------
 Tags:IslemlerimKartiSallaKazanKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "sallaKazan" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "sallakazan" değerini sayfa üzerinde olup olmadığını kontrol et.

393
Islemlerim Karti SMS Ayarlarim Kontrolu
---------------------------------------
 Tags:IslemlerimKartiSMSAyarlarimKontrolu

* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* Tum işlemlerim sayfasına git
* "smsAyarlarim" li elementi bulana kadar swipe et
* "smsAyarlarim" li elementi bul ve tıkla
* "smsAyalarimText" li elementi bul yoksa "SMS AYARLARI sayfası bulunamadı" mesajını hata olarak göster

391
Islemlerim Karti Akilli Fatura Kampanyasi Kontrolu
--------------------------------------------------
 Tags:IslemlerimKartiAkilliFaturaKampanyasiKontrolu

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "tumIslemlerim"li elementi bulana kadar "8" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "5" saniye bekle
* "akıllıFaturaKampanyası" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "Akıllı Fatura" değerini sayfa üzerinde olup olmadığını kontrol et.

395
Islemlerim Karti DortBucukG Aboneligim Kontrolu
-----------------------------------------------
 Tags:IslemlerimKartiDortBucukGAboneligimKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "dortBucukG" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "İNTERNET" değerini sayfa üzerinde olup olmadığını kontrol et.

394
Islemlerim Karti Guvenli Internet Kontrolu
------------------------------------------
 Tags:IslemlerimKartiGuvenliInternetKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tum işlemlerim sayfasına git
* Güvenli internet sayfasına git

396
Islemlerim Karti Faturaliya Gecis Kontrolu
------------------------------------------
 Tags:IslemlerimKartiFaturaliyaGecisKontrolu
* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "faturaliyaGecis"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "faturaliyaGecis" li elementi bul ve tıkla
* "5" saniye bekle
* "faturaliyaGecisKontrol" li element sayfada bulunuyor mu kontrol et


Islemlerim Karti Paycell Kartlarim Sayfasi Kayitli Paycell Kartinin Olmamasi -474
----------------------------------------------------------------------------
 Tags:IslemlerimKartiPaycellKartlarimSayfasiKayitliPaycellKartininOlmamasi
* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
"paycellveKayıtlıKartlarım" li elementi bul ve tıkla
"5" saniye bekle
* "tumIslemlerim" li elementi bul ve tıkla
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "paycellKartlarimYeni" li elementi bul ve tıkla
* "UygulamaIndir" li elementi bul yoksa "buton bulunamadı" mesajını hata olarak göster


Islemlerim Karti Paycell Kartlarim Sayfasi Kayitli Paycell Kartinin Olmasi -475
--------------------------------------------------------------------------
 Tags:IslemlerimKartiPaycellKartlarimSayfasiKayitliPaycellKartininOlmasi

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "5" saniye bekle
* "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* İçeriği "Paycell Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "Bakiye" değerini sayfa üzerinde olup olmadığını kontrol et.


Islemlerim Karti Kredi Kartlarim Sayfasi Kayitli Kredi Kartinin Olmamasi -36
------------------------------------------------------------------------
 Tags:IslemlerimKartiKrediKartlarimSayfasiKayitliKrediKartininOlmamasi

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "2" kere aşağıya kaydır
* İçeriği "Kredi Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Hide keyboard
* "krediKartiEkleKartNo" li elementi bul ve "5440786728974016" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
*  Hide keyboard
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "936" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementin  merkezine tıkla
* "50","50" oranlarından "50","20" oranlarına "1" kere swipe et
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "5" saniye bekle
* "kartDogrulamaSayfası" li element sayfada bulunuyor mu kontrol et


Islemlerim Karti Kredi Kartlarim Sayfasi Kayitli Kredi Kartinin Olmasi -476
----------------------------------------------------------------------
 Tags:IslemlerimKartiKrediKartlarimSayfasiKayitliKrediKartininOlmasi

 Numara:"5305713947" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
 "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "2" kere aşağıya kaydır
* İçeriği "Kredi Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "kartEklePopup" elementi bulunmuyorsa "krediKartiKaydetme" varsa "KAYITLI KREDİ KARTI BULUNMAMAKTADIR" uyarısı verilir
* "Kartı sil" değerini sayfa üzerinde olup olmadığını kontrol et.


Kullanimlarim Karti Kontrolu -477
----------------------------
 Tags:KullanimlarimKartiKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "kullanımTipiDropdownIkonu-kapalı" li elementin  merkezine tıkla
* "dropdownSMSLabel" li elementi bul ve tıkla
* "SMS" değerini sayfa üzerinde olup olmadığını kontrol et.
*  "SOL" yönüne swipe et
*  "SOL" yönüne swipe et
*  "SAĞ" yönüne swipe et

Kullanim Karti Paket Al Butonu
------------------------------
 Tags:KullanimKartiPaketAlButonu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "paketAlButonu"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "paketAlButonu" li elementi bul yoksa "buton bulunamadı" mesajını hata olarak göster

317
Kullanimlarim Karti Theatre Mod
-------------------------------
 Tags:KullanimlarimKartiTheatreMod

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* İçeriği "İNTERNET" e eşit olan elementli bul ve tıkla
* "2" saniye bekle
* "Paketler" değerini sayfa üzerinde olup olmadığını kontrol et.

369
Faturalarım Alanı Kontrol
-------------------------
 Tags:FaturalarimAlaniKontrolu

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dropdowmios"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "dropdowmios" li elementi bul ve tıkla
* "faturaDetay" li elementi bul yoksa "doğru sayfa değil" mesajını hata olarak göster
* "faturalarımAySecimi" li elementi bul ve varsa tıkla
* "faturaAyi" li elementi bul ve tıkla
* "faturaTutar" li elementi bul yoksa "bulunamadı" mesajını hata olarak göster


/* "30" saniye bekle
/* "faturaIncele" li elementi bul ve tıkla
/* "3" saniye bekle
/* "dropdownSecenek" li elementi bul ve tıkla
/* "2" saniye bekle
/* "dropdowmios" li elementi bul ve tıkla
/* "faturaKalemi" li elementi bulana kadar swipe et ve tıkla
/* "2" saniye bekle
/* "faturaDetay" li elementin  merkezine tıkla
/* "5" saniye bekle
/* "fıltreDetay" li elementi bul ve tıkla
/* "3" saniye bekle
/* "detaySecim" li elementi bul ve tıkla
/* "5" saniye bekle
/* "fıltreDetayıkı" li elementi bul ve tıkla
/* "3" saniye bekle
/* "detaySecimIkı" li elementi bul ve tıkla
/* "5" saniye bekle
/* geri butonuna bas
/* "2" saniye bekle
/* "FATURALARIM" değerini sayfa üzerinde olup olmadığını kontrol et.
/* "5" saniye bekle



Kredi Kartı Bilgileri Ekranında Ad Soyad Alanı Kontrolu -30
--------------------------------------------------
Tags:KrediKartBilgileriAdSoyadKontrolu

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Tum işlemlerim sayfasına git
"paycellveKayıtlıKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bulana kadar swipe et
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleKartNo" li elementi bul ve "5440786728974016" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
* Klavyeyi kapat
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "936" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementi bul ve tıkla
* "KrediKartKaydetTamam"li elementi bulana kadar "1" kere swipe yap ve elementi bul
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "adSsoyadEklePopup" li element sayfada bulunuyor mu kontrol et

Kredi Kartı Bilgileri Ekranında Kart numarası Alanı Kontrolu -31
----------------------------------------------------
Tags:KrediKartNumaraKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartNo" li elementi bul ve "54407867289740" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
* Klavyeyi kapat
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "936" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementi bul ve tıkla
* "KrediKartKaydetTamam"li elementi bulana kadar "1" kere swipe yap ve elementi bul
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "kartNoEklePopup" li element sayfada bulunuyor mu kontrol et

Kredi Kartı Bilgileri Ekranında Son Kullanma Tarihi Alanı Kontrolu -32
--------------------------------------------------------
Tags:KrediKartSonKullanmaTarihiKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartNo" li elementi bul ve "5440786728974016" değerini yaz
* Klavyeyi kapat
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "936" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementi bul ve tıkla
* "KrediKartKaydetTamam"li elementi bulana kadar "1" kere swipe yap ve elementi bul
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "kartTarıhEklePopup" li element sayfada bulunuyor mu kontrol et

pass aldı
Kredi Kartı Bilgileri Ekranında CVV Alanı Kontrolu -33
----------------------------------------
Tags:KrediKartCvvAlaniKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartNo" li elementi bul ve "5440786728974016" değerini yaz
* Klavyeyi kapat
* "2" saniye bekle
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementi bul ve tıkla
* "KrediKartKaydetTamam"li elementi bulana kadar "1" kere swipe yap ve elementi bul
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "kartCvvEklePopup" li element sayfada bulunuyor mu kontrol et


Kredi Kartı Bilgileri Ekranında Kredi Kartını Kaydet Checkbox Kontrolu -34
----------------------------------------------------------
Tags:KrediKartCheckboxKontrol

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartNo" li elementi bul ve "5440786728974016" değerini yaz
* Klavyeyi kapat
* "2" saniye bekle
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "936" değerini yaz
* Klavyeyi kapat
* "KrediKartKaydetTamam"li elementi bulana kadar "1" kere swipe yap ve elementi bul
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "kartCheckboxTiklaPopup" li element sayfada bulunuyor mu kontrol et


Kredi Kartı Bilgileri Ekranında Kart Scan Butonu Kontrolu -35
--------------------------------------------
Tags:KrediKartiScanButonuKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Klavyeyi kapat
* "kartScanBtn" li elementi bul ve tıkla
* "3" saniye bekle
* "ızınVer" li elementi bul ve varsa tıkla

Kredi Kartı Bilgileri Kredikartı silme kontrol -42
--------------------------------------------
Tags:IosKrediKartiBilgileriKredikartisilmekontrol

* Numara:"5305713947" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla

Kayıtlı Kredi Kartlarım Sayfası Yeni Kart Ekle Butonu Kontrolu -29
----------------------------------------------
Tags:KrediKartlarimYeniKartEkleKontrolu

* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bulana kadar swipe et
* "tumIslemlerim" li elementi bul ve tıkla
 "paycellveKayıtlıKartlarım"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bulana kadar swipe et
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "KrediKartlarım"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "KrediKartlarım" li elementi bul ve tıkla
* "3" saniye bekle
* "80","60" oranlarından "80","30" oranlarına "1" kere swipe et
* "yenıKredıKartEkle" elementi bulunmuyorsa "krediKartiKaydetmeText" varsa "KAYITLI KREDİ KARTI BULUNMAMAKTADIR" uyarısı verilir
* "yenıKredıKartEkle" li elementi bul ve tıkla
 "krediKartiKaydetme" li elementi bulana kadar swipe et
 "krediKartiTamamBtn" li elementi bulana kadar swipe et
* "2" saniye bekle

Kayıtlı Paycell Kart Olması Paycell App Lınk Kontrolu -46
----------------------------------------------
Tags:PaycellAppLinkKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* İçeriği "Paycell Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "50","60" oranlarından "50","30" oranlarına "1" kere swipe et
* "1" saniye bekle
* "paycellApp" li elementi bul ve tıkla
* "3" saniye bekle


Kayıtlı Paycell Kart Olması Paycell App Acilmasi Kontrolu
--------------------------------------------------
Tags:PaycellAppAcilmasiKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* İçeriği "Paycell Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "50","60" oranlarından "50","30" oranlarına "1" kere swipe et
* "1" saniye bekle
* "paycellApp" li elementi bul ve tıkla
* "3" saniye bekle
* "ızınVer" li elementi bul ve varsa tıkla
* "3" saniye bekle


Kayıtlı Paycell Kart Olmaması Paycell App Lınk Kontrolu
----------------------------------------------------
Tags:PaycellKartOlmamasiAppLinkKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* İçeriği "Paycell Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "50","60" oranlarından "50","30" oranlarına "1" kere swipe et
* "1" saniye bekle
* "paycellAppIndır" li elementi bul ve tıkla
* "3" saniye bekle


Kayıtlı Paycell Kart Olmaması Paycell App Acilmasi Kontrolu -44
--------------------------------------------
Tags:PaycellKartOlmamasiAppAcilmasiKontrolu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* İçeriği "Paycell Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "50","60" oranlarından "50","30" oranlarına "1" kere swipe et
* "1" saniye bekle
* "paycellAppIndır" li elementi bul ve tıkla
* "5" saniye bekle
* "ızınVer" li elementi bul ve varsa tıkla
* "3" saniye bekle


Bakiye Yukleme Miktarının Belirtilen Aralık Dışında Girilememesi -51
------------------------------------------------
Tags:BelliAraliktaBakiyeYuklemeKontrol

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* İçeriği "Paycell Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "bakıyeYukle" elementi bulunmuyorsa "paycellAppIndır" varsa "KAYITLI KART BULUNMAMAKTADIR" uyarısı verilir
* "bakıyeYukle" li elementi bul ve tıkla
* "BakıyeTutar" li elementi bul ve "5" değerini yaz
* Klavyeyi kapat
* "3" saniye bekle
* "80","50" oranlarından "80","30" oranlarına "1" kere swipe et
* "bakıyeDevam" li elementi bul ve tıkla
* "3" saniye bekle
* "bakıyeLımıtPopup" li element sayfada bulunuyor mu kontrol et

312
Internet Ek Paketinin Goruntulenmesı Prepaid
-----------------------------------
 Tags:InternetEkPaketininGoruntulenmesiPrepaid

* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "ekPaketIslemlerı" li elementi bulana kadar swipe et
* "ekPaketIslemlerı" li elementi bul ve tıkla
* "internetEkPaketleriText" li elementi bul varsa "başarısız" mesajını hata olarak göster


313
Internet Ek Paketinin Goruntulenmesı Postpaid
----------------------------------------
 Tags:internetEkPaketininGoruntulenmesiPostpaid

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "ekPaketIslemlerı"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "ekPaketIslemlerı" li elementi bul ve tıkla
* "5" saniye bekle
* "İnternet Ek Paketleri" değerini sayfa üzerinde olup olmadığını kontrol et.



Internet Ek Paketinin Goruntulenmesı Hıbrıt
-------------------------------------
 Tags:internetEkPaketininGoruntulenmesiHibrit

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "ekPaketIslemlerı"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "ekPaketIslemlerı" li elementi bul ve tıkla
* "5" saniye bekle
* "internetEkPaketleriText" li elementi bul yoksa "bulunamadı" mesajını hata olarak göster


Basarili Otomatik Odeme Talimati Verilebilmesi Postpaid -21
-------------------------------------------
 Tags:basariliOtomatikOdemeTalimatiVerilmesiPostpaid

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "2" saniye bekle
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "faturaAyarlarım"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "faturaAyarlarım" li elementi bul ve tıkla
* "faturaOtomatikOdemeTalimati" li elementi bul ve tıkla
* "2" saniye bekle
* "faturaOtomatıkOdemeTalımatıNumaraSecimAlani" li  telefonun  "70" ve elementin "50" kordinatına göre tıkla
* "50","70" oranlarından "50","20" oranlarına "1" kere swipe et
* "1" saniye bekle
* kayıtlı kart varsa odeme yap
* "faturaOtomatıkOdemeCheckBox" li element varsa  "50" "50" koordinatına tıkla
* "otomatıkOdemeDevamEt" li elementi bul ve tıkla
* "2" saniye bekle
* "otomatıkOdemeDevamEt" li elementi bul varsa "sayfaya geçilemedi" mesajını hata olarak göster

hediye kutum log-in
---------
 Tags:iosHediyeKutumKontrol
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve tıkla
* "tarihçe" elementinin koordinatlarına x="3" y="3" degerlerini ekleyerek tıkla
* "ayricaliklar" elementinin koordinatlarına x="3" y="3" degerlerini ekleyerek tıkla
* "keşfet" li element sayfada bulunuyor mu kontrol et


Logout Search Control
------------------
 Tags:logoutSearchControl

* Kullanıcı girişi yapılmışsa çıkış yap
* "LogoutaramaButonu" li elementi bul ve tıkla
* "aramaYapText" li elementi bul ve "kulaklık" değerini yaz


Logout Notification Control
----------------------
 Tags: logoutNotificationControl

* Kullanıcı girişi yapılmışsa çıkış yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "vazgec" li elementi bul ve tıkla


Sık Sorulan Sorular Kontrol
-------------------------
 Tags:sikSorulanSorularKontrol

* Kullanıcı girişi yapılmışsa çıkış yap
* "paketlerTabı" li elementi bul ve tıkla
* Swipe times "6"
* "incele" li elementi bul ve tıkla
* Swipe times "1"
* "sıkcaSorulanSorular"li elementi bulana kadar "10" kere swipe yap ve elementi bul



Ios Postpaid hatla Basarili Otomatik Odeme Talimati Verilebilmesi
------------------------------------------------
Tags:IosAndroidOtomatikYuklemeTalimatPostPaid
*"1" saniye bekle
IosAndroidOtomatikYuklemeTalimatPostPaid
/* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
/* "faturalarımAyarlarBtn"li elementi bulana kadar "4" kere swipe yap ve elementi bul
    /* "1" saniye bekle
/* "faturalarımAyarlarBtn" li elementi bul ve tıkla
    /* "4" saniye bekle
/* "otomatikOdemeTalimati" li elementi bul ve tıkla
    /* "5" saniye bekle
    /* sayfadaki "50" "40"  alana tıkla
* "10" saniye bekle
* "faturaTalımatAdi"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "faturaTalımatAdi" elementinin koordinatlarına x="10" y="35" degerlerini ekleyerek tıkla ve "test" yaz
* Hide keyboard
* "1" kere yukarı doğru kaydır
*"faturaGuvenlıkKodu" li elementi bul ve "458" değerini yaz
* Hide keyboard
* "2" kere yukarı doğru kaydır
* "OtomatikOdemeOnay" li elementi bul ve tıkla
* "OtomatikOdemeTamam" li elementi bul ve tıkla
* "3" kere yukarı doğru kaydır
* "DevamEtOtomatikOdemeBtn" li elementi bul ve tıkla
* "1" saniye bekle

Ios Paycell Başarılı Yükleme (Login) -56
------------------------------------------------
Tags:IosPaycellBasariliYuklemeLogin

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* Swipe times "1"
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "10" kere swipe yap ve elementi bul
* "paycellveKayıtlıKartlarım" li elementi bul ve tıkla
* "paycellKartlarım" li elementi bul ve tıkla
* "bakiyeYükleBtn" li elementi bul ve tıkla
* "yuklemekİstediginizMiktarıGiriniz" li elementi bul ve "10" değerini tek tek yaz
* Hide keyboard
* "DevamBtn" li elementi bul ve tıkla
* "2" saniye bekle
* "devamBtnPopUp" li elementi bul ve tıkla
* "cvvText" li elementi bul ve "458" değerini yaz
* "payTamamBtn" li elementi bul ve tıkla
* "kartDogrulamaSayfası" li element sayfada bulunuyor mu kontrol et


Ios Kayıtlı Kredi Kartı ile Fatura Ödeme ( Login ) -26
-------------------------------------------------------------------------
Tags:IosKayitliKrediKartiileFaturaOdemeLogin
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Fatura ödeme

Ios Kayıtsız Kredi Kartı ile Fatura Ödeme (Login) -13
--------------------------------------------------------------------------------------------------
Tags:IosKayitsizKrediKartiileFaturaOdemeLogin

* Numara:"5305713947" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Fatura ödeme sayfasına gir ve kontro et
//* "hemenOdeButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "hemenOdeButonu" li elementi bul ve tıkla
//* "baskaKrediKartıİleÖde" li elementi bul ve tıkla
//* "krediKartıİsim" li elementi bul ve "ümit gök" değerini yaz
//* "krediKartıNumarası" li elementi bul ve "5440 7867 2897 4016" değerini yaz
//* "krediKartıSonKullanmaTarihi" li elementi bul ve tıkla
//* "30","90" oranlarından "30","97" oranlarına "6" kere swipe et
//* "75","90" oranlarından "75","85" oranlarına "2" kere swipe et
//* "2" saniye bekle
//* "tarihAlanıtamamButonu" li elementi bul ve tıkla
//* "3" saniye bekle
//* "krediKartıCvv" li elementi bul ve "936" değerini yaz
//* "krediKartıHemenÖde" li elementi bul ve tıkla
//* "garanti3DGüvenlik" li element sayfada bulunuyor mu kontrol et


Kurumsal Logın GiftBox Goruntulenmemesi Kontrol
------------------------------------
 Tags:iosKurumsalLoginGiftBoxGoruntulenmemesiKontrol

 Kullanıcı girişi yapılmışsa çıkış yap
 "anasayfaGirisYapButonu" li elementi bul ve tıkla
 iOS 1466 ile Giris Yap
 "5376441466" değerini sayfa üzerinde olup olmadığını kontrol et.
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" elementi sayfada yer almıyor "bildirimlerButonu" yer alıyorsa "Kurumsal Loginde GiftBox Bulunmamaktadır" mesajı verilir



Tum Paketler Webview Kontrol iOS -69
----------------
 Tags:iOStumPaketlerWebviewKontrol

 Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "magazaButonu" li elementi bul ve tıkla
* "paketlerTabı" li elementi bul ve tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla

* "tümPaketler" li elementi bul ve tıkla
* "4" saniye bekle
 "tümTeklifler" li elementi bul ve tıkla
* "tümPaketler" li elementi bul varsa "tıklanmadı" mesajını hata olarak göster


Bana Uygun Lifecell Mega Mix PaketHemen Al Buton Kontrol iOS -75
--------------------------------
 Tags: IOSbanaUygunLifecellMegaMixPaketHemenAlButonKontrol
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "magazaButonu" li elementi bul ve tıkla
* "paketlerTabı" li elementi bul ve tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler" li elementi bul ve tıkla
* "tümTeklifler"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "tümTeklifler" li elementi bul ve tıkla
* "faturaliLifecell" li elementi bul ve tıkla
* "lifecellPaket" li elementi bul ve tıkla
* "lifecellMixPaket" li elementi bul ve tıkla
* "Hemen Al" değerini sayfa üzerinde olup olmadığını kontrol et.


Login Evden Cebe Transfer Postpaid -12
-------------------
 Tags:loginEvdenCebeTransferPostpaid

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "evdenCebeTransfer" li elementi bulana kadar swipe et
* "evdenCebeTransfer" li elementi bul ve tıkla
 "EvdenCebeGB" li elementi bul ve tıkla
* "evdenCepHemenAlBtn"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "evdenCepHemenAlBtn" li elementi bul ve tıkla


Login Tablet Vinn Internet Prepaid -11
------------------------
 Tags:loginTabletVinnInternetPrepaid
* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Vınn internet sayfasına gir
* "baskaKartIleOdeButonu" li elementi bulana kadar swipe et ve tıkla
* iOS Login Kart Bilgilerini Gir
* "3" saniye bekle
* "siparişOnayıÖdeme" elementinin koordinatlarına x="-7" y="0" degerlerini ekleyerek tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.

pass alındı 16 mart
Logout Evden Cebe Transfer Postpaid -5
-------------------
 Tags:logoutEvdenCebeTransferPostpaid
* Kullanıcı girişi yapılmışsa çıkış yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "evdenCebeTransfer" li elementi bul ve tıkla
* "EvdenCebeGB" li elementi bul ve tıkla
* "50","50" oranlarından "50","30" oranlarına "1" kere swipe et
* "evdenCepHemenAlBtn"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "evdenCepHemenAlBtn" li elementi bul ve tıkla
* "evdenCebeGsmNumber" li elementi bul ve tıkla
*"evdenCebeGsmNumber" li elementi bul, temizle ve "5354556825" değerini yaz
* "evdenCebeGsmŞifre" li elementi bul ve tıkla
* "evdenCebeGsmŞifre" li elementi bul, temizle ve "530530" değerini yaz
* Klavyeyi kapat
* "evdenCebeGirisyapBtnn" li elementi bul ve tıkla
* "logoutTLGSMtext" li elementi bul ve "5307458832" değerini yaz
* Klavyeyi kapat
* Swipe times "3"
* "transferGmail" li elementi bul, temizle ve "g@gmail.com" değerini yaz
* Klavyeyi kapat
* "transferGmailIki" li elementi bul ve tıkla
* "transferGmailIki" li elementi bul, temizle ve "g@gmail.com" değerini yaz
* Klavyeyi kapat
* "toolbarDoneButtonReferans" elementinin koordinatlarına x="-20" y="0" degerlerini ekleyerek tıkla
* "transferOnayla" li elementi bul ve tıkla
* "transferOnaylaCheckBoxRef" elementinin koordinatlarına x="10" y="0" degerlerini ekleyerek tıkla
* "transferSatinAl" li elementi bul ve tıkla
* "transferTalebTamamBtn" li element sayfada bulunuyor mu kontrol et


Logout Tablet Vinn Internet Prepaid -5
------------------------
 Tags:logoutTabletVinnInternetPrepaid

* Kullanıcı girişi yapılmışsa çıkış yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "vinnInternet" li elementi bul ve tıkla
 "EvdenCebeGB" li elementi bul ve tıkla
* "logoutVinnTLGSMtext" li elementi bul ve "5307385720" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "krediKartıIsimAlanı" li elementi bul ve "Turkcell Deneme" değerini yaz
*  Hide keyboard
* "kartNumarasıAlanı" li elementi bul ve "5440786728974016" değerini yaz
*  Hide keyboard
* "kartSonKullanmaTarihiAlanı" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
*  Hide keyboard
* "buKartileOdemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* "logoutVinnTLAdtext" li elementi bul ve "Turkcell Deneme" değerini yaz
* "logoutTabletTLGSMtext" li elementi bul ve "5354556825" değerini yaz
*  Hide keyboard
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "cvvAlanı" li elementi bul ve "936" değerini yaz
* "cvvBilgileri-mailAlanı" li elementi bul ve "g@gmail.com" değerini yaz
*  Hide keyboard
* "3" saniye bekle
/* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "siparişOnayıÖdeme" elementinin koordinatlarına x="-7" y="0" degerlerini ekleyerek tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.



Uygun Satin Alabilecegim Teklifler Sozlesme Kontrolu
--------------------------------
 Tags:uygunSatinAlabilecegimTekliflerSozlesmeKontroluIOS

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "magazaButonu" li elementi bul ve tıkla
* "paketlerTabı" li elementi bul ve tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "tümPaketler" li elementi bul ve tıkla
* "tümTeklifler"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "tümTeklifler" li elementi bul ve tıkla
* "faturaliLifecell" li elementi bul ve tıkla
* "lifecellPaket" li elementi bul ve tıkla
* "lifecellMixPaket" li elementi bul ve tıkla
* "paketHemenAlBtn"li elementi bulana kadar "3" kere swipe yap ve elementi bul
* "paketHemenAlBtn" li elementi bul ve tıkla
* "paketSecBtn" li elementi bul ve tıkla
* "paketDevamEt" li elementi bul ve tıkla
* "paketDevamEt2" li elementi bul ve tıkla



Otomatik Odeme Talimatinin iptal Edilmesi Pospaid -23
----------------------------------------
 Tags:otomatikOdemeTalimatininIptalEdilmesiPospaid

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "faturalarımAlani" li  telefonun  "85" ve elementin "30" kordinatına göre tıkla
* "faturaAyarlarım"li elementi bulana kadar "5" kere swipe yap ve elementi bul
 Swipe times "1"
* "faturaAyarlarım" li elementi bul ve tıkla
* "faturaOtomatikOdemeTalimati" li elementi bul ve tıkla
* "btn_talimatIptal" li elementi bul yoksa "başarısız" mesajını hata olarak göster





apatmaIkonu" li elementi bul ve varsa tıkla
/* "faturalarımAlani" li  telefonun  "85" ve elementin "30" kordinatına göre tıkla
/* "faturaOtomatıkOdemeTalımatı" li elementi bul ve tıkla
/* "2" saniye bekle
/* "faturaOtomatıkOdemeTalımatıNumaraSecimAlani" li  telefonun  "70" ve elementin "50" kordinatına göre tıkla
/* "50","70" oranlarından "50","20" oranlarına "1" kere swipe et
/* "1" saniye bekle
/* kayıtlı kart varsa odeme yap
/* "faturaOtomatıkOdemeCheckBox" li element varsa  "50" "50" koordinatına tıkla
/* "otomatıkOdemeDevamEt" li elementi bul ve tıkla
/* "3D" değerini sayfa üzerinde olup olmadığını kontrol et.
//otomatık odeme talimatlı no gelince devamı yazılacak

370
Sol Fatura Odeme -26
-----------------------------------
 Tags:solFaturaOdeme
* IOS SuperOnline Hesabı İle Giriş
* "faturayıInceleButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
/* "faturayıInceleButonu" li elementi bul ve tıkla
* "hemenOdeButonu" elementi bulunmuyorsa "faturayıInceleButonu" varsa "Ödenmemiş Fatura bulunmamaktadır!" uyarısı verilir
* "hemenOdeButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Turkcell Test" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartNo" li elementi bul ve "5440786728974016" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "5" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2021" değerini yaz
* Klavyeyi kapat
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "936" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementin  merkezine tıkla
* "50","50" oranlarından "50","20" oranlarına "1" kere swipe et
* "krediKartıHemenÖde" li elementi bul ve tıkla
* "5" saniye bekle
* "kartDogrulamaSayfası" li element sayfada bulunuyor mu kontrol et


363
IOS Otomatik Ödeme Talimatı Kartı Kontrolu -102
-------------------
 Tags:IOSOtomatikOdemeTalimatiKartiKontrolu
* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Otomatik ödeme talimatları sayfasına gir
* "faturaTalımatAdi"li elementi bulana kadar "4" kere swipe yap ve elementi bul

362
IOS Ödenmemiş Fatura Kartı Kontrol -103
---------------------
 Tags:IOSOdenmemisFaturaKartiKontrol
* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "odenmemisfaturaUyarısı" li elementi bulana kadar swipe et
* "odenmemisfaturaUyarısı" li element sayfada bulunuyor mu kontrol et


Sanal Kredi Karti Kayit IOS -27
-------------------
 Tags:sanalKrediKartiKayitIOS

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "50","75" oranlarından "50","30" oranlarına "15" kere swipe et
* "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "tumIslemlerim" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "sallaKazanPopup" li element varsa  "10" "10" koordinatına tıkla
* "tumIslemlerım-PaycellveKayıtlıKartlarım" li elementi bulana kadar swipe et ve tıkla
* "5" saniye bekle
* "2" kere aşağıya kaydır
* İçeriği "Kredi Kartlarım" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "kartiSil" li elementi bul ve varsa tıkla
* "kartSılTamam" li elementi bul ve varsa tıkla
* "3" saniye bekle
* "kartSılBasarılıPopup" li elementi bul ve varsa tıkla
* "5" saniye bekle
* "krediKartiEkleAd" li elementi bul ve "Umit GOK" değerini yaz
* Hide keyboard
* "krediKartiEkleKartNo" li elementi bul ve "4912057039101356" değerini yaz
* Klavyeyi kapat
* "krediKartiEkleKartTarihNo" li elementi bul ve tıkla
* "sonKullanmaTarihi-Ay" li elementi bul ve "7" değerini yaz
* "sonKullanmaTarihi-Yıl" li elementi bul ve "2020" değerini yaz
*  Hide keyboard
* "2" saniye bekle
* "krediKartiEkleKartCvv" li elementi bul ve "365" değerini yaz
* Klavyeyi kapat
* "krediKartKaydetBtn" li elementin  merkezine tıkla
* "50","50" oranlarından "50","20" oranlarına "1" kere swipe et
* "KrediKartKaydetTamam" li elementi bul ve tıkla
* "5" saniye bekle
* "kartDogrulamaSayfası" li element sayfada bulunuyor mu kontrol et


Search Autocomplete IOS -200
---------------
 Tags:searchAutocompleteIOS

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "aramaButonu" li elementi bul ve tıkla
* "aramaYapText" li elementi bul ve "kulak" değerini yaz
* "kulaklikSearchTextResult" li element sayfada bulunuyor mu kontrol et

Search History Kaydi IOS -201
--------------
Tags: searchHistoryKaydiIOS

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "aramaButonu" li elementi bul ve tıkla
* "aramaYapText" li elementi bul ve "Turk" değerini yaz
* "searchHistoryTextResult" li elementi bul ve tıkla
* "carpıButonIkı" li elementi bul ve tıkla
* "geriIOS" li elementi bul ve tıkla
* "aramaButonu" li elementi bul ve tıkla
* "searchHistoryTextResult" li element sayfada bulunuyor mu kontrol et


Search Tab Carpi Butonu IOS -205
----------------
 Tags:searchTabCarpiButonuIOS

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "aramaButonu" li elementi bul ve tıkla
* "aramaYapText" li elementi bul ve "deneme" değerini yaz
* "searchTabCarpi" li elementi bul ve tıkla
* "aramaYapText" li element sayfada bulunuyor mu kontrol et


Search Tab Gecis Kontrolu IOS -203
----------------
 Tags:searchTabGecisKontroluIOS

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "aramaButonu" li elementi bul ve tıkla
* "aramaYapText" li elementi bul ve "Turk" değerini yaz
* "searchHistoryTextResult" li elementi bul ve tıkla
* "carpıButonIkı" li elementi bul ve tıkla
* "searchHistoryTextResult" elementinin "0" .li elementi bul ve tıkla
* "2" saniye bekle
* "carpıButonIkı" li elementi bul ve tıkla
* "searchHistoryTextResult" elementinin "1" .li elementi bul ve tıkla
* "2" saniye bekle
* "carpıButonIkı" li elementi bul ve tıkla
* "searchHistoryTextResult" elementinin "2" .li elementi bul ve tıkla
* "2" saniye bekle
* "carpıButonIkı" li elementi bul ve tıkla
* "geriIOS" li elementi bul ve tıkla
* "5307458832" değerini sayfa üzerinde olup olmadığını kontrol et.



/////////////////////////////////////////////////////// 13 12 19

257,258,272,273
IOS Ürünlerim Kartı Kontrolü
------------------
 Tags:IOSUrulerimKartiKontrolu

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "tumUrunlerimButton" li elementi bulana kadar swipe et
 "platiniumAvantajPaketi" li element sayfada bulunuyor mu kontrol et
* "TLveAY" li element sayfada bulunuyor mu kontrol et
* "detayliBilgi" li element sayfada bulunuyor mu kontrol et
* "baslangicCheck" li element sayfada bulunuyor mu kontrol et
* "bitisCheck" li element sayfada bulunuyor mu kontrol et

264
IOS Tum Urunlerim Sayfasinda Basarili İptal
----------------
Tags: IOSTumUrunlerimSayfasindaBasariliIptal
* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
 Swipe times "2"
 "hizliIslemlerKarti"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "tumUrunlerimButton" li elementi bul ve tıkla
* "iptal"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "1" saniye bekle
 Swipe times "1"
* "2" saniye bekle
"kampanyalarimIsmi"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "iptal" elementinin koordinatlarına x="5" y="-25" degerlerini ekleyerek tıkla
* "eminMisinizYazisi" li element sayfada bulunuyor mu kontrol et


//IOS Tum Urunlerim Sayfasinda Ek Faydalarım Swipe(2)
//--------------------------

:TumUrunlerimSayfasindaEkFaydalarimSwipe
//ıdlendişrme bekliyor
//* Uygulamanın açıldığını kontrol et
//* Kullanıcı girişi yapılmışsa çıkış yap
//* "anasayfaGirisYapButonu" li elementi bul ve tıkla
//* iOS 5720 ile Giris Yap
//* "5" saniye bekle
//* "tumUrunlerimButton"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "tumUrunlerimButton" li elementi bul ve tıkla
//* "ekFaydalarimYazisi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "ekFaydaIptalButonu" li elementi hizala ve sagdan sola kaydır "5" kere y cordinatına "-10" ekle
//* "ekFaydaSwipeCheck" li element sayfada bulunuyor mu kontrol et
//swipee çalışmıyorrrrrrrrr---------------

//IOS Tum Urunlerim Sayfasinda Kampanya Ayrintilari
//------------------------------

IOSTumUrunlerimSayfasindaKampanyaAyrintilari
//ıdlendirme bekliyor
//* Uygulamanın açıldığını kontrol et
//* Kullanıcı girişi yapılmışsa çıkış yap
//* "anasayfaGirisYapButonu" li elementi bul ve tıkla
//* iOS 5720 ile Giris Yap
//* "tumUrunlerimButton"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "tumUrunlerimButton" li elementi bul ve tıkla
//* "urunlerimSayfasiKampanyaAyrintisi"li elementi bulana kadar "5" kere swipe yap ve elementi bul
//* "urunlerimSayfasiKampanyaTarihi" li element sayfada bulunuyor mu kontrol et

//IOS Urunlerim Karti Mevcut Paket Ayrintilari
//------------------------
//
//ıdlendirme bekliyor
//* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
//* "mevcutTarifeIsmi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "mevcutTarifeUcretBilgisi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "mevcutTarifeDetayi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "mevcutTarifeZamanBari"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "mevcutTarifeBaslangicTarihi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "mevcutTarifeBitisTarihi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "tumUrunlerimButton"li elementi bulana kadar "4" kere swipe yap ve elementi bul


IOS Urunlerim Sayfa Kontrolleri
--------------------------------
 Tags:IOSUrunlerimSayfaKontrolleri

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Dinamik kartları kapat
* "tumUrunlerimButton" li elementi bulana kadar swipe et
* "tumUrunlerimButton" li elementi bul ve tıkla
* "mevcutPaketIsmi" li element sayfada bulunuyor mu kontrol et
* "ekFaydaIsmi" li elementi bulana kadar swipe et
* "ekFaydaIsmi" li element sayfada bulunuyor mu kontrol et
* "kampanyalarimIsmi" li elementi bulana kadar swipe et
* "kampanyalarimIsmi" li element sayfada bulunuyor mu kontrol et
* "servislerimIsmi" li elementi bulana kadar swipe et
* "servislerimIsmi" li element sayfada bulunuyor mu kontrol et


//IOS Urunlerim Detayli Bilgi Kontrolleri
//-------------------------
//
//Idlendirme bekliyor
//
//* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
//* "mevcutTarifeDetayi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "mevcutTarifeDetayi" li elementi bul ve tıkla
//* "5" saniye bekle
//* "urunlerimDetayliAyrintiSayfasi" li element sayfada bulunuyor mu kontrol et
//* "urunlerimSayfasindaKapatmaButonu" li elementi bul ve tıkla
//* "tumUrunlerimButton"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "tumUrunlerimButton" li elementi bul ve tıkla
//* "urunlerimSayfasindaDetayliBilgiButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "urunlerimSayfasindaDetayliBilgiButonu" li elementi bul ve tıkla
//* "urunlerimDetayliAyrintiSayfasi" li element sayfada bulunuyor mu kontrol et
//* "urunlerimSayfasindaKapatmaButonu" li elementi bul ve tıkla
//* "kampanyaDetayliBilgiButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "kampanyaDetayliBilgiButonu" li elementi bul ve tıkla
//* "urunlerimDetayliAyrintiSayfasi" li element sayfada bulunuyor mu kontrol et
//* "urunlerimSayfasindaKapatmaButonu" li elementi bul ve tıkla
//* "servislerimDetayliBilgiButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "servislerimDetayliBilgiButonu" li elementi bul ve tıkla
//* "urunlerimDetayliAyrintiSayfasi" li element sayfada bulunuyor mu kontrol et
//* "urunlerimSayfasindaKapatmaButonu" li elementi bul ve tıkla


//IOS Tum Urunlerim Sayfasi Mevcut Paket Kontrolleri
//------------------------
//
//Idlendirme bekliyor
// * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
// * "tumUrunlerimButton"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "tumUrunlerimButton" li elementi bul ve tıkla
// * "urunlerimSayfasindaMevcutPaketIsmi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "urunlerimSayfasindaPaketZamanBari"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "urunlerimSayfasindaFiyatBilgisi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "urunlerimSayfasindaBaslangicTarihi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "urunlerimSayfasindaBitisTarihi"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "urunlerimSayfasindaDetayliBilgiButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
// * "urunlerimSayfasindaPaketiniDegistirButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul



////////////
////////////
////////////
////////////
////////////
////////////
////////////
////////////

IOS Guncel Faturami Goster
------------------

Tags:IOSGuncelFaturamiGoster

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Swipe times "1"
* "guncelFaturamiGosterButonu"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "guncelFaturamiGosterButonu" li elementi bul ve tıkla
* "faturayıInceleButonu" li element sayfada bulunuyor mu kontrol et

IOS Faturalarim Son Odeme Tarihi Kontrolu
---------------------
Tags:IOSFaturalarimSonOdemeTarihiKontrolu
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "2" saniye bekle
* Swipe times "1"
* "faturalarimSonOdemeTarihi"li elementi bulana kadar "5" kere swipe yap ve elementi bul

IOS Faturalarim Kartinda Hemen Ode Secenegi
----------------------------
Tags:IOSFaturalarimKartindaHemenOdeSecenegi
 Numara:"5307354973" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Fatura ödeme sayfasına gir ve kontro et
//* "hemenOdeButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
//* "odenmemisFaturaBilgisi" li element sayfada bulunuyor mu kontrol et
//* "hemenOdeButonu" li elementi bul ve tıkla
//* "odenmemisFaturaBilgisi" li elementi bul varsa "geçmedi" mesajını hata olarak göster


IOS Faturalarim Ayarlari Kontrolleri
--------------------

Tags:IOSFaturalarimAyarlariKontrolleri

* Numara:"5307354973" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "2" saniye bekle
* Swipe times "1"
* "faturaAyarlari"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "faturaAyarlari" li elementi bul ve tıkla
* "8" saniye bekle
* "faturaKontrolUyariLimiti" li element sayfada bulunuyor mu kontrol et
* "faturaGonderimYontemi" li element sayfada bulunuyor mu kontrol et
* "faturaKesimTarihi" li element sayfada bulunuyor mu kontrol et
* "faturaOtomatikOdemeTalimati" li element sayfada bulunuyor mu kontrol et



// burdan aşağisi yazılmadı

366
IOS Bireysel Kullanici Ile Fatura Ekraninda Turkcell Asistan
---------------------------------
Tags:--BilgiBekleniyorIOSBireyselKullaniciIleFaturaEkranindaTurkcellAsistan

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "faturayıInceleButonu"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "faturayıInceleButonu" li elementi bul ve tıkla
* "turkcellAsistanaBaglan" li elementi bul ve tıkla
* "3" saniye bekle
* "turkcellAsistanaBaglan" li elementi bul varsa "sayfaya geçilemedi" mesajını hata olarak göster

turkcell asıstan butonj ıosta bulunamadı bilgi bekleniyor

/AND Kurumsal Kullanici Ile Fatura Ekraninda Turkcell Asistan  (DigexTagler Android ile aynı)
/---------------------------------
/
/Tag:--BilgiBekleniyorANDKurumsalKullaniciIleFaturaEkranindaTurkcellAsistan
/
/* "5376441466" ile giriş yapılmamıssa giriş yap android şifre="530530"
/* "faturayıInceleButonu"li elementi bulana kadar "5" kere swipe yap ve elementi bul
/* "faturayıInceleButonu" li elementi bul ve tıkla
/* "turkcellAsistanaBaglan" li elementi bul ve tıkla
/turkcell asıstan butonj ıosta bulunamadı bilgi bekleniyor
/

368
IOS Prepaid Hat Ile Fatura Karti Goruntulenmeme Kontrolu
---------------------------------
Tags:IOSPrepaidHatIleFaturaKartiGoruntulenmemeKontrolu

* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "faturalarımAlani" li elementi bul varsa "Prepaid Hatta Faturalarım Alanı Bulunmamalı" mesajını hata olarak göster
* "50","70" oranlarından "50","30" oranlarına "1" kere swipe et
* "faturalarımAlani" li elementi bul varsa "Prepaid Hatta Faturalarım Alanı Bulunmamalı" mesajını hata olarak göster
* "50","70" oranlarından "50","30" oranlarına "1" kere swipe et
* "faturalarımAlani" li elementi bul varsa "Prepaid Hatta Faturalarım Alanı Bulunmamalı" mesajını hata olarak göster
* "50","70" oranlarından "50","30" oranlarına "1" kere swipe et

405
IOS Super Online Kullanici Ile Hizli Islemler Karti Kontrolleri
---------------------------------
Tags:IOSSuperOnlineKullaniciIleHizliIslemlerKartiKontrolleri
* SuperOnline Hesabı ile giriş yap
* "2" saniye bekle
 Swipe times "2"
 "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bulana kadar swipe et
* "tumIslemlerim" li elementi bul ve tıkla
* "3" saniye bekle
* "tumIslemlerim" li elementi bul varsa "TUM ISLEMLERİM SAYFASINA GİRİLEMEDİ" mesajını hata olarak göster
* "kablosuzAgIslemlerim1" li element sayfada bulunuyor mu kontrol et
* "nakilIslemlerimTest" li element sayfada bulunuyor mu kontrol et
"kablosuzAgIslemlerim1"li elementi bulana kadar "1" kere swipe yap ve elementi bul
* "hizmetDondurmaTEst" li element sayfada bulunuyor mu kontrol et
* "faturaAyarlarimTest" li element sayfada bulunuyor mu kontrol et
* "otomatikOdemeTalimatiTest" li element sayfada bulunuyor mu kontrol et
* "ileriTarihliPaketDegisikligiTest" li element sayfada bulunuyor mu kontrol et
* Swipe times "1"
* "guvenliInternet" li elementi bul yoksa "bulunamadı" mesajını hata olarak göster

406

IOS Super Online Kullanici Ile Kablosuz Ag Islemlerim Sayfasi
--------------------------------
Tags:IOSSuperOnlineKullaniciIleKablosuzAgISlemlerimSayfasi

* SuperOnline Hesabı ile giriş yap
* "2" saniye bekle
* Swipe times "2"
* "kablosuzAgIslemlerim"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "kablosuzAgIslemlerim" li elementi bul ve tıkla
* "10" saniye bekle
* "teknikİslemlerim" li element sayfada bulunuyor mu kontrol et

408
IOS Super Online Kullanici Ile Hizmet Dondurma Sayfasi
--------------------------------
Tags:IOSSuperOnlineKullaniciIleHizmetDondurmaSayfasi
* SuperOnline Hesabı ile giriş yap
* "hizmetDondurma"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "hizmetDondurma" li elementi bul ve tıkla
* "5" saniye bekle
* "gönderButonu"li elementi bulana kadar "5" kere swipe yap ve elementi bul

409
IOS Super Online Kullanici Ile Fatura Ayarlarim Sayfasi
--------------------------------
Tags:IOSSuperOnlineKullaniciIleFaturaAyarlarimSayfasi

* SuperOnline Hesabı ile giriş yap
* "faturaAyarlarım"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "faturaAyarlarım" li elementi bul ve tıkla
* Wait "7" seconds
* "faturaAyarlariBaslik" li element sayfada bulunuyor mu kontrol et

410
IOS Super Online Kullanici Ile Otomatik Odeme Talimati Sayfasi
--------------------------------
Tags:IOSSuperOnlineKullaniciIleOtomatikOdemeTalimatiSayfasi

* SuperOnline Hesabı ile giriş yap
* "otomatikOdemeTalimati"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "otomatikOdemeTalimati" li elementi bul ve tıkla
* "yeniTalimatEkle" li element sayfada bulunuyor mu kontrol et

411
IOS Super Online Kullanici Ile Ileri Tarihli Paket Degisikligi Sayfasi
--------------------------------
Tags:IOSSuperOnlineKullaniciIleIleriTarihliPaketDegisikligiSayfasi

* SuperOnline Hesabı ile giriş yap
* "tumIslemlerim" li elementi bulana kadar swipe et
* "tumIslemlerim" li elementi bul ve tıkla
 "ileriTarihliPaketDegisikligi"li elementi bulana kadar "6" kere swipe yap ve elementi bul
* "ileriTarihliPaketDegisikligi" li elementi bulana kadar swipe et
* "ileriTarihliPaketDegisikligi" li elementi bul ve tıkla
* "gönderButonu"li elementi bulana kadar "5" kere swipe yap ve elementi bul

412
IOS Super Online Kullanici Ile Guvenli Internet Sayfasi
--------------------------------
Tags:IOSSuperOnlineKullaniciIleGuvenliInternetSayfasi

* SuperOnline Hesabı ile giriş yap
* Swipe times "2"
* "tumIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "tumIslemlerim" li elementi bul ve tıkla
* "3" saniye bekle
* "tumIslemlerim" li elementi bul varsa "TUM ISLEMLERİM SAYFASINA GİRİLEMEDİ" mesajını hata olarak göster
* Swipe times "1"
* "guvenliInternet" li elementi bul ve tıkla
* "2" saniye bekle
* "guvenliInternetKontrol" li elementi bul yoksa "GUVENLİ INTERNET SAYFASINA GIRILEMEDİ" mesajını hata olarak göster

IOS Bireysel Data Ile Urunlerim Karti Kontrolu
-------------------------------------

Tags:IOSBireyselDataIleUrunlerimKartiKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "tumUrunlerimButton"li elementi bulana kadar "8" kere swipe yap ve elementi bul
* "tumUrunlerimButton" li element sayfada bulunuyor mu kontrol et


IOS Kurumsal Data Ile Urunlerim Karti Kontrolu
-----------------------
Tags:IOSKurumsalDataIleUrunlerimKartiKontrolu
* IOS "5376441466" numarası ve "530530" şifresi ile giriş yapılmamıssa giriş yap
* Tum ürünlerim sayfasına git
 "tumUrunlerimButton"li elementi bulana kadar "4" kere swipe yap ve elementi bul

//idlendirme bekliyor 16 mart
IOS Super Online Kullanıcısı Kullanım Kartı Kontrolu
---------------------------

Tags:IOSSuperOnlineKullanıcisiKullanimKartiKontrolu

* SuperOnline Hesabı ile giriş yap
* "kullanimKartiBasligi" li element sayfada bulunuyor mu kontrol et
* "superOnlineKullanimBari" li element sayfada bulunuyor mu kontrol et
* "superOnlineKullanimAciklamasi" li element sayfada bulunuyor mu kontrol et

// idlendime mevxut degil
IOS Indirme ve Yukleme Degerlerinin Toplam Kullanımı Vermesi Kontrolu
------------------------------------

Tags:IOSIndirmeVeYuklemeDegerlerininToplamKullanimiVermesiKontrolu

* SuperOnline Hesabı ile giriş yap
* Indirme ve yükleme değerlerinin toplamının toplam kullanımı verdiğini kontrol et


IOS Chatbot Kontrol Bireysel
------------
Tags:IOSChatbotKontrolBireysel
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
*Chatbota gir

IOS Chatbot Kontrol Kurumsal
------------
Tags:IOSChatbotKontrolKurumsal
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Chatbota gir

//29.01.2020

IOS Chatbot floating button geri dönülür
---------------------
Tags:IOSChatbotFloating
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Chatbota gir
* Chatbot floating button

senarya mehdi
IOS ChatBot Webchat yönlendirmesi -219
-------------------
Tags:IOSChatbotWebchat
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Chatbota gir
 ChatBot Webchat
220
IOS ChatBot İnternet Çekmiyor -212
---------------
Tags:IOSChatbotInternet
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Chatbota gir
* ChatBot İnternet


IOS İngilizce WebChat Girilir -214
----------------
Tags:IOSIngilizceWebChatGirilir

 Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Dil ingilizce yapılır
 Chatbota gir
 ChatBot Webchat
 "webChatKapat" li elementi
 Dil türkçe yapılır


IOS Chatbot Greetings İntenti Gerçekleştirilir
-------------------------
Tags:IOSChatbotGreetingsİntentiGerçekleştirilir

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "5" saniye bekle
* Chatbota gir
* "mesajBarı" li elementi bul tikla ve "merhaba" değerini yaz
* "gonderBtn" li elementi bul ve tıkla
* "5" saniye bekle


aynısından var
//IOS Network Talebi Internetim Yavaş
//--------------------
//Ta gs:IOSNetworkTalebiInternetimYavaş
//* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
//* Network Talepleri Sayfasına Gir
//* Arama ve Baglantı Check Element "internetimYavaş"
//
//IOS Network Talebi Sayfa İçerigini Düzgün Göremiyorum
//--------------------
//Ta gs:IOSNetworkTalebiSayfaİçeriginiDüzgünGöremiyorum
//* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
//* Network Talepleri Sayfasına Gir
//* Arama ve Baglantı Check Element "sayfaIceriginiKontrolEt"



6 Subat
404
IOS Super Online Hesabı Hızlı İşlemler Kartı İçerik Sayısı Kontrolu
-------------------------------------
 Tags:IOSSuperOnlineHesabiHizliİslemlerKartıİcerikSayisiKontrolu
* SuperOnline Hesabı ile giriş yap
* "2" saniye bekle
* Swipe times "2"
* "islemMerkeziBuyuklukKontrol"li elementi bulana kadar "4" kere swipe yap ve elementi bul

//13.02.2020
419
IOS NonTurkcell Hediye Icon Görüntülenmez
---------------------
 Tags:IOSNonTurkcellHediyeIconGoruntulenmez
* Non turkcell num:"5534656062" şifre:"123456" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul varsa "hediye iconu sayfada bulunuyor" mesajını hata olarak göster
/* Kullanıcı girişi yapılmışsa çıkış yap

420
IOS MGB Hediye Icon Görüntülenmez
-----------------
Tags:IOSMGBHediyeIconGoruntulenmez
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul varsa "hediye iconu sayfada bulunuyor" mesajını hata olarak göster

421
IOS Kurumsal Hediye Icon Görülür
-----------------
Tags:IOSKurumsalHediyeIconGorulur
* Numara:"5338972468" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul yoksa "hediye iconu sayfada bulunmuyor" mesajını hata olarak göster

422
IOS Bireysel Hediye Icon Görülür
--------------------
Tags:IOSBireyselHediyeIconGorulur
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
*"2" saniye bekle
* "hediyeKutum" li elementi bul yoksa "hediye iconu sayfada bulunmuyor" mesajını hata olarak göster


//ıdlendirme bekliyor 4 mart dogum tarihi girilemiyor

299
IOS Hesap Ekleme TCKN&Doğum Tarihi Hatalı Girişinde Hata Popup Görüntülenir
----------------------------------
Tags:IOSHesapEklemeTCKNDogumTarihiHataliGirisindeHataPopupGoruntulenir
* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "pp" li elementi bul ve tıkla
* "HesapEkleKaldırBtn" li elementi bul ve tıkla
* "hesapEkleBtn" li elementi bul ve tıkla
* "tc" li elementi bul, temizle ve "45106611958" değerini yaz
* "hesapEkleDogumTarihi" li elementi bul ve tıkla
* "btn_HesapEkleDevam" li elementi bul ve tıkla
* "popup_HesapEkle" li element sayfada bulunuyor mu kontrol et

423
IOS Bireysel Hediye Havuzu Tablerinin Görüntülenmesi
--------------------
Tags:IOSBireyselHediyeHavuzuTablerininGoruntulenmesi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_hediyelerim" li elementi bul yoksa "hediyelerim tab i sayfada bulunmuyor" mesajını hata olarak göster
* "tb_tarihce" li elementi bul yoksa "tarihce tab i sayfada bulunmuyor" mesajını hata olarak göster
* "tb_ayricaliklar" li elementi bul yoksa "ayricaliklar tab i sayfada bulunmuyor" mesajını hata olarak göster

424
IOS Bireysel Hediye Havuzu Karekod
-------------------
 Tags:IOSBireyselHediyeHavuzuKarekod
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_hediyelerim" li elementi bul ve tıkla
* "saatlik500" li elementi bul yoksa "ilk alanda bulunmadı" mesajını hata olarak göster
* "karakoduOkut" li elementi bul ve tıkla
* "3" saniye bekle
* "karakoduOkut" li elementi bul varsa "sayfaya geçilemedi" mesajını hata olarak göster

425
IOS Bireysel Hediye Havuzu Kullanılmayan Çekler
--------------------
 Tags:IOSBireyselHediyeHavuzuKullanilmayanCekler
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_tarihce" elementinin koordinatlarına x="2" y="2" degerlerini ekleyerek tıkla
/* "tb_tarihce" li elementi bul ve tıkla
* "btn_kullanılmayanCekler" li elementi bul ve tıkla
* "3" saniye bekle
* "kullanılmayanCeklerList" li elementi bul yoksa "listelenmedi" mesajını hata olarak göster

20.02.2020
427
IOS Bireysel Hediye Havuzu İnternet Kazanılan
-----------------------
Tags:IOSBireyselHediyeHavuzuInternetKazanilan
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
/* "tb_tarihce" li elementi bul ve tıkla
* "tb_tarihce" elementinin koordinatlarına x="0" y="0" degerlerini ekleyerek tıkla
* "btn_HediyeInternet" li elementi bul ve tıkla
* "1" saniye bekle
* "GB" li elementi bul yoksa "bulunamadı" mesajını hata olarak göster

431
IOS Bireysel Hediye Havuzu Ayricaliklar Kesfet
------------------------
Tags:IOSBireyselHediyeHavuzuAyricaliklarKesfet

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_ayricaliklar" elementinin koordinatlarına x="0" y="0" degerlerini ekleyerek tıkla
* "ayricalikKesfet" li elementi bul ve tıkla
* "1" saniye bekle
* "ayricalikKesfet" li elementi bul varsa "sayfaya geçilemedi" mesajını hata olarak göster

432
IOS Kurumsal Hediye Havuzu Iste Kazan Kampanyalari
------------------------
Tags:IOSKurumsalHediyeHavuzuIsteKazanKampanyalari

* Numara:"5338972468" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_ayricaliklar" li elementi hizala ve sagdan sola kaydır "1" kere y cordinatına "5" ekle
* "tb_istekazan" elementinin koordinatlarına x="0" y="0" degerlerini ekleyerek tıkla
/* "istekazanKampanya" li elementi bul ve tıkla
* "istekazanKampanya" elementinin koordinatlarına x="5" y="5" degerlerini ekleyerek 2 kere tıkla
/* "4" saniye bekle
* "istekazanKampanya" li elementi bul ve varsa tıkla
* "4" saniye bekle
* "istekazanHemenAl" li elementi bul yoksa "sayfaya geçilemedi" mesajını hata olarak göster

9.04.2020

IOS Bireysel Hediye Havuzu Son Uc Ay Kazandıklarım
--------------------------
Tags:IOSBryHHIsteSonUcAyKazandiklarim

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_tarihce" elementinin koordinatlarına x="2" y="2" degerlerini ekleyerek tıkla
* Kazandıklarım internet ve diger karsılastırılması

IOS Bireysel Hediye Havuzu Diger Buttonu
---------------------
Tags:IOSBryHHDigerButtonu

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_tarihce" elementinin koordinatlarına x="2" y="2" degerlerini ekleyerek tıkla
* "HHdiger" li elementi bul ve varsa tıkla
* "digerListelenen" li elementi bul yoksa "listelenmedi" mesajını hata olarak göster

IOS Bireysel Hediye Havuzu Platinum Ayrıcalıgı Kesfet
-----------------------------
Tags:IOSBryHHPlatinumAyrıcalıgıKesfet

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_ayricaliklar" li elementi bul ve tıkla
* "HHKesfet" li elementi bul ve tıkla
* "2" saniye bekle
* "HHKesfet" li elementi bul varsa "app ler açılmadı" mesajını hata olarak göster

IOS Bireysel Hediye Havuzu Paycell Git
--------------------
Tags:IOSBryHHPaycellGit

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "hediyeKutum" li elementi bul ve varsa tıkla
* "tb_hediyelerim" li elementi bul ve tıkla
* "btn_PaycellGit"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "btn_PaycellGit" li elementi bul ve tıkla
* "PaycellBilgilendirme" li elementi bul yoksa "hatalı popup" mesajını hata olarak göster
* "devam_btn" li elementi bul ve tıkla
* "3" saniye bekle
* "PaycellBilgilendirme" li elementi bul varsa "app ler açılmadı" mesajını hata olarak göster



14.04.2020
IOS Farklı Datalarla Kart Kont
--------------
Tags:IOSFarkliDatalarlaKartKont
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Listelenen kart kontrolleri
* Bireysel kullanıcı degistir
* Listelenen kart kontrolleri

20.04
IOS Kurumsal Ekleme Işleminde Güvenlik Sorusu
---------------------
 Tags:IOSKurumsalEklemeIslemindeGuvenlikSorusu

* Numara:"FaturalıNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "pp" li elementi bul ve tıkla
* "HesapEkleKaldırBtn" li elementi bul ve tıkla
* "hesapEkleBtn" li elementi bul ve tıkla
* "eklemeOncedenYapildi" li elementi bul yoksa "hata popup" mesajını hata olarak göster

IOS Kalan Kullanim Theatre Mod Paketler
----------------------
 Tags:IOSKalanKullanimTheatreModPaketler
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Theatre mod paket grup isimleri kontrolleri yapılır

IOS Kalan Kullanim Theatre Mod Paketler Grubu
----------------------
 Tags:IOSKalanKullanimTheatreModPaketGrubu
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Theatre mod paket grupları listesi kontrolleri yapılır


//idlendirme
IOS Kotalı SOL Kalan Kullanım Kartı Bilgileri Kontrolü
---------------------------
* SuperOnline Hesabı ile giriş yap
* SOL Kalan Kullanım Kartı Bilgileri Kontrol

IOS SuperOnline Nakil İşlemlerim Sayfası Kontrolü
------------------------
 Tags:IOSSuperOnlineNakilIslemlerimSayfasiKontrolu

*SuperOnline Hesabı ile giriş yap
* "2" saniye bekle
* Swipe times "2"
* "nakilIslemlerim"li elementi bulana kadar "9" kere swipe yap ve elementi bul
* "nakilIslemlerim" li elementi bul ve tıkla
* "3" saniye bekle
* "nakilIslemlerimPage" li elementi bul yoksa "nakilIslemlerimPage geçilemedi" mesajını hata olarak göster

IOS NonTurkcell Hızlı İslemler Kartı Kontrolü
----------------------
Tags:IOSNonTurkcellHizliIslemlerKartiKont

* Non turkcell num:"5534656062" şifre:"123456" ile giriş yapılmamışsa giriş yap
* Hızlı islemler kartı içeriği kontrolü

IOS NonTurkcell Hızlı İslemler Numaranı Taşı Kontrolü
------------------------
 Tags:IOSNonTurkcellHizliIslemlerNumaraniTasiKont

* Non turkcell num:"5534656062" şifre:"123456" ile giriş yapılmamışsa giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
* "numaraniTasi" li elementi bul ve tıkla
* "numaraniTasiPage" li elementi bul yoksa "numaraniTasi basligi bulunamadi" mesajını hata olarak göster
* "3" saniye bekle
* "hemenBasla" li elementi bul ve tıkla
* "hattimiTurkcelleTasimakİstiyorum" li elementi bul ve tıkla
* "numaraTasima" li elementi bul yoksa "numaraniTasi sayfası geçilemedi" mesajını hata olarak göster

IOS NonTurkcell Hızlı İslemler Yeni Hat Al Kontrolü
-------------------------
 Tags:IOSNonTurkcellHizliIslemlerYeniHatAlKont

* Non turkcell num:"5534656062" şifre:"123456" ile giriş yapılmamışsa giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
* "yeniHatAl" li elementi bul ve tıkla
* "3" saniye bekle
* "hemenBasla" li elementi bul ve tıkla
* "yeniHatAlmakİstiyorum" li elementi bul ve tıkla
* "yeniNumaraAl" li elementi bul yoksa "yeniHatAl geçilemedi" mesajını hata olarak göster

IOS NonTurkcell Hızlı İslemler TL Yükle Kontrolü
------------------------
 Tags:IOSNonTurkcellHizliIslemlerTLYukleKont

* Non turkcell num:"5534656062" şifre:"123456" ile giriş yapılmamışsa giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
* "TLtext" li elementi bul ve tıkla
* "tlYukleButonu" li elementi bul yoksa "tlYukle geçilemedi" mesajını hata olarak göster

IOS NonTurkcell Hızlı İslemler Ev İnternetini Ekle Kontrolü
------------------------
 Tags:IOSNonTurkcellHizliIslemlerEvInternetEkleKont

* Non turkcell num:"5534656062" şifre:"123456" ile giriş yapılmamışsa giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
* "evİnternetiEkle" li elementi bul ve tıkla
* "2" saniye bekle
* "evİnternetiEkle" li elementi bul varsa "evİnternetiEkle geçilemedi" mesajını hata olarak göster


IOS Fatura Ayarları Listesi Tabler Kontrolü
-------------------
 Tags:IOSFaturaAyarlariListesiTablerKont

 * Numara:"5307354973" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "faturalarımAyarlarBtn"li elementi bulana kadar "7" kere swipe yap ve elementi bul
 * "faturalarımAyarlarBtn" li elementi bul ve tıkla
 * "faturaAyarlarıText" li elementi bul yoksa "FATURA AYARLARI SAYFASINA GİREMEDİ" mesajını hata olarak göster
 * Listelenen fatura tablerin kontrolü

IOS Fatura Detay Ekranında Pdf Kontrolü
--------------------
 Tags:IOSFaturaDetayEkranıPdfKont
* Numara:"5307354973" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "urunlerim"li elementi bulana kadar "7" kere swipe yap ve elementi bul
* "faturayıInceleButonu" li elementi bul ve tıkla
* "btn_pdf" li elementi bul ve tıkla
* "btn_pdf" li elementi bul varsa "pdf açılmadı" mesajını hata olarak göster

IOS Hızlı İslemler Kartı Icon Kontrolü
--------------------
Tags:IOSHizliIslemlerIconKont
* Numara:"5307354973" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "paycellveKayıtlıKartlarım"li elementi bulana kadar "11" kere swipe yap ve elementi bul
* Hızlı işlemler kartı isim ve icon kontrolleri

