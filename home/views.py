from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth import logout

# Create your views here.

def home(request):

    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]

        if title:
            Todo.objects.create(
                title = title,
                details = details,
               user=request.user
            )
            return redirect("/")

    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    else:
        todos = None
    return render(request, "index.html", {"todos":todos})

def delete_task(request, pk):
    todo = get_object_or_404(Todo, id=pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect("/")

def signout(request):
    logout(request)
    return redirect("signin")