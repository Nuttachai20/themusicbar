from django.shortcuts import render


def index(request):
        return render( request,'frontend/index.html')
def about(request):
        return render( request,'frontend/about.html')
def contact(request):
        return render( request,'frontend/contact.html')
def citypop(request):
        return render( request,'frontend/citypop.html')
def funk(request):
        return render( request,'frontend/funk.html')
def bedroompop(request):
        return render( request,'frontend/bedroompop.html')


