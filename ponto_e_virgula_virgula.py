arquivo = open('CasosPorEstado.csv',encoding="Latin-1")      # Nome do arquivo de entrada
texto = arquivo.readlines()
arquivo.close()
resultado = []

for t in texto:
    aux = t.replace(";",",")
    resultado.append(aux)


arquivo = open("resultado.csv",'a', encoding="Latin-1")

for r in resultado:
    arquivo.write(r)

arquivo.close()

