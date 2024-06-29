from datetime import datetime, timedelta
from taskqueue.models import Task
from .models import Metrics
from rest import log
from rest import decorators as rd
from rest import settings

PUSH_METRICS_TO_CLOUDWATCH = settings.get("PUSH_METRICS_TO_CLOUDWATCH", False)


@rd.periodic(minute=15, hour=10)
def run_cleanup(force=False, verbose=False, now=None):
    count = Metrics.objects.filter(expires__lte=datetime.now()).delete()
    if count > 0:
        logger = log.getLogger("auditlog", filename="auditlog.log")
        logger.info(f"METRICS.CLEANUP {count} expired records deleted")


@rd.periodic(minute=15, hour=11, weekday=1)
def run_checks(force=False, verbose=False, now=None):
    Task.Publish("metrics", "run_monitoring", channel="tq_app_handler")


@rd.periodic(minute=rd.PERIODIC_EVERY_5_MINUTES)
def run_aws_metrics(force=False, verbose=False, now=None):
    if PUSH_METRICS_TO_CLOUDWATCH:
        from metrics.providers import aws
        aws.publishLocalMetrics()
