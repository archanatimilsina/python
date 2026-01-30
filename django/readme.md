# Django Movies CRUD App

A simple Django CRUD application for managing movies using
Function-Based Views and HTML templates.

---

##  Model

~~~python
from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
~~~

---

##  Views

~~~python
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies


def list_movie(request):
    movies = Movies.objects.all()
    return render(request, "home/index.html", {"movies": movies})


def create_movie(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Movies.objects.create(name=name)
        return redirect("list_movie")
    return render(request, "home/create.html")


def update_movie(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        movie.name = request.POST.get("name")
        movie.save()
        return redirect("list_movie")
    return render(request, "home/update.html", {"movie": movie})


def delete_movie(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("list_movie")
    return render(request, "home/delete.html", {"movie": movie})


def about_view(request):
    return HttpResponse("<h1>About Us</h1>")
~~~

---

##  URLs

~~~python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_movie, name="list_movie"),
    path("create/", views.create_movie, name="create_movie"),
    path("update/<int:pk>/", views.update_movie, name="update_movie"),
    path("delete/<int:pk>/", views.delete_movie, name="delete_movie"),
]
~~~

---

## Templates

### templates/home/index.html

~~~html
<h1>Movies</h1>
<a href="{% url 'create_movie' %}">Add Movie</a>

<ul>
  {% for movie in movies %}
    <li>
      {{ movie.name }}
      <a href="{% url 'update_movie' movie.id %}">Edit</a>
      <a href="{% url 'delete_movie' movie.id %}">Delete</a>
    </li>
  {% empty %}
    <li>No movies available</li>
  {% endfor %}
</ul>
~~~

---

### templates/home/create.html

~~~html
<h1>Create Movie</h1>

<form method="post">
  {% csrf_token %}
  <input type="text" name="name" placeholder="Movie name" required>
  <button type="submit">Save</button>
</form>
~~~

---

### templates/home/update.html

~~~html
<h1>Update Movie</h1>

<form method="post">
  {% csrf_token %}
  <input type="text" name="name" value="{{ movie.name }}" required>
  <button type="submit">Update</button>
</form>
~~~

---

### templates/home/delete.html

~~~html
<h1>Delete Movie</h1>

<p>Are you sure you want to delete "{{ movie.name }}"?</p>

<form method="post">
  {% csrf_token %}
  <button type="submit">Yes, Delete</button>
</form>
~~~

---

## Run Commands

~~~bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~



username = 'archana'
password = shine

incase you forget the password use this code
python3 manage.py shell 
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='your_superuser_username')
user.set_password('new_strong_password')
user.save()

