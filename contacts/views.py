from django.shortcuts import render, get_object_or_404
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html',{
        'contacts': contacts
        })


def show_contact(request, contact_id):
        # contact = Contact.objects.get()
        contact = get_object_or_404(Contact, id=contact_id)
        return render(request, 'contacts/show_contact.html',{
            'contact': contact
        })
