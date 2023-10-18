from django.db import transaction
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.utils import timezone
from django.contrib import messages  # Import messages module for displaying error messages

from datetime import timedelta

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contactsapp/list.html', {'contacts': contacts})

# def create_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Commit the transaction to save the new contact
#             transaction.commit()
#             return redirect('contact_list')
#     else:
#         form = ContactForm()
#     return render(request, 'contactsapp/contact_list.html', {'form': form})


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.date_joined = timezone.now()
            
            # Check if date_expired is earlier than date_joined
            if contact.date_expired and contact.date_expired < contact.date_joined:
                messages.error(request, "Date expired cannot be earlier than Date joined.")
                return redirect('create_contact')  # Redirect back to the create contact page with an error message
            
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contactsapp/contact_list.html', {'form': form})


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contactsapp/edit_contact.html',  {'contact': contact, 'form': form})

# def delete_contact(request, pk):
#     contact = Contact.objects.get(pk=pk)
#     if request.method == 'POST':
#         contact.delete()
#         return redirect('contact_list')
#     return render(request, 'contactsapp/delete_contact.html', {'contact': contact})




def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    
    # Check if date_expired is less than a year ago
    if contact.date_expired and (timezone.now() - contact.date_expired) <= timedelta(days=365):
        if request.method == 'POST':
            contact.delete()
            return redirect('contact_list')
    else:
        messages.error(request, "Date expired is more than a year ago. Cannot delete the contact.")
    
    return render(request, 'contactsapp/delete_contact.html', {'contact': contact})



