"""прослойка"""

# from hitcount.models import HitCount
from .models import HitCount


# получаем ответ "get_response" из любого уровня middleware
def hit_count_middleware(get_response):
    """Функция которая вернёт функцию обработки запроса, делающую полезную работу"""
    # аналогична декоратору
    def middleware(request):
        # считаем только успешные переходы до первого сбоя в "get_response"
        # response = get_response(request)
        hc, created = HitCount.objects.get_or_create(path=request.path)
        if not created:
            hc.hits += 1
        hc.save()
        # считаем все переходы в том числе и с ошибками
        response = get_response(request)
        return response

    return middleware

