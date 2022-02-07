from django.db import models
from distutils.command import upload
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.


class Posteos(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
#    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Fecha y hora
    created_on = models.DateTimeField(auto_now_add=True)
    # Solo fecha
    created_on = models.DateField(auto_now_add=True)

# Default human-readable representation of the object.
# Django will use it in many places, such as the administration site.
    def __str__(self):
        return 'Creado el: ' + str(self.created_on) + ' - ' + self.title

    class Meta:
        ordering = ['-created_on']

# Adonde mandar despues de la creacion
    # def get_absolute_url(self):
    #     return reverse('home')
