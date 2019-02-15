from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# defines model for a single step (or box) from prescribing guide flowchart
class Step(models.Model):
    # Fields
    name = models.CharField(help_text='Enter step title', max_length=25)
    description = models.TextField(help_text='Enter step description')
    
    # Metadata
    class Meta: 
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Step."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Step object (in Admin site etc.)."""
        return self.name

# defines model for disorder treatment type and corresponding steps
class Treatment(models.Model):
    # Fields
    name = models.CharField(help_text='Enter disorder treatment type title', max_length=25)
    steps = models.ManyToManyField(Step)
    
    # Metadata
    class Meta: 
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Treatment."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Treatment object (in Admin site etc.)."""
        return self.name

# defines model for a medication used by prescribers
class Medication(models.Model):
    # Fields
    name = models.CharField(help_text='Enter medication name', max_length=25)
    category = models.CharField(help_text='Enter medication type', max_length=50)
    initial_dose = models.FloatField(help_text='Enter medication initial dose in mg')
    maximum_dose = models.FloatField(help_text='Enter medication maximum dose in mg')
    titration = models.TextField(help_text='Enter medication titration information')
    comments = models.TextField(help_text='Enter comments about medication') 
    side_effects = models.TextField(help_text='Enter side effects for medication')
    
    # Metadata
    class Meta: 
        ordering = ['category','name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Medication."""
        return reverse('model-detail-view', args=[str(self.id)])
  
    def __str__(self):
        """String for representing the Medication object (in Admin site etc.)."""
        return self.name
'''
# defines model for a prescriber
class Prescriber(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    # Metadata
    class Meta: 
        ordering = ['user']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Prescriber."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Prescriber object (in Admin site etc.)."""
        return self.user.get_username()
'''
# defines model for a patient in treatment process
class Patient(models.Model):
    # Fields
    first_name = models.CharField(help_text='Enter patient first name and middle initial', max_length=30)
    last_name = models.CharField(help_text='Enter patient last name', max_length=50)
    dob = models.DateField(help_text='Enter patient date of birth')
    address = models.CharField(help_text='Enter patient current address', max_length=150)
    email = models.EmailField(help_text='Enter patient current email', max_length=50)
    phone = models.CharField(help_text='Enter patient current phone number', max_length=20)
    # prescriber = models.ForeignKey(Prescriber, null=True, on_delete=models.SET_NULL)
    current_step = models.ForeignKey(Step, null=True, on_delete=models.SET_NULL)
    # list of PHQ-9 scores
    # visit history
    next_visit = models.DateTimeField(help_text='Enter the next visit date and time of the patient if applicable', blank=True, default=timezone.now)
    medications = models.ManyToManyField(Medication)
    notes = models.TextField(help_text='Enter any prescriber notes about patient')
 
    
    # Metadata
    class Meta: 
        ordering = ['last_Name','first_Name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Patient."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Patient object (in Admin site etc.)."""
        return self.last_Name

