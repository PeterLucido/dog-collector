from django.db import models
from django.urls import reverse
from datetime import date
from django.db import models
from django.contrib.auth.models import User

meals = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def _str_(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('toy-detail', kwargs={'pk': self.id})
  
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('dog-detail', kwargs={'dog_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(meals)
  
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=meals,
    default=meals[0][0]
  )

  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  dog = models.OneToOneField(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for dog_id: {self.dog_id} @{self.url}"