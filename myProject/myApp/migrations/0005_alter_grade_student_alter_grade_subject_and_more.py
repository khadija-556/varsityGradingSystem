# Generated by Django 5.0.1 on 2024-02-03 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_student_model_subjectmodel_delete_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.student_model'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.subjectmodel'),
        ),
        migrations.RemoveField(
            model_name='student_model',
            name='subject',
        ),
        migrations.AlterField(
            model_name='subjectmodel',
            name='credit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_model',
            name='subject',
            field=models.ManyToManyField(null=True, to='myApp.subjectmodel'),
        ),
    ]
