# Generated by Django 4.0.3 on 2022-06-14 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_alter_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='regularuser',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='regularuser',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='regularuser',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='regularuser',
            name='surname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='regularuser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('sent_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]