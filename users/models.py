from __future__ import unicode_literals
#import AbstractUser
from django.contrib.auth.models import AbstractUser
# referring to the settings.AUTH_USER_MODEL instead of referring directly to the custom User model.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.

#new function for deal with duplicated name for the avatar
def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return "Avatar/{}.{}".format(uuid.uuid4(), extension)

def scramble_uploaded_transcript(instance, filename):
    extension = filename.split(".")[-1]
    return "Transcript/{}.{}".format(uuid.uuid4(), extension)

#customer the user model to set a boolean status for enroll student profile or company profile
#should be careful you must user the custom user instead of user model and set the auth path
class CustomUser(AbstractUser):
    USER_TYPE          = (
        (1, "student"),
        (2, "company")
    )
    user_type          = models.IntegerField(choices=USER_TYPE,default=1)

class Skill(models.Model):

    SKILL_TYPE          = (
        (1, "technical skill"),
        (2, "soft skill")
    )
    name                = models.CharField(max_length=30)
    skill_type          = models.IntegerField(choices=SKILL_TYPE,default=1)

    class Meta:
        unique_together = ('name',)
        ordering        = ['name']

    def __str__(self):
        return self.name


class Interest(models.Model):

    inte_name           = models.CharField(max_length=30)

    class Meta:
        ordering        = ['inte_name']

    def __str__(self):
        return self.inte_name

#student profile
#one-to-one relation
class StudentProfile(models.Model):

    user                = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE,related_name = 'student_profile')
    location            = models.CharField(max_length=64,blank=True)
    about               = models.TextField(max_length=100, blank=True, default='')
    phone               = models.IntegerField(null=True, blank=True)
    birthday            = models.DateField(null=True, blank=True)
    image               = models.ImageField('Avatar', upload_to=scramble_uploaded_image, null=True, blank=True) #new
    linked_in_website   = models.URLField(null=True, blank=True)
    twitter_website     = models.URLField(null=True, blank=True)
    facebook_website    = models.URLField(null=True, blank=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(auto_now=True)
    owned_skills        = models.ManyToManyField(Skill,)
    chosen_interests    = models.ManyToManyField(Interest)

    @property
    def user__user_id(self):
        return self.user.id

    def __str__(self):
        return self.user.username

# many to many relations
class OwnedSkills(models.Model):
    skill               = models.ForeignKey(Skill, on_delete=models.CASCADE)
    studentprofile             = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)


class ChosenInterests(models.Model):
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE,
                                 null  = True,
                                 blank = True,)
    studentprofile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)


# one to many relations
class Transcript(models.Model):
    studentprofile      = models.ForeignKey(StudentProfile, related_name='transcripts',on_delete=models.CASCADE, null=True)
    transcript_name     = models.CharField(max_length = 50, default='')
    transcript          = models.FileField('Transcript',upload_to=scramble_uploaded_transcript, null=True, blank=True) #new
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['transcript_name']

    def __str__(self):
        return self.transcript_name


class Education(models.Model):

    edu_name            = models.CharField(max_length = 50)
    qualification       = models.CharField(max_length = 30)
    institute           = models.CharField(max_length = 20)
    description         = models.CharField(max_length = 80, blank = True)
    date_started        = models.DateField(null=True, blank=True)
    date_ended          = models.DateField(null=True, blank=True)

    studentprofile      = models.ForeignKey(
        StudentProfile,
        on_delete       = models.CASCADE,
        related_name    = 'education'
    )

    class Meta:
        ordering        = ['edu_name']

    def __str__(self):
        return self.edu_name


class Wh (models.Model):

    company_name           = models.CharField(max_length=60)
    title               = models.CharField(max_length=50)
    description         = models.CharField(max_length=100, blank=True)
    reference           = models.CharField(max_length = 100,blank=True)
    date_started        = models.DateField(null=True, blank=True)
    date_ended          = models.DateField(null=True, blank=True)

    studentprofile      = models.ForeignKey(
        StudentProfile,
        related_name    = 'work_history',
        on_delete       = models.CASCADE,
    )

    class Meta:
        ordering        = ['company_name']

    def __str__(self):
        return self.work_name

class SkillTest (models.Model):

    skill_name          = models.CharField(max_length=30)
    score               = models.IntegerField(null=True, blank=True)

    studentprofile      = models.ForeignKey(
        StudentProfile,
        related_name    = 'skill_test',
        on_delete       = models.CASCADE,
    )

    class Meta:
        ordering        = ['skill_name']

    def __str__(self):
        return self.skill_name





#########################################################################################################################
#company profile
#one-to-one relation
class CompanyProfile(models.Model):

    user                = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE, related_name = 'company_profile')
    location            = models.CharField(max_length=64,blank=True)
    about               = models.TextField(max_length=100, blank=True, default='')
    phone               = models.IntegerField(null=True, blank=True)
    tax                 = models.IntegerField(null=True, blank=True)
    image               = models.ImageField('Avatar', upload_to=scramble_uploaded_image, null=True, blank=True) #new
    linked_in_website   = models.URLField(null=True, blank=True)
    twitter_website     = models.URLField(null=True, blank=True)
    facebook_website    = models.URLField(null=True, blank=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username


#one to many relationship
class Policy(models.Model):

    policy_name         = models.CharField(max_length = 50)
    description         = models.CharField(max_length = 80, blank = True)

    companyprofile      = models.ForeignKey(
        CompanyProfile,
        on_delete       = models.CASCADE,
        related_name    = 'policies',
        null            = True,
        blank           = True,
    )

    class Meta:
        ordering        = ['policy_name']

    def __str__(self):
        return self.policy_name

# create the profile model by judging it is a student or company
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == 1:
        StudentProfile.objects.get_or_create(user = instance)
    else:
        CompanyProfile.objects.get_or_create(user = instance)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.student_profile.save()
    else:
        instance.company_profile.save()
