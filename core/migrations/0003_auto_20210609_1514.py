# Generated by Django 3.1.7 on 2021-06-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210608_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MWF', 'Shift Mon Wed Fri'), ('TTS', 'Shift Tue Thu Sat'), ('F', 'Shift All Week')], max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='day',
            field=models.CharField(blank=True, default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(choices=[('MWF', 'Shift Mon Wed Fri'), ('TTS', 'Shift Tue Thu Sat'), ('F', 'Shift All Week')], max_length=4),
        ),
    ]