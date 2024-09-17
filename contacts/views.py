from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm  # Import the ContactForm from your forms.py

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Added Successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def view_contact(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contacts/view_contact.html', {'contact': contact})

def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Updated Successfully!')
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update_contact.html', {'form': form})

def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, 'Contact Deleted Successfully!')
    return redirect('home')

def search_contacts(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(last_name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})