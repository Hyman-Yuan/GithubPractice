def my_middleware(get_response):

    print('启用中间件')

    def middleware(request):
        print('接收请求')
        response = get_response(request)
        print('发送响应')
        return response

    return middleware
