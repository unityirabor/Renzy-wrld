from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
      category_name = models.CharField(max_length=100, unique= True)
      slug = models.SlugField(max_length=200, unique=True)
      description = models.TextField(max_length=255, blank=True)
      cat_image = models.ImageField(upload_to='photos/categories', blank=True)
      is_available  = models.BooleanField(default=True)

      #changing model plural name
      class Meta:
        verbose_name = "category",
        verbose_name_plural = 'categories',

      def get_url(self):
        return reverse('products_by_category', args=[self.slug])

      def __str__(self):
            return self.category_name
       
