# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Project(models.Model):
    # 项目名称
    name = models.CharField(max_length=255, verbose_name="项目名称")
    # 项目简介
    introduction = models.TextField(verbose_name="项目简介", blank=True)
    # 是否年度计划内项目
    planned = models.BooleanField(
        verbose_name="计划内项目",
        help_text="是否年度计划内项目",
        default=True
    )
    # 立项申请（允许立项）及照片
    permit = models.BooleanField(
        help_text="是否有立项申请（年度计划内项目不需要）",
        default=False
    )
    permit_img = models.ImageField(
        help_text="项目立项申请扫描图片",
        blank=True
    )
    # 立项单及照片
    approval_chart = models.BooleanField(help_text="立项单流程是否完成", default=False)
    approval_chart_img = models.ImageField(help_text="项目立项单扫描图片",
                                           blank=True)
    # 招投标表及照片
    tendering_chart = models.BooleanField(help_text="招投标登记表流程是否完成", default=False)
    tendering_agency_img = models.ImageField(
        help_text="招投标登记表扫描图片",
        blank=True
    )
    # 招标代理
    tendering_agency = models.CharField(
        max_length=255,
        help_text="项目招标代理情况",
        blank=True
    )
    # 招标控制价
    controlled_price = models.IntegerField(
        help_text="项目招标控制价（精确到整数，单位元）",
        blank=True,
        default=0
    )
    # 中标单位
    successful_bidder = models.CharField(
        max_length=255,
        help_text="中标单位信息",
        blank=True
    )
    # 中标价格
    bid_price = models.IntegerField(
        help_text="项目中标价格（精确到整数，单位元）",
        blank=True,
        default=0
    )
    # 监理单位
    supervisor = models.CharField(
        max_length=255,
        help_text="项目监理单位信息",
        blank=True
    )
    # 审计单位
    audit = models.CharField(
        max_length=255,
        help_text="项目审计单位信息",
        blank=True
    )
    # 合同签订
    contract = models.BooleanField(help_text="合同签订情况", default=False)
    # 网上系统录入
    online_system_input = models.BooleanField(help_text="招投标管理系统录入情况", default=False)
    # 工程验收及验收单照片
    acceptance = models.BooleanField(help_text="工程验收情况", default=False)
    acceptance_img = models.ImageField(help_text="工程验收单图片",
                                       blank=True)
    # 最终审定价格
    audit_price = models.IntegerField(help_text="工程最终审定价格", blank=True, default=0)

    def __unicode__(self):
        return self.name
