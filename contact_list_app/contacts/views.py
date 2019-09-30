from django.shortcuts import render
from django.views import View
from .models import Person

# Create your views here.


class Index(View):

    def get(self, request):

        all_contacts = Person.objects.all()
        return render(request, 'index.html', {'all_contacts': all_contacts})
