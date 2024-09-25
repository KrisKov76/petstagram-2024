from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)  # запазва обекта в базата, без super().save не се запазва в базата

# функцията slugify замества всякакви спейсове с тирета и всякакви символи, които не са ASCII ги премахва
