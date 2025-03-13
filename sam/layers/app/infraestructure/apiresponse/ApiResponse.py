import json
    
class ApiResponse:
    @staticmethod
    def __validate_status_code(status_code: int):
        if status_code is None or status_code == "":
            raise "The status_code invalid"

    def response(self, status_code: int, body: dict) -> dict:
        self.__validate_status_code(status_code)
        return {
            "statusCode": status_code,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps(body)
        }
    
    def method_not_allowed(self):
        return self.response(405, {"error": "Method not allowed"})
