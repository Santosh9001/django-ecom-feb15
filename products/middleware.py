import datetime

# def timing(get_response):
#     def middleware(request):
#         request.current_time = datetime.datetime.now()
#         response = get_response(request)
#         print("hello")
#         return response
#     return middleware

class Timing:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        request.current_time = datetime.datetime.now()
        response = self.get_response(request)
        print("Something")
        return response
