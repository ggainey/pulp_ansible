# Generated by Django 2.2.4 on 2019-09-06 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0011_collectionimport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectionimport',
            options={'ordering': ['task___created']},
        ),
        migrations.RemoveField(
            model_name='collectionimport',
            name='name',
        ),
        migrations.RemoveField(
            model_name='collectionimport',
            name='namespace',
        ),
        migrations.RemoveField(
            model_name='collectionimport',
            name='version',
        ),
    ]
