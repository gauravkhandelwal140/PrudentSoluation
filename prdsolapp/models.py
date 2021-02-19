from django.core.validators import RegexValidator
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from smart_selects.db_fields import ChainedForeignKey
from import_export.admin import ImportExportModelAdmin


class Bank(models.Model):
    #Bank_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    Bank_name=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.Bank_name

    class Meta:
        verbose_name_plural = "Bank"

class Grade(models.Model):
    grade=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.grade

    class Meta:
        verbose_name_plural = "Grade"

class Designation(models.Model):
    designation=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.designation

    class Meta:
        verbose_name_plural = "Designation"

class State(models.Model):
    #State_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    State_name=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.State_name

    class Meta:
        verbose_name_plural = "State"

class District(models.Model):
   district_name=models.CharField(max_length=150)
   state = models.ForeignKey(State, on_delete=models.CASCADE)
   class Meta:
       unique_together = ('state','district_name')
       verbose_name_plural = "District"


   def __str__(self):
        return self.district_name


class City(models.Model):
    State_name = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    District = ChainedForeignKey(
        District,  # the model where you're populating your countries from
        chained_field="State_name",  # the field on your own model that this field links to
        chained_model_field="state",  # the field on Country that corresponds to newcontinent
        show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    )
    cityname = models.CharField(max_length=150)
    def __str__(self):
        return self.cityname

    class Meta:
        unique_together = ('cityname','State_name','District')
        verbose_name_plural = "City"

'''grade = (
    ("BM", "BM"),
    ("ABM", "ABM"),
    ("C", "C"),
    ("D", "D"),)'''

class Vertical(models.Model):
    #Sales_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    Vetical_name=models.CharField(max_length=130,unique=True)
    #Sales_Bank=models.ForeignKey(Bank,blank=True, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.Vetical_name

    class Meta:
        verbose_name_plural = "Vertical"


class KeySkill(models.Model):
   # KeySkill_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    KeySkill_name=models.CharField(max_length=130,unique=True)
   # KeySkill_Bank=models.ForeignKey(Bank,blank=True, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.KeySkill_name


    class Meta:
        verbose_name_plural = "Key Skill"




# designation_name = (
#     ("Branch Manager", "Branch Manager"),
#     ("Teller", "Teller"),
#     ("Assistent", "Assistent"),
#     )


class Branch(models.Model):
    # KeySkill_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    State = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    District = ChainedForeignKey(
        District,  # the model where you're populating your countries from
        chained_field="State",  # the field on your own model that this field links to
        chained_model_field="state",  # the field on Country that corresponds to newcontinent
        show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    )
    # City = ChainedForeignKey(
    #     City,  # the model where you're populating your countries from
    #     chained_field="District",  # the field on your own model that this field links to
    #     chained_model_field="District",  # the field on Country that corresponds to newcontinent
    #     show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    # )
    city=ChainedForeignKey(
        City,  # the model where you're populating your countries from
        chained_field="District",  # the field on your own model that this field links to
        chained_model_field="District",  # the field on Country that corresponds to newcontinent
        show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    )

    Branch_name = models.CharField(max_length=130, unique=True)

    class Meta:
        unique_together = ('Branch_name','city','State','District')
        verbose_name_plural = "Branch"
    # KeySkill_Bank=models.ForeignKey(Bank,blank=True, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.Branch_name




class Employee(models.Model):
    First_name = models.CharField(max_length=150)
    Middle_Name = models.CharField(max_length=150,blank=True,null=True)
    Last_name = models.CharField(max_length=150, null=True)
    Phone_no = models.CharField(
        validators=[
            RegexValidator('^[0-9]{10}$',
                           message='Invalid mobile number'
                           )],
        unique=True,max_length=10)
    Alternative_Phone_no = models.CharField(
        validators=[
            RegexValidator('^[0-9]{10}$',
                           message='Invalid mobile number'
                           )],
        max_length=10, null=True, blank=True)
    Email = models.EmailField(null=True, unique=True)
    # Bank_name=models.CharField(max_length=50,null=True,blank=True)
    Bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    #State = models.ForeignKey(State, on_delete=models.CASCADE)
    #District = models.ForeignKey(District, on_delete=models.CASCADE)
    #City = models.ForeignKey(City, on_delete=models.CASCADE)
    State = models.ForeignKey(State,null=True, on_delete=models.CASCADE)
    District = ChainedForeignKey(
        District,  # the model where you're populating your countries from
        chained_field="State",  # the field on your own model that this field links to
        chained_model_field="state",  # the field on Country that corresponds to newcontinent
        show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    )
    City = ChainedForeignKey(
        City,  # the model where you're populating your countries from
        chained_field="District",  # the field on your own model that this field links to
        chained_model_field="District",  # the field on Country that corresponds to newcontinent
        show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    )
    Branch_name=ChainedForeignKey(
        Branch,  # the model where you're populating your countries from
        chained_field="City",  # the field on your own model that this field links to
        chained_model_field="city",  # the field on Country that corresponds to newcontinent
        show_all=False,  # only shows the countries that correspond to the selected continent in newcontinent
    )

    #Branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    #Location = models.CharField(max_length=50)
    Key_Skill = models.ForeignKey(KeySkill, on_delete=models.CASCADE)
    Vertical = models.ForeignKey(Vertical, on_delete=models.CASCADE)
    Cluster_head = models.CharField(max_length=50)
    Team_leader = models.CharField(max_length=50)
    #Branch_code=models.CharField(max_length=50,null=True,blank=True)
    Designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    #CTC_in_Lacs = models.CharField(max_length=5)
    CTC_in_Lacs=models.DecimalField(max_digits=5, decimal_places=2)
    Remarks = models.CharField(blank=True, null=True, max_length=150)
   # CreatedAt = models.DateTimeField(auto_now_add=True, blank=True, null=True,read_only=True)
    #UpdatedAt = models.DateTimeField(auto_now=True, blank=True, null=True,read_only=True

    class Meta:
        verbose_name_plural = "Employee"