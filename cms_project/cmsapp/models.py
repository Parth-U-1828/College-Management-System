from django.db import models
class DeptModel(models.Model):
	did = models.IntegerField(primary_key=True)
	dname = models.CharField(max_length=40)


	def __str__(self):
		return self.dname


class StudentModel(models.Model):
	rno = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	dept = models.ForeignKey(DeptModel,on_delete = models.CASCADE)

	def __str__(self):
		return self.name



