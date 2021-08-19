from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST)
    print(dir(form))
    if form.is_valid():
        contact_response = Contact.objects.create(**form.cleaned_data)
        contact_response.save()

        return redirect(reverse_lazy('index'))

    else:
        return redirect(reverse_lazy('index'))
