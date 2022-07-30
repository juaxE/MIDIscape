# Määrittelydokumentti
Opinto-ohjelma: TKT

### Projektin aihe ja toteutus
Lähden ratkaisemaan esimerkkiaihetta koneoppimisen piiristä, laskennallisesta luovuudesta musiikissa. Toteutukseen käytän ainakin esimerkissä mainittuja Markovin ketjua ja trie-tietorakennetta.

Ohjelmalle on tarkoitus syöttää joukko MIDI-tiedostoja. Lähtökohtaisesti ideana on syöttää pelin **Old School Runescape**-musiikkia [kattavasta_kirjastosta](https://drive.google.com/drive/folders/19X4_7DKZikAEveTaLT2B0HfwFeYZLoaP). Mikäli laatu tai määrä ei ole projektiin sopiva, harkitaan muita vaihtoehtoja. Ohjelma käy tiedostot [MIDO-kirjastoa](https://mido.readthedocs.io/en/latest/) hyödyntäen läpi nuotti nuotilta ja luo trie-tietorakenteen joka kuvastaa melodiakulkujen todennäköisyyttä. Tämän jälkeen ohjelma generoi uuden MIDI-tiedoston opitun perusteella Markovin ketjua soveltaen.

Pseudokoodina esitettynä ohjelma on kutakuinkin seuraavanlainen:
n=kappaleiden määrä
m=nuottien määrä
for i=0 to n-1
    for j=0 to m-1
        if(j!=0)
        trie[j-1][j]++
generoi(x)

Aikavaativuudeltaan ohjelma olisi yksinkertaisessa muodossaan siis kahden silmukan vuoksi enintään O(n^2) ja tilavaativuudeltaan enintään O(n). Optimoitavaa voi hyvin olla sillä en vielä ymmärrä kovin perusteellisesti algoritmia ja tietorakennetta.




### (Ohjelmointi)kielet
Toteutan projektin ensisijaisesti Python-ohjelmointikielellä. Vertaisarvioida voin myös Javaa ja JavaScriptiä. Toteutan projektin mahdollisimman suomeksi.

