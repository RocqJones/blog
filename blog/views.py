from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# At this point conventional naming is useful to make life easier when things start to get more complicated