from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def academics(request):
    return render(request, "academics.html")

def event(request):
    return render(request, "event.html")

def admissions(request):
    return render(request, "admissions.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")


# Custom Error Pages
def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)

def custom_server_error(request):
    return render(request, "500.html", status=500)
