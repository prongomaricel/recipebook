from django.shortcuts import render, redirect
from django.http import HttpResponse
from RecipeBookApp.models import Dish, Creator, Recipe


def RecipeBook(request):
    dishes = Creator.objects.all()
    return render(request, 'homepage.html', {'dishes' : dishes})

def Recipes(request):
    dishes = Creator.objects.all()
    return render(request, 'added.html',{'dishes' : dishes})


def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')

def Profile(request, cId):
    creatorId =Creator.objects.get(id=cId)
#   dishes = Dish.objects.filter(CreatorId=creatorId)
    return render(request, 'profile.html', {'CreatorId':creatorId})

#   return render(request, 'homepage.html')

def ViewList(request, cId):
    creatorId =Creator.objects.get(id=cId)
#   dishes = Dish.objects.filter(CreatorId=creatorId)
    return render(request, 'recipe.html', {'CreatorId':creatorId})

def NewList(request):
#   newCreator = Creator.objects.create()
    newCar = Creator.objects.create(crName=request.POST['fName'],crGender=request.POST['gender'],crEAddress=request.POST['fEAddress'], crContactNumber=request.POST['fContactNumber'])
#   Dish.objects.create(CreatorId=newCreator, crName=request.POST['fName'],)
    return redirect(f'/{newCar.id}/')

def ViewList2(request, cId):
    creatorId =Creator.objects.get(id=cId)
#   dishes = Dish.objects.filter(CreatorId=creatorId)
    return render(request, 'recipe_output.html', {'CreatorId':creatorId})

def AddDish(request, cId):
    creatorId = Creator.objects.get(id=cId)
    Dish.objects.create(CreatorId=creatorId, dNameofDish=request.POST['nNameofDish'],dMainIngredient=request.POST['nMainIngredient'],dDifficulty=request.POST['nDifficulty'],dCategory=request.POST['nCategory'],dServings=request.POST['nServings'],dPrep=request.POST['nPrepTime'],dCook=request.POST['nCookTime'],dTotal=request.POST['nTotalTime'], dDate=request.POST['nDate'],)#rQuantity=request.POST['nQuantity'],rIngredients=request.POST['nIngredients'],rProcedures=request.POST['nProcedures'],)
    return redirect(f'/{creatorId.id}/Recipe')


def UpdateRecipe(request, eId):
    CreatorId = Dish.objects.get(id=eId)
    CreatorId.dNameofDish = request.POST['nNameofDish']
    CreatorId.dMainIngredient = request.POST['nMainIngredient']
    CreatorId.dDifficulty = request.POST['nDifficulty']
    CreatorId.dCategory = request.POST['nCategory']
    CreatorId.dServings = request.POST['nServings']
    CreatorId.dPrep = request.POST['nPrepTime']
    CreatorId.dCook = request.POST['nCookTime']
    CreatorId.dTotal = request.POST['nTotalTime']
    CreatorId.save()
    return redirect('/')

def DeleteRecipe(request, eId):
    CreatorId = Dish.objects.get(id=eId)
    CreatorId.delete()
    return redirect('/')

def EditRecipe(request, eId):
    creatorId = Dish.objects.get(id=eId)
    context = {'CreatorId' : creatorId}
    return render (request, 'recipe_output.html', context)

# def Output(request, cId):
#     creatorId =Creator.objects.get(id=cId)
# #   dishes = Dish.objects.filter(CreatorId=creatorId)
#     return render(request, 'recipe_output.html', {'CreatorId':creatorId})

# def Dishes(request, cId):
#     creatorId = Creator.objects.get(id=cId)
#     Dish.objects.create(CreatorId=creatorId)#, dNameofDish=request.POST['nNameofDish'],dMainIngredient=request.POST['nMainIngredient'],dDifficulty=request.POST['nDifficulty'],dCategory=request.POST['nCategory'],dServings=request.POST['nServings'],)#rQuantity=request.POST['nQuantity'],rIngredients=request.POST['nIngredients'],rProcedures=request.POST['nProcedures'],)
#     return redirect(f'/{creatorId.id}/Dishes')






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
