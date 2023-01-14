from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat


# Create your views here.
def index(request):
    contacts = Contact.objects.order_by('name').filter(
        show=True
    )
    paginator = Paginator(contacts, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html',{
        'contacts': contacts
        })


def show_contact(request, contact_id):
        # contact = Contact.objects.get()
        contact = get_object_or_404(Contact, id=contact_id)

        if not contact.show:
            raise Http404()

        return render(request, 'contacts/show_contact.html',{
            'contact': contact
        })


def find(request):
    termo = request.GET.get('termo')
    campos = Concat('name', Value(' '), 'last_name')
    # contacts = Contact.objects.order_by('name').filter(
    #    Q(name__icontains=termo) | Q(last_name__icontains=termo),
        
    #    show=True
    # )
    contacts = Contact.objects.annotate(
        full_name = campos
        ).filter(
            Q(full_name__icontains=termo) | Q(phone__icontains=termo)
        )
    paginator = Paginator(contacts, 3)
    pages = request.GET.get('p')
    contacts = paginator.get_page(pages)

    return render(request, 'contacts/find.html',{
        'contacts': contacts
    })