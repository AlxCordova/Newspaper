from django.contrib.auth.mixins import LoginRequiredMixin # accesos al app
from django.core.exceptions import PermissionDenied # accesos de usuarios
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article, Comment
from .forms import CommentForm
from django.shortcuts import render

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
    comment_form = CommentForm

    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST, request.FILES)
    #     if comment_form.is_valid():
    #         comment_form.save()
    #             # do something.
    # else:
    #     comment_form = AuthorFormSet()
    
    # render(template_name, {'comment_form': comment_form})
    
    # comment_form = Form(instance=self.obj, data=request.POST, files=request.FILES)
    # if comment_form.is_valid():
    #     obj = comment_form.save(commit=False)
    # if comment_form.is_valid():
    #     comment_form.save()
    # else:
    #     comment_form = CommentForm()
    
    # return render(request, template_name,{'comment_form': comment_form})
    # def CommentForm(request):
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         # obj=comment_form.save(commit=False)
    #         obj.save()
    #         #context = {'form': comment_form}
    #     else:
    #         context = {'error': 'The post has been successfully created. Please enter boq'}
    #         return render(request, template_name, {'comment_form': comment_form})
            

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)