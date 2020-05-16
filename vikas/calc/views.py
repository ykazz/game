from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html",{'name':"VIKAS07"})

def add(request):
    vala1=str(request.POST['a1'])
    vala2=str(request.POST['a2'])
    vala3=str(request.POST['a3'])
    vala4=str(request.POST['a4'])
    vala5=str(request.POST['a5'])
    vala6=str(request.POST['a6'])

    valb1=int(request.POST['b1'])
    valc1=int(request.POST['c1'])
    vald1=int(request.POST['d1'])
    vale1=int(request.POST['e1'])
    valf1=int(request.POST['f1'])
    valg1=int(request.POST['g1'])
    valh1=int(request.POST['h1'])
    vali1=int(request.POST['i1'])
    valj1=int(request.POST['j1'])
    valk1=int(request.POST['k1'])
    vall1=int(request.POST['l1'])
    valm1=int(request.POST['m1'])
    valn1=int(request.POST['n1'])
    valo1=int(request.POST['o1'])
    res1= valb1 + valc1 + vald1 + vale1 +valf1 + valg1 + valh1 + vali1 + valj1 + valk1 + vall1 + valm1 + valn1 + valo1

    valb2=int(request.POST['b2'])
    valc2=int(request.POST['c2'])
    vald2=int(request.POST['d2'])
    vale2=int(request.POST['e2'])
    valf2=int(request.POST['f2'])
    valg2=int(request.POST['g2'])
    valh2=int(request.POST['h2'])
    vali2=int(request.POST['i2'])
    valj2=int(request.POST['j2'])
    valk2=int(request.POST['k2'])
    vall2=int(request.POST['l2'])
    valm2=int(request.POST['m2'])
    valn2=int(request.POST['n2'])
    valo2=int(request.POST['o2'])
    res2= valb2 + valc2 + vald2 + vale2 +valf2 + valg2 + valh2 + vali2 + valj2 + valk2 + vall2 + valm2 + valn2 + valo2

    valb3=int(request.POST['b3'])
    valc3=int(request.POST['c3'])
    vald3=int(request.POST['d3'])
    vale3=int(request.POST['e3'])
    valf3=int(request.POST['f3'])
    valg3=int(request.POST['g3'])
    valh3=int(request.POST['h3'])
    vali3=int(request.POST['i3'])
    valj3=int(request.POST['j3'])
    valk3=int(request.POST['k3'])
    vall3=int(request.POST['l3'])
    valm3=int(request.POST['m3'])
    valn3=int(request.POST['n3'])
    valo3=int(request.POST['o3'])
    res3= valb3 + valc3 + vald3 + vale3 +valf3 + valg3 + valh3 + vali3 + valj3 + valk3 + vall3 + valm3 + valn3 + valo3


    valb4=int(request.POST['b4'])
    valc4=int(request.POST['c4'])
    vald4=int(request.POST['d4'])
    vale4=int(request.POST['e4'])
    valf4=int(request.POST['f4'])
    valg4=int(request.POST['g4'])
    valh4=int(request.POST['h4'])
    vali4=int(request.POST['i4'])
    valj4=int(request.POST['j4'])
    valk4=int(request.POST['k4'])
    vall4=int(request.POST['l4'])
    valm4=int(request.POST['m4'])
    valn4=int(request.POST['n4'])
    valo4=int(request.POST['o4'])
    res4= valb4 + valc4 + vald4 + vale4 +valf4 + valg4 + valh4 + vali4 + valj4 + valk4 + vall4 + valm4 + valn4 + valo4

    

    valb5=int(request.POST['b5'])
    valc5=int(request.POST['c5'])
    vald5=int(request.POST['d5'])
    vale5=int(request.POST['e5'])
    valf5=int(request.POST['f5'])
    valg5=int(request.POST['g5'])
    valh5=int(request.POST['h5'])
    vali5=int(request.POST['i5'])
    valj5=int(request.POST['j5'])
    valk5=int(request.POST['k5'])
    vall5=int(request.POST['l5'])
    valm5=int(request.POST['m5'])
    valn5=int(request.POST['n5'])
    valo5=int(request.POST['o5'])
    res5= valb5 + valc5 + vald5 + vale5 +valf5 + valg5 + valh5 + vali5 + valj5 + valk5 + vall5 + valm5 + valn5 + valo5

    
    valb6=int(request.POST['b6'])
    valc6=int(request.POST['c6'])
    vald6=int(request.POST['d6'])
    vale6=int(request.POST['e6'])
    valf6=int(request.POST['f6'])
    valg6=int(request.POST['g6'])
    valh6=int(request.POST['h6'])
    vali6=int(request.POST['i6'])
    valj6=int(request.POST['j6'])
    valk6=int(request.POST['k6'])
    vall6=int(request.POST['l6'])
    valm6=int(request.POST['m6'])
    valn6=int(request.POST['n6'])
    valo6=int(request.POST['o6'])
    res6= valb6 + valc6 + vald6 + vale6 +valf6 + valg6 + valh6 + vali6 + valj6 + valk6 + vall6 + valm6 + valn6 + valo6



    
    
    return render(request,"result.html",{'Result1':res1, 'Result2':res3, 'Result3':res3, 'Result4':res4, 'Result5':res5, 'Result6':res6 , 'A1':vala1 , 'A2':vala2 , 'A3':vala3 , 'A4':vala4 , 'A5':vala5 , 'A6':vala6})



    