# szpital_diff
gdzie są świeżo zamknięte / otwarte szpitale?
## zależności
- python i pip
- tabula-py
```pip install tabula-py```
- java (wymagana przez tabula-py)
## źródło plików
https://www.nfz.gov.pl/biuletyn-informacji-publicznej-mazowieckiego-ow-nfz/wykaz-szpitali-zakwalifikowanych-do-psz/
## uruchomienie
```python szpital_diff.py [stary_pdf] [nowy_pdf]```
- gdzie [stary_pdf] i [nowy_pdf] mogą być ścieżkami względnymi, bezwzględnymi a nawet URL
## uwagi
- nie biorę odpowiedzialności za wykorzystanie skryptu w celu innym niż referencyjnym
- w obecnej postaci skrypt daje niestety dużo false positivów ze względu na błędy i niekonsekwencje w wypełnianiu tych tabel przez MZ (pisanie nazwy ulic raz z imieniem raz bez, inny zapis numeru budynku itd), wynik skryptu należy przejrzeć ręcznie
