from django.shortcuts import render

# added
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)

            # get the button name
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
                
                        
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete="False")
                else:
                    print("invalid input")
                
        
        return render(response, "polls/list.html", {"ls": ls})
    
    return render(response, "polls/home.html", {})


def home(response):
    return render(response, "polls/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            # 1 line below is for saving the data after User model is
            # applied into ToDoList model
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id) 
    else:
        form = CreateNewList()
    return render(response, "polls/create.html", {"form": form}) 

def view(response):
    return render(response, "polls/view.html", {})
