# Generated by Django 4.2.4 on 2023-08-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcm_django', '0011_fcmdevice_fcm_django_registration_id_user_id_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('devices', models.ManyToManyField(to='fcm_django.fcmdevice')),
            ],
        ),
    ]
