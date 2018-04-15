class Response(object):
    def __init__(self, success=False, records=0, data=None, msg_response=None):
        self.success = success
        self.records = records
        self.data = data
        self.msg_response = msg_response if msg_response is not None else ""

    def json(self):
        return {'success': self.success,
                'records': self.records,
                'data': self.data,
                'msg_response': self.msg_response
                }
