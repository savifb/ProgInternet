paises = ['Brasil', 'Argentina', 'França', 'Bélgica', 'Egito', 'Uruguai', 'Suécia']



paises.insert(len(paises),'Chile')

paises.remove('Argentina')

del paises[3]

paises.insert(int((len(paises))/2), 'Argélia')

print(paises)

paises.insert(int((len(paises))/2), 'Austrália')

print(paises)