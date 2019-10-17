from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# se programan los metodos aca.
# Create your views here.

def index(request):
    """
    Función vista para la pagina inicio de sitio.
    """
    #Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    #Libros disponibles (status ='a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() #El 'all()' esta implicito por defecto.

    # Renderiza la plantilla mHTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,
        'num_instances_available':num_instances_available,'num_authors':num_authors},
    )