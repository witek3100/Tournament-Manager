# Generated by Django 4.1.7 on 2023-04-01 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_scores_assists_remove_scores_goals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.match'),
        ),
    ]