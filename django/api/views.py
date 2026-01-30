from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# model object- student
# def student_detail(request):
#    stu = Student.objects.get(id=1)
# #    print(stu)
#    serializer = StudentSerializer(stu)
# #    print(serializer.data)
#    json_data= JSONRenderer().render(serializer.data)
# #    print(json_data)
#    return HttpResponse(json_data, content_type="application/json")


# with the parameter
def student_detail(request,pk):
   stu = Student.objects.get(id=pk)
#    print(stu)
   serializer = StudentSerializer(stu)
#    print(serializer.data)
   json_data= JSONRenderer().render(serializer.data)
#    print(json_data)
   return HttpResponse(json_data, content_type="application/json")


def student_list(request):
   stu= Student.objects.all()
   serializer = StudentSerializer(stu, many=True)
   json_data= JSONRenderer().render(serializer.data)
   return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def student_create(request):
   if request.method == "POST":
      json_data = request.body
      print(f"request body contains {json_data}")
      stream = io.BytesIO(json_data)
      pythondata = JSONParser().parse(stream=stream)
      print(f"Python data is {pythondata}")
      serializer= StudentSerializer(data= pythondata)
      if serializer.is_valid():
         serializer.save()
         res={"msg":"Data Created"}
         json_data= JSONRenderer().render(res)
         print(json_data)
         return HttpResponse(json_data,content_type="application/json")
      json_data= JSONRenderer().render(serializer.errors)
      return HttpResponse(json_data,content_type="application/json")