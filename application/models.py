from django.db import models

class Steps(models.Model):
	
	name = models.TextField(help_text='Enter step title')
	description = models.TextField(help_text='Enter step description')
    
    # Metadata
    class Meta: 
        ordering = ['title']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name