from django.shortcuts import redirect, render
from .models import Student

# Create your views here.

def student_home(request):
    data = Student.objects.all()
    if request.POST:
        # data = request.POST
        # print("Post message received", data)
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        per = request.POST.get('per')
        photo = request.FILES.get('photo')
        print(roll, name, per, photo)
        Student.objects.create(
            roll = roll,
            stud_name = name,
            per = per,
            photo = photo
        )
        return redirect('/student/')
    # print(data)
    if request.GET.get('search'):
        # data = Student.objects.filter(roll=request.GET.get('search'))
        data = Student.objects.filter(stud_name__icontains=request.GET.get('search'))
    return render(request, "student.html", context={'data':data})

def edit_data(request, id):
    data = Student.objects.get(id=id)
    if request.POST:
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        per = request.POST.get('per')
        photo = request.FILES.get('photo')
        data.roll = roll
        data.stud_name = name
        data.per = per
        if photo:
            data.photo = photo
        data.save()
        return redirect('/student/')
    return render(request, 'edit.html', context={'data':data})

def delete_data(request, id):
    Student.objects.get(id=id).delete()
    return redirect("/student/")