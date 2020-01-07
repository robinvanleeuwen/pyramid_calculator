import unittest

from pyramid import testing


class CalculationTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        
    def tearDown(self) -> None:
        testing.tearDown()
        
    def test_calculation_success(self):
        from ..views.calculator import Calculator
        request = testing.DummyRequest(json_body={"calculation": "8 * 2"}, method="POST")
        c = Calculator(request)
        response = c.calc()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body, {"result": "16.0"})

    def test_calculation_invalid_json(self):
        from ..views.calculator import Calculator
        request = testing.DummyRequest(json_body={"calculation": "8 *333 2"}, method="POST")
        c = Calculator(request)
        response = c.calc()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body, {"error": "Invalid calculation given: ignored: *333"})

    def test_no_calculation_in_json(self):
        from ..views.calculator import Calculator
        request = testing.DummyRequest(json_body={"bananarama": "8 * 2"}, method="POST")
        c = Calculator(request)
        response = c.calc()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body, {"error": "no calculation request given"})

    def test_calculation_too_complex(self):
        from ..views.calculator import Calculator
        request = testing.DummyRequest(json_body={"calculation": "8 * 2 * 7 / 3"}, method="POST")
        c = Calculator(request)
        response = c.calc()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body, {"error": "unknown exception (calculation too complex?)"})
