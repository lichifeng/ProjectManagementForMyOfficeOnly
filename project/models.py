# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
from django.core.urlresolvers import reverse
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
    permit_choices = (
        (True, "已办理"),
        (False, "未办理")
    )
    permit = models.BooleanField(
        verbose_name="立项申请",
        help_text="是否有立项申请（年度计划内项目不需要）",
        default=False,
        choices=permit_choices
    )
    permit_img = models.ImageField(verbose_name="立项申请", help_text="项目立项申请扫描图片", blank=True)
    # 立项单及照片
    approval_chart_choices = (
        (1, "已立项"),
        (0, "办理中"),
        (2, "未办理")
    )
    approval_chart = models.IntegerField(
        verbose_name="项目立项", help_text="立项单办理情况", default=0, choices=approval_chart_choices
    )
    approval_chart_img = models.ImageField(verbose_name="项目立项单", help_text="项目立项单扫描图片", blank=True)
    # 招投标表及照片
    tendering_chart_choices = (
        (0, "办理中"),
        (1, "市级公开"),
        (2, "镇级公开"),
        (3, "邀请招标"),
        (4, "竞争性谈判"),
        (5, "询价发包"),
        (6, "直接发包"),
    )
    tendering_chart = models.IntegerField(
        verbose_name="招标登记", help_text="招投标登记表办理情况", default=0, choices=tendering_chart_choices
    )
    tendering_chart_img = models.ImageField(verbose_name="招标登记表", help_text="招投标登记表扫描图片", blank=True)
    # 招标代理
    tendering_agency = models.CharField(
        max_length=255,
        help_text="项目招标代理情况",
        blank=True,
        verbose_name="招标代理"
    )
    # 开标日期
    bid_date = models.DateField(blank=True, null=True, verbose_name="开标日期")
    # 招标控制价
    controlled_price = models.IntegerField(
        help_text="精确到整数，单位元",
        blank=True,
        default=0,
        verbose_name="招标控制价"
    )
    # 中标单位
    successful_bidder = models.CharField(
        max_length=255,
        help_text="包括中标单位名称，项目联系人及联系方式",
        blank=True,
        verbose_name="中标单位"
    )
    # 中标价格
    bid_price = models.IntegerField(
        help_text="精确到整数，单位元",
        blank=True,
        default=0,
        verbose_name="中标价格"
    )
    # 监理单位
    supervisor = models.CharField(
        max_length=255,
        help_text="包括监理单位名称，项目联系人及联系方式",
        blank=True,
        verbose_name="监理单位"
    )
    # 审计单位
    audit = models.CharField(
        max_length=255,
        help_text="包括审计单位名称，项目联系人及联系方式",
        blank=True,
        verbose_name="审计单位"
    )
    # 合同签订
    contract_choices = (
        (True, "已签订"),
        (False, "未签订"),
    )
    contract = models.BooleanField(verbose_name="合同签订", default=False, choices=contract_choices)
    # 网上系统录入
    online_system_input_choices = (
        (True, "已录入"),
        (False, "未录入"),
    )
    online_system_input = models.BooleanField(
        verbose_name="系统录入", help_text="镇招投标监管系统录入情况", default=False, choices=online_system_input_choices
    )
    # 工程验收及验收单照片
    acceptance_choices = (
        (True, "已验收"),
        (False, "未验收")
    )
    acceptance = models.BooleanField(verbose_name="工程验收", default=False, choices=acceptance_choices)
    acceptance_img = models.ImageField(verbose_name="竣工验收单", help_text="工程验收单扫描图片", blank=True)
    # 最终审定价格
    audit_price = models.IntegerField(verbose_name="审定价格", help_text="工程最终审定价格", blank=True, default=0)
    # 开工和竣工日期
    project_begin = models.DateField(blank=True, null=True, verbose_name="开工日期")
    project_finish = models.DateField(blank=True, null=True, verbose_name="竣工日期")


    def get_prices(self):
        return self.controlled_price / 10000, self.bid_price / 10000, self.audit_price / 10000

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class Note(models.Model):
    content = models.TextField(verbose_name="待办事项")
    project = models.ForeignKey(Project, verbose_name="所属项目")
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['done']

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "[{0}]的#{1}事项".format(self.project.name, self.pk)
