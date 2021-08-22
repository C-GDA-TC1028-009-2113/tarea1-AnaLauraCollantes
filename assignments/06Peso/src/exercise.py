def main():
    #escribe tu código abajo de esta línea
    peso_i = float(input('Dame el peso inicial: '))
    peso_f = float(input('Dame el peso final: '))
    meses = int(input('Dame la cantidad de meses: '))
    peso_por_mes = (peso_i-peso_f)/meses
    print('Lo que debes bajar por mes es: '+ str(peso_por_mes))






if __name__ == '__main__':
    main()
