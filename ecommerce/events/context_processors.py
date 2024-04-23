def username(request):
    return {'auto_fill_username':request.session.get('username')}