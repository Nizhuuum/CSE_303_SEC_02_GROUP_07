# Generated by Django 3.2.6 on 2021-08-28 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spm', '0008_dean_t_department_head_t_gfaculty_t_vc_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessments_T',
            fields=[
                ('Assessment ID', models.IntegerField(primary_key=True, serialize=False)),
                ('assessments_name', models.CharField(max_length=20)),
                ('Total Marks', models.FloatField()),
                ('Obtain Marks', models.FloatField()),
                ('co', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.co_t')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.school_t')),
            ],
        ),
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('Section No', models.IntegerField(primary_key=True, serialize=False)),
                ('semester_name', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('No of student', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.course_t')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.gfaculty_t')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Enrollment_T',
            fields=[
                ('Enrollment ID', models.IntegerField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.section_t')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.student_t')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_T',
            fields=[
                ('Evaluation ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Obtain Marks', models.FloatField()),
                ('Total Marks', models.FloatField()),
                ('assessments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.assessments_t')),
                ('student_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.student_enrollment_t')),
            ],
        ),
    ]
