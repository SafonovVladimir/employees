from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    date_hired = models.DateField()
    email = models.EmailField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="employees"
    )

    def __str__(self):
        return f"{self.full_name} ({self.position})"
