# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150520_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='acceptance',
            field=models.BooleanField(default=False, help_text='\u5de5\u7a0b\u9a8c\u6536\u60c5\u51b5'),
        ),
        migrations.AlterField(
            model_name='project',
            name='approval_chart',
            field=models.BooleanField(default=False, help_text='\u7acb\u9879\u5355\u6d41\u7a0b\u662f\u5426\u5b8c\u6210'),
        ),
        migrations.AlterField(
            model_name='project',
            name='audit',
            field=models.CharField(help_text='\u9879\u76ee\u5ba1\u8ba1\u5355\u4f4d\u4fe1\u606f', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='audit_price',
            field=models.IntegerField(default=0, help_text='\u5de5\u7a0b\u6700\u7ec8\u5ba1\u5b9a\u4ef7\u683c', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='bid_price',
            field=models.FloatField(default=0, help_text='\u9879\u76ee\u4e2d\u6807\u4ef7\u683c\uff08\u7cbe\u786e\u5230\u6574\u6570\uff0c\u5355\u4f4d\u5143\uff09', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='contract',
            field=models.BooleanField(default=False, help_text='\u5408\u540c\u7b7e\u8ba2\u60c5\u51b5'),
        ),
        migrations.AlterField(
            model_name='project',
            name='controlled_price',
            field=models.IntegerField(default=0, help_text='\u9879\u76ee\u62db\u6807\u63a7\u5236\u4ef7\uff08\u7cbe\u786e\u5230\u6574\u6570\uff0c\u5355\u4f4d\u5143\uff09', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='introduction',
            field=models.TextField(help_text='\u9879\u76ee\u7b80\u4ecb', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='online_system_input',
            field=models.BooleanField(default=False, help_text='\u62db\u6295\u6807\u7ba1\u7406\u7cfb\u7edf\u5f55\u5165\u60c5\u51b5'),
        ),
        migrations.AlterField(
            model_name='project',
            name='permit',
            field=models.BooleanField(default=False, help_text='\u662f\u5426\u6709\u7acb\u9879\u7533\u8bf7\uff08\u5e74\u5ea6\u8ba1\u5212\u5185\u9879\u76ee\u4e0d\u9700\u8981\uff09'),
        ),
        migrations.AlterField(
            model_name='project',
            name='planned',
            field=models.BooleanField(default=True, help_text='\u662f\u5426\u5e74\u5ea6\u8ba1\u5212\u5185\u9879\u76ee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='successful_bidder',
            field=models.CharField(help_text='\u4e2d\u6807\u5355\u4f4d\u4fe1\u606f', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.CharField(help_text='\u9879\u76ee\u76d1\u7406\u5355\u4f4d\u4fe1\u606f', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tendering_agency',
            field=models.CharField(help_text='\u9879\u76ee\u62db\u6807\u4ee3\u7406\u60c5\u51b5', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tendering_chart',
            field=models.BooleanField(default=False, help_text='\u62db\u6295\u6807\u767b\u8bb0\u8868\u6d41\u7a0b\u662f\u5426\u5b8c\u6210'),
        ),
    ]
