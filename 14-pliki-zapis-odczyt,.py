file = open('countries_capitals.txt', 'w+')

countries_capitals = {'Poland': 'Warszawa', 'Czechia': 'Praga', 'Germany': 'Berlin'}

for country, capital in countries_capitals.items():
    file.write(country + ' - ' + capital + '\n')

file.close()

###

file = open('countries_capitals.txt')
for line in file.readline():
    print(line.strip())