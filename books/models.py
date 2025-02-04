from django.db import models

class Author (models.Model):
  name = models.CharField(max_length=100)
  birth_date = models.DateField()

  def _str_(self):
    return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    publish_date = models.DateField()

    def __str__(self):
        return self.title
