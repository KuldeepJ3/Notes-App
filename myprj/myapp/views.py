from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from . forms import CreateUserForm, LoginForm, CreateNoteForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Note

# Create your views here.
	
def home(request):
	return render(request, 'home.html')

def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("home")


    context = {'loginform':form}

    return render(request, 'registration/login.html', context=context)

@login_required(login_url='login')
def notes_list(request):
	if request.user.is_authenticated:
		user = request.user
		notes = Note.objects.filter(user=user).order_by('-created_at')
		context = {'notes': notes}
		return render(request, 'list.html', context)
	else:
		return redirect('login/')

def register(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('login')

	context = {'registerform':form}

	return render(request, 'lsapp/register.html', context=context)

@login_required(login_url='login')
def logout(request):

	auth.logout(request)

	return redirect('home')

@login_required(login_url='login')
def create_note(request):
	if request.method == 'POST':
		form = CreateNoteForm(request.POST)
		if form.is_valid():
			user = request.user
			note = Note.objects.create(user=user, title=form.cleaned_data['title'], content=form.cleaned_data['content'])
			return redirect('list')
	else:
		form = CreateNoteForm()
	context = {'form': form}
	return render(request, 'create_note.html', context)

@login_required(login_url='login')
def delete_note(request, pk):
  # Get the note object based on the primary key (pk)
  note = get_object_or_404(Note, pk=pk, user=request.user)
  
  if request.method == 'POST':
    # If it's a POST request (confirmation), delete the note
    note.delete()
    # Redirect to the list view after successful deletion
    
    return redirect('list')
  else:
    # If it's a GET request (confirmation prompt), display confirmation message
    context = {'note': note}
    return render(request, 'delete_note.html', context)


@login_required(login_url='login')
def note_detail_edit(request, note_id):
  note = get_object_or_404(Note, pk=note_id, user=request.user)

  if request.method == 'POST':
    form = CreateNoteForm(request.POST, instance=note)  
    if form.is_valid():
      form.save()
      return redirect('list')  
  else:
    form = CreateNoteForm(instance=note)

  context = {'note': note, 'form': form}
  return render(request, 'note_detail_edit.html', context)

@login_required(login_url='login')
def note_detail(request, note_id):
  note = get_object_or_404(Note, pk=note_id, user=request.user)
  context = {'note': note}
  return render(request, 'note_detail.html', context)

