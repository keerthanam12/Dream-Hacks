from django.contrib import admin
from .models import ElementaryStudent
from .models import *
from .models import QuizSubmission



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

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'test_link', 'questions')
    search_fields = ('name', 'description', 'questions')

admin.site.register(Assignments, AssignmentAdmin)


@admin.register(QuizSubmission)
class QuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'assignment', 'answer_1', 'answer_2', 'answer_3', 'answer_4']