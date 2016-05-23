from django.shortcuts import render

# Create your views here.


def node_list(request):

    return render(request, 'asset/node_list.html')
