from Base.models.request_model import Request


def get_top():
    all_requests = Request.objects.all()
    top_requests = {}
    for request in all_requests:
        if top_requests.get(request.text):
            top_requests[request.text] += 1
        top_requests.setdefault(request.text, 1)
    return top_requests

