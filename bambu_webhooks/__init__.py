from bambu_webhooks.sites import WebHookSite, NotRegistered

try:
    import json as simplejson
except ImportError:
    from django.utils import simplejson

__version__ = '2.0'
site = WebHookSite()

def send(hook, user, data = {}, hash = None):
    """
    Save the data for a named webhook to the database, so it can be sent off to the receiver outside of
    the request-response cycle.
    
    :param hook: The name of the webhook
    :param user: The user whose webhook receiver should be called
    :param data: The data to be sent (must be serialisable by Python's JSON library)
    :param hash: An optional hash to distinguish this object from others
    
    Uniquely identifying an object with a hash means that if the function that triggers the webhook is called
    multiple times within the same minute, only the latest version of the data will be sent to the webhook
    receiver.
    """
    
    if not hook in site._registry:
        raise NotRegistered('Hook %s not registered' % hook)
    
    json = simplejson.dumps(data, default = str)
    for receiver in user.webhooks.filter(hook = hook):
        receiver.cue(json, hash)