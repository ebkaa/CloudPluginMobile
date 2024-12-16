Specification Heading
=====================
Created by nurgul on 9.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
Bildirimlerim Tabi Kontrolu
---------------------------
 Tags:BildirimlerimTabiKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir

Mesajlarim Tabi Kontrolu
---------------------------
 Tags:MesajlarimTabiKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Mesajlarım Tabına geç

Siparislerim Tabi Kontrolu
---------------------------
Tags:SiparislerimTabiKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından siparişlerim tabına geç

Bireysel Kullanici ile Taleplerim Tabi Kontrolu
-----------------------------------------------
 Tags:BireyselKullaniciileTaleplerimTabiKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç

Kurumsal Kullanici ile Taleplerim Tabi Kontrolu
-----------------------------------------------
 Tags:KurumsalKullaniciileTaleplerimTabiKontrolu
 * Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç

Randevularim Tabi Kontrolu
--------------------------
 Tags:RandevularimTabiKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Randevularım tabına geç

IOS Bildirimlerim sola kaydırıldığında sil butonunun cikmasi
-------------------------------------------------------------------------------
 Tags:IOSBildirimlerimSolaKaydirildigindaSilButonununCikmasi
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* "77","33" oranlarından "33","33" oranlarına "1" kere swipe et
* "SilBtn" li element sayfada bulunuyor mu kontrol et

IOS Bildirim Bulunmadiginda Uyarı Mesajı Kontrol -80
--------------------------------------------------------
Tags:IOSBildirimBulunmadigindaUyariMesajiKontrol
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* bildirimleri sil
* geri butonuna bas
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "bidirimYokturUyarısı" li elementi bul yoksa "bulunamadı" mesajını hata olarak göster

IOS Bildirimlerim Kurumsal Kullanıcılarda Yeni Talep Aç Butonunun Olmaması -94
-------------------------------------
Tags:IOSBildirimlerimKurumsalKullanicilardaYeniTalepAcButonununOlmamasi
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç
* "yeniTalepAç" li elementi bul varsa "kurumsal hesapta yeni talep aç butonu bulunmaması gerekir" mesajını hata olarak göster

IOS Bildirimlerim Yeni Talep ac butonuna tiklandiginda Yeni Talep Ac Ekraninin Acilmasi -95
----------------------------------------------
Tags:IOSBildirimlerimYeniTalepAcbutonunatiklandigindaYeniTalepAcEkranininAcilmasi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç
* Tableplerim tabında yeni talep aç

IOS Bildirimlerim Randevu Talebi Bulunmayan Kullanıci Ekraninda Uyarı Degerinin Gösterilmesi -96
-------------------------------------------------
Tags:IOSBildirimlerimRandevuTalebiBulunmayanKullaniciEkranindaUyariDegerininGosterilmesi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Randevularım tabına geç
* "10" saniye bekle
* "talebinizBulunmamaktadirUyari" li elementi bul yoksa "Randevunuz bulunmamaktadır uyarısı görülemedi" mesajını hata olarak göster

// randevu talebi coronadan sonra düzelt
IOS Bildirimlerim Randevu Talebi Bulunan Kullanıcı Ekranında Talep Detaylarının Yer Alması -97
-------------------------------------------------
Tags:IOSBildirimlerimRandevuTalebiBulunanKullaniciEkranindaTalepDetaylarininYerAlmasi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Bildirimler sayfasına gir
 Bildirimlerim sayfasından Randevularım tabına geç
 "randevuTarihi" li element sayfada bulunuyor mu kontrol et
 "randevuSebebi" li element sayfada bulunuyor mu kontrol et

//corona
IOS Bildirimlerim Randevu Sayfasındaki Listelenen Randevularda İptal Detaylı Bilgi Butonunun Olması -98
-------------------------------------------------
 Tags:IOSBildirimlerimRandevuSayfasindakiListelenenRandevulardaIptalDetayliBilgiButonununOlmasi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 Bildirimler sayfasına gir
 Bildirimlerim sayfasından Randevularım tabına geç
 "detaylıBilgi" li element sayfada bulunuyor mu kontrol et

IOS Bildirimlerim Non Turkcell Hesap Ile Işlem Merkezinde Sadece Bildirimlerim Tabının Olması -99
--------------------------------------------------
 Tags:IOSBildirimlerimNonTurkcellHesapIleIslemMerkezindeSadeceBildirimlerimTabininOlmasi
* Non turkcell num:"5054039973" şifre:"123456" ile giriş yapılmamışsa giriş yap
/* Numara:"5054039973" ve şifre:"123456" ile giriş yapılmamışsa giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
/* "islemMerkeziButonu" elementinin koordinatlarına x="20" y="-20" degerlerini ekleyerek tıkla
* Bildirimler sayfasına gir
* "bildirimlerMesajlarım" li elementi bul varsa "nonTurkcell Hesapta Sadece Bildirimlerim Sekmesi olmalı" mesajını hata olarak göster
* "bildirimlerRandevularım" li elementi bul varsa "nonTurkcell Hesapta Sadece Bildirimlerim Sekmesi olmalı" mesajını hata olarak göster

IOS Bldirimlerim Superonline Hesap Ile Taleplerim TabiKontrolü -101
-----------------------------
Tags:IOSBildirimlerimSuperonlineHesapIleTaleplerimTabiKontrolu
* IOS SuperOnline Hesabı İle Giriş
* "islemMerkeziButonu" li elementi bul ve tıkla
* Bildirimler sayfasına gir
* "taleplerimTabı" li elementi bul ve tıkla
* "5" saniye bekle
* "TALEPLERİM" değerini sayfa üzerinde olup olmadığını kontrol et.

IOS Bildirimlerim Superonline hesap ile bildirimlerim tabı kontrolü -100
--------------------------------------
 Tags:IOSBildirimlerimSuperonlineHesapIleBildirimlerimTabiKontrolu
* IOS SuperOnline Hesabı İle Giriş
* "islemMerkeziButonu" li elementi bul ve tıkla
* Bildirimler sayfasına gir

IOS Bildirimlerim Taleplerim Tabı Ust Kısmında Statu KONTROLU -92
--------------------------------------
 Tags:IOSBildirimlerimTaleplerimTabiUstKismindaStatuKONTROLU
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç
* "bildirimlerTaleplerimRenkbarıKontrolu" li element sayfada bulunuyor mu kontrol et

IOS Bildirimlerim Siparislerim tabinin siparişlerim webview gösterilmesi -91
--------------------------------------
 Tags:IOSBildirimlerimSiparislerimTabininSiparislerimWebviewGosterilmesi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından siparişlerim tabına geç
*"iptalEdilenTaleplerim" li element sayfada bulunuyor mu kontrol et

IOS Bildirimlerim Yeni Talep Ac Buton Kontrol
-----------------------
 Tags: IOSBildirimlerimYeniTalepAcButonKontrol
 Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç
* "yeniTalepAç" li element sayfada bulunuyor mu kontrol et

Webview Siparislerim Tab Kontrol IOS
------------------------------------
 Tags:webviewSiparislerimTabKontrolIOS
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
 Bildirimlerim sayfasından siparişlerim tabına geç
 "iptalEdilenTaleplerim" li element sayfada bulunuyor mu kontrol et

Bildirimlerim Taleplerim Tabı Statu Kontrol IOS
--------------------------------------
 Tags:bildirimlerimTaleplerimTabiStatuKontrolIOS
* IOS "5307458832" numarası ve "530530" şifresi ile giriş yapılmamıssa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından Taleplerim tabına geç
* "bildirimlerTaleplerimRenkbarıKontrolu" li element sayfada bulunuyor mu kontrol et

IOS Baslangic Deneme Calismicak
---------
Tags:IOSBaslangicDenemeCalismicak
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla
* "200","360" koordinatlarına tıkla