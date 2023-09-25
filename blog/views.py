from django.shortcuts import render

posts = [
    {
        "author": "Pawan Bhatt",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "Sept 25,2023",
    },
    {
        "author": "John Doe",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "Aug 20,2023",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts, "title": "Home"}
    return render(request, template_name="blog/home.html", context=context)


def about(request):
    context = {"title": "About"}
    return render(request, template_name="blog/about.html", context=context)
