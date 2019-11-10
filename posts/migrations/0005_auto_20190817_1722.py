# Generated by Django 2.2.4 on 2019-08-17 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nex_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_post', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='prev_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_post', to='posts.Post'),
        ),
    ]
