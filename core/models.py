from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    slogan = models.CharField(max_length=255, help_text="Phrase d'accroche affichée sur l'accueil")
    history = models.TextField(help_text="Historique de l'entreprise")
    mission = models.TextField(blank=True, null=True, help_text="Mission de l'entreprise")
    vision = models.TextField(blank=True, null=True, help_text="Vision de l'entreprise")
    values = models.TextField(blank=True, null=True, help_text="Valeurs fondamentales")
    logo = models.ImageField(upload_to="company/", blank=True, null=True, help_text="Logo de l'entreprise")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Informations de l'entreprise"

