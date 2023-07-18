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