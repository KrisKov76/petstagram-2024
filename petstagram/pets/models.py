from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)  # Първо съхраняваме обекта, за да получи ID
            self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)  # Запазваме отново, за да се съхрани slug-а

    def __str__(self):
        return self.name
