# Generated by Django 2.0.9 on 2020-01-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runnerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_1',
            fields=[
                ('table_1_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='表一id')),
                ('table_1_content', models.CharField(blank=True, max_length=3000, null=True, verbose_name='表一内容')),
                ('table_1_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='表一标题')),
                ('table_1_user', models.CharField(blank=True, max_length=30, null=True, verbose_name='表一作者')),
                ('time', models.DateField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '表一',
                'verbose_name_plural': '表一',
                'db_table': 'table_1',
            },
        ),
        migrations.CreateModel(
            name='Table_2',
            fields=[
                ('table_2_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='表二id')),
                ('table_2_content', models.CharField(blank=True, max_length=3000, null=True, verbose_name='表二内容')),
                ('table_2_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='表二标题')),
                ('table_2_user', models.CharField(blank=True, max_length=30, null=True, verbose_name='表二作者')),
                ('time', models.DateField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '表二',
                'verbose_name_plural': '表二',
                'db_table': 'table_2',
            },
        ),
        migrations.CreateModel(
            name='Table_3',
            fields=[
                ('table_3_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='表三id')),
                ('table_3_content', models.CharField(blank=True, max_length=3000, null=True, verbose_name='表三内容')),
                ('table_3_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='表三标题')),
                ('table_3_user', models.CharField(blank=True, max_length=30, null=True, verbose_name='表三作者')),
                ('time', models.DateField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '表三',
                'verbose_name_plural': '表三',
                'db_table': 'table_3',
            },
        ),
        migrations.CreateModel(
            name='Table_4',
            fields=[
                ('table_4_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='表四id')),
                ('table_4_content', models.CharField(blank=True, max_length=3000, null=True, verbose_name='表四内容')),
                ('table_4_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='表四标题')),
                ('table_4_user', models.CharField(blank=True, max_length=30, null=True, verbose_name='表四作者')),
                ('time', models.DateField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '表四',
                'verbose_name_plural': '表四',
                'db_table': 'table_4',
            },
        ),
    ]