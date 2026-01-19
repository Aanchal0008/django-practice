from django.shortcuts import redirect, render
from .models import Student

# Create your views here.

def student_home(request):
    if request.POST:
        data = request.POST
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
    return render(request, "student.html")