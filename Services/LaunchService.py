import uuid

class Response:
    def __init__(self,ok,body):
        self.ok = ok
        self.body = body

    def new_response(self):
        print(self.body)
        return {"ok": self.ok, "body": self.body}
    
class LaunchService:
    def __init__(self):
        self.launchList = []

    def get_launch_list(self):

        if self.launchList == []:
            response = Response(False, {"error": 'No launches Aviable'})
            print(response)
            return response.new_response()
        response = Response(True, self.launchList)
        return response.new_response()

    def get_launch_by_uuid(uuid):

        launch = [single_launch for single_launch in self.launchList if single_launch['uuid'] == uuid]

        if len(launch) == 0:
            response = Response(False, {"message": 'Launch not Found'})
            return response.new_response()
        
        response = Response(True, launch)
        return response.new_response()
