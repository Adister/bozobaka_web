from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import json
import datetime
import time

from qrcodes.models import qr_code, usage, download, key_value, ordering, ratings, differnt_use
from users.models import users

# Global variables
response_data = {}
response_data['key'] = 'error'
response_data['message'] = ''

def response(key,msg):
    response_data['key'] = key
    response_data['message'] = msg

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def log_new_qr(request):

    if request.method != 'POST':
        # Got a GET request. INVALID
        return response('error','POST method only')
    
    if 'code' in request.POST and 'user_key'  and 'key' in request.POST:
        
        code = request.POST.get('code', '')
        user_key = request.POST.get('user_key', '')
        key = request.POST.get('key', '')
        user_location = request.POST.get('location', '')
        user_os = request.POST.get('os', 'android')
        
        qrcode = code
        code = code.split('-')
        type = ''

        if len(code) == 2:
            type = str(code[1])

        if not qrcode or not user_key or not key:
            return response('error','qrcode or user_id or key cannot be empty')
        else:
            # qrcode and user_id and key parameter present in POST request
            # detect the type i.e. download or rating etc
            
            # validate key is correct
            # Process further for correct key only
            if key != 'adister@123':
                return response('error','INVALID key')

            ## Got correct key
            ## Not find the type and process accordingly. 
            ## I have written brute force type code here since no I can find no better method

            ## Get the primary_key associated with the qrcode
            try:
                qrcode_ptr = qr_code.objects.get(qr_code_generated = qrcode)
                users_ptr = users.objects.get(id=user_key)

            except qr_code.DoesNotExist or users.DoesNotExist:
                ## The qrcode recieved is not present in our system
                ## User scanned different QR Code
                different_use_ptr = different_use.objects.create(qr_code_recieved=qrcode, user_id=users_ptr, os=user_os, location=user_location)
                return response('error','INVALID parameter values')
            
            else:
                ## qrcode present in our db. Process it
                
                ## Log the recieved info in the usage table
                usage_ptr = usage.objects.create(qr_code_id=qrcode_ptr, user_id=users_ptr, os=user_os, location=user_location)

                if type == '1':
                    ## '1' means attendance type i.e. which simply returns the response_text in qrcode table
                    return response('success',qrcode_ptr.response_text)

                elif type == '2':
                    ## '2' means download type. Fetch link from 'download' table and return it
                    ## The required things are already logged into 'usage' table
                    try:
                        download_ptr = download.objects.get(qr_code_id=qrcode_ptr)
                    except download.DoesNotExist:
                        return response('error','The download link was not given')
                    else:
                        return response('success', download_ptr.download_link)

                elif type == '3':
                    ## '3' means rating type system i.e. requires on input from the user
                    try:
                        key_value_ptr = key_value.objects.filter(qr_code_id=qrcode_ptr).order_by("key")
                    except key_value.DoesNotExist:
                        return response('error','No such qrcode')
                    else:
                        ## fetched the key_value pairs. Return it in json
                        for data in key_value_ptr.iterator():
                            response_data[data.key] = data.value

                        response_data['usage_id'] = usage_ptr.id
                        return response('success','Recieve type 3 key value pairs')

                elif type == '4':
                    ## '4' means ordering type. required input from user

                    try:
                        key_value_ptr = key_value.objects.filter(qr_code_id=qrcode_ptr).order_by("key")
                    except key_value.DoesNotExist:
                        return response('error','No such qrcode')
                    else:
                        ## fetched the key_value pairs. Return it in json
                        for data in key_value_ptr.iterator():
                            response_data[data.key] = data.value

                        response_data['usage_id'] = usage_ptr.id
                        return response('success','Recieve type 4 key value pairs')
                else:
                    ## got invalid type. return error
                    return response('error', 'Invalid type')

    else:
        ## IMP parameters not present
        ## Return error
        return response('error', 'Required parameters not present')        

@csrf_exempt
def log_rating(request):

    if request.method != 'POST':
        # Got a GET request. INVALID
        return response('error','POST method only')

    if 'usage_id' in request.POST and 'key' in request.POST and 'rating_key' in request.POST and 'qr_code_id' in request.POST:
        
        user_qr_code_id = request.POST.get('qr_code_id','')
        user_usage_id = request.POST.get('usage_id','')
        user_key = request.POST.get('key','')
        user_rating_key = request.POST.get('rating_key','')

        if user_key != 'adister@123':
            return response('error', 'INVALID KEY')

        if user_rating_key and user_usage_id and user_qr_code_id:
            try:
                usage_ptr = usage.objects.get(id=user_usage_id)
                qr_code_ptr = qr_code.objects.get(id=user_qr_code_id)
                key_value_ptr = key_value.objects.get(id=user_rating_key)
            except:
                return response('error', 'invalid parameter values')
            else:
                rating_ptr = ratings.objects.create(usage_id=usage_ptr, key_value_id=key_value_ptr)

                return response('success', qr_code_ptr.response_text)

        else:
            ## Empty parameter values
            return response('error', 'Empty parameter values')
    else:
        ## IMP parameters not present
        return response('error', 'Required paramters not present')

@csrf_exempt
def log_order(request):

    if request.method != 'POST':
        # Got a GET request. INVALID
        return response('error','POST method only')

    if 'usage_id' in request.POST and 'key' in request.POST and 'rating_key' in request.POST and 'order_value' in request.POST and 'qr_code_id' in request.POST:
        
        user_qr_code_id = request.POST.get('qr_code_id','')
        user_usage_id = request.POST.get('usage_id','')
        user_key = request.POST.get('key','')
        user_rating_key = request.POST.get('rating_key','')
        user_order_value = request.POST.get('order_value','')

        user_rating_key = user_rating_key.split('-')
        user_order_value = user_order_value.split('-')

        if len(user_order_value) != len(user_rating_key):
            return response('error', 'INVALID rating key')

        if user_key != 'adister@123':
            return response('error', 'INVALID KEY')

        if user_rating_key and user_usage_id and user_qr_code_id and user_order_value:
            try:
                usage_ptr = usage.objects.get(id=user_usage_id)
                qr_code_ptr = qr_code.objects.get(id=user_qr_code_id)
                
            except usage.DoesNotExist or qr_code.DoesNotExist:
                return response('error', 'invalid parameter values')
            else:

                i = 0
                while i<len(user_rating_key):
                    try:
                        key_value_ptr = key_value.objects.get(id=int(user_rating_key[i]))
                    except key_value.DoesNotExist:
                        return response('error', 'INVALID values sent')
                    else:
                        order_ptr = ordering.objects.create(usage_id=usage_ptr, key_value_id=key_value_ptr, quantity=int(user_order_value[i]))
                    i += 1

                return response('success', qr_code_ptr.response_text)

        else:
            ## Empty parameter values
            return response('error', 'Empty parameter values')
    else:
        ## IMP parameters not present
        return response('error', 'Required paramters not present')