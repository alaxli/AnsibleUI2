#!usr/bin/env python
# coding:utf-8
from django.contrib import admin
from asset import models


class HostInline(admin.TabularInline):
    model = models.HostLog
    readonly_fields = ('born_time', )
    raw_id_fields = ('op', )
    suit_classes = 'inline-group suit-tab suit-tab-log show'


class HostAdmin(admin.ModelAdmin):
    inlines = (HostInline,)
    raw_id_fields = ('maintenance_group_name',)
    readonly_fields = ('born_time', )
    list_display = ('sn', 'type', 'vendor', 'status')
    search_fields = ('sn', 'type', 'vendor', 'product_model')
    list_filter = ('type', 'vendor', 'idc', 'status')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'vendor', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date',
                         'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'power', 'status', 'maintenance_date',
                         'maintenance_group_name'],
                         'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        ),
    ]
    suit_form_tabs = (('general', '基础信息'), ('log', '资产状态变更'), ('config', '资产配置'))
    suit_form_includes = (
        # ('asset/host_tag/host_status_action.html', 'top', 'log'),
        # ('asset/maintenance_log_table.html', 'bottom', 'log'),
    )


class NetworkDeviceAdmin(admin.ModelAdmin):

    list_display = ('type', 'vendor', 'product_model', 'sn', 'be_from')
    search_fields = ('type', 'vendor', 'product_model', 'sn', 'be_from')
    readonly_fields = ('born_time', )
    list_filter = ('type', 'vendor', 'be_from')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'vendor', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date', 'contract',
                         'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'status', 'power', 'maintenance_date',
                         'maintenance_group'],
                        'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'), ('log', '资产状态变更'))
    suit_form_includes = (
        # ('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )

class StorageAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'manufacturers', 'sn', 'be_from', 'ownership', 'contract')
    search_fields = ('device_type', 'manufacturers', 'sn', 'be_from', 'ownership', 'contract')
    readonly_fields = ('born_time', )
    list_filter = ('device_type', 'be_from', 'ownership')
    fieldsets = [
        (
            '资产基础信息', {
                'fields': [
                    'device_type', 'manufacturers', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date',
                    'contract', 'disk_num', 'disk_model', 'disk_fru', 'fsp_num', 'ext_fsp_num', 'power_num',
                    'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'state', 'maintenance_date',
                    'maintenance_group',
                ],
                'classes': [
                    'suit-tab', 'suit-tab-general'
                ]
            }
        ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'), ('log', '资产状态变更'))
    suit_form_includes = (
        #('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )

class TapeAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'product_model', 'sn', 'be_from', 'ownership', 'manufacturers')
    search_fields = ('device_type', 'product_model', 'sn', 'be_from', 'manufacturers', 'ownership__name')
    list_filter = ('device_type', 'product_model', 'be_from')
    readonly_fields = ('born_time', )
    fieldsets = [
        (
            '资产基础信息', {
                'fields': [
                    'device_type', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date',
                    'manufacturers', 'contract', 'strongbox', 'tape_library_name', 'state'
                ],
                'classes': [
                    'suit-tab', 'suit-tab-general'
                ]
            }
        ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'),)
    suit_form_includes = (
        ('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'part_No', 'amount', 'inventory_num', 'color', 'size', 'be_from',
                    'ownership')
    list_filter = ('device_type', 'be_from', 'part_No')
    search_fields = ('device_type', 'be_from', 'part_No')
    readonly_fields = ('born_time',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'product_model', 'sn', 'amount', 'size', 'be_from', 'purchase_date')
    search_fields = ('type', 'product_model', 'size', 'be_from')
    readonly_fields = ('born_time', )
    list_filter = ('type', 'be_from')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'product_model', 'sn', 'amount', 'size', 'be_from', 'ownership', 'purchase_date',
                         'vendor', 'contract', 'location', 'using_status', 'maintenance_date', 'maintenance_section',
                         'abandon_time'],
                        # 'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                # 'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'number', 'be_from', 'purchase_date', 'vendor')
    search_fields = ('name', 'version', 'number', 'be_from', 'purchase_date', 'vendor')
    readonly_fields = ('born_time', )
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['name', 'version', 'number', 'be_from', 'purchase_date', 'vendor', 'contract', 'related_app',
                         'user_name', 'user_phone', 'user_email', 'use_status', 'maintenance_date'],
                        # 'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                # 'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]

class IndustryGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    readonly_fields = ('born_time',)

class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('maintenance_group', 'maintenance_contact', 'maintenance_phone')
    search_fields = ('maintenance_group', 'maintenance_contact', 'maintenance_phone')
    readonly_fields = ('born_time',)

class HostLogAdmin(admin.ModelAdmin):
    raw_id_fields = ('sn',)
    list_display = ('sn', 'state', 'peo', 'op', 'born_time')
    readonly_fields = ('born_time', )

class HostSparePartAdmin(admin.ModelAdmin):
    list_display = ('host', 'type', 'sn', 'vendor', 'mem', 'disk')
    readonly_fields = ('born_time',)
    raw_id_fields = ('host', )

class NetworkSparePartAdmin(admin.ModelAdmin):
    list_display = ('host', 'sn', 'type', 'vendor', 'born_time')
    search_fields = ('sn', 'type', 'vendor')
    list_filter = ('type', 'vendor')
    readonly_fields = ('born_time', )

admin.site.register(models.Host, HostAdmin)
admin.site.register(models.NetworkDevice, NetworkDeviceAdmin)
admin.site.register(models.Storage, StorageAdmin)
admin.site.register(models.Tape, TapeAdmin)
admin.site.register(models.Tools, ToolsAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Software, SoftwareAdmin)
admin.site.register(models.IndustryGroup, IndustryGroupAdmin)
admin.site.register(models.Maintenance, MaintenanceAdmin)
admin.site.register(models.HostLog, HostLogAdmin)
admin.site.register(models.HostSparePart, HostSparePartAdmin)
admin.site.register(models.NetworkSparePart, NetworkSparePartAdmin)
# admin.site.register(models.DataCenter, DataCenterAdmin)
# admin.site.register(models.Zone, ZoneAdmin)
# admin.site.register(models.RackUnit, RackUnitAdmin)