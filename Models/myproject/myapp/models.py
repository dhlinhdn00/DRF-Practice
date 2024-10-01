from django.db import models
from datetime import date
from geography.models import ZipCode
from django.utils.text import slugify

"""
    Fields
"""
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

"""
Automatic primary key fields
Verbose field names
"""
class Poll(models.Model):
    name = models.CharField(max_length=100)

class Site(models.Model):
    url = models.URLField()

class Place(models.Model):
    address = models.CharField(max_length=255)

class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    person_id = models.CharField(max_length=10, primary_key=True)
    
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="the related poll")
    sites = models.ManyToManyField(Site, verbose_name="list of sites")
    place = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name="related place")

    def __str__(self):
        return self.name

class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType, max_length=10)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

"""
Many-to-one relationships
"""
class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    company_that_makes_it = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE,
        related_name="cars_made_by_company"
    )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE,
        related_name="cars_by_manufacturer"
    )

"""
Many-to-many relationships
"""
class Topping(models.Model):
    # ...
    pass


class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)

"""
Extra fields on many-to-many relationships
"""
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

"""
Models across files
"""
class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

"""
Field name restrictions
"""
class Example(models.Model):
    foo__bar = models.IntegerField()  # 'foo__bar' has two underscores!

"""
Meta options
"""
class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

"""
Model methods
"""
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"

"""
Overriding predefined model methods
"""
class Blog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField()

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        if (
            update_fields := kwargs.get("update_fields")
        ) is not None and "name" in update_fields:
            kwargs["update_fields"] = {"slug"}.union(update_fields)
        super().save(**kwargs)

"""
Model inheritance
Abstract base classes
"""
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

"""
Meta inheritance
"""
class CommonInfo(models.Model):
    # ...
    class Meta:
        abstract = True
        ordering = ["name"]

class Student(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = "student_info"

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ["name"]

class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False


class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass

class OtherModel(models.Model):
    name = models.CharField(max_length=100)

class Base(models.Model):
    m2m = models.ManyToManyField(
        OtherModel,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass

"""
Multi-table inheritance
"""
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

"""
Meta and multi-table inheritance
"""
class ChildModel(ParentModel):
    # ...
    class Meta:
        # Remove parent's ordering effect
        ordering = []

"""
Inheritance and reserve relation
"""
class Supplier(Place):
    customers = models.ManyToManyField(Place)

"""
Proxy models
"""
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass

class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True

"""
Proxy model managers
"""
class NewManager(models.Manager):
    # ...
    pass

class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True

class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True

class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True

"""
Multiple inheritance
"""
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)

class BookReview(Book, Article):
    pass

class Piece(models.Model):
    pass

class Article(Piece):
    article_piece = models.OneToOneField(
        Piece, on_delete=models.CASCADE, parent_link=True
    )

class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

class BookReview(Book, Article):
    pass