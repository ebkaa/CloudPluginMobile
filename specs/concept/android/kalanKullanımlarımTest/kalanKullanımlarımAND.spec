Specification Heading
=====================
Created by sahabt on 2019-10-23

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

309
And Kalan Kullanımlarım Kartı Kontrol 8832
----------------
 Tags:AndKalanKullanimlarimKartiKontrol8832

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "kalanGünSayısı"li elementi bulana kadar "4" kere swipe yap ve elementi bul

310
And Kalan Kullanımlarım Kartı Kontrol 2468
----------------
 Tags:AndKalanKullanimlarimKartiKontrol2468
* Numara:"5338972468" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "kalanGünSayısı"li elementi bulana kadar "4" kere swipe yap ve elementi bul



AND kalan kullanım tarih kontrolü
-------
 Tags:ANDkalankullanimTarihKontrolu
 * Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
 * "dinamikKartlarıKapatmaIkonu" li elementi bul ve varsa tıkla
* "kalanGünSayısı"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* paket bitimi tarihi kontrolü yap hata alırsan "   tarih kontrolü eşleşmedi  " mesajını göster

AND Yenileme Bitis Kont
--------------
 Tags:ANDYenilemeBitisKont

* Numara:"5307458832" ve şifre:"530530" ile giriş yapılmamışsa giriş yap
* "paketAlButonu"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "yenilemeBitis" li elementi bul yoksa "yanlış formatta yazılmış" mesajını hata olarak göster

AND Kotasız Ürün Kalan Kullanımlar Kartı Kontrolü
-------------------------
Tags:ANDKotasizKalanKullanimlarKartiKont
* SuperOnline Hesabı ile giriş yap
* "btn_ekPaketAl"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "limitsizKullanimKarti" li elementi bul yoksa "limitsizKullanimKarti bulunamadı" mesajını hata olarak göster
* Sol limitsiz Kullanim Karti alan kontrolleri


AND Kademeli Kotalı Kalan Kullanım Ürün Kalan Kullanımlar Kartı Kontrolü
-------------------------
Tags:ANDKademeliKalanKullanimlarKartiKont
*Non turkcell num:"5349287820" şifre:"530530" ile giriş yapılmamışsa giriş yap
* "kablosuzIslem"li elementi bulana kadar "4" kere swipe yap ve elementi bul
* "kademeliKotaliKarti" li elementi bul yoksa "kademeliKotaliKarti bulunamadı" mesajını hata olarak göster
* Sol Kademeli Kullanim Karti alan kontrolleri

