from django.http import HttpResponse
from django.template import loader, context
def vista_saludo(request):
    return HttpResponse("hola putito")


def pretty_view(request):
    templatet = loader.get_template("index.html")
    documento = templatet.render()
    return HttpResponse(documento)

