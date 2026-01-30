from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method != "POST":
        JsonResponse({"error":"Request method should be POST"})
    
    try:
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        
        if not username or not password:
            return JsonResponse({"error":"username or password required"})
        
        if User.objects.filter(username= username).exists:
            return JsonResponse({"error":"user already exists"})    


    except json.JSONDecodeError:
        return JsonResponse({"error":"Invalid JSON"}, status= 400)
