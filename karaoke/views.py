from django.shortcuts import render

def index(request):
    context= {
        'nomes':[
            'eric',
            'bruno',
            'camila',
        ],
        'vazio': False,
        'teste': 'teste'
    return render(request, 'index.html', {'minha var':'hack station'})
