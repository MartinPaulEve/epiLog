'''
    epiLog: an object annotation system
    Copyright 2012 Martin Paul Eve

    This file is part of epiLog.

    epiLog is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    epiLog is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with epiLog. If not, see <http://www.gnu.org/licenses/>.

'''

from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from django.http import Http404
from django.template import RequestContext
from django_openid_auth.forms import OpenIDLoginForm
from django_openid_auth import views as OpenIDProcess
from django.contrib.auth import (REDIRECT_FIELD_NAME, authenticate, login as auth_login)
from django.shortcuts import redirect
from django.contrib.auth import logout as signout

def homepage(request):
    if request.method == 'POST': # If the form has been submitted...
        form = OpenIDLoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return OpenIDProcess.login_begin(request, template_name='openid/login.html',
                login_complete_view='openid-complete',
                form_class=OpenIDLoginForm,
                render_failure=OpenIDProcess.default_render_failure,
                redirect_field_name=REDIRECT_FIELD_NAME)
            
    else:
        form = OpenIDLoginForm() # An unbound form
        
    return render_to_response('homepage.html',
                              {'form': form},
                              context_instance=RequestContext(request))
    
def logout(request):
    signout(request)
    return redirect('/')