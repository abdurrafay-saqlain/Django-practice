from django.shortcuts import render

def hello_world(request):
    return render(request,'hello_world.html',{})
#  render() looks for HTML templates inside a directory called templates inside your app directory. 
    
# Create your views here.
