from django.db import models
from django.utils.timezone import now
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from django.conf import settings
from Registration.models import Users

# Create your models here.

class Parent(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE




    parent_id = models.AutoField(primary_key=True)
    parent_name = models.CharField(max_length=100)
    parent_email_address = models.CharField(max_length=150)
    parent_image = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="parent_user")
    created_at = models.DateTimeField(default=now)





    class Meta:
        db_table = 'report_card_parent'



    def __str__(self):
        return self.parent_name