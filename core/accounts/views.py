from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Login

# Create your views here.

def form_view(request):
    if request.method == 'POST':
        userid = request.POST.get('userid', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not userid or not password:
            messages.error(request, 'Please enter both User ID and Password', extra_tags='danger')
            return render(request, 'accounts.html')
        
        # Check if user exists with matching credentials
        user = Login.objects.filter(user_id=userid, password=password).first()
        if user:
            messages.success(request, f'Welcome {userid}!', extra_tags='success')
            return redirect('/student/')
        else:
            messages.error(request, 'Invalid User ID or Password', extra_tags='danger')
    
    return render(request, 'accounts.html')

def table_view(request):
    emails = ["example@gmail.com", "abhinhi@gmail.com", "kuchbhi@gmail.com", "demo04@gmail.com", "afsana@gmail.com"]
    userids = ["example", "abhinhi", "kuchbhi", "demo", "afsana"]
    passwords = ['asd', 'fgh', 'jkl', 'qwe', 'rty']
    
    table = list(zip(emails, userids, passwords))
    return render(request, 'table.html', context={"table": table})

def login_data(request):
    if request.method == 'POST':
        userid = request.POST.get('userid', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        
        # Validation
        if not userid or not email or not password1 or not password2:
            messages.error(request, 'All fields are required', extra_tags='danger')
            return render(request, 'register.html')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match', extra_tags='danger')
            return render(request, 'register.html')
        
        if len(password1) < 6:
            messages.error(request, 'Password must be at least 6 characters', extra_tags='danger')
            return render(request, 'register.html')
        
        # Check if user already exists
        if Login.objects.filter(user_id=userid).exists():
            messages.error(request, 'User ID already exists', extra_tags='danger')
            return render(request, 'register.html')
        
        if Login.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered', extra_tags='danger')
            return render(request, 'register.html')
        
        # Create new user
        Login.objects.create(
            user_id=userid,
            password=password1,
            email=email
        )
        messages.success(request, 'Registration successful! Please login.', extra_tags='success')
        return redirect('/')
    
    return render(request, 'register.html')