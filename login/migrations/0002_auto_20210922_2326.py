# Generated by Django 3.2.7 on 2021-09-22 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='password',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to='login.usermodel'),
        ),
    ]
