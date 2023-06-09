# Generated by Django 3.0.5 on 2023-05-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0012_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
