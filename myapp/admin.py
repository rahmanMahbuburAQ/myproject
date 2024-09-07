from django.contrib import admin
from .models import Course, Instructor, Student, Enrollment, Transaction, Review

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'level', 'language', 'instructor', 'date_created')
    search_fields = ('title', 'description', 'instructor__name')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio')
    search_fields = ('name', 'email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled', 'completed')
    list_filter = ('completed', 'date_enrolled')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'transaction_date', 'amount_paid')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating', 'date_added')
    list_filter = ('rating', 'date_added')


