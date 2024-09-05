from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.mail import send_mail

from journaux.forms import ContactUsForm, JournalForm   # new
from .models import Journal

from django.contrib.auth.decorators import login_required

# VUE AVEC UNE DEF ET LA METHODE render()
def listeJournaux(request):
    # Objet de contexte => qui contient les data
    journaux = Journal.objects.all()

    # Appel du template en lui envoyant les data
    # La clé du dico "journaux" sera utilisée dans le template pr afficher les data
    return render(request, "journaux/journal_liste.html", {"journaux":journaux})


# VUE GENERIQUE, AVEC UNE CLASSE (dérivée de ListView)
class HomePageView(ListView):
    model = Journal
    template_name = "journaux/journal_liste.html"
    context_object_name = "journaux"

# Vue pour la page de détails
def journal_detail(request, id):
    journal = Journal.objects.get(id=id)
    return render(request, "journaux/journal_detail.html", {'journal':journal})

# La vue du formulaire de contact
def contact(request):

    # Méthode HTTP
    if request.method == "POST":
        # Formulaire avec les données
        form = ContactUsForm(request.POST)

        # Valider les données
        if form.is_valid():
            send_mail(
                subject = f'Message from {form.cleaned_data["name"] or "Anyone"}',
                message = form.cleaned_data["message"],
                from_email = form.cleaned_data["email"],
                recipient_list = ["admin@toto.com"],
            )

            # Après envoi de email, rediriger vers une page
            return redirect('email-sent')

    else:
       form = ContactUsForm()   # Affiche formulaire vide

    return render(request, "journaux/contact.html", {"form":form})


# Vue pour la page de confirmation d'envoi de l'email
def email_sent(request):
    return render(request, "journaux/email_sent.html")

# Ajouter un nouveau journal : menu réservé aux connectés = autorisation
@login_required(login_url="/users/login/", redirect_field_name=None)
# @login_required(login_url="/users/login/")
def journal_create(request):
    if request.method == 'POST':
        # form = JournalForm(request.POST) # 
        form = JournalForm(request.POST, request.FILES) # Upload
        if form.is_valid():
            # Nouveau Journal, sauvé en db et récupéré
            journal = form.save()
            
            # Redirection
            # avec arguments : url et id
            return redirect('journaux_detail', journal.id)

    else:
        form = JournalForm()

    return render(request,'journaux/journal_create.html', {'form': form}) 