from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Book Object: {self.id}, {self.title}, {self.desc}"

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Books, related_name= "book_authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        book = ""
        if len(self.books.all()) == 0:
            book = "This author has no books"
        else:
            for i in self.books.all():
                book += i.title + ", "
        return f"Author Object: id = {self.id}, first name = {self.first_name}, last name = {self.last_name}, Books = {book}"