from django.db import models
from core import models as core_models


class Person(core_models.TimeStampedModel):
    KIND_ACTOR = "Actor"
    KIND_DIRECTOR = "Director"
    KIND_WRITER = "Writer"

    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=120)
    kind = models.CharField(choices=KIND_CHOICES,
                            default=KIND_ACTOR,
                            max_length=10)
    photo=models.ImageField()

    def __str__(self):
      return self.name
