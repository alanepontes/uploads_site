from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.http import HttpResponse
from .models import PostDocument
from .forms import PostDocumentForm
import mimetypes



def home(request):
    posts_documents = PostDocument.objects.all().order_by("-published_date")
    return render(request, "home.html", {'posts_documents' : posts_documents})

def post_document_detail(request, id):
    post_document = get_object_or_404(PostDocument, id=id)
    return render(request, "post_document_detail.html", {'post_document' : post_document})

@login_required(login_url="login/")
def post_document_new(request):

    if request.method == "POST":
        form = PostDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            post_document = form.save(commit=False)
            post_document.author = request.user
            post_document.published_date = timezone.now()
            post_document.docfile = request.FILES['docfile']
            post_document.save()
            return redirect('log.views.post_document_detail', id=post_document.id)
    else:
        form = PostDocumentForm()
    return render(request, 'post_document_edit.html', {'form': form})

def post_document_edit(request, id):
    post_document = get_object_or_404(PostDocument, id=id)
    if request.method == "POST":
        form = PostDocumentForm(request.POST, request.FILES, instance=post_document)
        if form.is_valid():
            post_document = form.save(commit=False)
            post_document.author = request.user
            post_document.published_date = timezone.now()
            post_document.docfile = request.FILES['docfile']
            post_document.save()
            return redirect('log.views.post_document_detail', id=post_document.id)
    else:
        form = PostDocumentForm(instance=post_document)
    return render(request, 'post_document_edit.html', {'form': form})

def post_document_download(request, id):

    post_document = get_object_or_404(PostDocument, id=id)

    filename = post_document.docfile.name.split('/')[-1]
    response = HttpResponse(post_document.docfile, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def post_document_delete(request, id):
    post_document = PostDocument.objects.get(id=id)

    if request.user == post_document.author:
        post_document.delete()

    return HttpResponseRedirect(reverse('home'))
