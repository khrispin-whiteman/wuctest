# Generated by Django 4.1.1 on 2023-02-18 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0008_remove_assessment_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Assessment Type')),
            ],
        ),
        migrations.DeleteModel(
            name='AssessmentScore',
        ),
        migrations.AddField(
            model_name='assessment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assessment',
            name='total_marks',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='date',
            field=models.DateTimeField(verbose_name='Date Of Assessment'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='assessment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_of_assessment', to='schoolapp.assessmenttype'),
        ),
    ]
