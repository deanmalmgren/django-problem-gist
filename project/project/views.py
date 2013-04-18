from django.template import RequestContext
from django.shortcuts import render_to_response

def wtf(request):
    from django.conf import settings
    print 'wtf', settings.TEMPLATE_CONTEXT_PROCESSORS
    return render_to_response(
        "wtf.html", {},
        context_instance=RequestContext(request),
    )
