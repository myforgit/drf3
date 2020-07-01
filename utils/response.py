from  rest_framework.response import Response

class apiresponse(Response):

    def __init__(self,status=200,massge=0,results=None,http_status=None, headers=None,
                 exception=False, **kwargs):
        data= {
            "starus":status,
            "massge":massge
        }

        if  results is not None:
            data["resulte"]=results

        data.update(kwargs)

        super().__init__(data=data, status=http_status, headers=headers, exception=exception)