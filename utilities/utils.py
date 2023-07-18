from rest_framework.views import (
    set_rollback,
    exception_handler,
)


class ResponseInfo(object):
    """
    Class for setting how API should send response.
    """

    def __init__(self, **args):
        self.response = {
            "status_code": args.get("status", 200),
            "error": args.get("error", None),
            "data": args.get("data", []),
            "message": [args.get("message", "Success")],
        }


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Update the structure of the response data.
    if response is not None:
        customized_response = dict()
        customized_response["error"] = []

        for key, value in response.data.items():
            error = key
            customized_response["status_code"] = response.status_code
            customized_response["error"] = error
            customized_response["data"] = None
            if response.status_code == 401:
                if type(value[0]) is dict:
                    customized_response["message"] = [value[0]["message"]]
                else:
                    customized_response["message"] = [value]
            else:
                if type(value) is list:
                    customized_response["message"] = [value[0]]
                else:
                    customized_response["message"] = [value]

        response.data = customized_response

        # rollback unused DB calls.
        set_rollback()

    return response
