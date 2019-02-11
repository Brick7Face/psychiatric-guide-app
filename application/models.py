from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# defines model for disorder treatment type and corresponding steps
class Treatment(models.Model):
    # Fields
    name = models.TextField(help_text='Enter disorder treatment type title')
    
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

# defines model for a single step (or box) from prescribing guide flowchart
class Step(models.Model):
    # Fields
    name = models.TextField(help_text='Enter step title')
    description = models.TextField(help_text='Enter step description')
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, default='incomplete')
    
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

# defines model for a prescriber
class Prescriber(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Metadata
    class Meta: 
        ordering = ['user']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user.get_username()

# defines model for a patient in treatment process
class Patient(models.Model):
    # Fields
    first_Name = models.TextField(help_text='Enter patient first name and middle initial')
    last_Name = models.TextField(help_text='Enter patient last name')
    DOB = models.DateField(help_text='Enter patient date of birth')
    address = models.TextField(help_text='Enter patient current address')
    email = models.EmailField(help_text='Enter patient current email')
    phone = models.TextField(help_text='Enter patient current phone number')
    prescriber = models.ForeignKey(Prescriber, null=True, on_delete=models.SET_NULL)
    current_Step = models.ForeignKey(Step, null=True, on_delete=models.SET_NULL)
    # list of PHQ-9 scores
    # visit history
    next_Visit = models.DateTimeField(help_text='Enter the next visit date and time of the patient if applicable', blank=True, default=timezone.now)
    medications = models.ManyToManyField(Medication)
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

