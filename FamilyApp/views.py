from django.shortcuts import render
from FamilyApp.models import *
from FamilyApp.forms import *
from django.http import HttpResponse

def visualizar(request):

    return render(request, "FamilyApp/inicio.html") 

def resultados(request):

    if request.method == "GET":

        nombre = request.GET["nombre"]
            
        resultado = Spells.objects.filter(nombre__icontains = nombre)

        return render(request, "FamilyApp/resultados.html/", {"resultado":resultado, "busqueda":nombre})
   
    return render(request, f"FamilyApp/hechizos.html")

    
def spells(request):

    formulario1 = SpellsFormulario(request.POST or None)

    if request.method == "POST": 

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            hechizo = Spells(nombre = info["nombre"],
                             nivel = info["nivel"],
                             escuela = info["escuela"])

            hechizo.save()

            return render(request, "FamilyApp/inicio.html/")   

    return render(request, "FamilyApp/Hechizos.html/", {"form1": formulario1})


def monsters(request):

    formulario1 = MonstersFormulario(request.POST or None)

    if request.method == "POST": 

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            monster = Monsters(nombre = info["nombre"],
                               nivel_desafio = info["nivel_desafio"],
                               terreno = info["terreno"])

            monster.save()

            return render(request, "FamilyApp/inicio.html/")
        

    return render(request, "FamilyApp/monstruos.html/", {"form1": formulario1})


def weapons(request):

    formulario1 = WeaponsFormulario(request.POST or None)

    if request.method == "POST": 

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            weapon = Weapons(nombre = info["nombre"],
                               tipo = info["tipo"],
                               versatil = info["versatil"])

            weapon.save()

            return render(request, "FamilyApp/inicio.html/")
        

    return render(request, "FamilyApp/armas.html/", {"form1": formulario1})




    



    


