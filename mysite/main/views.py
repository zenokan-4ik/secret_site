from django.shortcuts import render
from django.http import HttpResponse
from .models import Secret
from django.views.decorators.csrf import csrf_exempt

def index(request):
    data = {
        'data': [i.get_data()['text'] for i in Secret.objects.all()]
    }
    return render(request, 'main/index.html', data)

@csrf_exempt
def add(request):
    text = request.POST.get('text')
    new = Secret(text=text)
    new.save()
    return HttpResponse('Успешно! Ты молодец!')

@csrf_exempt
def view(request):
    key = request.POST.get('key')
    if key != '1324':
        return HttpResponse('False')
    else:
        return HttpResponse('True')