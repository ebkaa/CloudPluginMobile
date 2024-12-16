Specification Heading
=====================
Created by sahabt on 11.12.2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Bildirimlerim Tabi Kontrolu
---------------------------
Tags:androidbildirimlerimTabıKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* "mesajlarım" li elementi bul ve tıkla


Mesajlarim Tabi Kontrolu
---------------------------
 Tags:androidMesajlarımTabKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li element sayfada bulunuyor mu kontrol et


Siparişlerim Tabi Kontrolu
---------------------------
 Tags:androidSiparislerimTabKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* Bildirimler sayfasına gir
* Bildirimlerim sayfasından siparişlerim tabına geç



Bireysel Kullanici ile Taleplerim Tabi Kontrolu
-----------------------------------------------
 Tags:androidBireyselKullaniciTaleplerimTabKontrolu
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
* "5" saniye bekle
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla
* "10" saniye bekle



Kurumsal Kullanici ile Taleplerim Tabi Kontrolu
-----------------------------------------------
 Tags:androidKurumsalKullaniciTaleplerimTabKontrolu
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
* "5" saniye bekle
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla
* "10" saniye bekle



Randevularim Tabi Kontrolu
--------------------------
 Tags:androidRandevularimTabKontrolu
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
* "5" saniye bekle
* Değeri "RANDEVULARIM" e eşit olan elementli bul ve tıkla
* "10" saniye bekle


AND Bildirimlerim sola kaydırıldığında sil butonunun cikmasi
-------------------------------------------------------------------------------
 Tags:ANDBildirimlerimSolaKaydirildigindaSilButonununCikmasi
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "4" saniye bekle
* "bildirimlerButonu" li elementi bul ve tıkla
*"4" saniye bekle
* "77","33" oranlarından "33","33" oranlarına "1" kere swipe et
* "SilBtn" li element sayfada bulunuyor mu kontrol et


AND Bildirim Bulunmadiginda Uyarı Mesajı Kontrol -80
--------------------------------------------------------
Tags:ANDBildirimBulunmadigindaUyarıMesajıKontrol
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
*"4" saniye bekle
* bildirimleri sil
* geri butonuna bas
* "bildirimlerButonu" li elementi bul ve tıkla
* "bidirimYokturUyarısı" li element sayfada bulunuyor mu kontrol et

AND Bildirimlerim SMS İceriginin Tek Satira Sigmadiginda Arti İsaretinin Gösterilmesi -84
------------------------------------------------
Tags:ANDBildirimlerimSMSİcerigininTekSatiraSigmadigindaArtiİsaretininGösterilmesi
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li element sayfada bulunuyor mu kontrol et
* "mesajlarımArtıİşareti" li element sayfada bulunuyor mu kontrol et
* "mesajlarımSpinner" li elementi bul ve tıkla
* "gonderilenSms" li elementi bul ve tıkla
* "mesajlarımArtıİşareti" li elementi bul varsa "Artı işareti bulunmaması gerekiyordu" mesajını hata olarak göster

AND Bildirimlerim Mesajlarim Ekraninda Gelen Giden Smsler Bir Arada Tarih Bazında Siralanmasi -85
-------------------------------------------------------
 Tags:ANDBildirimlerimMesajlarimEkranindaGelenGidenSmslerBirAradaTarihBazındaSiralanmasi
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li elementi bul ve tıkla
* "2" saniye bekle
* mesajlarım tarih sıralaması kontrolu

AND Bildirimlerim mesajlarım Search Alanina Harf Ya Da Sayi Yazildiginda Search Action Baslamasi -89
--------------------------------------------------------------------------------
Tags:ANDBildirimlerimMesajlarımSearchAlaninaHarfYaDaSayiYazildigindaSearchActionBaslamasi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li elementi bul ve tıkla
* "2" saniye bekle
* "BildirimlerMEsajlarSearchBar" li elementi bul ve "..." değerini yaz
* "BildirimlerMesajlar" li elementi bul varsa "Searchbara girilen degere göre tepki alınamadı" mesajını hata olarak göster



AND Mesajlarımda Arama Sonucu Mesaj Bulunamadı Uyarısı Alınması -90
-------------------------------------
 Tags:ANDMesajlarımdaAramaSonucuMesajBulunamadıUyarısıAlınması
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* "mesajlarım" li elementi bul ve tıkla
* "2" saniye bekle
* "BildirimlerMEsajlarSearchBar" li elementi bul ve "..." değerini yaz
* "mesajlarımSonuçBulunamadı" li element sayfada bulunuyor mu kontrol et

AND Bildirimlerim Sayfanin En Alt Kisminda Yeni Talep Ac butonunu yer almasi
---------------------------------------
Tags:ANDBildirimlerimSayfaninEnAltKismindaYeniTalepAcButonunuYerAlmasi
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla
* "yeniTalepAç" li element sayfada bulunuyor mu kontrol et


//TESTİNİUM DEĞİŞTİR tag Royalty
AND Bildirimlerim Kurumsal Kullanıcılarda Yeni Talep Aç Butonunun Olmaması -95
-------------------------------------
Tags:ANDBildirimlerimKurumsalKullanicilardaYeniTalepAcButonununOlmaması
* Numara:"5376441466" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla
* "yeniTalepAç" li elementi bul yoksa "kurumsal hesapta yeni talep aç butonu yok bulunması gerekir" mesajını hata olarak göster


AND Bildirimlerim Yeni Talep ac butonuna tiklandiginda Yeni Talep Ac Ekraninin Acilmasi -95
----------------------------------------------
Tags:ANDBildirimlerimYeniTalepAcbutonunatiklandigindaYeniTalepAcEkranininAcilmasi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla
* "yeniTalepAç" li elementi bul ve tıkla
* "5" saniye bekle
* "talepSayfarıKontrol" li element sayfada bulunuyor mu kontrol et

AND Bildirimlerim Randevu Talebi Bulunmayan Kullanıci Ekraninda Uyarı Degerinin Gösterilmesi -96
-------------------------------------------------
Tags:ANDBildirimlerimRandevuTalebiBulunmayanKullaniciEkranindaUyariDegerininGosterilmesi
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
* "5" saniye bekle
* Değeri "RANDEVULARIM" e eşit olan elementli bul ve tıkla
* "5" saniye bekle
* "talebinizBulunmamaktadirUyari" li element sayfada bulunuyor mu kontrol et

//corona
AND Bildirimlerim Randevu Talebi Bulunan Kullanıcı Ekranında Talep Detaylarının Yer Alması -97
-------------------------------------------------
Tags:ANDBildirimlerimRandevuTalebiBulunanKullaniciEkranindaTalepDetaylarininYerAlmasi
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "bildirimlerButonu" li elementi bul ve tıkla
 "5" saniye bekle
 Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
 "5" saniye bekle
 Değeri "RANDEVULARIM" e eşit olan elementli bul ve tıkla
 "randevuTarihi" li element sayfada bulunuyor mu kontrol et
  "randevuSebebi" li element sayfada bulunuyor mu kontrol et

//corona
AND Bildirimlerim Randevu Sayfasındaki Listelenen Randevularda İptal Detaylı Bilgi Butonunun Olması -98
-------------------------------------------------
 Tags:ANDBildirimlerimRandevuSayfasindakiListelenenRandevulardaIptalDetayliBilgiButonununOlmasi

 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
  "bildirimlerButonu" li elementi bul ve tıkla
  "5" saniye bekle
  Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
  "5" saniye bekle
  Değeri "RANDEVULARIM" e eşit olan elementli bul ve tıkla
  "detaylıBilgi" li element sayfada bulunuyor mu kontrol et


AND Bildirimlerim Non Turkcell Hesap Ile Işlem Merkezinde Sadece Bildirimlerim Tabının Olması -99
--------------------------------------------------
 Tags:ANDBildirimlerimNonTurkcellHesapIleIslemMerkezindeSadeceBildirimlerimTabininOlmasi
* Non turkcell num:"5054039973" şifre:"123456" ile giriş yapılmamışsa giriş yap
/* Numara:"5054039973" ve şifre:"123456" ile giriş yapılmamışsa giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
/* "islemMerkeziButonu" elementinin koordinatlarına x="20" y="-20" degerlerini ekleyerek tıkla
* Bildirimler sayfasına gir
* "bildirimlerMesajlarım" li elementi bul varsa "nonTurkcell Hesapta Sadece Bildirimlerim Sekmesi olmalı" mesajını hata olarak göster
* "bildirimlerRandevularım" li elementi bul varsa "nonTurkcell Hesapta Sadece Bildirimlerim Sekmesi olmalı" mesajını hata olarak göster
* 9973 çıkış yap


AND Bldirimlerim Superonline Hesap Ile Taleplerim TabiKontrolü -101
-----------------------------
 Tags:ANDBildirimlerimSuperonlineHesapIleTaleplerimTabiKontrolu

 * SuperOnline Hesabı ile giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla

AND Bildirimlerim Superonline hesap ile bildirimlerim tabı kontrolü -100
------------------------------------
 Tags:ANDBildirimlerimSuperonlineHesapIleBildirimlerimTabiKontrolu

 * SuperOnline Hesabı ile giriş yap
* "islemMerkeziButonu" li elementi bul ve tıkla
* "bildirimlerButonu" li elementi bul ve tıkla

AND Bildirimlerim Taleplerim Tabı Ust Kısmında Statu KONTROLU -92
--------------------------------------
 Tags:ANDBildirimlerimTaleplerimTabiUstKismindaStatuKONTROLU

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerButonu" li elementi bul ve tıkla
* "5" saniye bekle
* Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
* "5" saniye bekle
* Değeri "TALEPLERİM" e eşit olan elementli bul ve tıkla
* "3" saniye bekle
* "bildirimlerTaleplerimRenkbarıKontrolu" li element sayfada bulunuyor mu kontrol et


ANDBildirimlerim Siparislerim tabinin siparişlerim webview gösterilmesi -91
--------------------------------------
 Tags:ANDBildirimlerimSiparislerimTabininSiparislerimWebviewGosterilmesi
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "bildirimlerButonu" li elementi bul ve tıkla
 * "5" saniye bekle
 * Değeri "SİPARİŞLERİM" e eşit olan elementli bul ve tıkla
 * "5" saniye bekle
 *"iptalEdilenTaleplerim" li element sayfada bulunuyor mu kontrol et


AND Talep Ilet Yeni Talep Ilet Sayfasındak Onceki Talepleriniz Yazısına Tıklandığında Taleplerim Tabının Acilmasi -149
-------------------------------------------------------------------------------------------------------------------
  Tags:ANDTalepIletYeniTalepIletSayfasindakiOncekiTaleplerinizYazisinTiklandigindaTaleplerimTabininAcilmasi
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 * "yardımButonu" li elementi bul ve tıkla
 * "yeniTalepIlet" li elementi bul ve tıkla
 * "oncekiTaleplerim" li elementi bul ve tıkla
 * "taleplerimSekmesiCheck" li element sayfada bulunuyor mu kontrol et

AND Baslangic Deneme Calismicak
----------------
 Tags:ANDBaslangicDenemeCalismicak
* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "2" saniye bekle
* "570","1200" koordinatlarına tıkla
* "570","1200" koordinatlarına tıkla