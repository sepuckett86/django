from django.http import HttpResponse
from django.shortcuts import render

from .models import Pairname, Currency, Exchange, Datablock

def basicForm(request):
    if request.method == 'POST':
        currency1 = request.POST.get('currency1')
        currency2 = request.POST.get('currency2')
        print(currency1, currency2)

    return render(request, 'organizer/basicForm.html', {'currencies': ['BTC', 'LTC', 'ETH']})

def homepage(request):
    data1 = Datablock.objects.all()[0]
    pair_list = data1.pairname.all()
    pair_string = " ".join([pair.name for pair in pair_list])
    output = "Pairname: " + pair_string

    return HttpResponse(output)
