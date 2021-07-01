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
    patronNombres = '^[a-zA-Z0-9 .:]*$'

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

def verificacion2(lista):
    n = len(lista)
    var = False

    for a in range(n):
        name = lista[a][0]
        pla = lista[a][1]
        year = lista[a][2]
        cate = lista[a][3]
        stock = lista[a][4]
        if str(nombreJuegos(str(name))) == "True" and str(nombreJuegos(str(pla))) == "True" and str(
                lanza(str(year))) == "True" and str(clas(str(cate))) == "True" and str(
                enteros(str(stock))) == "True":
            var = True
        else:
            var = False
            break
    return var

def verificacion3(lista):
    n = len(lista)
    var = False

    for a in range(n):
        name = lista[a][0]
        fecha1 = lista[a][1]
        copias = lista[a][2]
        stock = lista[a][3]
        if str(nombreJuegos(str(name))) == "True" and str(fechas(str(fecha1))) == "True" and str(
                enteros(str(copias))) == "True" and str(enteros(str(stock))) == "True":
            var = True
        else:
            var = False
            break
    return var

def verificacion4(lista):
    n = len(lista)
    var = False

    for a in range(n):
        name = lista[a][0]
        fecha1 = lista[a][1]
        cantidad = lista[a][2]
        monto = lista[a][3]
        if str(enteros(str(monto)))=="True":
            monto1=str(monto)
            monto1+=".00"
            montox="True"
            print("entero")
        elif str(puntoD(str(monto)))=="True":
            monto1=monto
            print("es decimal")
            montox="True"
        else:
            montox="False"


        if str(nombreJuegos(str(name))) == "True" and str(fechas(str(fecha1))) == "True" and str(
                enteros(str(cantidad))) == "True" and montox == "True":
            var = True
        else:
            var = False
            break
    return var

def xml1(lista):
    n=len(lista)
    xml=""
    for a in range(n):
        name=lista[a][0]
        ape=lista[a][1]
        edad=lista[a][2]
        fecha1=lista[a][3]
        fecha2=lista[a][4]

        xml+="\t<clientes>\n" \
             "\t\t<nombre>"+str(name)+"</nombre>\n" \
             "\t\t<apellido>"+str(ape)+"</apellido>\n" \
             "\t\t<edad>"+str(edad)+"</edad>\n" \
             "\t\t<fechaCumpleaños>"+str(fecha1)+"</fechaCumpleaños>\n" \
             "\t\t<fechaPrimeraCompra>"+str(fecha2)+"</fechaPrimeraCompra>\n" \
             "\t</clientes>\n"

    return xml

def xml2(lista):
    n=len(lista)
    xml=""
    for a in range(n):
        name = lista[a][0]
        pla = lista[a][1]
        year = lista[a][2]
        cate = lista[a][3]
        stock = lista[a][4]

        xml+="\t<juegos>\n" \
             "\t\t<nombre>"+str(name)+"</nombre>\n" \
             "\t\t<plataforma>"+str(pla)+"</plataforma>\n" \
             "\t\t<añoLanzamiento>"+str(year)+"</añoLanzamiento>\n" \
             "\t\t<clasificacion>"+str(cate)+"</clasificacion>\n" \
             "\t\t<stock>"+str(stock)+"</stock>\n" \
             "\t</juegos>\n"

    return xml

def xml3(lista):
    n=len(lista)
    xml=""
    for a in range(n):
        name = lista[a][0]
        fecha1 = lista[a][1]
        copias = lista[a][2]
        stock = lista[a][3]

        xml+="\t<juegosMasVendidos>\n" \
             "\t\t<nombre>"+str(name)+"</nombre>\n" \
             "\t\t<fechaUltimaCompra>"+str(fecha1)+"</fechaUltimaCompra>\n" \
             "\t\t<copiasVendidas>"+str(copias)+"</copiasVendidas>\n" \
             "\t\t<stock>"+str(stock)+"</stock>\n" \
             "\t</juegosMasVendidos>\n"

    return xml

def xml4(lista):
    n=len(lista)
    xml=""
    for a in range(n):
        name = lista[a][0]
        fecha1 = lista[a][1]
        cantidad = lista[a][2]
        monto = lista[a][3]
        if str(enteros(str(monto))) == "True":
            monto1 = str(monto)
            monto1 += ".00"
            montox = "True"
            print("entero")
        elif str(puntoD(str(monto))) == "True":
            monto1 = monto
            print("es decimal")
            montox = "True"
        else:
            montox = "False"

        xml+="\t<mejoresClientes>\n" \
             "\t\t<nombre>"+str(name)+"</nombre>\n" \
             "\t\t<fechaUltimaCompra>"+str(fecha1)+"</fechaUltimaCompra>\n" \
             "\t\t<cantidadComprada>"+str(cantidad)+"</cantidadComprada>\n" \
             "\t\t<cantidadGastada>"+str(monto1)+"</cantidadGastada>\n" \
             "\t</mejoresClientes>\n"

    return xml

##VISTAS

def index(request):
    if request.method=='POST':
        xmlTOTAL=""
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



        veri1=verificacion1(listaC)
        veri2 = verificacion2(listaJ)
        veri3 = verificacion3(listaJM)
        veri4 = verificacion4(listaMC)

        if str(veri1)=="True" and str(veri2)=="True" and str(veri3)=="True" and str(veri4)=="True":
            data="Los archivos CSV no contienen ningun error"
            xml11=str(xml1(listaC))
            xml22=str(xml2(listaJ))
            xml33=str(xml3(listaJM))
            xml44=str(xml4(listaMC))
            xmlTOTAL+="<Chet>\n"
            xmlTOTAL+=xml11
            xmlTOTAL += xml22
            xmlTOTAL += xml33
            xmlTOTAL += xml44
            xmlTOTAL += "</Chet>"
            context={
                'data':data,
                'str_xml':xmlTOTAL
            }
        else:
            data="Los archivos CSV poseen algun error"
            context={
                'data':data
            }




        return render(request,'index.html',context)

    elif request.method=='GET':
        data=""
        context={
            'data':data,
        }
        return render(request,'index.html',context)
