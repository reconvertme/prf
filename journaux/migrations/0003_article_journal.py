# Generated by Django 4.0.10 on 2024-09-02 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journaux', '0002_article_journal_dispo_journal_genre_journal_webpage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journaux.journal'),
        ),
    ]
