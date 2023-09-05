from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno=models.IntegerField(max_length=10,primary_key=True)
    Dname=models.CharField(max_length=50,null=False)
    Location=models.CharField(max_length=25)
    def __str__(self):
        return self.Dname

class Emp(models.Model):
    EmpNo=models.IntegerField(max_length=10,primary_key=True)
    Ename=models.CharField(max_length=50,null=False)
    Job=models.CharField(max_length=50)
    Sal=models.IntegerField(max_length=10,null=False)
    HireDate=models.DateField(max_length=50,null=False)
    Comm=models.IntegerField(max_length=50,null=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Ename


    


