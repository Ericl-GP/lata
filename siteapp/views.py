from django.shortcuts import render

def base(request):
    return render(request,"st/base.html")

def cessao0(request):
    return render(request,"pg/cessao0.html")

def cessao1(request):
    return render(request,"pg/cessao1.html")

def cessao2(request):
    return render(request,"pg/cessao2.html")

def cessao3(request):
    return render(request,"pg/cessao3.html")

def cessao4(request):
    return render(request,"pg/cessao4.html")

def cessao5(request):
    return render(request,"pg/cessao5.html")

def cessao6(request):
    return render(request,"pg/cessao6.html")

def cessao7(request):
    return render(request,"pg/cessao7.html")

#------------------------------------------
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts
from .forms import PostsForm


# Create your views here.
def cessao1(request):
    template_name = 'pg/cessao1.html' # template
    posts = Posts.objects.all() # query com todas as postagens
    context = { # cria context para chamar no template
        'posts': posts
        }
    return render(request, template_name, context) # render


def post_create(request):
    if request.method == 'POST': # para metodo POST
        form = PostsForm(request.POST, request.FILES) # pega as informações do form
        if form.is_valid(): # se for valido
            form = form.save(commit=False)
            form.save() # salva
            
            messages.success(request, 'O post foi criado com sucesso') # mensagem quando cria o post
            return HttpResponseRedirect(reverse('cessao1')) # coloquei para retornar post-list
        
    form = PostsForm() # senão carrega o formulario  
    return render(request, 'pg/post-form.html', {"form": form}) # nesse template


def post_detail(request, id):
    template_name = 'pg/post-detail.html' # template
    post = Posts.objects.get(id=id) # Metodo Get
    context = { # cria context para chamar no template
        'post': post
        }
    return render(request, template_name, context) # render


def post_update(request, id):
    post = get_object_or_404(Posts, id=id) # id do post
    form = PostsForm(request.POST or None, request.FILES or None, instance=post) # pega as informações do form
    if form.is_valid(): # se for valido
        form.save() # salva
        
        messages.warning(request, 'O post foi atualizado com sucesso') # mensagem quando cria o post
        return HttpResponseRedirect(reverse('post-detail', args=[post.id])) # coloquei para retornar post-list
         
    return render(request, 'pg/post-form.html', {"form": form}) # nesse template


def post_delete(request, id): 
    post = Posts.objects.get(id=id) # pelo ID pega o objeto
    if request.method == 'POST':         
        post.delete()
        messages.error(request, 'O post foi deletado com sucesso') # quando deleta post 
        return HttpResponseRedirect(reverse('cessao1')) # retorna rota post-list
    return render(request, 'pg/post-delete.html') # nesse template