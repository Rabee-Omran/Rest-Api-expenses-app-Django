from rest_framework import response
from rest_framework.views import exception_handler

from authentication.views import AuthUserAPIView


def custom_exception_handler(exc, context):

    handlers = {
        'ValiddationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,

    }
    response = exception_handler(exc, context)

    #add status code to response
    if response is not None:

        # import pdb ; pdb.set_trace()

##########################

        #custom status code and message for custom view
        if "AuthUserAPIView" in str(context['view']) and exc.status_code == 401:
            response.status_code = 200
            response.data = {'is logged in :' : False, 'status_code' : 200}

            return response

#########################


        response.data['status_code'] = response.status_code

    #return exception class name
    exception_class = exc.__class__.__name__


    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_authentication_error(exc, context, response):
    response.data =  {
        'error': 'please login first. ',
        'status_code' : response.status_code
    }

    return response 


def _handle_generic_error(exc, context, response):
    return response
