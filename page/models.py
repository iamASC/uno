from django.db import models

# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="В наличии")
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.SET_NULL)
    price = models.FloatField()
    def get_is_stock(self):
        if self.in_stock:
            return '+'
        else:
            return ''

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии)"
        return s

    class Meta:
        ordering = ['-price','name']
        unique_together = ('category', 'name', 'price')
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class BlogArticle(models.Model):
    title = models.CharField(unique_for_date="pubdate", max_length=1000)
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)
