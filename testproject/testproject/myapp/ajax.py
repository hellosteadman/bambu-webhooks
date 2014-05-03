from bambu_ajax import site

@site.register
def my_ajax_function(request):
    return [
        'a', 'list', 'of', 'things'
    ]