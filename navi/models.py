from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='navi/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Resource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
