# Generated by Django 4.0.6 on 2022-07-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_places_description_long_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ('id_pic',), 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='images',
            name='id_pic',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='places',
            name='place_id',
            field=models.UUIDField(auto_created=True, unique=True),
        ),
    ]