# Generated by Django 2.0.9 on 2020-01-17 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinPlan',
            fields=[
                ('join_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='参与id')),
                ('detail', models.CharField(blank=True, max_length=30, null=True, verbose_name='参与训练的备注')),
                ('time', models.DateField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '参与',
                'verbose_name_plural': '参与',
                'db_table': 'participate',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='训练表id')),
                ('plan_content', models.CharField(max_length=300, verbose_name='训练内容')),
                ('plan_type', models.CharField(max_length=30, verbose_name='训练科目')),
                ('plan_speed', models.CharField(max_length=30, verbose_name='训练配速')),
                ('plan_place', models.CharField(max_length=30, verbose_name='训练地点')),
                ('plan_mileage', models.CharField(max_length=30, verbose_name='训练距离')),
                ('time', models.DateField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '训练表',
                'verbose_name_plural': '训练表',
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('picture', models.CharField(max_length=300, verbose_name='微信头像')),
                ('telNumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='收货人手机号码')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'User',
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='plan_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runnerapp.User', verbose_name='管理者'),
        ),
        migrations.AddField(
            model_name='joinplan',
            name='plan',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='runnerapp.Plan', verbose_name='训练计划'),
        ),
        migrations.AddField(
            model_name='joinplan',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='runnerapp.User', verbose_name='参与者'),
        ),
    ]
