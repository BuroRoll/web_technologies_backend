from django.http import HttpResponse
from django.shortcuts import redirect, render


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>BrowserCookies</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("BrowserCookies<br> cookie created")
    else:
        response = HttpResponse("BrowserCookies <br> Your browser does not accept cookies")
    return response


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>BrowserCookies<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of BrowserCookies</h1><br>"
    if request.session.get('name'):
        response += f"Name : {request.session.get('name'))} < br > "
    if request.session.get('password'):
        response += f"Password : {request.session.get('password')} <br>"
        return HttpResponse(response)
    else:
        return redirect('create/')


def delete_session(request):
    try:
        # Delete a specific session key
        del request.session['name']
        del request.session['password']
        # Delete all session data
        request.session.flush()
    except KeyError:
        pass
        # Redirect to a page after deleting session data
    return HttpResponse("<h1>BrowserCookies<br>Session Data cleared</h1>")
