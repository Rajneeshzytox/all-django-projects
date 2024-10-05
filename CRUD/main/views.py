from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader


from .models import StuData
import datetime 


# Create your views here.
def form(request):
    if(request.method == 'POST'):
        stu_name = request.POST.get('stu_name')
        roll_no = request.POST.get('roll_no')
        stu_class = request.POST.get('stu_class')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        date_of_entry = datetime.datetime.now()

        stu_object = StuData(stu_name=stu_name, roll_no=roll_no, stu_class=stu_class, gender=gender, dob=dob, date_of_entry=date_of_entry)
        stu_object.save()
         

    return render(request, 'form.html')

def viewData(request):
    template = loader.get_template('view.html')
    students = StuData.objects.all().values()
    context = {
        'students': students,
    }
 
    return HttpResponse(template.render(context, request))


def updateData(request, id):
    
    template = loader.get_template('update.html')
    
    if (request.method == 'POST'):
        stu_name = request.POST.get('stu_name')
        roll_no = request.POST.get('roll_no')
        stu_class = request.POST.get('stu_class')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')

        user = StuData.objects.get(id=id)
        user.stu_name = stu_name
        user.roll_no = roll_no
        user.gender = roll_no
        user.stu_class = stu_class
        user.gender = gender
        user.dob = dob

        user.save()

    student = StuData.objects.get(id=id)
    context = {
        'user': student,

    }
   
    return HttpResponse(template.render(context, request))


def deleteData(request, b):
    student = StuData.objects.get(id=b)
    student.delete()
    return HttpResponse("""
        user deleted
        <script>window.location.replace('/view-data')</script>
""")
