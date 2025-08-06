from django.db import models
from users.models import CustomUser # import our CustomUser model

# Create your models here.
class Job(models.Model):
  """
  Represents a single job or lead in the system, from creation to completion.
  """

  #These are the stages for our Kanban board.
  STATUS_CHOICES =[
    ('new','New '),
    ('contacted', 'Contacted'),
    ('quoted', 'Quote Sent'),
    ('scheduled', 'Job Scheduled'),
    ('done', 'Work Complete'),
    ('paid', 'Paid & Closed')
  ]

   # This links the job to a specific user. If the user is deleted, all their jobs are deleted.

  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='jobs')

  # Core Job Details
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
  customer_email = models.EmailField(blank=True, null=True)
  customer_phone = models.CharField(max_length=20, blank=True, null=True)
  job_description = models.TextField(blank=True, null =True)
  address = models.CharField(max_length=255, blank=True, null=True) 

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 

  class Meta:
    ordering = ['-created_at'] # Show the newest jobs first by defauly.

  def __str__(self):
    return f"job for {self.customer_name or 'Unknown'} ({self.user.email})"
  