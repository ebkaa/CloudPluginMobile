Specification Heading
=====================
Created by nurgul on 7.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.


Logout TL Yukle
---------------
 Tags:LogoutTLYukle
* Kullanıcı girişi yapılmışsa çıkış yap
* TL yükle sayfasına gir
* Logout Kart Bilgilerini Gir

TL Yukle Kayitli Kart -8
---------------------
 Tags:TLYukleKayitliKart
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "tlYukleButonu" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "kayıtlıKartIleOdeme-onBilgilendirmeCheckbox" elementinin koordinatlarına x="3" y="3" degerlerini ekleyerek tıkla
* "seciliKartIleOdemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* "cvvAlanı" li elementi bul ve "936" değerini yaz
* "cvvBilgileri-mailAlanı" li elementi bul ve "g@gmail.com" değerini yaz
*  Hide keyboard
* "siparisOnayıCheckBox" elementinin koordinatlarına x="3" y="3" degerlerini ekleyerek tıkla
* "odemeYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


TL Yukle Kredi Karti ile Odeme -7
------------------------------
 Tags:TLYukleKrediKartiileOdeme

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "tlYukleButonu" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "baskaKartIleOdeButonu" li elementi bulana kadar swipe et ve tıkla
* iOS Login Kart Bilgilerini Gir
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Logout Hazir Kart Paket Yukle -3
-----------------------------
 Tags:LogoutHazirKartPaketYukle
* Kullanıcı girişi yapılmışsa çıkış yap
* Hazırkart paket yükle sayfasına gir
* Logout Kart Bilgilerini Gir

IOS Hazir Kart Paket Yukle Kayitli Kart -9
-----------------------------------
 Tags:HazirKartPaketYukleKayitliKart
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Hazırkart paket yükle sayfasına gir
* Kayıtlı kart kontrol
* Kayıtlı kart bilgilerini doldur

Hazir Kart Paket Yukle Kredi Karti ile Odeme
--------------------------------------------
 Tags:HazirKartPaketYukleKrediKartiileOdeme

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "hazırKartPaketYukle" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanıYeni" li elementi bul ve tıkla
 "yuklemeYapılacakGSMNoAlanı" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanıYeni" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "baskaKartIleOdeButonu" li elementi bulana kadar swipe et ve tıkla
* iOS Login Kart Bilgilerini Gir
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Logout Cepten Internet -4
----------------------
 Tags:LogoutCeptenInternet

* Kullanıcı girişi yapılmışsa çıkış yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "ceptenInternet" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
*  Hide keyboard
* "ilerleButonu" li elementi bul ve tıkla
* "krediKartıIsimAlanı" li elementi bul ve "Kullanıcı Adı" değerini yaz
*  Hide keyboard
* "kartNumarasıAlanı" li elementi bul ve "KrediKartNo" değerini yaz
*  Hide keyboard
* "kartSonKullanmaTarihiAlanı" li elementi bul ve tıkla
* son kullanma tarihi gir
*  Hide keyboard
* "buKartileOdemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* iOS Logout Kart Bilgilerini Gir
* "3" saniye bekle
* "logoutCheckBox2" li elementi bul ve tıkla
* "odemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Cepten Internet Kayitli Kart -10
----------------------------
 Tags:CeptenInternetKayitliKart

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "5" saniye bekle
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "ceptenInternet" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "kayıtlıKartIleOdeme-onBilgilendirmeCheckbox" li elementi bul ve tıkla
* "seciliKartIleOdemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* "cvvAlanı" li elementi bul ve "936" değerini yaz
* "cvvBilgileri-mailAlanı" li elementi bul ve "g@gmail.com" değerini yaz
*  Hide keyboard
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Cepten Internet Kredi Karti ile Odeme
-------------------------------------
 Tags:CeptenInternetKrediKartiileOdeme

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "ceptenInternet" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "baskaKartIleOdeButonu" li elementi bulana kadar swipe et ve tıkla
* iOS Login Kart Bilgilerini Gir
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Logout Bilgisayardan Internet
-----------------------------
 Tags:LogoutBilgisayardanInternet

* Kullanıcı girişi yapılmışsa çıkış yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "vinnInternet" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
*  Hide keyboard
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
* iOS Logout Kart Bilgilerini Gir
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Bilgisayardan Internet Kayitli Kart
-----------------------------------
 Tags:BilgisayardanInternetKayitliKart

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "vinnInternet" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "kayıtlıKartIleOdeme-onBilgilendirmeCheckbox" li elementi bul ve tıkla
* "seciliKartIleOdemeYapButonu" li elementi bulana kadar swipe et ve tıkla
* "cvvAlanı" li elementi bul ve "936" değerini yaz
* "cvvBilgileri-mailAlanı" li elementi bul ve "g@gmail.com" değerini yaz
*  Hide keyboard
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


Bilgisayardan Internet Kredi Karti ile Odeme
--------------------------------------------
 Tags:BilgisayardanInternetKrediKartiileOdeme

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "vinnInternet" li elementi bul ve tıkla
* "ilkPaketSecenegi" li elementi bul ve tıkla
* "yuklemeYapılacakGSMNoAlanı" li elementi bul, temizle ve "5354556825" değerini yaz
* "ilerleButonu" li elementi bul ve tıkla
* "baskaKartIleOdeButonu" li elementi bulana kadar swipe et ve tıkla
* iOS Login Kart Bilgilerini Gir
* "3" saniye bekle
* "siparisOnayıCheckBox" li elementi bul ve tıkla
* "3" saniye bekle
* "odemeYapButonu" li elementi bul ve tıkla
* "15" saniye bekle
* "PaymentWeb" değerini sayfa üzerinde olup olmadığını kontrol et.


TL Durumum
----------
 Tags:TLDurumum

* Numara:"5354556825" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "detayPrepaid"li elementi bulana kadar "5" kere swipe yap ve elementi bul
* "detayPrepaid" li elementi bul ve tıkla
* "5" saniye bekle
*"dogrulamaEkrani" li elementi bul yoksa "basarısız" mesajını hata olarak göster

 "detayPrepaidAySecimi" li elementi bul ve tıkla
 "detayPrepaidAySecimiALanı" li elementi bul ve tıkla
 "detayPrepaidTumuSecimi" li elementi bul ve tıkla
 "detaySecimIkı" li elementi bul ve tıkla


TL Durumum Anasayfa TL Yukle Butonu Aktif Kontrolu Prepaid -17
-------------------------------------------
 Tags: TLDurumumAnasayfaTLYukleButonuAktifKontroluPrepaid

 Kullanıcı girişi yapılmışsa çıkış yap
 "anasayfaGirisYapButonu" li elementi bul ve tıkla
 iOS 6825 ile Giris Yap
 "5354556825" değerini sayfa üzerinde olup olmadığını kontrol et.
* Numara:"PrepaidNumara" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "AnasayfaTLYukleButonu" li elementi bulana kadar swipe et
* "AnasayfaTLYukleButonu" li elementi bul ve tıkla
* "tlYukleButonu" li elementi bul ve tıkla
* "TLtext" li element sayfada bulunuyor mu kontrol et

