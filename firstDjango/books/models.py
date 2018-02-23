from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):  # Creating a class of table name

    def get_absolute_url(self):
        return reverse('books:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + '-' + self.author  # This is separately added funct to display the contents of the Book table instead of just the object name

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    book_image = models.CharField(max_length=1000)

# Now you need to add migrations to this table so that the actual bd table will be created at the backend
# For that show the path to books.app.BooksConfig to setting.py under installed apps
# Then on terminal, python3 manage.py makemigrations books. Then python3 manage.py sqlmigrate books 0001. Then python3 manage.py migrate
# Whenever you make changes to database under models.py, do the above steps to make it reflect on the backend
'''
Adding data
root@kali:~/PycharmProjects/djangoTrials/firstDjango# python3 manage.py shell
Python 3.6.3 (default, Oct  3 2017, 21:16:13) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from books.models import Book  # To get the db
>>> Book.objects.all()  # To list the objects in the db
<QuerySet []>  # Says that it is empty
>>> a = Book()  # Create a new Book object a
>>> a.name = "Harry Potter"  # Adding data
>>> a.author = "JKR"
>>> a.price = "200"
>>> a.type = "Novel"
>>> a.save()  # Saving the object a
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> a.author  # Querying
'JKR'
>>>exit() 
'''
'''
Filter function
root@kali:~/PycharmProjects/djangoTrials/firstDjango# python3 manage.py shell
Python 3.6.3 (default, Oct  3 2017, 21:16:13) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from books.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter-JKR>, <Book: Manna-SHJ>]>  # after adding __str__() to the class Books, we are getting this instead of the listing of objects
>>> Book.objects.filter(pk = 1)  # filter(primaryKey = 1) to ge the details of just one object whose pk ==1
<QuerySet [<Book: Harry Potter-JKR>]>
>>> 
'''