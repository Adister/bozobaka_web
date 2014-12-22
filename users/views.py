from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

import json
import datetime

from users.models import fb_users, gplus_users, users
from qrcodes.views import response

# Global variables
response_data = {}
response_data['key'] = 'error'
response_data['message'] = ''

@csrf_exempt
def validate_request(request):

    if request.method != 'POST':
        # Got a GET request. INVALID
        #return response('error', 'POST method only')
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    if 'type' in request.POST and 'user_id' in request.POST and 'key' in request.POST:
        
        type = request.POST.get('type', '')
        user_id = request.POST.get('user_id', '')
        key = request.POST.get('key', '')

        if not type or not user_id or not key:
            return response('error', 'type or user_id or key cannot be empty')            
        else:
            # type and user_id and key parameter present in POST request
            # detect the type i.e. fb or gplus
            
            # validate id key is correct
            # Process further for correct key only
            if key != 'adister@123':
                return response('error', 'INVALID key')                            

            user_fb_id = ''
            user_gplus_id = ''
            primary_email = request.POST.get('email', '')
            user_name = request.POST.get('name', '')
            user_gender = request.POST.get('gender', '')
            user_location = request.POST.get('location', '')
            user_phone = request.POST.get('phone', '')
            user_image_url = request.POST.get('image_url', '')
            user_profile_url = request.POST.get('profile_url', '')
            user_dob = request.POST.get('dob', datetime.datetime.now())
            user_os = request.POST.get('os', 'android')
            user_os_version = request.POST.get('os_version', '')
            user_secondary_email = request.POST.get('secondary_email', '')

            if type == 'fb':
                user_fb_id = request.POST.get('user_id', '')
                
                ## Check if the current user is already present in our db
                try:
                    p = fb_users.objects.get(user_id = user_fb_id)

                except fb_users.DoesNotExist:
                    ## New user
                    ## Log him into the fb_users table and then users table
                    p = fb_users.objects.create(user_id=user_fb_id, email=primary_email, name=user_name, gender=user_gender, location=user_location, phone=user_phone, image_url=user_image_url, profile_url=user_profile_url, date_of_birth=user_dob, mobile_os=user_os, secondary_email=user_secondary_email, os_version=user_os_version, date_added=datetime.datetime.now())

                    ## If primary_email is not empty then there might be some user in users table who did a gplus login with same email
                    ## Look for that user
                    if primary_email:
                        try:
                            u = users.objects.get(email=primary_email)

                        except users.DoesNotExist:
                            ## User with given email not present i.e. a completely new user
                            ## Log him into the users table and return the primary key

                            u = users.objects.create(email=primary_email, date_added=datetime.datetime.now(), fb_id=user_fb_id, gplus_id=user_gplus_id)
                            return response(str(u.id), 'New fb user with primary email added to users')

                        else:
                            ## User with the given email present already.

                            if not u.fb_id:
                                ## He previously registered through gplus. Update the fb id for him and return primary_key
                                users.objects.filter(email=primary_email).update(fb_id=user_fb_id)
                                return response(str(u.id), 'Updated the fb ID for the user')
                            else:
                                ## Already linked both fb and gplus
                                return response(str(u.id), 'Previously linked fb and gplus')
                    else:
                        ## we got an empty email address. 
                        ## We have not option but to log into and return the primary_key
                        temp_var = user_fb_id + '@facebook.com'
                        u = users.objects.create(email=temp_var, date_added=datetime.datetime.now(), fb_id=user_fb_id, gplus_id=user_gplus_id)

                        return response(str(u.id), 'added fb user with facebook email')
                else:
                    ## Already registered user
                    ## Search for the fb_id in users table and return its primary key
                    p_n = users.objects.get(fb_id=user_fb_id)
                    return response(str(p_n.id), 'Already registered fb user')

            elif type == 'gplus':
                user_gplus_id = request.POST.get('user_id', '')
                
                ## Check if the current user is already present in our db
                try:
                    p = gplus_users.objects.get(user_id = user_gplus_id)

                except gplus_users.DoesNotExist:
                    ## New user
                    ## Log him into the gplus_users table and then users table
                    p = gplus_users.objects.create(user_id=user_gplus_id, email=primary_email, name=user_name, gender=user_gender, location=user_location, phone=user_phone, image_url=user_image_url, profile_url=user_profile_url, date_of_birth=user_dob, mobile_os=user_os, secondary_email=user_secondary_email, os_version=user_os_version, date_added=datetime.datetime.now())

                    ## If primary_email is not empty then there might be some user in users table who did a gplus login with same email
                    ## Look for that user
                    if primary_email:
                        try:
                            u = users.objects.get(email=primary_email)

                        except users.DoesNotExist:
                            ## User with given email not present i.e. a completely new user
                            ## Log him into the users table and return the primary key

                            u = users.objects.create(email=primary_email, date_added=datetime.datetime.now(), fb_id=user_fb_id, gplus_id=user_gplus_id)
                            
                            return response(str(u.id), 'added new user to users')

                        else:
                            ## User with the given email present already.
                            ## He previously registered through fb. Update the gplus_id for him and return primary_key
                            if not u.gplus_id:
                                users.objects.filter(email=primary_email).update(gplus_id=user_gplus_id)
                                return response(str(u.id), 'updated gplus id in users for already registered fb user')
                            else:
                                return response(str(u.id), 'Already linked gplus and fb account')
                    else:
                        ## we got an empty email address. 
                        ## We have not option but to log into and return the primary_key
                        u = users.objects.create(email=user_gplus_id, date_added=datetime.datetime.now(), fb_id=user_fb_id, gplus_id=user_gplus_id)

                        return response(str(u.id), 'added gplus user with gplus id')
                else:
                    ## Already registered user
                    ## Search for the gplusid in users table and return its primary key
                    try:
                        p_n = users.objects.get(gplus_id=user_gplus_id)
                    except users.DoesNotExist:
                        return response('error', 'type of error should not occur')
                    else:
                        return response(str(p_n.id), 'Already registered gplus user')

            else:
                return response('error', 'INVALID type')
                
    else:
        # type or user_id or key not present in POST request
        # cannot process this, return error
        return response('error', 'fatal error')        
            
    