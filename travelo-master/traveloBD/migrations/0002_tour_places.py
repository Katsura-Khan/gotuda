# Generated by Django 4.0.2 on 2022-04-09 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveloBD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('des', models.TextField(default='give the describtion')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/%y')),
                ('dist_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='traveloBD.dist_info')),
            ],
        ),
    ]
