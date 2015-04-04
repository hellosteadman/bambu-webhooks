from bambu_webhooks.models import Action
import bambu_cron as cron

class WebHooksJob(cron.CronJob):
    frequency = cron.MINUTE

    def run(self, logger):
        for action in Action.objects.all():
            action.send()

cron.site.register(WebHooksJob)
