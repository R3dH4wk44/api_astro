class Response:
    def __init__(self,ok,logged):
        
        self.ok = ok
        self.logged = logged

    def new_response(self):
        return {
            "ok": self.ok,
            "logged":self.logged
        }



class UserService:

    def __init__(self):
            self.userList = [{'user_name':'Hans', "password": 'buymeathermomix'}]

    def login(self,user):

            user_name = user['user_name']
            user_to_compare = [user_selected for user_selected in self.userList if user_selected['user_name'] == user['user_name']]
           
            
            print(user_to_compare)
            if len(user_to_compare) == 0:
                response = Response(False,False)
                return response.new_response()

            if user_to_compare[0]['password'] == user['password']:
                response = Response(True,True)
                return response.new_response()
            if user_to_compare[0]['password'] != user['password']:
                response = Response(True,False)
                return response.new_response()



    def register(self,user):

        user_name = user['user_name']
        user_to_compare = [user_selected for user_selected in self.userList if user_selected['user_name'] == user['user_name']]     

        if len(user_to_compare) > 0:
            response = Response(False,False)
            return response.new_response

        self.userList.append(user)
        response = Response(True,True)
        return response.new_response()       
   

        
