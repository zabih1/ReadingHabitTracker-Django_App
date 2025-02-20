from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('TECH', 'Tech Book'),
        ('NOVEL', 'Novel'),
    ]
    
    STATUS_CHOICES = [
        ('READING', 'Reading'),
        ('DONE', 'Done'),
        ('NOT_STARTED', 'Not Started'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='NOT_STARTED')
    
    def __str__(self):
        return self.name