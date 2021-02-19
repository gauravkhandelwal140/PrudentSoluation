from django.contrib import admin
from django.contrib.auth.models import Group
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Employee, State, KeySkill, Vertical, Bank, Grade, Designation, City, District, Branch
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = 'Prudent Solutions'
admin.site.unregister(Group)
admin.site.site_title = "Prudent Solutions"
admin.site.index_title = 'Prudent Solutions Dashboard'


@admin.register(Designation)
class designationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'designation',)


@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'State_name',)


@admin.register(KeySkill)
class KeySkillAdmin(ImportExportModelAdmin):
    list_display = ('id', 'KeySkill_name',)


@admin.register(Vertical)
class VerticalAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Vetical_name',)


@admin.register(Bank)
class BankAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Bank_name',)


@admin.register(Grade)
class BankAdmin(ImportExportModelAdmin):
    list_display = ('id', 'grade',)


class BranchResource(resources.ModelResource):
    state_name = fields.Field(column_name='State', attribute='State',
                              widget=ForeignKeyWidget(State, 'State_name'))

    district_name = fields.Field(column_name='District', attribute='District',
                                 widget=ForeignKeyWidget(District, 'district_name'))
    city_name = fields.Field(column_name='City', attribute='city',
                             widget=ForeignKeyWidget(City, 'cityname'))

    class Meta:
        model = Branch
        fields = ('id', 'Branch_name', 'state_name', 'district_name', 'city_name')
        export_order = ('id', 'Branch_name', 'state_name', 'district_name', 'city_name')



@admin.register(Branch)
class BankAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Branch_name', 'State', 'District', 'city')
    resource_class = BranchResource

class CityResource(resources.ModelResource):
    state_name = fields.Field(column_name='state', attribute='State_name',
                              widget=ForeignKeyWidget(State, 'State_name'))

    district_name = fields.Field(column_name='district', attribute='District',
                                 widget=ForeignKeyWidget(District, 'district_name'))

    class Meta:
        model = City
        fields = ('id', 'cityname', 'district_name', 'state_name')
        export_order = ('id', 'cityname', 'district_name', 'state_name')
        import_id_fields=('state_name','district_name')



@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'cityname', 'District', 'State_name')
    resource_class = CityResource


# admin.site.register(City)
class DistrictResource(resources.ModelResource):
    state_name = fields.Field(column_name='State', attribute='state',
                              widget=ForeignKeyWidget(State, 'State_name'))

    class Meta:
        model = District
        fields = ('id','district_name','state_name')
        export_order = ('id','district_name','state_name')


@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('id', 'state', 'district_name',)
    resource_class = DistrictResource



# admin.site.register(District)
class EmployeeResource(resources.ModelResource):
    bank_name = fields.Field(column_name='Bank', attribute='Bank',
                             widget=ForeignKeyWidget(Bank, 'Bank_name'))

    state_name = fields.Field(column_name='State', attribute='State',
                              widget=ForeignKeyWidget(State, 'State_name'))

    district_name = fields.Field(column_name='District', attribute='District',
                                 widget=ForeignKeyWidget(District, 'district_name'))

    # district_id=fields.Field(column_name='District', attribute='District',
    #                              widget=ForeignKeyWidget(District, 'id'))

    city_name = fields.Field(column_name='City', attribute='City',
                             widget=ForeignKeyWidget(City, 'cityname'))

    branch_name = fields.Field(column_name='Branch', attribute='Branch_name',
                               widget=ForeignKeyWidget(Branch, 'Branch_name'))

    keyskill_name = fields.Field(column_name='KeySkill', attribute='Key_Skill',
                                 widget=ForeignKeyWidget(KeySkill, 'KeySkill_name'))

    vertical_name = fields.Field(column_name='Vertical', attribute='Vertical',
                                 widget=ForeignKeyWidget(Vertical, 'Vetical_name'))

    designation_name = fields.Field(column_name='Designation', attribute='Designation',
                                    widget=ForeignKeyWidget(Designation, 'designation'))

    grade_name = fields.Field(column_name='Grade', attribute='Grade',
                              widget=ForeignKeyWidget(Grade, 'grade'))

    class Meta:
        model = Employee
        fields = ('id', 'First_name', 'Middle_Name', 'Last_name', 'Phone_no', 'Alternative_Phone_no',
                  'Email', 'bank_name', 'state_name', 'district_name', 'city_name', 'branch_name',
                  'keyskill_name', 'vertical_name', 'Cluster_head', 'Team_leader',
                  'designation_name', 'grade_name', 'CTC_in_Lacs', 'Remarks')

        export_order = ('id', 'First_name', 'Middle_Name', 'Last_name', 'Phone_no', 'Alternative_Phone_no',
                        'Email', 'bank_name', 'state_name', 'district_name', 'city_name', 'branch_name',
                        'keyskill_name', 'vertical_name', 'Cluster_head', 'Team_leader',
                        'designation_name', 'grade_name', 'CTC_in_Lacs', 'Remarks')


@admin.register(Employee)
class Employee_infoAdmin(ImportExportModelAdmin):
    list_display = ['First_name', 'Last_name', 'Phone_no', 'Bank', 'Branch_name',
                    'City', 'District', 'Key_Skill',
                    'Vertical', 'Cluster_head', 'Team_leader', 'Designation', 'Grade', 'CTC_in_Lacs']

    list_filter = (
        ('Bank', RelatedDropdownFilter),
        ('State', RelatedDropdownFilter),
        ('City', RelatedDropdownFilter),
        ('Designation', RelatedDropdownFilter),
        ('Vertical', RelatedDropdownFilter),
    )
    search_fields = ('First_name', 'Phone_no', 'Email', 'Cluster_head', 'Team_leader')
    resource_class = EmployeeResource

# admin.site.register(Employee_info,adminEmployee_info)
