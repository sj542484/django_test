# Generated by Django 2.1.8 on 2019-06-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfarm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentlist',
            name='gid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='equipmentlist',
            name='start_but_statue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipmentlist',
            name='statue_statue',
            field=models.IntegerField(default=0),
        ),
    ]
