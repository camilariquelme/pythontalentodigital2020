from django.db import models

# Create your models here.
class Book(models.Model):
        title = models.CharField(max_length=255)
        descripcion = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        def __repr__(self):
            return f"Book_id={self.id}, name={self.title}"

class Publisher(models.Model):
        name = models.CharField(max_length=255)
        note = models.CharField(max_length=255)
        books = models.ManyToManyField(Book, related_name="publishers")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        def __repr__(self):
            return f"Publisher_id={self.id}, name={self.name} ,books={self.books}, note={self.note}"
