Specification Heading
=====================
Created by sahabt on 2019-10-14

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Arama Özel Tv+ log-out
----------------
 Tags:AramaOzelTvPlus
* "ızınVer" li elementi bul ve varsa tıkla
* Giriş yapılmışsa çıkış yap
* "aramaBtn" li elementi bul ve tıkla
* "aramaBar" li elementi bul ve "Tv+" değerini yaz
* "özelTv+" li elementi bul ve tıkla
* "2" saniye bekle
* "özelTv+Check" li element sayfada bulunuyor mu kontrol et

Bildirimlerim kontrol log-out
----------------
 Tags:BildirimlerimKontrollogout
* "ızınVer" li elementi bul ve varsa tıkla
* Giriş yapılmışsa çıkış yap
* "bildirimlerim" li elementi bul ve tıkla
* "bildirimlerimCheck" li element sayfada bulunuyor mu kontrol et
* "vazgeçBtnN" li elementi bul ve tıkla
* "2" saniye bekle
* "anaSayfaCheck" li element sayfada bulunuyor mu kontrol et

paketler kontrol log-out -58
----------------
 Tags:paketlerKontrollogout
* "ızınVer" li elementi bul ve varsa tıkla
* Giriş yapılmışsa çıkış yap
* "1" saniye bekle
* "paketlerTab" li elementi bul ve tıkla
* "inceleBtn"li elementi bulana kadar "2" kere swipe yap ve elementi bul
* "inceleBtn" li elementi bul ve tıkla
* "5" saniye bekle
* "7" kere yukarı doğru kaydır
* "1" saniye bekle
* "sıkcaSorulanSorular" li element sayfada bulunuyor mu kontrol et

paketler kontrol log-in
----------------
 Tags:paketlermKontrollogin
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "dijitalMagaza" li elementi bul ve tıkla
* "paketlerTab" li elementi bul ve tıkla
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "inceleBtn" li elementi bul ve tıkla
* "2" saniye bekle
* "turkcellKampanya" li element sayfada bulunuyor mu kontrol et

Bildirimlerim kontrol log-in
----------------
 Tags:BildirimlerimKontrollogin
* Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "5" saniye bekle
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "bildirimlerTabı" li elementi bul ve tıkla
* "2" saniye bekle
* "mesajlarım" li element sayfada bulunuyor mu kontrol et

hediye kutum log-in
---------
 Tags:HediyeKutumKontrol
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "hediyeKutum" li elementi bul ve tıkla
 "tarihçe" li elementi bul ve tıkla
* "tb_ayricaliklar" li elementi bul ve tıkla
* "2" saniye bekle
* "keşfet" li element sayfada bulunuyor mu kontrol et

Yeni Servis Alma log-in
-----------------------
 Tags:YeniServisAlmaLogin
 * Numara:"5307385720" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 *Dinamik kartları kapat
* Tum ürünlerim sayfasına git
* "4" kere yukarı doğru kaydır
* "yeniServisAlButonu" li elementi bul ve tıkla
* "3" saniye bekle
* "servislerCheck" li element sayfada bulunuyor mu kontrol et
