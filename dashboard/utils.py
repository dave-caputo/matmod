from assessments.models import Assessment
from clients.models import Client
from questionnaires.models import Qre


def get_client_list():
    return Client.objects.all()


def get_qre_list():
    return Qre.objects.all()


def get_assess_list():
    return Assessment.objects.all()
