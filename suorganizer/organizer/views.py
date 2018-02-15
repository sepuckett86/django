from django.http.response import HttpResponse

from .models import Tag, Startup, NewsLink

def homepage(request):
    tag_list = Tag.objects.all()
    startup_list = Startup.objects.all()
    output = ", ".join([tag.name for tag in tag_list])
    output = output + '<br>'
    output = output + ", ".join([startup.name for startup in startup_list])
    output = output + '<br>'
    return HttpResponse(output)
