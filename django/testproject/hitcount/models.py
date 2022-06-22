from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

# должен быть один в системе
some_signal = Signal()

# Create your models here.

class HitCount(models.Model):
    """Модель для подсчёта кол-ва посещений страниц"""
    path = models.CharField(max_length=512, primary_key=True)
    hits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.path} ({self.hits})'

    # добавляем функционал по сохранению модели, можем сигналом, а можем переопределением метода "save" модели
    # при использовании иерархии моделей, наследований
    def save(self, *args, **kwargs):
        """Переопределяем метод сохранения модели"""
        # print(self)
        # вызываем наш кастомный сигнал. "self" - это будет "sender", можно передавать именованные параметры "test=1"
        # в "**kwargs". Сигналы необходимы для устранения циклических зависимостей
        # some_signal.send(self)
        some_signal.send(self, test=1)
        return super().save(*args, **kwargs)


# @receiver(post_save, sender=HitCount1) # использование для 2-й модели
# @receiver(post_save, sender=HitCount)   # использование для 1-й модели
# def post_save_hit(sender, instance, *args, **kwargs):
#     # выводим текстовое представление посещённой ссылки в консоль
#     print(instance)

# наш кастомный сигнал от нашего сигнала, делаем функцию, в ней уже не будет "instance"
@receiver(some_signal)
def post_save_hit(sender, *args, **kwargs):
    # выводим текстовое представление посещённой ссылки в консоль
    print(sender)
