from django.db import models
from django.db.models.query import QuerySet
from django.utils.timezone import now
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
# Create your models here.

#todo: QuerySet, Manager

# class SoftDeleteQuerySet(QuerySet):
    
#     def delete(self):
#         for obj in self:
#             obj.is_delete=1
#             obj.save()



# class SoftDeleteManager(models.Manager):
#     def get_queryset(self):
#         return SoftDeleteQuerySet(self.model, using=self._db).filter(is_delete=1)


# class SoftDeleteModel(models.Model):
#     class Meta:
#         abstract = True

#     is_delete = models.PositiveSmallIntegerField(default=0)


#     objects = SoftDeleteManager()
#     original_objects = models.Manager()



#     def delete(self):
#         self.is_delete=1
#         self.save()


class Classes(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE


    class_id = models.AutoField(primary_key=True)
    class_code = models.CharField(max_length=100)
    class_name = models.CharField(min_length=100)
    # is_delete = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(default=now)




    class Meta:
        db_table = 'report_card_class'


    def __str__(self):
        return self.class_code



class Section(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
     

    section_id = models.AutoField(primary_key=True)
    section_code = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    class = models.ForeignKey(Classes, on_detete=models.CASCADE)
    # is_delete = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(default=now)




    class Meta:
        db_table = 'report_card_section'



    def __str__(self):
        return self.section_code