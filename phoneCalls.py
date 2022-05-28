import requests
import csv
users = []
slownik= {}
url = 'https://raw.githubusercontent.com/khashishin/repozytorium_z_plikiem_polaczenia/main/phoneCalls.csv'
r = requests.get(url, allow_redirects=True)
open('phoneCalls.csv', 'wb').write(r.content)
class Polaczenia():
     def __init__(self, filename):
        self.filename = filename
    
    def pobierz_najczesciej_dzwoniacego():
        with open(self.filename, 'r') as fin:
            reader = csv.reader(fin, delimiter=",")
            next(reader, None)
            for row in reader:
                if int(row[0]) not in slownik:
                    slownik[int(row[0])] = 1
                else:
                    slownik[int(row[0])] += 1

        list = [(k, v) for k, v in slownik.items() if v == max(slownik.values())]
        return list[0]

class SprawdzDzwoniacegoTest(TestCase):
    def test_czy_abonent_najczesciej_dzwoniacy_rozponany_poprawnie(self):
        mp = Polaczenia("phoneCalls.csv")
        wynik = mp.pobierz_najczesciej_dzwoniacego()
        self.assertEqual((226,5), wynik)
if __name__ == '__main__':
    print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())


