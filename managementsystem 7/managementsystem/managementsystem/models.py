# models.py
from django.db import models
from django.contrib.auth.models import User


class ElementaryStudent(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    standard = models.CharField(max_length=10)
    number_of_subjects = models.PositiveIntegerField()
    tamil_mark = models.PositiveIntegerField()
    english_mark = models.PositiveIntegerField()
    maths_mark = models.PositiveIntegerField()
    science_mark = models.PositiveIntegerField()
    social_mark = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()
    percentage = models.FloatField()
    pass_fail_status = models.CharField(max_length=10)

    # New fields for subject grades
    tamil_grade = models.CharField(max_length=2, blank=True, null=True)
    english_grade = models.CharField(max_length=2, blank=True, null=True)
    maths_grade = models.CharField(max_length=2, blank=True, null=True)
    science_grade = models.CharField(max_length=2, blank=True, null=True)
    social_grade = models.CharField(max_length=2, blank=True, null=True)

    def calculate_total_marks(self):
        # Sum up the marks for all subjects
        subject_marks = [
            self.tamil_mark,
            self.english_mark,
            self.maths_mark,
            self.science_mark,
            self.social_mark,
        ]
        self.total_marks = sum(subject_marks)

    def calculate_percentage(self):
        if self.number_of_subjects > 0:
            self.percentage = (self.total_marks / (self.number_of_subjects * 100)) * 100
        else:
            self.percentage = 0.0

    def determine_pass_fail_status(self):
        passing_percentage = 40.0
        if self.percentage >= passing_percentage:
            self.pass_fail_status = 'Pass'
        else:
            self.pass_fail_status = 'Fail'

    def determine_grades(self):
        # Determine grades based on marks (you can customize this logic)
        self.tamil_grade = self.calculate_grade(self.tamil_mark)
        self.english_grade = self.calculate_grade(self.english_mark)
        self.maths_grade = self.calculate_grade(self.maths_mark)
        self.science_grade = self.calculate_grade(self.science_mark)
        self.social_grade = self.calculate_grade(self.social_mark)

    def calculate_grade(self, mark):
        # Customize this logic based on your grading system
        if mark >= 90:
            return 'A+'
        elif mark >= 80:
            return 'A'
        elif mark >= 70:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        self.calculate_total_marks()
        self.calculate_percentage()
        self.determine_pass_fail_status()
        self.determine_grades()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_number} - {self.standard} - {self.pass_fail_status}"
class MiddleStudent(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    standard = models.CharField(max_length=10)
    number_of_subjects = models.PositiveIntegerField()
    tamil_mark = models.PositiveIntegerField()
    english_mark = models.PositiveIntegerField()
    maths_mark = models.PositiveIntegerField()
    science_mark = models.PositiveIntegerField()
    social_mark = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()
    percentage = models.FloatField()
    pass_fail_status = models.CharField(max_length=10)

    # New fields for subject grades
    tamil_grade = models.CharField(max_length=2, blank=True, null=True)
    english_grade = models.CharField(max_length=2, blank=True, null=True)
    maths_grade = models.CharField(max_length=2, blank=True, null=True)
    science_grade = models.CharField(max_length=2, blank=True, null=True)
    social_grade = models.CharField(max_length=2, blank=True, null=True)

    def calculate_total_marks(self):
        # Sum up the marks for all subjects
        subject_marks = [
            self.tamil_mark,
            self.english_mark,
            self.maths_mark,
            self.science_mark,
            self.social_mark,
        ]
        self.total_marks = sum(subject_marks)

    def calculate_percentage(self):
        if self.number_of_subjects > 0:
            self.percentage = (self.total_marks / (self.number_of_subjects * 100)) * 100
        else:
            self.percentage = 0.0

    def determine_pass_fail_status(self):
        passing_percentage = 40.0
        if self.percentage >= passing_percentage:
            self.pass_fail_status = 'Pass'
        else:
            self.pass_fail_status = 'Fail'

    def determine_grades(self):
        # Determine grades based on marks (you can customize this logic)
        self.tamil_grade = self.calculate_grade(self.tamil_mark)
        self.english_grade = self.calculate_grade(self.english_mark)
        self.maths_grade = self.calculate_grade(self.maths_mark)
        self.science_grade = self.calculate_grade(self.science_mark)
        self.social_grade = self.calculate_grade(self.social_mark)

    def calculate_grade(self, mark):
        # Customize this logic based on your grading system
        if mark >= 90:
            return 'A+'
        elif mark >= 80:
            return 'A'
        elif mark >= 70:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        self.calculate_total_marks()
        self.calculate_percentage()
        self.determine_pass_fail_status()
        self.determine_grades()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_number} - {self.standard} - {self.pass_fail_status}"
    

class HighStudent(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    standard = models.CharField(max_length=10)
    number_of_subjects = models.PositiveIntegerField()
    tamil_mark = models.PositiveIntegerField()
    english_mark = models.PositiveIntegerField()
    maths_mark = models.PositiveIntegerField()
    science_mark = models.PositiveIntegerField()
    social_mark = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()
    percentage = models.FloatField()
    pass_fail_status = models.CharField(max_length=10)

    # New fields for subject grades
    tamil_grade = models.CharField(max_length=2, blank=True, null=True)
    english_grade = models.CharField(max_length=2, blank=True, null=True)
    maths_grade = models.CharField(max_length=2, blank=True, null=True)
    science_grade = models.CharField(max_length=2, blank=True, null=True)
    social_grade = models.CharField(max_length=2, blank=True, null=True)

    def calculate_total_marks(self):
        # Sum up the marks for all subjects
        subject_marks = [
            self.tamil_mark,
            self.english_mark,
            self.maths_mark,
            self.science_mark,
            self.social_mark,
        ]
        self.total_marks = sum(subject_marks)

    def calculate_percentage(self):
        if self.number_of_subjects > 0:
            self.percentage = (self.total_marks / (self.number_of_subjects * 100)) * 100
        else:
            self.percentage = 0.0

    def determine_pass_fail_status(self):
        passing_percentage = 40.0
        if self.percentage >= passing_percentage:
            self.pass_fail_status = 'Pass'
        else:
            self.pass_fail_status = 'Fail'

    def determine_grades(self):
        # Determine grades based on marks (you can customize this logic)
        self.tamil_grade = self.calculate_grade(self.tamil_mark)
        self.english_grade = self.calculate_grade(self.english_mark)
        self.maths_grade = self.calculate_grade(self.maths_mark)
        self.science_grade = self.calculate_grade(self.science_mark)
        self.social_grade = self.calculate_grade(self.social_mark)

    def calculate_grade(self, mark):
        # Customize this logic based on your grading system
        if mark >= 90:
            return 'A+'
        elif mark >= 80:
            return 'A'
        elif mark >= 70:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        self.calculate_total_marks()
        self.calculate_percentage()
        self.determine_pass_fail_status()
        self.determine_grades()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_number} - {self.standard} - {self.pass_fail_status}"
    

class HighSecondaryBioMathStudent(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    standard = models.CharField(max_length=10)
    number_of_subjects = models.PositiveIntegerField()
    tamil_mark = models.PositiveIntegerField()
    english_mark = models.PositiveIntegerField()
    maths_mark = models.PositiveIntegerField()
    physics_mark = models.PositiveIntegerField()
    chemistry_mark = models.PositiveIntegerField()
    biology_mark = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()
    percentage = models.FloatField()
    pass_fail_status = models.CharField(max_length=10)

    # New fields for subject grades
    tamil_grade = models.CharField(max_length=2, blank=True, null=True)
    english_grade = models.CharField(max_length=2, blank=True, null=True)
    maths_grade = models.CharField(max_length=2, blank=True, null=True)
    physics_grade = models.CharField(max_length=2, blank=True, null=True)
    chemistry_grade = models.CharField(max_length=2, blank=True, null=True)
    biology_grade = models.CharField(max_length=2, blank=True, null=True)

    def calculate_total_marks(self):
        # Sum up the marks for all subjects
        subject_marks = [
            self.tamil_mark,
            self.english_mark,
            self.maths_mark,
            self.physics_mark,
            self.chemistry_mark,
            self.biology_mark,
        ]
        self.total_marks = sum(subject_marks)

    def calculate_percentage(self):
        if self.number_of_subjects > 0:
            self.percentage = (self.total_marks / (self.number_of_subjects * 100)) * 100
        else:
            self.percentage = 0.0

    def determine_pass_fail_status(self):
        passing_percentage = 40.0
        if self.percentage >= passing_percentage:
            self.pass_fail_status = 'Pass'
        else:
            self.pass_fail_status = 'Fail'

    def determine_grades(self):
       
        self.tamil_grade = self.calculate_grade(self.tamil_mark)
        self.english_grade = self.calculate_grade(self.english_mark)
        self.maths_grade = self.calculate_grade(self.maths_mark)
        self.physics_grade = self.calculate_grade(self.physics_mark)
        self.chemistry_grade = self.calculate_grade(self.chemistry_mark)
        self.biology_grade = self.calculate_grade(self.biology_mark)

    def calculate_grade(self, mark):
        
        if mark >= 90:
            return 'A+'
        elif mark >= 80:
            return 'A'
        elif mark >= 70:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        self.calculate_total_marks()
        self.calculate_percentage()
        self.determine_pass_fail_status()
        self.determine_grades()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_number} - {self.standard} - {self.pass_fail_status}"
    
class HighSecondaryComputerScienceStudent(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    standard = models.CharField(max_length=10)
    number_of_subjects = models.PositiveIntegerField()
    tamil_mark = models.PositiveIntegerField()
    english_mark = models.PositiveIntegerField()
    maths_mark = models.PositiveIntegerField()
    physics_mark = models.PositiveIntegerField()
    chemistry_mark = models.PositiveIntegerField()
    computer_science_mark = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()
    percentage = models.FloatField()
    pass_fail_status = models.CharField(max_length=10)

    # New fields for subject grades
    tamil_grade = models.CharField(max_length=2, blank=True, null=True)
    english_grade = models.CharField(max_length=2, blank=True, null=True)
    maths_grade = models.CharField(max_length=2, blank=True, null=True)
    physics_grade = models.CharField(max_length=2, blank=True, null=True)
    chemistry_grade = models.CharField(max_length=2, blank=True, null=True)
    computer_science_grade = models.CharField(max_length=2, blank=True, null=True)

    def calculate_total_marks(self):
        # Sum up the marks for all subjects
        subject_marks = [
            self.tamil_mark,
            self.english_mark,
            self.maths_mark,
            self.physics_mark,
            self.chemistry_mark,
            self.computer_science_mark,
        ]
        self.total_marks = sum(subject_marks)

    def calculate_percentage(self):
        if self.number_of_subjects > 0:
            self.percentage = (self.total_marks / (self.number_of_subjects * 100)) * 100
        else:
            self.percentage = 0.0

    def determine_pass_fail_status(self):
        passing_percentage = 40.0
        if self.percentage >= passing_percentage:
            self.pass_fail_status = 'Pass'
        else:
            self.pass_fail_status = 'Fail'

    def determine_grades(self):
        # Determine grades based on marks (you can customize this logic)
        self.tamil_grade = self.calculate_grade(self.tamil_mark)
        self.english_grade = self.calculate_grade(self.english_mark)
        self.maths_grade = self.calculate_grade(self.maths_mark)
        self.physics_grade = self.calculate_grade(self.physics_mark)
        self.chemistry_grade = self.calculate_grade(self.chemistry_mark)
        self.computer_science_grade = self.calculate_grade(self.computer_science_mark)

    def calculate_grade(self, mark):
        # Customize this logic based on your grading system
        if mark >= 90:
            return 'A+'
        elif mark >= 80:
            return 'A'
        elif mark >= 70:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        self.calculate_total_marks()
        self.calculate_percentage()
        self.determine_pass_fail_status()
        self.determine_grades()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_number} - {self.standard} - {self.pass_fail_status}"
    

class Assignments(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    test_link = models.URLField()
    
    # New field for questions
    questions = models.TextField()

    def __str__(self):
        return self.name





   