from bs4 import BeautifulSoup
f = open("tableau.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')
f.close()

for ligne in soup.find_all('tr'):
    cols = ligne.find_all('td')
    if len(cols) > 1:
        num_dep = cols[0].string
        if num_dep is None:
            num_dep = cols[0].contents[1].string
        nom_dep = cols[1].find_all('a')[0].string
        prefs = cols[5]
        for pref in prefs.find_all('a'):
            b = pref.find('b')
            if not (b is None):
                main_pref = b.string
            print(pref.string)
        print(num_dep, nom_dep, main_pref)
    print('_______')
