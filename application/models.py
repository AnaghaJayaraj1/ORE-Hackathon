from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):

    NOACTION = 'N'
    ACTION = 'A'
    VERIFIED = 'V'
    ACTIONTAKEN = [
        (NOACTION, 'No Action'),
        (ACTION, 'Action'),
        (VERIFIED, 'Verified'),
    ]

    DEATH = 'D'
    BIRTH = 'B'
    REVENUE = 'R'
    CONTRACT = 'C'
    TYPE_OF_CERTIFICATE = [
        (DEATH, 'Death Certificate'),
        (BIRTH, 'Birth Certificate'),
        (REVENUE, 'Revenue Certificate'),
        (CONTRACT, 'Contract Certificate'),
    ]

    date = models.DateField(max_length=100)
    name = models.CharField(max_length=100)
    typeofcertificate = models.CharField(
        max_length=1,
        choices=TYPE_OF_CERTIFICATE,
        default=BIRTH,
    )

    empid = models.CharField(max_length=100, default=000)
    fileid = models.CharField(max_length=100)
    action = models.CharField(
        max_length=1,
        choices=ACTIONTAKEN,
        default=NOACTION,
    )

    def __str__(self):
        return self.fileid
