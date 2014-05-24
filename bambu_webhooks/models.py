from django.db import models, transaction
from django.utils.timezone import now
from django.conf import settings
from bambu_webhooks import helpers
import requests, logging

LOGGER = logging.getLogger('bambu_webhooks')

class Receiver(models.Model):
    """
    A callback (or receiver) for a webhook call
    """
    
    user = models.ForeignKey('auth.User', related_name = 'webhooks')
    """The user who registered the webhook callback"""
    
    hook = models.CharField(max_length = 100, choices = helpers.get_hook_choices(), db_index = True)
    """The function to hook into"""
    
    url = models.URLField(max_length = 255, db_index = True)
    """The URL to post data to"""
    
    last_called = models.DateTimeField(null = True, blank = True)
    """The date the URL was last posted to"""
    
    def __unicode__(self):
        return self.action
    
    def cue(self, data, hash):
        if hash:
            self.actions.filter(hash = hash).delete()
        
        self.actions.create(
            hash = hash,
            data = data
        )
    
    class Meta:
        unique_together = ('url', 'hook', 'user')
        ordering = ('hook',)
        db_table = 'webhooks_receiver'

class Action(models.Model):
    """
    A temporary place to store data that is to be sent to a webhook receiver outside of the
    request-response cycle
    """
    
    receiver = models.ForeignKey(Receiver, related_name = 'actions')
    """The receiver that data is to be sent to"""
    
    hash = models.CharField(max_length = 100, null = True, blank = True, db_index = True)
    """A hash identifying the object being sent. This prevents multiple saves of a model from calling the same URL multiple times (only the last version of the object is sent)"""
    
    data = models.TextField(null = True, blank = True)
    """A JSON-serialised representation of the data"""
    
    def __unicode__(self):
        return self.hash or '(Unhashed)'
    
    def send(self):
        try:
            response = requests.post(self.receiver.url,
                data = {
                    '_action': self.receiver.hook,
                    '_hash': self.hash,
                    'data': self.data
                }
            )
        except:
            LOGGER.warn('Unable to send webhook action',
                exc_info = True,
                extra = {
                    'data': {
                        'hook': self.receiver.hook
                    }
                }
            )
        
        with transaction.commit_on_success():
            self.receiver.last_called = now()
            self.receiver.save()
            self.delete()
    
    class Meta:
        db_table = 'webhooks_action'