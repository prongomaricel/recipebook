from django.shortcuts import render, redirect
from django.http import HttpResponse
from RecipeBookApp.models import Dish, Creator


def RecipeBook(request):
    dishes = Creator.objects.all()
    return render(request, 'homepage.html',{'dishes' : dishes})


#   return render(request, 'homepage.html')

def ViewList(request, cId):
    creatorId =Creator.objects.get(id=cId)
#   dishes = Dish.objects.filter(CreatorId=creatorId)
    return render(request, 'next.html', {'CreatorId':creatorId})


def NewList(request):
#   newCreator = Creator.objects.create()
    newCar = Creator.objects.create(crName=request.POST['fName'],crGender=request.POST['fGender'], crEAddress=request.POST['fEAddress'], crContactNumber=request.POST['fContactNumber'])
#   Dish.objects.create(CreatorId=newCreator, crName=request.POST['fName'],)
    return redirect(f'/RecipeBookApp/{newCar.id}/')


def AddDish(request, cId):
    creatorId = Creator.objects.get(id=cId)
    Dish.objects.create(CreatorId=creatorId, dNameofDish=request.POST['nNameofDish'],dMainIngredient=request.POST['nMainIngredient'],dDifficulty=request.POST['nDifficulty'],dCategory=request.POST['nCategory'],dServings=request.POST['nServings'],)
    return redirect(f'/RecipeBookApp/{creatorId.id}/')

def dataManipulation(request):
    #Creating an entry
    creator = Creator(crName='Maricel Prongo', crGender='Male',)
    creator.save()

    #Read All Entries
    objects = Creator.objects.all()
    result = 'Printing all entiries in Creator model : <br>'
    for x in objects:
        res += x.crName+'<br>'

    #Read a specific entry:
    crName = Creator.objects.get(id = '1')
    res += 'Printing One enrty <br>'
    res += crName.Address


    #Delete an entry
    res += '<br> Deleting an entry <br>'
    crName.delete()

    #Update
    creator = Creator(crName='Maricel Prongo', crGender='Male')
    creator.save()
    res += 'Updating entry <br>'

    creator = Creator.objects.get(crName = 'Maricel Prongo')
    creator.crGender = "Female"
    creator.save()
    res = ""

    #Filtering data:
    qs = Dish.objects.filter(crName = 'Maricel Prongo')
    res += "Found : %s results <br>" %len(qs)

    #Ordering results
    qs = Creator.objects.order_by('crGender')
    for x in qs:
        res += crName + x.crGender +'<br>'
