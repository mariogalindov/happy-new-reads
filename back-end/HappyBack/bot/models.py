from django.db import models

class Character(models.Model):
    book_name = models.CharField(max_length=250)
    reading_start_time = models.DateTimeField()
    book_length = models.PositiveIntegerField()
    user_id = models.CharField(max_length=250, unique=True)
    start_date = models.DateTimeField(auto_now_add=True)
    expected_end_date = models.DateTimeField(auto_now=False)
    average_pages_to_read = models.PositiveIntegerField()
    pages_read = models.PositiveIntegerField(default=0)
    snooze = models.DateTimeField(null=True)

    def __str__(self):
        return self.book_name






 