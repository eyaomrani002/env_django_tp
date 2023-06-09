# Generated by Django 4.1.7 on 2023-03-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AL', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='Al', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='Categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.categorie'),
        ),
    ]
