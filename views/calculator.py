import simplejson as json
from calculator.simple import SimpleCalculator
from pyramid.response import Response
from pyramid.view import view_config, view_defaults

@view_defaults(route_name="calc")
class Calculator:
    def __init__(self, request):
        self.request = request
        self.view_name = "Calculator"

    @view_config(
        renderer="json",
        request_method="POST"
    )
    def calc(self) -> Response:

        if "calculation" not in self.request.json_body:
            response_text = json.dumps({"error": "no calculation request given"})
            return Response(response_text)


        c = SimpleCalculator()
        c.run(self.request.json_body["calculation"])

        if any("ignored" in e for e in c.log):
            response_text = json.dumps(({"error": f"Invalid calculation given: {[e for e in c.log if 'ignored' in e][0]}"}))
            return Response(response_text)

        result = [e for e in c.log if 'result' in e]

        if len(result) == 1:
            result[0] = result[0].replace("result: ", "")
            response_text = json.dumps({"result": result[0]})
            return Response(response_text)

        response_text = json.dumps({"error": "unknown exception (calculation too complex?)"})
        return Response(response_text)


