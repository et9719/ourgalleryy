''' Imports '''
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, NewsPost, Comment
from .forms import CommentForm, NewsForm, PostForm


class PostList(generic.ListView):
    ''' What the users should be able to see on the site '''
    # What model we are using for this view
    model = Post
    # Only show posts that have a status of published and order
    # them by the date they were created on.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # What page users will see this on
    template_name = 'gallery.html'
    # How many posts we want to see on the page at one time.
    paginate_by = 6


class PostDetail(View):
    ''' Add view for each individual post'''
    def get(self, request, slug, *args, **kwargs):
        """ Get comments for each post """
        # First filter through the post so we get just the active ones.
        queryset = Post.objects.filter(status=1)
        # Get specific post via its slug.
        post = get_object_or_404(queryset, slug=slug)
        # Then get the approved comments attached to that post.
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Find out if logged in user has liked the post.
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ post comments for each post """
        # First filter through the post so we get just the active ones.
        queryset = Post.objects.filter(status=1)
        # Get specific post via its slug.
        post = get_object_or_404(queryset, slug=slug)
        # Then get the approved comments attached to that post.
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Find out if logged in user has liked the post.
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # Get the data from the form.
        comment_form = CommentForm(data=request.POST)
        # If all fields have been completed, process the comment.
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        # If form is not valid, return empty comment form.
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


@login_required
def add_post(request):
    """ Add a post """
    # if user is not authenticated
    if not request.user.is_authenticated:
        return redirect(reverse('account_login'))
    if request.method == 'POST':
        # if form is filled out correctly save post
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('post_detail', args=[post.slug]))
    else:
        form = PostForm()

    template = 'add_post.html'
    context = {
            'form': form,
        }
    return render(request, template, context)


@login_required
def delete_post(request, slug):
    ''' Delete post '''
    post = get_object_or_404(Post, slug=slug)
    if (post.artist == request.user and request.user.is_authenticated):
        # delete post
        post.delete()
    return redirect(reverse('gallery'))


@login_required
def delete_comment(request, comment_id):
    ''' Delete comment '''
    comment = Comment.objects.get(id=comment_id)
    r = request.user
    post = comment.post
    if (comment.name == r.username and r.is_authenticated):
        # delete comment
        comment.delete()
    return redirect(reverse('gallery'))


class PostLike(View):
    ''' Allow users to like or unlike a post '''
    def post(self, request, slug):
        ''' Find out if user has liked it or not and
            allow user to toggle between the two '''
        # Get the relevant post.
        post = get_object_or_404(Post, slug=slug)
        # Toggle likes, check if post is already like
        # If it is then then remove the like.
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        # If it hasn’t been liked we need to add the like.
        else:
            post.likes.add(request.user)
        # Define where we want to redirect the
        # user when a page is liked or unliked.
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class NewsPostList(generic.ListView):
    ''' What the users should be able to see on the site '''
    # What model we are using for this view
    model = NewsPost
    # Only show posts that have a status of published and order
    # them by the date they were created on.
    queryset = NewsPost.objects.filter(status=1).order_by('-created_on')
    # What page users will see this on
    template_name = 'news.html'
    # how many posts we want to see on the page at one time.
    paginate_by = 6


class NewsPostDetail(View):
    ''' Add view to allow users to see each news post '''
    def get(self, request, slug, *args, **kwargs):
        """ get active posts, get slug for each one and
            render relevant post """
        # First filter through the post so we get just the active ones.
        queryset = NewsPost.objects.filter(status=1)
        # Get specific post via its slug.
        newspost = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "news_detail.html",
            {
                "newspost": newspost,
            }
        )


@login_required
def add_news(request):
    """ Add a news article """
    # if user is not admin show error message
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        # if form is filled out correctly save
        # news and show success message.
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect(reverse('news_detail', args=[news.slug]))
    else:
        form = NewsForm()

    template = 'add_news.html'
    context = {
            'form': form,
        }
    return render(request, template, context)


@login_required
def edit_news(request, slug):
    """ Add a news article """
    # if user is not admin show error message
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    # get news
    newspost = get_object_or_404(NewsPost, slug=slug)
    if request.method == 'POST':
        # if form is filled out correctly save
        form = NewsForm(request.POST, request.FILES, instance=newspost)
        if form.is_valid():
            form.save()
            return redirect(reverse('news_detail', args=[newspost.slug]))
    else:
        form = NewsForm(instance=newspost)

    template = 'edit_news.html'
    context = {
            'form': form,
            'newspost': newspost,
        }
    return render(request, template, context)


@login_required
def delete_news(request, slug):
    ''' Delete news article '''
    newspost = get_object_or_404(NewsPost, slug=slug)
    if (request.user.is_superuser):
        # delete news article
        newspost.delete()
    return redirect(reverse('news'))
