from django.db import models



class Category(models.Model):
    title = models.CharField(max_length= 70)
    title_en = models.CharField(max_length= 70)
    description = models.TextField()
    description_en = models.TextField()
    image = models.FileField(upload_to='images')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Categories'

class Tour(models.Model):
    title = models.CharField(max_length= 70)
    title_en = models.CharField(max_length= 70)
    description = models.TextField()
    description_en = models.TextField()
    image = models.FileField(upload_to='static/images')
    
    def __str__(self):
        return self.title
    


class Place(models.Model):
    title = models.CharField(max_length= 70)
    title_en = models.CharField(max_length= 70)
    description = models.TextField()
    description_en = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    ordering = models.IntegerField()
    image = models.FileField(upload_to='static/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Place')
    icon = models.FileField(upload_to='static/icons')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='Place')
    
    def __str__(self):
        return self.title
    
    