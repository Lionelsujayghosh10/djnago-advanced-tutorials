from django.db import models
from django.utils.timezone import now
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from ClassSection.models import Classes, Section
from Parent.models import Parent
from django.conf import settings
# Create your models here.



class Student(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE




    student_id = models.AutoField(primary_key=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="stduent_class")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="student_section")
    student_name = models.CharField(max_length=150)
    student_code = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    student_image = models.ImageField('Image', upload_to='Images/student/', null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="parent", null=True)
    created_at = models.DateTimeField(default=now)




    class Meta:
        db_table = 'report_card_student'



    def __str__(self):
        return self.student_name

