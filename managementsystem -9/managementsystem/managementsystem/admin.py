from django.contrib import admin
from .models import ElementaryStudent
from .models import *
from .models import Quiz, QuizQuestion,QuizAnswer



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

admin.site.register(Assignments1, AssignmentAdmin)

admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)


