from django.contrib import admin
from .models import ElementaryStudent
from .models import *



class ElementaryStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'standard', 'total_marks', 'percentage', 'pass_fail_status')
    search_fields = ('name', 'roll_number')
  
admin.site.register(ElementaryStudent, ElementaryStudentAdmin)

class MiddleStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'standard', 'total_marks', 'percentage', 'pass_fail_status')
    search_fields = ('name', 'roll_number')
   


admin.site.register(MiddleStudent, MiddleStudentAdmin)

class HighStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'standard', 'total_marks', 'percentage', 'pass_fail_status')
    search_fields = ('name', 'roll_number')

admin.site.register(HighStudent, HighStudentAdmin)

class HighSecondaryBioMathStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'standard', 'total_marks', 'percentage', 'pass_fail_status')
    search_fields = ('name', 'roll_number')
    
admin.site.register(HighSecondaryBioMathStudent, HighSecondaryBioMathStudentAdmin)

class HighSecondaryComputerScienceStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'standard', 'total_marks', 'percentage', 'pass_fail_status')
    search_fields = ('name', 'roll_number')
   
admin.site.register(HighSecondaryComputerScienceStudent, HighSecondaryComputerScienceStudentAdmin)