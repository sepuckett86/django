from django.http.response import HttpResponse

def homepage(request):
    return HttpResponse(
    '<h1>Hello (again) World!</h1>'

    )
