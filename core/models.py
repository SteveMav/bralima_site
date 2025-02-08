from django.db import models
from django.core.exceptions import ValidationError

class CompanyInfo(models.Model):
    slogan = models.CharField(max_length=255, help_text="Phrase d'accroche affichée sur l'accueil")
    history = models.TextField(help_text="Historique de l'entreprise")
    word_of_director = models.TextField(help_text="Mots de directeur de l'entreprise", null=True)
    mission = models.TextField(blank=True, null=True, help_text="Mission de l'entreprise")
    vision = models.TextField(blank=True, null=True, help_text="Vision de l'entreprise")
    values = models.TextField(blank=True, null=True, help_text="Valeurs fondamentales")
    logo = models.ImageField(upload_to="company/", blank=True, null=True, help_text="Logo de l'entreprise")
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if CompanyInfo.objects.exists() and not self.pk:
            raise ValidationError("Une seule instance de CompanyInfo est autorisée.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Informations de l'entreprise"
    
class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    event = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="gallery/")
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"


