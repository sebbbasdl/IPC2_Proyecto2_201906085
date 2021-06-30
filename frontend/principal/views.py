import os

from django.shortcuts import render
import request
import re
from unicodedata import normalize
#import pathlib
#from pathlib import Path
#from os import path
def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122)

def isNumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)


def nombre(nom):
    # Sirve para nombreC, apellidoC
    patronNombres=  '^[a-zA-Z]*$'

    nom= re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize("NFD", nom), 0, re.I)

    nom=normalize('NFC', nom)

    print(nom)

    return bool(re.search(patronNombres,nom))


def nombreMC(nom):
    patronNombres = '^[a-zA-Z ]*$'

    nom = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize("NFD", nom), 0, re.I)

    nom = normalize('NFC', nom)

    print(nom)

    return bool(re.search(patronNombres, nom))





def nombreJuegos(nom):
    patronNombres = '^[a-zA-Z .:]*$'

    nom = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize("NFD", nom), 0, re.I)

    nom = normalize('NFC', nom)

    print(nom)

    return bool(re.search(patronNombres, nom))


def fechas(fecha):
    patronFechas='(\d{2})[/](\d{2})[/.-](\d{4})$'

    return bool(re.search(patronFechas, fecha))




def enteros(num):
    patronNum='^[1-9]\d*$'

    return bool(re.search(patronNum, num))



def puntoD(num):
    patronNum = '^[1-9]\d*(\.\d+)$'

    return bool(re.search(patronNum, num))



def lanza(year):
    patronNum = '\d\d\d\d'

    return bool(re.search(patronNum, year))

def nombreP(nom):
    patronNum = '^[a-zA-Z ]*$'

    return bool(re.search(patronNum, nom))

def clas(c):
    var=False

    if c=="E" or c=="T" or c=="M":
        var=True
    else:
        var=False

    return var


def verificacion1(lista):
    n=len(lista)
    var =False

    for a in range(n):
        name=lista[a][0]
        ape=lista[a][1]
        edad=lista[a][2]
        fecha1=lista[a][3]
        fecha2=lista[a][4]
        if str(nombre(str(name)))=="True" and str(nombre(str(ape)))=="True" and str(enteros(str(edad))) =="True" and str(fechas(str(fecha1)))=="True" and str(fechas(str(fecha2)))=="True":
            var=True
        else:
            var=False
            break
    return var







##VISTAS

def index(request):
    if request.method=='POST':
        # arch=archivo.read()
        # print(arch)
        # data1=csv1.read()
        csv1= request.FILES['document1']
        nombre1=request.FILES.get('document1')
        ruta1="C:\\Users\\sebas\\Downloads\\"+str(nombre1)

        archivo=open(ruta1,'r')
        print("--------Clientes-------")

        listaC=[]
        for filas in archivo:
            filas = filas.rstrip()
            divi = ","  # split
            listaU = filas.split(divi)
            listaC.append(listaU)
        print(listaC)








        """listad1=list(str(data1))
        listad1.pop(0)
        listad1.pop(0)
        listad1.pop(len(listad1)-1)
        for listaC in listad1:
            clientes+=str(listaC)

        print("--------Clientes-------")
        print(clientes)"""



        csv2 = request.FILES['document2']
        data2 = csv2.read()
        nombre2 = request.FILES.get('document2')
        ruta2 = "C:\\Users\\sebas\\Downloads\\" + str(nombre2)

        archivo2 = open(ruta2, 'r')
        print("--------Juegos-------")

        listaJ = []
        for filas2 in archivo2:
            filas2 = filas2.rstrip()
            divi = ","  # split
            listaUJ = filas2.split(divi)
            listaJ.append(listaUJ)
        print(listaJ)

        csv3 = request.FILES['document3']
        data3 = csv3.read()
        nombre3 = request.FILES.get('document3')
        ruta3 = "C:\\Users\\sebas\\Downloads\\" + str(nombre3)

        archivo3 = open(ruta3, 'r')
        print("--------JuegosMasVendidos-------")

        listaJM = []
        for filas3 in archivo3:
            filas3 = filas3.rstrip()
            divi = ","  # split
            listaUJM = filas3.split(divi)
            listaJM.append(listaUJM)
        print(listaJM)



        csv4 = request.FILES['document4']
        data4 = csv4.read()
        nombre4 = request.FILES.get('document4')
        ruta4 = "C:\\Users\\sebas\\Downloads\\" + str(nombre4)

        archivo4 = open(ruta4, 'r')
        print("--------MC-------")

        listaMC = []
        for filas4 in archivo4:
            filas4 = filas4.rstrip()
            divi = ","  # split
            listaUMC = filas4.split(divi)
            listaMC.append(listaUMC)
        print(listaMC)


        return render(request,'index.html')

    elif request.method=='GET':
        data="Hola perro"
        context={
            'data':data,
        }
        return render(request,'index.html',context)
