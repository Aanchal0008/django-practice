from django.shortcuts import render

# Create your views here.

def form_view(request):
    return render(request, 'accounts.html')

def table_view(request):
    emails = ["example@gmail.com", "abhinhi@gmail.com", "kuchbhi@gmail.com", "demo04@gmail.com", "afsana@gmail.com"]
    userids = ["example", "abhinhi", "kuchbhi", "demo", "afsana"]
    passwords = ['asd', 'fgh', 'jkl', 'qwe', 'rty']
    
    table = list(zip(emails, userids, passwords))
    return render(request, 'table.html', context={"table": table})