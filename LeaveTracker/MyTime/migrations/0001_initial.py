# Generated by Django 2.2.5 on 2019-10-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('working_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_from', models.DateTimeField()),
                ('leave_to', models.DateTimeField()),
                ('days', models.IntegerField(default=0)),
                ('notes', models.CharField(max_length=1000)),
            ],
        ),
    ]