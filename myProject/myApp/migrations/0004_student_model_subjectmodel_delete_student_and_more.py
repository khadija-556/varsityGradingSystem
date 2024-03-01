# Generated by Django 5.0.1 on 2024-02-03 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_grade_student_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('depertment', models.CharField(max_length=120, null=True)),
                ('subject', models.CharField(max_length=120, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100, null=True)),
                ('student_code', models.CharField(max_length=100, null=True)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='subject',
        ),
        migrations.AlterField(
            model_name='grade',
            name='marks',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.student_model'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.subjectmodel'),
        ),
    ]
