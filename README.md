# pyramid_calculator
Simple Pyramid microservice for calculations

Simple API service to do calculations. POSTS requests to <base-url>/calc should conform to a JSON format

    { "calculation": "6 * 42" }

which results in a JSON message

    { "result": "252.0" }
    
Possible error results in case of malformed calculation requests:

    {"calculation": "4 * (1&38*} " -> {"error": "Invalid calculation given: ignored (1&38*"}
    {"calculation": "4 * 2 * 6 / 8} " -> {"error": "unknown exception (calculation too complex?)"}
    {"bananarama": "1 + 1" }  -> {"error": "no calculation request given"}
    
Tests can be run with the included `nosetests`
    
    
 
