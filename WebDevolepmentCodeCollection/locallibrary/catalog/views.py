from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
  
  """
  Функция отображения для домашней страницы сайта.
  """
  # Генерация "количеств" некоторых главных объектов
  num_books=Book.objects.all().count()
  num_instances=BookInstance.objects.all().count()
  # Доступные книги (статус = 'a')
  num_instances_available=BookInstance.objects.filter(status__exact='a').count()
  num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
  
  # Number of visits to this view, as counted in the session variable.
  num_visits = request.session.get('num_visits', 1)
  request.session['num_visits'] = num_visits+1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
  
  return render(
    request,
      'index.html',
      context=
      {'num_books': num_books, 'num_instances': num_instances, 'num)instances)availabel': num_instances_available, 'num_authors':num_authors, 'num_visits':num_visits}, # num_visits appended   
    )

from django.views import generic

class BookListView(generic.ListView):
  model= Book
  paginate_by = 10  
class BookDetailView(generic.DetailView):
  model = Book
  
  
class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author
  
  
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
  """
  Generic class-based view listing books on loan to current user.
  """
  model = BookInstance
  template_name ='catalog/bookinstance_list_borrowed_user.html'
  paginate_by = 10
  
  def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
      
      
# Added as part of challenge!
from django.contrib.auth.mixins import PermissionRequiredMixin

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
  
  """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
  model = BookInstance
  permission_required = 'catalog.can_mark_returned'
  template_name = 'catalog/bookinstance_list_borrowed_all.html'
  paginate_by = 10

  def get_queryset(self):
    
    return (
      
      BookInstance.objects.filter(borrower=self.request.user)
      .filter(status__exact='o')
      .order_by('due_back')
        )
  
  


def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author
  
  
  
  
from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
  
  """
  View function for renewing a specific BookInstance by librarian
  """
  book_inst = get_object_or_404(BookInstance, pk=pk)
  
  # If this is a POST request then process the Form data
  if request.method =='POST':
    
    # Create a form instance and populate it with data from the request (binding):
    form = RenewBookForm(request.POST)
    
    # Check if the form is valid:
    if form.is_valid():
       # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
       book_inst.due_back = form.cleaned_data['renewal_date']
       book_inst.save()
       
       # redirect to a new URL:
       return HttpResponseRedirect(reverse('all-borrowed'))
      
  # If this is a GET (or any other method) create the default form.
  else:
    proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
    form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
    
  return render(request, 'catalog/book_renew_librarian.html', {'form' :form, 'bookinst' :book_inst})


class AuthorCreate(CreateView):
  model = Author
  fields = '__all__'
  initial={'date_of_death' : ''}
  
class AuthorUpdate(UpdateView):
  model = Author
  fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
  
class AuthorDelete(DeleteView):
  model = Author
  success_url = reverse_lazy('authors')
  
  
# Classes created for the forms challenge
class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']
    permission_required = 'catalog.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_mark_returned'  
  