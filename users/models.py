from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
  """
  This is the central user model for LeadHammer. It extends Django's default user and adds all application-specific fields.
  """
  # We will use email as the unique identifier instead of username.
  # The default User model has username, first_name, last_name, email, password, etc.
  # We are adding our own fields below.

  # ---- BILLING & STATUS ----  
  stripe_customer_id = models.CharField(max_length=255, blank=True, null=True, help_text='THe users Stripe Customer ID.')
  subscription_status = models.CharField(max_length=20, default='inactive', help_text="e.g., active, inactive, trialing")

  # ---- APPLICATION SETTINGS ----
  alert_phone_number = models.CharField(max_length=20, blank=True, null=True, help_text='The phone number to receive SMS alerts.')

  # ---- UNIQUE IDENTIFIER ----
  # This is the secret key that links a public URL to this user's account.
  webhook_id = models.UUIDField(default=uuid.uuid4,editable=False, unique=True, db_index=True)

  def __str__(self):
    return self.email