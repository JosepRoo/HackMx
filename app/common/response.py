class Response(object):
    def __init__(self, success=False, records=0, data=None, msg_response=""):
        self.success = success
        self.records = records
        self.data = data
        self.msg_response = msg_response

    def json(self):
        return {'success': self.success,
                'records': self.records,
                'data': self.data,
                'msgResponse': self.msgResponse
                }
