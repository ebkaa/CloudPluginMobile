Specification Heading
=====================
Created by nurgul on 5.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Basarili Login
--------------
 Tags:BasariliLogin
* IOS "5307385720" numarası ve "123456" şifresi ile giriş yapılmamıssa giriş yap

Kurumsal Login
--------
 Tags:KurumsalLogin
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap

Wifi Login
-------
 Tags:WifiLogin
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap

232
mail ile Basarili Login
----------------------
Tags:mailIleBasariliLogin

* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "epostaAlanı" li elementi bul ve "umit.gok@consultant.turkcell.com.tr" değerini tek tek yaz
* Klavyeyi kapat
* "loginDevambutonu" li elementi bul ve tıkla
* "5" saniye bekle
* "sifreGirisalanı" li elementi bul ve "530530" değerini yaz
* Klavyeyi kapat
* "girisYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "5376441465" değerini sayfa üzerinde olup olmadığını kontrol et.



Hatali Sifre ile Login
----------------------
 Tags:HataliSifreileLogin
IOS "5307385720" numarası ve "123456" şifresi ile giriş yapılmamıssa giriş yap
* Kullanıcı girişi yapılmışsa çıkış yap
* Hatalı şifre ile login ol



 "anasayfaGirisYapButonu" li elementi bul ve tıkla
 "gsmNumarasıalanı" li elementi bul ve "5307385720" değerini tek tek yaz
  Hide keyboard
 "loginDevambutonu" li elementi bul ve tıkla
 "2" saniye bekle
 "sifreileGirisyapButonu" li elementi bul ve tıkla
 "sifreGirisalanı" li elementi bul ve "123456" değerini yaz
  Hide keyboard
  girisYapButonu
 "girisYapButonu" li elementi bul ve tıkla
 "5" saniye bekle
 "Hata" değerini sayfa üzerinde olup olmadığını kontrol et.

225
Kayit Ol
--------
 Tags:KayitOl
* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "uyeDegilsenkayıtOlbutonu" li elementi bul ve tıkla
* "2" saniye bekle
* "uyeOlgsmNumarasıalanı" li elementi bul, temizle ve "5369871234" değerini yaz
*  Hide keyboard
* "uyeEmailalanı" li elementi bul, temizle ve "g@gmail.com" değerini yaz
*  Hide keyboard
* "uyeSifregirisAlanı" li elementi bul, temizle ve "123456" değerini yaz
*  Hide keyboard
* "uyeSifretekrarAlanı" li elementi bul, temizle ve "123456" değerini yaz
*  Hide keyboard
* "kayitOlbutonu" li elementi bul ve tıkla
* "5" saniye bekle
* "doğrulama kodu gönderildi" değerini sayfa üzerinde olup olmadığını kontrol et.

238

çıkartılacak
Sifre Degistir
--------------
 Tags:SifreDegistir

* Kullanıcı girişi yapılmışsa çıkış yap
 "anasayfaGirisYapButonu" li elementi bul ve tıkla
 "5" saniye bekle
 "epostaAlanı" li elementi bul, temizle ve "nese.aydin@sahabt.com" değerini yaz
  Hide keyboard
 "loginDevambutonu" li elementi bul ve tıkla
 "5" saniye bekle
 "sifreDegistirButonu" li elementi bul ve tıkla
 "2" saniye bekle
 "eskiSifrealanı" li elementi bul ve "530530" değerini yaz
  Hide keyboard
 "yeniSifreAlanı" li elementi bul ve "531531" değerini yaz
  Hide keyboard
 "yeniSifreTekrarAlanı" li elementi bul ve "531531" değerini yaz
  Hide keyboard
 "1" saniye bekle
 "sifreDegistirButonu" li elementi bul ve tıkla
 "5" saniye bekle
 "Şifreniz başarıyla değiştirilmiştir" değerini sayfa üzerinde olup olmadığını kontrol et.
 "tamamButonu" li elementi bul ve tıkla
 "2" saniye bekle
 "sifreDegistirButonu" li elementi bul ve tıkla
 "5" saniye bekle
 "eskiSifrealanı" li elementi bul ve "531531" değerini yaz
  Hide keyboard
 "yeniSifreAlanı" li elementi bul ve "530530" değerini yaz
  Hide keyboard
 "yeniSifreTekrarAlanı" li elementi bul ve "530530" değerini yaz
  Hide keyboard
 "sifreDegistirButonu" li elementi bul ve tıkla
 "5" saniye bekle
 "Şifreniz başarıyla değiştirilmiştir" değerini sayfa üzerinde olup olmadığını kontrol et.

Login ve Anasayfa Kontrolu
--------------------------
 Tags:LoginveAnasayfaKontrolu

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "KALAN KULLANIMLARIM" değerini sayfa üzerinde olup olmadığını kontrol et.
* "1" kere aşağıya kaydır
* "FATURALARIM" değerini sayfa üzerinde olup olmadığını kontrol et.
* "5" kere aşağıya kaydır

Logout
------
 Tags:Logout

* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* İçeriği "5307385720" e eşit olan elementli bul ve tıkla
* "2" kere aşağıya kaydır
* "profilAyarGit" li elementi bulana kadar swipe et ve tıkla
* "3" saniye bekle
* "cikisButonu" li elementi bulana kadar swipe et ve tıkla
* "popupCikisYapButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "Giriş Yap" değerini sayfa üzerinde olup olmadığını kontrol et.

Ozel Sıfre Yetkisi ile Login
--------------------
 Tags:IosOzelSifreYetkisiileLogin
* Numara:"5338972468" ve şifre:"530530" ile giriş yapılmamışsa giriş yap

Sifresiz Basarılı Logın
------------------
 Tags:IosSifresizBasariliLogin

* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "gsmNumarasıalanı" li elementi bul ve "5307385720" değerini yaz
* Hide keyboard
* "loginDevambutonu" li elementi bul ve tıkla
* "sifresizHizliGiris" li elementi bul ve tıkla
* "tekKullanimlikSifreAlani" li elementi bul yoksa "tek kullanılcak şifre girişi ekranı gelmedi" mesajını hata olarak göster



Sifresiz Basarısız Logın
-----------------
 Tags:IosSifresizBasarisizLogin

* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "3" saniye bekle
 "gsmNumarasıalanı" li elementi bul ve "5307387243" değerini tek tek yaz
* "gsmNumarasıalanı" li elementi bul ve "5307458832" değerini yaz
* Hide keyboard
* "loginDevambutonu" li elementi bul ve tıkla
* "sifresizHizliGiris" li elementi bul ve tıkla
* "12" saniye bekle
* Sifresiz hızlı giris yap

 "tekKullanimlikSifreAlani" li elementi bul ve "1345" değerini yaz
 Hide keyboard
 "sifresizDevamEtBtn" li elementi bul ve tıkla
 "yanlış" değerini sayfa üzerinde olup olmadığını kontrol et.


IOS Non-Turkcell Müşterinin Kayıt Olmasını Isteyen Ekran Açılır
------------------------------------------------------------
 Tags:IOSNon-TurkcellMusterininKayitOlmasiniIsteyenEkranAcilir
* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
 * IOS non-turkcell hesap ile kayıtsız giriş

20.04

IOS Nonturkcell Müşteri yanlış mail popup
--------------------
Tags:IOSNonturkcelMusteriYanlisMailPopup

* Kullanıcı girişi yapılmışsa çıkış yap
* "anasayfaGirisYapButonu" li elementi bul ve tıkla
* "epostaAlanı" li elementi bul ve "b@testinium.com" değerini yaz
* Klavyeyi kapat
* "loginDevambutonu" li elementi bul ve tıkla
* "kayıtGerekliPopup" li elementi bul yoksa "popup görümtülenmedi" mesajını hata olarak göster

IOS Beni Hatırla Buton Kontrol
------------------
Tags:IOSBeniHatirlaButonKontrol
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Uygulamayı kapat ve tekrar ac


// isimdeki beni unut kısmı önemli silinmemesi ricadır :)
 NOT:Kullanıcı girişi yapılmışsa çıkış yap adımı gereksiz degil :)
IOS Beni Hatırla Buton Kontrol Beni Unut
------------------
Tags:IOSBeniHatirlaButonKontrolBeniUnut

* Kullanıcı girişi yapılmışsa çıkış yap
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Uygulamayı kapat ve tekrar ac
