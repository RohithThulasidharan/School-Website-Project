# Generated by Django 3.2.8 on 2021-11-03 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20211103_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='parent',
            field=models.ForeignKey(db_column='Parent_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.parents'),
        ),
    ]
