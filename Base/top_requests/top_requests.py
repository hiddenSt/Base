from Base.models import RequestModel


def get_top():
    all_requests = RequestModel.objects.all()
    top_requests = {}
    for request in all_requests:
        if top_requests.get(request.text):
            top_requests[request.text] += 1
        top_requests.setdefault(request.text, 1)
    return top_requests
