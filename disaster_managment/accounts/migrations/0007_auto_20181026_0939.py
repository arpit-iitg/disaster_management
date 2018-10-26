# Generated by Django 2.1.2 on 2018-10-26 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20181026_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(max_length=3)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128)),
                ('State', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=40)),
                ('Locality', models.CharField(max_length=100)),
                ('Pin', models.IntegerField(max_length=6)),
                ('PhoneNumber', models.IntegerField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
