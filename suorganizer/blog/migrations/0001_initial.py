# Generated by Django 2.0.2 on 2018-02-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=63, unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('startups', models.ManyToManyField(related_name='blog_posts', to='organizer.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'blog_post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
