from django.shortcuts import render


def main(request):
    """Представление для отображения главной страницы"""
    return render(request, 'index.html')
