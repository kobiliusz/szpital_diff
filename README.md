# szpital_diff
gdzie są świeżo zamknięte / otwarte szpitale?
## wymagania
- python i pip
- tabula-py
```pip install tabula-py```
- java (wymagana przez tabula-py)
## źródło plików
np dla województwa mazowieckiego:
https://www.nfz.gov.pl/biuletyn-informacji-publicznej-mazowieckiego-ow-nfz/wykaz-szpitali-zakwalifikowanych-do-psz/
## uruchomienie
```python szpital_diff.py [stary_pdf] [nowy_pdf]```
- gdzie [stary_pdf] i [nowy_pdf] mogą być ścieżkami względnymi, bezwzględnymi a nawet URL
## uwagi
- nie biorę odpowiedzialności za wykorzystanie skryptu w celu innym niż referencyjnym
- w obecnej postaci skrypt daje niestety (edit: już nie tak dużo) false positivów ze względu na błędy (głównie) i niekonsekwencje w wypełnianiu tych tabel przez MZ (np ulica raz jest Bosko a raz Bosco (sic)), wynik skryptu należy przejrzeć ręcznie
