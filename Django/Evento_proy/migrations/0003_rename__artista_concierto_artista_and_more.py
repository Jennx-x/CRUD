# Generated by Django 5.1.2 on 2024-11-21 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evento_proy', '0002_rename_artista_concierto__artista_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concierto',
            old_name='_artista',
            new_name='artista',
        ),
        migrations.RenameField(
            model_name='concierto',
            old_name='_duracion',
            new_name='duracion',
        ),
        migrations.RenameField(
            model_name='conferencia',
            old_name='_orador',
            new_name='orador',
        ),
        migrations.RenameField(
            model_name='conferencia',
            old_name='_tema',
            new_name='tema',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='_fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='_lugar',
            new_name='lugar',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='_nombre',
            new_name='nombre',
        ),
    ]
