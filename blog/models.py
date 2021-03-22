from django.db import models

from author.models import Author


class Category:
    pass

# Many to one
# Many blogs will with a single writer


class BlogPost(models.Model):
    title = models.CharField(max_length=300, null=True)
    authors = models.ManyToManyField(
        Author, blank=True)
    image = models.ImageField(upload_to="blog_images", blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"My Django Blog: {self.title}"

    # inner class
    class Meta:
        db_table = "myblogpost"
        verbose_name_plural = "My Blog Post"

    def upper_title(self):
        return self.title.upper()


# Relational Database
# Sqlite3, Mysql, Postgres

# One to One relation
# Many to one Relation
# Many to Many Relation


# Non relational database
# MongoDB

# One to One Relation
class Country():
    pass


class Capital():
    pass


class User():
    pass


class Profile:
    pass

# Many to one relationship
# Foreign Key


class Mother:
    pass


class Children:
    pass

# Many to Many relationship
