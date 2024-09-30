from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


STATUS = (
    (0, 'New'),
    (1, 'Process'),
    (2, 'Completed'),
    (3, 'Cancelled'),
)


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS)
    deadline = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
