from django.db import models

# Create your models here.


class Product(models.Model):


    COLORS = (
        ('white', 'WHITE'),
        ('black', 'BLACK'),
        ('yellow', 'YELLOW')
    )

    title = models.CharField(max_length=120)
    desc = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=10, choices=COLORS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        db_table = 'products'
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'