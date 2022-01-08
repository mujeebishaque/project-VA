from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class IndexView(View):
    def get(self, request):
        template = 'index.html'
        return render(request, template, context={})
    
    def post(self, request):
        template = 'index.html'
        return render(request, template, context={})