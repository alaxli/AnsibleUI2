#!usr/bin/env python
# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
import sys
from settings import *
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.


class Host(models.Model):

    class Meta:

        verbose_name = '物理服务器'
        verbose_name_plural = '物理服务器'

    def __unicode__(self):
        return self.sn
    # 资产基础信息
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    type = models.CharField('设备类型', choices=host_type_choices, max_length=20, null=True, blank=True)
    vendor = models.CharField('生产厂商', max_length=50, null=True, blank=True)
    product_model = models.CharField('产品型号', max_length=100, null=True, blank=True)
    sn = models.CharField('SN号', max_length=50, unique=True, null=True)
    be_from = models.CharField('资产来源', max_length=20, choices=asset_befrom_choices, blank=True)
    ownership = models.ForeignKey('IndustryGroup', verbose_name='资产归属', related_name='ownership', null=True, blank=True)
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    contract = models.CharField('采购合同', max_length=50, null=True, blank=True)
    # cpu、内存、硬盘
    cpu_amount = models.IntegerField('CPU数量', null=True, blank=True)
    cpu_frequency = models.IntegerField('CPU主频', null=True, blank=True)
    memory = models.IntegerField('内存G', null=True, blank=True)
    disk_amount = models.IntegerField('硬盘数量', null=True, blank=True)
    power = models.IntegerField('电源数量', null=True, blank=True)
    # 维保信息
    idc = models.CharField('数据中心', choices=datacenter_choices, max_length=50, null=True, blank=True)
    zone = models.CharField('机柜区域', choices=zone_choices, max_length=20, null=True, blank=True)
    cabinet = models.IntegerField('机柜号', choices=cabinet_choices, null=True, blank=True)
    unit_start = models.IntegerField('机架起始位', choices=rack_unit_choices, null=True, blank=True)
    unit_end = models.IntegerField('机架结束位', choices=rack_unit_choices, null=True, blank=True)
    # entrance_date = models.DateField('入场时间', null=True, blank=True)
    # entrance_peo = models.CharField('入场人员', max_length=50, null=True, blank=True)
    # entrance_phone = models.CharField('入场人员联系方式', max_length=50, null=True, blank=True)
    # entrance_mail = models.EmailField('入场人员邮箱', null=True, blank=True)
    status = models.CharField('使用状态', choices=asset_status_choices, max_length=20, null=True, blank=True)
    maintenance_date = models.DateField('维保到期日', null=True, blank=True)
    maintenance_group_name = models.ForeignKey('Maintenance', verbose_name='维保单位', related_name='m_group')
    # maintenance_contact = models.CharField('维保联系人', max_length=20, null=True, blank=True)
    # maintenance_phone = models.CharField('维保电话', max_length=50, null=True, blank=True)
    # out_date = models.DateField('出场时间', null=True, blank=True)
    # out_reason = models.CharField('出场原因', max_length=100, null=True, blank=True)
    # out_peo = models.CharField('出场人员', max_length=50, null=True, blank=True)
    # out_phone = models.CharField('出场人员联系方式', max_length=50, null=True, blank=True)
    # out_mail = models.EmailField('出场人员邮箱', null=True, blank=True)
    # 管理人员信息
    sys_admin = models.CharField('系统管理员', max_length=50, null=True, blank=True)
    sys_admin_contact = models.CharField('联系电话', max_length=50, null=True, blank=True)
    sys_admin_mail = models.EmailField('管理员邮箱', null=True, blank=True)
    # 服务器信息转移到ops.models

     # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    # born_time = models.DateTimeField(default=datetime.datetime.now)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)
    # update_time = models.DateTimeField(default=datetime.datetime.now)


class NetworkDevice(models.Model):
    # 资产基础信息
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    type = models.CharField('设备类型', choices=network_choices, max_length=20, null=True, blank=True)
    vendor = models.CharField('生产厂商', max_length=50, null=True, blank=True)
    product_model = models.CharField('产品型号', max_length=100, null=True, blank=True)
    sn = models.CharField('SN号', max_length=50, unique=True, null=True, blank=True)
    be_from = models.CharField('资产来源', max_length=20, choices=asset_befrom_choices, blank=True)
    ownership = models.ForeignKey('IndustryGroup', verbose_name='资产归属', null=True)
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    contract = models.CharField('采购合同', max_length=50, null=True, blank=True)
    power = models.IntegerField('电源数量', null=True, blank=True)
    # 维保信息
    idc = models.CharField('数据中心', choices=datacenter_choices, max_length=50, null=True, blank=True)
    zone = models.CharField('机柜区域', choices=zone_choices, max_length=20, null=True, blank=True)
    cabinet = models.IntegerField('机柜号', choices=cabinet_choices, null=True, blank=True)
    unit_start = models.IntegerField('机架起始位', choices=rack_unit_choices, null=True, blank=True)
    unit_end = models.IntegerField('机架结束位', choices=rack_unit_choices, null=True, blank=True)
    entrance_date = models.DateField('入场时间', null=True, blank=True)
    entrance_peo = models.CharField('入场人员', max_length=50, null=True, blank=True)
    entrance_phone = models.CharField('入场人员联系方式', max_length=50, null=True, blank=True)
    entrance_mail = models.EmailField('入场人员邮箱', null=True, blank=True)
    # datacenter = models.CharField('数据中心', max_length=50, null=True, blank=True)
    # cabinet_row = models.CharField('机柜列', max_length=20, null=True, blank=True)
    # cabinet_num = models.CharField('机柜号', max_length=20, null=True, blank=True)
    # cabinet_U = models.CharField('机柜U', max_length=20, null=True, blank=True)
    status = models.CharField('使用状态', choices=asset_status_choices, max_length=20, null=True, blank=True)
    maintenance_date = models.DateField('维保到期日', null=True, blank=True)
    maintenance_group = models.ForeignKey('Maintenance', verbose_name='维保单位')
    # maintenance_contact = models.CharField('维保联系人', max_length=20, null=True, blank=True)
    # maintenance_phone = models.CharField('维保电话', max_length=50, null=True, blank=True)
    out_date = models.DateField('出场时间', null=True, blank=True)
    out_reason = models.CharField('出场原因', max_length=100, null=True, blank=True)
    out_peo = models.CharField('出场人员', max_length=50, null=True, blank=True)
    out_phone = models.CharField('出场人员联系方式', max_length=50, null=True, blank=True)
    out_mail = models.EmailField('出场人员邮箱', null=True, blank=True)
    # 管理人员信息
    sys_admin = models.CharField('系统管理员', max_length=50, null=True, blank=True)
    sys_admin_contact = models.CharField('联系电话', max_length=50, null=True, blank=True)
    sys_admin_mail = models.EmailField('管理员邮箱', null=True, blank=True)
    local_admin = models.CharField('本地管理员', max_length=50, null=True, blank=True)
    local_admin_contact = models.CharField('联系电话', max_length=50, null=True, blank=True)
    local_admin_mail = models.EmailField('管理员邮箱', null=True, blank=True)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)
    # 网络设备表，信息自动收集

    class Meta:

        verbose_name = '网络设备'
        verbose_name_plural = '网络设备'

    def __unicode__(self):
        return self.sn


class Storage(models.Model):
    # 资产信息
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    device_type = models.CharField(u'设备类型', max_length=20, null=True, blank=True, choices=storage_type_choices)
    manufacturers = models.CharField(u'生产厂商', null=True, blank=True, max_length=15)
    product_model = models.CharField(u'产品型号', max_length=100, null=True, blank=True)
    sn = models.CharField(u'SN号', max_length=50, unique=True, null=True, blank=True)
    be_from = models.CharField(u'资产来源', max_length=20, choices=asset_befrom_choices, blank=True)
    ownership = models.ForeignKey('IndustryGroup', verbose_name='归属单位', null=True, blank=True)
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    contract = models.CharField(u'采购合同号', max_length=50, null=True, blank=True)
    # 配置信息
    disk_num = models.IntegerField(u'硬盘数量', null=True, blank=True)
    disk_model = models.CharField(u'硬盘规格', max_length=50, null=True, blank=True)
    disk_fru = models.CharField(u'硬盘FRU', max_length=50, null=True, blank=True)
    fsp_num = models.CharField(u'控制器host FSP数量', max_length=10, null=True, blank=True)
    ext_fsp_num = models.CharField(u'控制器扩展FSP数量', max_length=10, null=True, blank=True)
    power_num = models.IntegerField(u'电源数量', null=True, blank=True)
    # sys_admin = models.CharField(u'管理员', null=True, blank=True, max_length=15)
    # sys_admin_contact = models.CharField(u'管理员电话', null=True, blank=True, max_length=11)
    # sys_admin_mail = models.EmailField(u'管理员邮箱', null=True, blank=True)
    # 设备维护信息
    idc = models.CharField(u'数据中心', choices=datacenter_choices, max_length=50, null=True, blank=True)
    zone = models.CharField(u'机柜区域', choices=zone_choices, max_length=20, null=True, blank=True)
    cabinet = models.IntegerField(u'机柜号', choices=cabinet_choices, null=True, blank=True)
    unit_start = models.IntegerField(u'机架起始位', choices=rack_unit_choices, null=True, blank=True)
    unit_end = models.IntegerField(u'机架结束位', choices=rack_unit_choices, null=True, blank=True)
    # entrance_date = models.DateField(u'入场时间', null=True, blank=True)
    # entrance_peo = models.CharField(u'入场办理人员', max_length=50, null=True, blank=True)
    # entrance_phone = models.CharField(u'入场办理人员联系方式', max_length=50, null=True, blank=True)
    # entrance_mail = models.EmailField(u'入场办理人员邮箱', null=True, blank=True)
    maintenance_date = models.DateField(u'维保到期日', null=True, blank=True)
    maintenance_group = models.ForeignKey('Maintenance', verbose_name='维保单位')
    state = models.CharField(u'使用状态', null=True, blank=True, choices=asset_status_choices, max_length=15)
    '''
    # 存储运维？
    hostname = models.CharField(u'主机名', max_length=20, null=True, blank=True)
    ip = models.GenericIPAddressField(u'ip地址', null=True, blank=True)
    manage_ip = models.GenericIPAddressField(u'管理ip', null=True, blank=True)
    app_type = models.CharField(u'应用类型', max_length=20, null=True, blank=True)
    app_description = models.CharField(u'应用描述', max_length=100, null=True, blank=True)
    firmware_version = models.CharField(u'控制器firmware版本', max_length=10, null=True, blank=True)
    is_fiber_switch = models.NullBooleanField(u'是否为光纤交换机', null=True, blank=True)
    fiber_switch_port = models.CharField(u'光交端口', max_length=10, null=True, blank=True)
    total_capacity = models.CharField(u'存储总量', max_length=10, null=True, blank=True)
    available_capacity = models.CharField(u'可用存储容量', max_length=10, null=True, blank=True)
    total_SAS_capacity = models.CharField(u'SAS总容量', max_length=10, null=True, blank=True)
    total_NL_SAS_capacity = models.CharField(u'NL_SAS总容量', max_length=10, null=True, blank=True)
    raid = models.CharField(u'RAID', max_length=10, null=True, blank=True)
    storage_pool_size = models.CharField(u'存储池大小', max_length=20, null=True, blank=True)
    LUN_number = models.CharField(u'LUN总量', max_length=10, null=True, blank=True)
    is_LUN_shared = models.NullBooleanField(u'LUN是否共享', null=True, blank=True)
    LUN_map_number = models.CharField(u'裸LUN映射数量', max_length=10, null=True, blank=True)
    LUN_map_host = models.CharField(u'映射主机', max_length=10, null=True, blank=True)
    host_mount_LUN_info = models.CharField(u'主机挂载LUN信息', max_length=10, null=True, blank=True)
    APP_manager = models.CharField(u'应用负责人', max_length=15, null=True, blank=True)
    APP_manager_phone = models.CharField(u'应用负责人电话', max_length=13, null=True, blank=True)
    APP_manager_email = models.EmailField(u'应用负责人邮箱', null=True, blank=True)
    '''
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '存储设备'
        verbose_name_plural = '存储设备'

    def __unicode__(self):
        return self.hostname


class Tape(models.Model):
    # 资产信息
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    device_type = models.CharField(u'设备类型', max_length=20, null=True, blank=True, choices=tape_type_choices)
    product_model = models.CharField(u'产品型号', max_length=100, null=True, blank=True, choices=tape_model_choices)
    sn = models.CharField(u'SN号', max_length=50, unique=True, null=True, blank=True)
    be_from = models.CharField(u'资产来源', max_length=20, choices=asset_befrom_choices, null=True, blank=True)
    ownership = models.ForeignKey('IndustryGroup', verbose_name='资产归属')
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    manufacturers = models.CharField(u'生产厂商', null=True, blank=True, max_length=15)
    contract = models.CharField(u'采购合同号', max_length=50, null=True, blank=True)
    # maintenance_date = models.DateField(u'维保到期日', null=True, blank=True)
    # maintenance_group = models.ForeignKey('Maintenance', verbose_name='维保单位', blank=True, null=True)
    # 配置信息
    # admin = models.CharField(u'管理员', null=True, blank=True, max_length=15)
    # admin_contact = models.CharField(u'管理员电话', null=True, blank=True, max_length=11)
    # admin_mail = models.EmailField(u'管理员邮箱', null=True, blank=True)

    strongbox = models.CharField(u'保险柜', null=True, blank=True, max_length=20)
    tape_library_name = models.CharField(u'带库名称', null=True, blank=True, max_length=15)
    state = models.CharField(u'使用状态', null=True, blank=True, choices=tape_status_choices, max_length=15)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '磁带'
        verbose_name_plural = '磁带'

    def __unicode__(self):
        return self.sn


class Tools(models.Model):
    # 工具表
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    device_type = models.CharField('工具类型', max_length=50, choices=device_type_choices)
    part_No = models.CharField('产品型号', max_length=50, choices=product_type_choices)
    amount = models.IntegerField('总数量', null=True, blank=True)
    inventory_num = models.IntegerField('库存量', null=True, blank=True)
    color = models.CharField('颜色', max_length=30, null=True, blank=True)
    size = models.CharField('规格', max_length=50, null=True, blank=True)
    be_from = models.CharField('资产来源', max_length=20, choices=asset_befrom_choices, blank=True)
    ownership = models.ForeignKey('IndustryGroup', verbose_name='资产归属', null=True, blank=True)
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    vendor = models.CharField('生产厂商', max_length=50, null=True, blank=True)
    approach_date = models.DateField('入场时间', null=True, blank=True)
    location = models.CharField('存放位置', max_length=50, choices=datacenter_choices)
    using_status = models.CharField('使用状态', max_length=50, choices=asset_status_choices)
    note = models.TextField('备注', max_length=200, null=True, blank=True)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '工具'
        verbose_name_plural = '工具'

    def __unicode__(self):
        return self.device_type


class Equipment(models.Model):
    # 辅助设备表
    # 资产基础信息
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    type = models.CharField('设备类型', choices=equipment_choice, max_length=20, null=True, blank=True)
    product_model = models.CharField('产品型号', max_length=100, null=True, blank=True)
    sn = models.CharField('SN号', max_length=50, unique=True, null=True, blank=True)
    amount = models.IntegerField('数量', null=True)
    size = models.CharField('规格', max_length=50, null=True, blank=True)
    be_from = models.CharField('资产来源', max_length=20, choices=asset_befrom_choices, blank=True)
    ownership = models.ForeignKey('IndustryGroup', verbose_name='资产归属', null=True, blank=True)
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    vendor = models.CharField('生产厂商', max_length=50, null=True, blank=True)
    contract = models.CharField('采购合同', max_length=50, null=True, blank=True)
    # approach_date = models.DateField('入场时间', null=True, blank=True)
    # approach_name = models.CharField(u'入场人员名字', max_length=30, blank=True, null=True)
    # approach_number = models.CharField(u'入场人员电话', max_length=30, blank=True, null=True)
    # approach_email = models.CharField(u'入场人员邮箱', max_length=30, blank=True, null=True)
    location = models.CharField('存放位置', max_length=10, choices=datacenter_choices)
    using_status = models.CharField('使用状态', max_length=10, choices=asset_status_choices)
    maintenance_date = models.DateField('维保到期日', null=True, blank=True)
    maintenance_section = models.ForeignKey('Maintenance', verbose_name='维保单位')
    abandon_time = models.DateField('报废时间', null=True, blank=True)
    # maintenance_person = models.CharField('维保人员', max_length=30, blank=True)
    # maintenance_number = models.CharField(u'维保电话', max_length=30, blank=True, null=True)
    # vout_date = models.DateField('出场时间', null=True, blank=True)
    # out_name = models.CharField(u'出场人员名字', max_length=30, blank=True, null=True)
    # out_number = models.CharField(u'出场人员电话', max_length=30, blank=True, null=True)
    # out_email = models.CharField(u'出场人员邮箱', max_length=30, blank=True, null=True)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '机房辅助设备'
        verbose_name_plural = '机房辅助设备'

    def __unicode__(self):
        return self.sn


class Software(models.Model):
    # 软件表
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    name = models.CharField('软件名称', max_length=200, null=True, blank=True)
    version = models.CharField('版本号', max_length=200, null=True, blank=True)
    number = models.IntegerField('数量', null=True, blank=True)
    be_from = models.CharField('资产来源', choices=Asset_source_choices, max_length=10, null=True, blank=True)
    # ownership = models.ForeignKey(Company, verbose_name='资产归属', related_name='company_id', null=True)
    purchase_date = models.DateField(u'采购日期', null=True, blank=True)
    vendor = models.CharField('生产厂商', max_length=200, null=True, blank=True)
    contract = models.CharField('购买合同号', max_length=50, null=True, blank=True)
    entrance_date = models.DateField('入场时间', null=True, blank=True)
    entrance_peo = models.CharField('入场办理人员姓名', max_length=50, null=True, blank=True)
    entrance_phone = models.CharField('入场办理人员电话', max_length=20, null=True, blank=True)
    entrance_mail = models.CharField('入场办理人员邮箱', max_length=50, null=True, blank=True)
    # location = models.ForeignKey(Location, verbose_name='使用位置', related_name='location_id', null=True)
    related_app = models.CharField('所属应用', max_length=50, null=True, blank=True)
    user_name = models.CharField('使用联系人', max_length=50, null=True, blank=True)
    user_phone = models.CharField('使用联系人电话', max_length=20, null=True, blank=True)
    user_email = models.CharField('使用联系人邮箱', max_length=50, null=True, blank=True)
    use_status = models.CharField('使用状态', choices=Use_status_choices, max_length=10, null=True, blank=True)
    maintenance_date = models.DateField('维保到期日期', null=True, blank=True)
    # maintain = models.ForeignKey(Maintenance, verbose_name='维保单位', related_name='maintain_id', null=True)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '软件'
        verbose_name_plural = '软件'

    def __unicode__(self):
        return self.name


class IndustryGroup(models.Model):
    # 公司表（产业集团等）
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    name = models.CharField('公司名称', max_length=100, unique=True, null=True, blank=True)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '归属单位'
        verbose_name_plural = '归属单位'

    def __unicode__(self):
        return self.name


class Maintenance(models.Model):
    # 维保单位
    # uid = models.UUIDField('uuid', default=uuid.uuid1, auto_created=True, editable=False)
    maintenance_group = models.CharField(u'维保单位名称', unique=True, max_length=100, null=True)
    maintenance_contact = models.CharField(u'维保联系人', max_length=100, null=True)
    maintenance_phone = models.CharField(u'维保电话', max_length=20, null=True, blank=True)
    # 自动信息
    born_time = models.DateTimeField(u'创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:

        verbose_name = '维保单位'
        verbose_name_plural = '维保单位'

    def __unicode__(self):
        return self.maintenance_group


class CPU(models.Model):
    asset = models.OneToOneField(Host, verbose_name='主机', to_field='sn', null=True, blank=True)
    cpu_model = models.CharField(u'CPU型号', max_length=128, blank=True)
    cpu_count = models.SmallIntegerField(u'物理cpu个数', blank=True)
    cpu_core_count = models.SmallIntegerField(u'cpu核数')
    memo = models.TextField(u'备注', null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'CPU部件'
        verbose_name_plural = "CPU部件"

    def __unicode__(self):
        return self.cpu_model


class RAM(models.Model):
    asset = models.ForeignKey(Host, verbose_name='主机', to_field='sn', null=True, blank=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    model = models.CharField(u'内存型号', max_length=128)
    slot = models.CharField(u'插槽', max_length=64)
    capacity = models.IntegerField(u'内存大小(MB)')
    memo = models.CharField(u'备注', max_length=128, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s:%s:%s' % (self.asset_id, self.slot, self.capacity)

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = "RAM"
        unique_together = ("asset", "slot")
    auto_create_fields = ['sn', 'slot', 'model', 'capacity']


class Disk(models.Model):
    asset = models.ForeignKey(Host, verbose_name='主机', to_field='sn', null=True, blank=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    slot = models.CharField(u'插槽位', max_length=64)
    manufactory = models.CharField(u'制造商', max_length=64, blank=True, null=True)
    model = models.CharField(u'磁盘型号', max_length=128, blank=True, null=True)
    capacity = models.FloatField(u'磁盘容量GB')
    iface_type = models.CharField(u'接口类型', max_length=64, choices=disk_iface_choice, default='SAS')
    memo = models.TextField(u'备注', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    auto_create_fields = ['sn', 'slot', 'manufactory', 'model', 'capacity', 'iface_type']

    class Meta:
        unique_together = ("asset", "slot")
        verbose_name = '硬盘'
        verbose_name_plural = "硬盘"

    def __unicode__(self):
        return '%s:slot:%s capacity:%s' % (self.asset_id, self.slot, self.capacity)


class NIC(models.Model):
    asset = models.ForeignKey(Host, verbose_name='主机', to_field='sn', null=True, blank=True)
    name = models.CharField(u'网卡名', max_length=64, blank=True, null=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    model = models.CharField(u'网卡型号', max_length=128, blank=True, null=True)
    mac_address = models.CharField(u'MAC', max_length=64, unique=True)
    ip_address = models.GenericIPAddressField(u'IP', blank=True, null=True)
    net_mask = models.CharField(max_length=64, blank=True, null=True)
    bonding = models.CharField(max_length=64, blank=True, null=True)
    memo = models.CharField(u'备注', max_length=128, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s:%s' % (self.asset_id, self.macaddress)

    class Meta:
        verbose_name = u'网卡'
        verbose_name_plural = u"网卡"
        # unique_together = ("asset_id", "slot")
    auto_create_fields = ['name', 'sn', 'model', 'mac_address', 'ip_address', 'net_mask', 'bonding']


class RaidAdaptor(models.Model):
    asset = models.ForeignKey(Host, verbose_name='主机', to_field='sn', null=True, blank=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    slot = models.CharField(u'插口', max_length=64)
    model = models.CharField(u'型号', max_length=64, blank=True, null=True)
    memo = models.TextField(u'备注', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("asset", "slot")
