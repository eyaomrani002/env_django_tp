# Generated by Django 4.1.7 on 2023-03-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_fournisseur_produitnc_commande_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='adresse',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('AL', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='Al', max_length=50),
        ),
    ]