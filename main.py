from flask import redirect

def tel_redirect(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request.args and 'tel' in request.args:
        return redirect("tel:" + str(request.args.get('tel')), code=301)
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return "No request"
