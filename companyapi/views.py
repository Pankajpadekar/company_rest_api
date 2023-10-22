from django.http import HttpResponse

def homme_page(request):
    print("home page requested")
    return HttpResponse("<h1>This is Home page</h1>")