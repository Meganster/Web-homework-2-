from cgi import parse_qsl, parse_qs

html = """
<html>
<body>
   <form method="post" action="">
        <p>
           intVal: <input type="text" name="intVal" value="%(intVal)s">
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
</body>
</html>
"""

def app(environ, start_response):
    status = '200 OK'

    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    d = parse_qs(environ['wsgi.input'].read(request_body_size))

    intVal = d.get('intVal', [''])[0]

    htmlPart = ""
    htmlPart += html % {
        'intVal': intVal or 'Empty',
    }

    postLine = "POST data:<br>"

    for key in d:
        postLine += str(key) + ": "
        for value in d[key]:
            postLine += str(value) + " "
        postLine += "<br>"

    d = parse_qsl(environ["QUERY_STRING"])

    getLine = "GET data:<br>"
    if environ["QUERY_STRING"] != '':
        for ch in d:
            getLine += " = ".join(ch)
            getLine += "<br>"


    response_body = (htmlPart + "<br><br>" + postLine +
        "<br><br>" + getLine)
    output_len =(sum(len(line) for line in response_body))

    response_headers = [('Content-type','text/html'),
                        ('Content-Length',str(output_len))]
    start_response(status, response_headers)
    return response_body
