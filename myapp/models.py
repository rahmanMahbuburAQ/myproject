from django.db import models

# Create your models here.

class Course(models.Model):

    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in hours")
    level = models.CharField(max_length=100, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    language = models.CharField(max_length=50, choices=[('Dart', 'Dart'), ('Java', 'Java'), ('Python', 'Python'), ('JavaScript', 'JavaScript')])
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, related_name='courses')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='instructors/', blank=True, null=True)

    def __str__(self):
        return self.name


from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_courses = models.ManyToManyField(Course, through='Enrollment', related_name='students')

    def __str__(self):
        return self.user.username
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
    

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.student.user.username} bought {self.course.title} for {self.amount_paid}"



class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username}'s review for {self.course.title}"


