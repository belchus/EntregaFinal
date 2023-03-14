from django.http import HttpResponse
from django.template import Template,Context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as UserAuthfrom
from  django.views.generic import TemplateView


def inicio(request):
    return render(request, 'index.html')

def Warning(req):
    return render(req,'warning.html')


def Movies(request):
    return render(request, 'movies.html')


def Busqueda(request):
    return render(request, 'busqueda.html')

def Resultados(request):
    return render(request, 'resultados.html')



#Formulario para agregar una pelicula a nuestra base de datos
@login_required
def add_form(request):
    if request.method == "POST":
        addmovie = AddMovie(request.POST)

        if addmovie .is_valid():
            data = addmovie.cleaned_data
            newProd = Movie(
                title=data['title'],
                            
                description=data['description'],
                tag=data['tag']
                            )

            newProd.save()
            return redirect(Movies)
            
        else:
            return render(request, 'movies.html', {'AddMovie': AddMovie})
    
    addmovie= AddMovie()
    all_movies = Movie.objects.all()
    return render(request, 'movies.html', {'AddMovie': AddMovie,'all_movies': all_movies})




#Formulario para dejar una reseña a una pelicula

@login_required
def review_form(request,pk=0):
    form = AddNewReview()
    user= User.objects.get(username=request.user.username)
    print(user)

    if request.method == 'POST':
        form = AddNewReview(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
           
            new_review = Review(
                            user=user,
                            title = data['title'],
                            text = data['text'],
                            )
            new_review.save()
            return redirect(all_reviews)

    context = {'form':form}
    return render(request, 'newreview.html', context)

#Formulario para buscar una pelicula

def find_movie(request):

    if request.GET['title']:
        title = request.GET['title']
        movies = Movie.objects.filter(title__icontains=title)

        return render(request, 'resultados.html', {'movies': movies, 'title': title})

    else:
        respuesta = "No se ha encontrado la pelicula deseada"

    return HttpResponse(respuesta)
    
#Formulario para registrarse

def register(req):
    if req.method == 'POST':

        form = UserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            form.save()
            return render(req, 'sucess.html', {'message': "Usuario creado"})

    else: 
        form = UserCreationForm()

    return render(req, 'register.html', {'form': form})


#Formulario para logearse

def login_request(req):
    form = UserCreationForm()

    if req.method == 'POST':
        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            passw = form.cleaned_data['password']

            user = authenticate(username = username, password = passw)
            print(username,passw,user)
            if user is not None:
                login(req, user)
                return render(req, 'login-suc.html', {'message': f'Welcome, {user}!'})
                
            else:
                
              return render(req, 'login.html', {'message': f'Error: el usaurio no existe', 'form': form})
        else:
            return render(req, 'login.html', {'message':f'Error, datos incorrectos', 'form':form})
    form= AuthenticationForm()
    return render(req, 'login.html',{'form':form})


#Formulario para editar el perfil

@login_required
def edit_profile(req):
    user = UserAuth.objects.get(id = req.user.id)

    if req.method == 'POST':
        my_form = UserEditForm(req.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            user.username = data['username']
            user.email = data['email']
            user.first_name = data['name']
            user.last_name = data['lastname']
            
            user.save()

            return redirect(inicio)

    
    else:
        perform = UserEditForm(initial = {
                                      'username': user.username,
                                      'email': user.email,
                                      'name': user.first_name,
                                      'lastname': user.last_name,
                                       })
    
        return render(req, 'edit-profile.html', {'perform': perform, 'user': user})
    return    render(req, 'warning.html', {'message':f'Necesitas estar logeado para realizar esta accion', 'my_form':my_form})
  
    
#Formulario para crear nuestro avatar en la base de datos

@login_required
def create_avatar(req):
    
    if req.method == 'POST':
        perform = AvatarForm(req.POST, req.FILES)
        if perform.is_valid():
            try:
                old_avatar=Avatar.objects.get(user=req.user)
                if(old_avatar.image):
                    old_avatar.delete()
            except: pass
       
            
        avatar = Avatar(user=req.user, image=perform.cleaned_data['image'])
        avatar.save()
        return redirect(inicio)
    else:
        perform  = AvatarForm()
        return render(req, 'edit-avatar.html', {'perform': perform})
    

#Funcion para traer todas las reseñas
@login_required
def all_reviews(request):
    all_reviews = Review.objects.all()

    context = {'all_reviews': all_reviews, }

    return render(request, 'reviews.html', context)



#Formulario para comentar

def detail_reviews(request, pk):
    review = Review.objects.get(id=pk)
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        newReply = AddReply(request.POST)
        if newReply.is_valid():
            data = newReply.cleaned_data

            new_rev = Reply(
                text=data['text'],
                title=data['title'],
                user=user,
                review=review)
            new_rev.save()
            return redirect(f'/revdetail/{review.id}')
    else:
        newReply = AddReply()
    all_reviews = Review.objects.filter(id=user.id)
    rev = len(all_reviews) > 0
    rev_context = {'all': all_reviews, 'rev': rev}
    all_reply = Reply.objects.all()
    context = {'review': review, 'req': str(request.user),
               'replys': rev_context,
               'AddReply': AddReply(),
               'all_reply': all_reply}

    return render(request, 'revdetail.html', context)




#Funcion para eliminar la respuesta

@login_required
def delete_reply(request, pk):
    oldreview = Reply.objects.get(id= pk)
    context = {'delete': oldreview}
    print('reviewdelete',oldreview.id)

    if request.method == 'POST':
        oldreview.delete()
        return redirect(all_reviews)

    return render(request, 'warning.html', context)


#Funcion para borrar la reseña

@login_required
def delete_review(request, pk):
    oldreview = Review.objects.get(id= pk)
    context = {'delete': oldreview}

    if request.method == 'POST':
        oldreview.delete()
        return redirect(all_reviews)

    return render(request,'warning.html', context)

#Formulario para actualizar la reseña

@login_required
def update_review(request, pk):
    revupdate = Review.objects.get(id= pk)
    rev_form = AddReview(instance=revupdate)
    update = True


    context = {'form': rev_form, 'update': update}

    if request.method == 'POST':
        form = AddNewReview(request.POST, request.FILES, instance=revupdate)
        form.save()
        
        return redirect(f'/revdetail/{revupdate.id}')


    return render(request, 'newreview.html', context)
 

class Error_404(TemplateView):
    template_name = '404.html'