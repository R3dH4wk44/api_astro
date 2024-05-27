def uservalidation(user_name,password):
    if type(user_name) is not str:
        return {"user_check": False, "error": 'Username must be a string'}

    if type(password) is not str:
        return {"password_check": False, "user_check": True, "error": 'Password must be a string'}
    
    if len(user_name) > 20:
        return {"user_check": False, "password_check":True, "error": 'Username too long 20 Character Max'}

    if len(password) > 20:
        return {"password_check": False, "user_check":True, "error": 'Password too long, 20 Characters Max'}
    return {"password_check": True, "user_check": True}