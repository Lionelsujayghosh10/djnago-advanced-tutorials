from django.db import models
from django.db.models.query import QuerySet
from django.utils.timezone import now
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from ClassSection.models import Classes, Section



class Subject(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE


    subject_id = models.AutoField(primary_key=True)
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)




    class Meta:
        db_table = 'report_card_subject'


    def __str__(self):
        return self.subject_code





class AssignSubject(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    assign_subject_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='classes')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section')
    assign_at = models.DateTimeField(default=now)




    class Meta:
        db_table = 'report_card_assign_subject'




    def __str__(self):
        return self.assign_subject_id