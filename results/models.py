from django.db import models


class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    maths = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()
    computer = models.IntegerField()
    social = models.IntegerField()

    total = models.IntegerField(blank=True, null=True, editable=False)
    percentage = models.FloatField(blank=True, null=True, editable=False)
    grade = models.CharField(max_length=2, blank=True, editable=False)

    def save(self, *args, **kwargs):
        # Calculate total
        self.total = (
            self.maths +
            self.english +
            self.science +
            self.computer +
            self.social
        )

        # Calculate percentage
        self.percentage = self.total / 5

        # Assign grade
        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 40:
            self.grade = "D"
        else:
            self.grade = "F"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.total}"

    class Meta:
        verbose_name_plural = "Marks"