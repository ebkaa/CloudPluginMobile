Specification Heading
=====================
Created by sahabt on 10.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
AND Basarili Login
----------------
Tags:AndroidBasariliLogin
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap

AND Kurumsal Login
--------
 Tags:AndroidKurumsalLogin
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap

AND Wifi Login
-------
 Tags:AndroidWifiLogin
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap

232
mail ile Basarili Login
----------------------
Tags:AndroidmailIleBasariliLogin
* Kullanıcı girişi yapılmışsa çıkış yap
* Mail hesabı ile giriş yap kullanıcı adı: "umit.gok@consultant.turkcell.com.tr" Şifre "530530"



Hatali Sifre ile Login
----------------------
Tags:AndroidHataliSifreileLogin
* Kullanıcı girişi yapılmışsa çıkış yap
* Hatalı şifre ile login ol
255
Kayit Ol
----------------
Tags:AndroidKayitOl
* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "uyeDegilsenkayıtOlbutonu" li elementi bul ve tıkla
* "2" saniye bekle
* "uyeOlgsmNumarasıalanı" li elementi bul, temizle ve "5369871234" değerini yaz
* Klavyeyi kapat
* "uyeEmailalanı" li elementi bul, temizle ve "g@gmail.com" değerini yaz
* Klavyeyi kapat
* "uyeSifregirisAlanı" li elementi bul, temizle ve "123456" değerini yaz
* Klavyeyi kapat
* "uyeSifretekrarAlanı" li elementi bul, temizle ve "123456" değerini yaz
* Klavyeyi kapat
* "kayitOlbutonu" li elementi bul ve tıkla
* "5" saniye bekle
* "doğrulama kodu gönderildi" değerini sayfa üzerinde olup olmadığını kontrol et.

238 / koşumlardan çıkartıldı
Sifre Degistir
----------------
Tags:AndroidSifreDegistir
* Kullanıcı girişi yapılmışsa çıkış yap
//* "kayitOlbutonu" li elementi bul yoksa "SENARYO GÜNCELLENMEKTEDİR.. İLERDE İŞLEME ALINACAKTIR" mesajını hata olarak göster
//* "anasayfaGirisYapButonu" li elementi bul ve tıkla
//* "4" saniye bekle
//* "epostaAlanı" li elementi bul ve tıkla
//* "epostaAlanı" li elementi bul, temizle ve "nese.aydin@sahabt.com" değerini yaz
//* Klavyeyi kapat
//* "loginDevambutonu" li elementi bul ve tıkla
//* "4" saniye bekle
//* "sifreDegistirButonu" li elementi bul ve tıkla
//* "2" saniye bekle
//* "uyeEmailalanı" li elementi bul, temizle ve "nese.aydin@sahabt.com" değerini yaz
//* Klavyeyi kapat
//* "2" saniye bekle
//* "eskiSifrealanı" li elementi bul ve "530531" değerini yaz
//* Klavyeyi kapat
//* "1" saniye bekle
//* "2" kere aşağıya kaydır
//* "3" saniye bekle
//* "yeniSifreAlanı" li elementi bul ve "531530" değerini yaz
//* Klavyeyi kapat
//* "yeniSifreTekrarAlanı" li elementi bul ve "531530" değerini yaz
//* Klavyeyi kapat
//* "3" saniye bekle
//* "sifreDegistir" li elementi bul ve tıkla
//* "7" saniye bekle
//* "Şifreniz başarıyla değiştirilmiştir" değerini sayfa üzerinde olup olmadığını kontrol et.
//* "2" saniye bekle
//* "tamamButonu" li elementi bul ve tıkla
//* "2" saniye bekle
//* "sifreDegistirButonu" li elementi bul ve tıkla
//* "6" saniye bekle
//* "eskiSifrealanı" li elementi bul ve "531531" değerini yaz
//* Klavyeyi kapat
//* "1" saniye bekle
//* "2" kere aşağıya kaydır
//* "3" saniye bekle
//* "yeniSifreAlanı" li elementi bul ve "530530" değerini yaz
//* Klavyeyi kapat
//* "yeniSifreTekrarAlanı" li elementi bul ve "530530" değerini yaz
//* Klavyeyi kapat
//* "3" saniye bekle
//* "sifreDegistir" li elementi bul ve tıkla
//* "7" saniye bekle
//* "Şifreniz başarıyla değiştirilmiştir" değerini sayfa üzerinde olup olmadığını kontrol et.

Login ve Anasayfa Kontrolu
--------------------------
Tags:AndroidLoginveAnasayfaKontrolu
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * Dinamik kartları kapat

Logout
------
Tags:AndroidLogout
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "anasayfaNumraAlanı" li elementi bul ve tıkla
* "2" saniye bekle
* "profilAyarlarınaGitAND" li elementi bulana kadar swipe et ve tıkla
* "3" saniye bekle
* "1" kere aşağıya kaydır
* "1" saniye bekle
* Çıkış yap butonuna tıkla ve kontrol et

Özel şifre yetkilisi ile loginde kişiselleştirme kartında şirketim bannerı görünmesi
--------------------------------------------
 Tags:OzelSifreYetkilisiIleLogindeKisisellestirmeKartindaSirketimBanneriGorunmesi
* Numara:"5338972468" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "5338972468" değerini sayfa üzerinde olup olmadığını kontrol et.

Şifresiz başarılı login(Mobile connect)
-------------------------
 Tags:SifresizBasariliLogin(MobileConnect)
* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
 * 7243 ile Şifresiz Giris Yap

Şifresiz başarısız login(Mobile connect)
-------------------------------------------------------
 Tags:SifresizBasarisizLogin(MobileConnect)
* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
 * 7243 ile Hatalı Şifresiz Giris Yap


AND Non-Turkcell Müşterinin Kayıt Olmasını Isteyen Ekran Açılır
------------------------------------------------------------
 Tags:ANDNon-TurkcellMusterininKayitOlmasiniIsteyenEkranAcilir
* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* AND non-turkcell hesap ile kayıtsız giriş

AND Nonturkcell Müşteri yanlış mail popup
--------------------
Tags:ANDNonturkcelMusteriYanlisMailPopup

* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "epostaAlanı" li elementi bul ve "b@testinium.com" değerini yaz
* Klavyeyi kapat
* "loginDevambutonu" li elementi bul ve tıkla
* "kayıtGerekliPopup" li elementi bul yoksa "popup görümtülenmedi" mesajını hata olarak göster

AND Beni Hatırla Buton Kontrol
------------------
Tags:ANDBeniHatirlaButonKontrol
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Uygulamayı kapat ve tekrar ac

//Kullanıcı girişi yapılmışsa çıkış yap adımının silinmemesi gerekir
AND Beni Hatırla Buton Kontrol Beni Unut
------------------
Tags:ANDBeniHatirlaButonKontrolBeniUnut
* Kullanıcı girişi yapılmışsa çıkış yap
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Uygulamayı kapat ve tekrar ac