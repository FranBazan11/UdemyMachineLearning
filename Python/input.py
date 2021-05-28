carta = '3c'

##convierto la parte de string en un entero o int con el metodo int()
parteNumericaDeLaCarta = (int(carta[0])-1)

##convierto la parte de int en algo de tipo string con str() ya que carta por como lo definimos es un string
cartaAnterior = str(parteNumericaDeLaCarta) + carta[1]

cartaPosterior = str((int(carta[0])+1)) + carta[1]
print(cartaAnterior)
print(cartaPosterior)