from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Message envoyé  avec succès')
            form.save()
            return redirect('contact:contact')
        else:
            messages.error(request, 'Erreur lors de l\'envoi du message')
            return redirect('contact:contact')

    else:
        form = ContactForm()   
    return render(request, 'contact/contact.html', {'form': form})

# Create your views here.
