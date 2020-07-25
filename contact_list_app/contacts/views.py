from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Telephone, Email, Address

# Create your views here.


class Index(View):

    def get(self, request):
        all_contacts = Person.objects.all()
        return render(request, 'index.html', {'all_contacts': all_contacts})


class AddANewContact(View):

    def get(self, request):
        return render(request, 'add_a_new_contact.html')

    def post(self, request):

        new_person = Person()
        new_person.first_name = request.POST.get('first_name')
        new_person.last_name = request.POST.get('last_name')
        new_person.description = request.POST.get('description')
        new_person.save()

        telephone_number = request.POST.get('telephone_number')
        new_telephone = ""
        if not Telephone.objects.filter(telephone_number):
            new_telephone = Telephone()
            new_telephone.number = telephone_number
            new_telephone.type = request.POST.get('telephone_type')
            new_telephone.save()
        else:
            new_telephone = Telephone.objects.get(telephone_number)
        new_person.telephone = new_telephone

        email_address = request.POST.get('email_address')
        new_email = ""
        if not Email.objects.filter(email_address):
            new_email = Email()
            new_email.email_address = email_address
            new_email.type = request.POST.get('email_type')
            new_email.save()
        else:
            new_email = Email.objects.get(email_address)
        new_person.email = new_email

        # new_address = Address()
        # new_address.city = request.POST.get('city')
        # new_address.street_name = request.POST.get('street_name')
        # new_address.street_number = request.POST.get('street_number')
        # new_address.apartment_number = request.POST.get('apartment_number')
        # new_address.save()
        new_person.address = Address.objects.get_or_create(city=request.POST.get('city'),
                                                           street_name=request.POST.get('street_name'),
                                                           street_number=request.POST.get('street_number'),
                                                           apartment_number=request.POST.get('apartment_number'))[0]

        new_person.save()

        return redirect('index')


class ModifyAContact(View):

    def get(self, request, contact_id):
        contact = Person.objects.get(pk=contact_id)
        return render(request, 'modify_a_contact.html', {'contact': contact})

    def post(self, request, contact_id):
        contact = Person.objects.get(pk=contact_id)
        contact.first_name = request.POST.get("first_name")
        contact.last_name = request.POST.get("last_name")
        contact.description = request.POST.get("description")
        contact.address = Address.objects.get_or_create(city=request.POST.get('city'),
                                                        street_name=request.POST.get('street_name'),
                                                        street_number=request.POST.get('street_number'),
                                                        apartment_number=request.POST.get('apartment_number'))[0]
        contact.email = Email.objects.get_or_create(email_address=request.POST.get('email_address'),
                                                    type=request.POST.get('email_type'))[0]
        contact.telephone = Telephone.objects.get_or_create(number=request.POST.get('telephone_number'),
                                                            type=request.POST.get('telephone_type'))


class DeleteAContact(View):

    def get(self, request, contact_id):
        return render(request, 'delete_a_contact.html')

    def post(self, request, contact_id):
        Person.objects.get(pk=contact_id).delete()
        return redirect('index')


class ContactDetails(View):

    def get(self, request, contact_id):
        contact = Person.objects.get(pk=contact_id)
        return render(request, 'contact_details.html', {'contact': contact})
