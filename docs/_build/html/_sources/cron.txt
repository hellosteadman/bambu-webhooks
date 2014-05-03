Cron job
========

The Webhooks cron job takes all the temporarily-stored data meant to send to webhook receivers and sends
that data. It runs every minute, allowing webhooks to work outside of the request-response cycle but without
the need to setup an asynchronous handler like Celery.

Also, the use of the hash prevents the same webhook from being called multiple times for the same object, if
that object rapidly changes inside a minute. This can happen if you put your webhook call inside the
``save()`` method of your model.

Installation
------------

Once you've installed Bambu Webhooks, make sure to run ``manage.py cron --setup`` so that Bambu Cron can
pick up the Webhooks cron job.