
from django.db import models
from users.models import CompanyProfile,StudentProfile
from datetime import datetime

from taggit.managers import TaggableManager

# Create your models here.
class Company(models.Model):
    """
    A company with its details.
    """
    added_by = models.ForeignKey(CompanyProfile,
                                 on_delete=models.CASCADE,
                                 default = '')

    name = models.CharField(max_length = 200)
    telephone = models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    address = models.TextField(blank=True, default='')
    date_add = models.DateTimeField('date created',default=datetime.now, editable=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Category(models.Model):

    cate_name           = models.CharField(max_length=50)

    class Meta:
        ordering        = ['cate_name']

    def __str__(self):
        return self.cate_name


class Job(models.Model):
    """
    A job with its details.
    """
    STATUS_CHOICES =  (
        (1,'Open'),
        (2,'Suspended'),
        (3,'Filled'),
        (4,'Cancelled')
    )

    #post_by = models.ForeignKey()

    status = models.IntegerField('status', choices=STATUS_CHOICES, default=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='job',
                                null = True, blank = True)

    title    = models.CharField('title',max_length = 200)
    #title_slug (if repeated job title appeared)
    description = models.TextField('description', blank = True, default='')
    tags = TaggableManager(blank = True)  # matching data in interest in profiles
    location = models.CharField(max_length=64,blank=True)
    category = models.ManyToManyField(Category)
    start_date = models.DateField(null=True, blank=True)
    due_date   = models.DateField(null=True, blank=True)
    date_add   = models.DateTimeField('date created',auto_now_add=True, null = True)
    date_updated = models.DateTimeField('date update', auto_now=True)


    class Meta:
        ordering = ["date_updated"]

    def __str__(self):
        return self.title

class Applicant(models.Model):
    """
    A job applicant.
    """
    STATUS_CHOICES = (
        ((0, 'unattended')),
        ((1, 'candidate')),
        ((2, 'not qualified')),
        ((3, 'over qualified')),
        ((4, 'delisted')),
        ((5, 'winner')),
    )

    user = models.ForeignKey(StudentProfile,
                             on_delete=models.CASCADE,
                             related_name="job_applicant",
                             default='')
    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE,
                            related_name="job",
                            default='')
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=0)
    date_applied = models.DateTimeField('date applied', auto_now_add=True, editable=False)

    class Meta:
        unique_together = (('user', 'job'),)
        ordering = ["date_applied"]

    def __str__(self):
        return self.status