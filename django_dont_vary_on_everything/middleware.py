# -*- coding: utf-8 -*-

class RemoveVaryHeadersMiddleware(object):

    def process_response(self, request, response):
        try:
            del response['Vary'] 
        except:
            pass
        return response
