from django.shortcuts import render


def handler403(request, exception):
    """
    Render custom 403 template instead of default.
    """
    return render(request, '403.html', status=403)


def handler404(request, exception):
    """
    Render custom 404 template instead of default.
    """
    return render(request, '404.html', status=404)


def handler405(request, exception):
    """
    Render custom 405 template instead of default.
    """
    return render(request, '405.html', status=405)


def handler500(request):
    """
    Render custom 500 template instead of default.
    """
    return render(request, '500.html', status=500)
