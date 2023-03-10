from django.http import HttpResponse
from django.template import Template,Context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as UserAuth

def saludo(req):
 return HttpResponse("Hola coder")

def probando(req):
 mi_html = open('C:/Users/belu9/Desktop/EntregaPython/ProyectoCoder/AppCoder/static/index.html')
 plantilla = Template(mi_html.read())
 mi_html.close()
 contexto = Context()
 documento = plantilla.render(contexto)
 return HttpResponse(documento)
 
def Login(request):
    return render(request,'login.html')

def Register(req):
    return render(req,'register.html')

def about_me(request):
    return render(request, 'about-me.html')


def inicio(request):
    return render(request, 'index.html')

def Avatars(request):
    return render(request, 'avatar.html')

def Movies(request):
    return render(request, 'movie.html')

def Lista(request):
    return render(request, 'lista.html')

def Reviews(request):
    return render(request, 'reviews.html')

def Busqueda(request):
    return render(request, 'busqueda.html')

def Resultados(request):
    return render(request, 'resultados.html')



#Formulario para agregar un producto a nuestra base de datos
def add_form(request):
    if request.method == "POST":
        addmovie = AddMovie(request.POST)

        if addmovie .is_valid():
            data = addmovie.cleaned_data
            newProd = Movie(
                title=data['title'],
                img=data['img'],
                            
                description=data['description'],
                tag=data['tag']
                            )

            newProd.save()
            return redirect(inicio)
            


        else:
            return render(request, 'movies.html', {'AddMovie': AddMovie})
    
    addmovie= AddMovie()
    return render(request, 'movies.html', {'AddMovie': AddMovie})



#Formulario para agregar una orden  a nuestra base de datos

def review_form(request):
    if request.method == "POST":
        addreview = AddReview(request.POST)

        if addreview .is_valid():
            data = addreview.cleaned_data
            newRev = Review(title=data['title'],
                            img=data['img'],
                            user=data['user'],
                            date=data['date'],
                            stars=data['stars'],
                            text =data['text'])

            newRev.save()
            return redirect(inicio)
        else:
            return render(request, 'reviews.html', {'AddReview': AddReview})    

    addreview = AddReview()
    return render(request, 'reviews.html', {'AddReview': AddReview})


def fav_form(request):
    if request.method == "POST":
        myFavs = AddFav(request.POST)

        if myFavs.is_valid():
            data = myFavs.cleaned_data
            newFav = Movie(name=data['name'],
                             address=data['address'],
                             phone=data['phone'],
                              online=data['online'])

            newFav.save()
            return redirect(inicio)

    myFavs = AddFav()
    return render(request, 'lista.html', {'AddFav': AddFav})



def find_movie(request):

    if request.GET['title']:
        title = request.GET['title']
        movies = Movie.objects.filter(title__icontains=title)

        return render(request, 'resultados.html', {'movies': movies, 'title': title})

    else:
        respuesta = "No se ha encontrado la pelicula deseada"

    return HttpResponse(respuesta)
    

def register(req):
    if req.method == 'POST':

        form = UserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            form.save()
            return render(req, 'success.html', {'message': "Usuario creado"})

    else: 
        form = UserCreationForm()

    return render(req, 'register.html', {'form': form})



def login_request(req):
    form = UserCreationForm()

    if req.method == 'POST':
        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            passw = form.cleaned_data.get('pass')

            user = authenticate(user = user, passw = passw)

            if user is not None:
                login(req, user)
                return render(req, 'login-suc.html', {'message': f'Welcome, {user}!'})

            else:
                return render(req, 'login.html', {'message': f'Error: el usaurio no existe', 'form': form})
        else:
            return render(req, 'login.html', {'message':f'Error, datos incorrectos', 'form':form})
    form= AuthenticationForm()
    return render(req, 'login.html',{'form':form})




@login_required
def edit_profile(req):
    user = UserAuth.objects.get(id = req.user.id)

    if req.method == 'POST':
        my_form = UserEditForm(req.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            user.username = data['username']
            user.email = data['email']
            user.name = data['name']
            user.lastname = data['lastname']
            
            user.save()

            return redirect('perf')

    
    else:
        perform = UserEditForm(initial = {
                                      'username': user.username,
                                      'email': user.email,
                                      'name': user.name,
                                      'lastname': user.lastname,
                                       })
    
    return render(req, 'edit-profile.html', {'perform': perform, 'user': user})

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
        return redirect('reviews')
    else:
        perform  = AvatarForm()
        return render(req, 'edit-avatar.html', {'perform': perform})
    

def all_reviews(request):
    all_reviews = Review.objects.all().order_by('-tag')

    context = {'all_reviews': all_reviews, }

    return render(request, 'reviews.html', context)


def detail_reviews(request, pk):
    review = Movie.objects.get(tag=pk)

    newReview = AddNewReview()

    if request.method == 'POST':
        newReview= AddReview(request.POST)
        if  newReview.is_valid():
            data =  newReview.cleaned_data

            new_rev = Review(starts = review, 
                                  text = data['text'],
                                  username=request.user)
            new_rev.save()
            return redirect(f'/revdetail/{review.tag}')
    all_reviews = Review.objects.filter(tag=movie.tag)
    rev = len(all_reviews) > 0

    rev_context = {'all': all_reviews, 'rev': rev}
    context= {'review': review, 'req': str(request.user), 
              'comments':rev_context, 
              'AddNewreview':AddNewReview}
    
    return render(request, 'revdetail.html', context)

@login_required
def delete_review(request, pk):
    oldreview = Review.objects.get(id= pk)
    context = {'delete': oldreview}
    print('reviewdelete',oldreview.tag.tag)

    if request.method == 'POST':
        oldreview.delete()
        return redirect(f'/revdetail.html/{oldreview.tag.tag}')

    return render(request, 'warning.html', context)

@login_required
def review_form(request):
    form = AddNewReview()

    if request.method == 'POST':
        form = AddNewReview(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
           
            new_review = Review(user = request.user,
                            title = data['title'],
                            username=data['user'],
                            text = data['text'],
                            stars = data['stars'])
            new_review.save()
            return redirect('reviews')

    context = {'form':form}
    return render(request, 'newreview.html', context)

@login_required
def delete_review(request, pk):
    oldreview = Review.objects.get(id= pk)
    context = {'delete': oldreview}

    if request.method == 'POST':
        oldreview.delete()
        return redirect('reviews')

    return render(request, 'warning.html', context)

@login_required
def update_post(request, pk):
    revupdate = Review.objects.get(tag= pk)
    rev_form = AddReview(instance=revupdate)
    update = True


    context = {'form': rev_form, 'update': update}

    if request.method == 'POST':
        form = AddNewReview(request.POST, request.FILES, instance=revupdate)
        form.save()
        
        return redirect(f'/revdetail/{revupdate.id}')


    return render(request, 'newreview.html', context)