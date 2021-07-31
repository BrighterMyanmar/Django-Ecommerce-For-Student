from django.shortcuts import redirect

def getList(group):
    groups = []
    for g in group:
        groups.append(g.name)
    return groups

def allow_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request,*args,**kwargs):
            if(request.user.groups.exists()):
                gps = request.user.groups.all()
                groups = getList(gps)
                matches = list(set(groups).intersection(set(allowed_roles)))
                if len(matches) > 0:
                    return view_fun(request,*args,**kwargs)
                else :
                    return redirect('/user/login')
            else :
                return redirect('/user/login')
        return wrapper_fun
    return decorator
            

