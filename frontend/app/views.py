from django.shortcuts import render
import request

# Create your views here.
from django.utils.datastructures import MultiValueDict


def index(request):
    if request.method=='POST':
        archivos=""
        csv1= request.FILES['document1']
        data1=csv1.read()
        print("--------Clientes-------")
        print(str(data1))
        csv2 = request.FILES['document2']
        data2 = csv2.read()
        print("--------Juegos-------")
        print(str(data2))
        csv3 = request.FILES['document3']
        data3 = csv3.read()
        print("--------JuegoMas-------")
        print(str(data3))
        csv4 = request.FILES['document4']
        data4 = csv4.read()
        print("--------MC-------")
        print(str(data4))


        return render(request,'index.html')
    elif request.method=='GET':
        data="Hola perro"
        context={
            'data':data,
        }
        return render(request,'index.html',context)
