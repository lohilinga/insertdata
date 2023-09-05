# Generated by Django 4.2.3 on 2023-08-17 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('Deptno', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('EmpNo', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Ename', models.CharField(max_length=50)),
                ('Job', models.CharField(max_length=50)),
                ('Sal', models.IntegerField(max_length=10)),
                ('HireDate', models.DateField(max_length=50)),
                ('Comm', models.IntegerField(max_length=50, null=True)),
                ('Deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]