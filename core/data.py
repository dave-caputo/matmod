from django.contrib.auth import get_user_model

from clients.models import Client
from questionnaires.models import Qre, Question, Section


def load_test_data():

    User = get_user_model()

    User.objects.create_superuser(
        username='davecaputo',
        email='davecaputo@outlook.com',
        password='mypassword',
    )

    Client.objects.create(
        name='ACME LTD')

    Client.objects.create(
        name='SKYNET CORP')

    fgmt = Qre.objects.create(
        name='Fruit Gourmet Maturity Model'
    )

    tropical = Section.objects.create(
        qre=fgmt,
        name='Tropical Fruits'
    )

    berries = Section.objects.create(
        qre=fgmt,
        name='Berries'
    )

    Question.objects.create(
        qre=fgmt,
        section=tropical,
        question='You eat at 5 mangos a week.'
    )

    Question.objects.create(
        qre=fgmt,
        section=tropical,
        question='You climb palm trees to get coconuts at least once a day.'
    )

    Question.objects.create(
        qre=fgmt,
        section=berries,
        question='You eat raspberries with your cereal every morning.'
    )

    Question.objects.create(
        qre=fgmt,
        section=berries,
        question='You have a blueberry smoothie when everyone else is ordering coffee.'
    )
