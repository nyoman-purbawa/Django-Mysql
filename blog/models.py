from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Render(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model): 
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    fill = models.TextField(null=True)
    
    OPTION_CATEGORY = [
        ('python', 'python'),
        ('django', 'django'),
        ('javascript', 'javascript'),
    ]
     
    categories = models.CharField(max_length=50, null=True, choices=OPTION_CATEGORY)
    publications = models.OneToOneField(Publication, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    

class ReadList(models.Model):
    renders = models.ForeignKey(Render, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
