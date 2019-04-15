from django.http import HttpResponse
from django.views import View
from django.shortcuts import render



def index(request):
    return render(request, 'lgmssis/index.html')


# def courselist(request):
#     return render(request, 'lgmssis/course-listing.html')
def my_render_callback(response):
    # Do content-sensitive processing
    do_post_processing()


def courselist(request):
    # Create a response
    response = TemplateResponse(request, 'lgmssis/course-listing.html', {})
    # Register the callback
    response.add_post_render_callback(my_render_callback)
    # Return the response
    return response
