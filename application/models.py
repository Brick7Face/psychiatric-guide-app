from django.db import models

# defines model for a single step (or box) from prescribing guide flowchart
class Step(models.Model):
    # Fields
    name = models.TextField(help_text='Enter step title')
    description = models.TextField(help_text='Enter step description')
    
    # Metadata
    class Meta: 
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

# defines model for a medication used by prescribers
class Medication(models.Model):
    # Fields
    name = models.TextField(help_text='Enter medication name')
    category = models.TextField(help_text='Enter medication type')
    initial_Dose = models.FloatField(help_text='Enter medication initial dose in mg')
    maximum_Dose = models.FloatField(help_text='Enter medication maximum dose in mg')
    titration = models.TextField(help_text='Enter medication titration information')
    comments = models.TextField(help_text='Enter comments about medication') 
    side_Effects = models.TextField(help_text='Enter side effects for medication')
    
    # Metadata
    class Meta: 
        ordering = ['category','name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

# defines model for a patient in treatment process
class Patient(models.Model):
    # Fields
    first_Name = models.TextField(help_text='Enter patient first name and middle initial')
    last_Name = models.TextField(help_text='Enter patient last name')
    DOB = models.DateField(help_text='Enter patient date of birth')
    address = models.TextField(help_text='Enter patient current address')
    email = models.EmailField(help_text='Enter patient current email')
    phone = models.TextField(help_text='Enter patient current phone number')
    # program
    # list of PHQ-9 scores
    # visit history
    # next visit
    # medicines
    # current treatment progress (step)
    notes = models.TextField(help_text='Enter any prescriber notes about patient')
 
    
    # Metadata
    class Meta: 
        ordering = ['last_Name','first_Name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

# defines model for a prescriber
# defines model for PHQ-9 score and corresponding disorder
# defines model for disorder treatment type and corresponding steps
