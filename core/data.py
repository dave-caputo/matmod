from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from clients.models import Client
from questionnaires.models import Qre
from questions.models import Question
from sections.models import Section

from .admin import CustomAdminSite


def load_test_data():

    # Admin site

    site = Site.objects.get_current()
    site.name = 'Tech Modelling'
    site.save()

    CustomAdminSite.name = site.name

    # User

    User = get_user_model()

    User.objects.create_superuser(
        username='superuser',
        email='test_user@example.com',
        password='mypassword',
    )

    User.objects.create_user(
        username='test_admin1',
        email='test_admin1@example.com',
        password='somepassword',
        is_staff=True,
    )

    User.objects.create_user(
        username='test_admin2',
        email='test_admin2@example.com',
        password='somepassword',
        is_staff=True,
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

    frozen_fruit = Section.objects.create(
        qre=fgmt,
        name='Frozen fruit'
    )

    Question.objects.create(
        section=tropical,
        question='You eat at 5 mangoes a week.',
        choice_text_1='I eat zero mangoes. I hate them.',
        choice_text_2='I have a mango once in a blue moon.',
        choice_text_3='I eat at least 3 mangoes a week.',
        choice_text_4='I eat 4 mangoes a week and feel great.',
        choice_text_5='I eat 5 or more mangoes a day because I can\'t have enough of them.',
    )

    Question.objects.create(
        section=tropical,
        question='You climb palm trees to get coconuts at least once a day.',
        choice_text_1='I climb palm trees but avoid the coconuts.',
        choice_text_2='I eat coconuts once a month but rarely climb the palm tree.',
        choice_text_3='I climb every other day.',
        choice_text_4='I climb every day, eat my coconuts and feel no shame about it.',
        choice_text_5='Nobody climbs palm trees to get coconuts more than me every a day.',
    )

    Question.objects.create(
        section=berries,
        question='You add raspberries to your cereal every morning.',
        choice_text_1='I only eat sausage and eggs for breakfast.',
        choice_text_2='I dont have anything against raspberries in my cereal but I rarely have them.',
        choice_text_3='I add raspberries with my cereal once a month.',
        choice_text_4='I mostly add rasbperries but sometimes I need to change and add blueberries instead.',
        choice_text_5='I only know the meanining of breakfast as having cereal with raspberries.',
    )

    Question.objects.create(
        section=berries,
        question='You have a blueberry smoothie when everyone else is ordering coffee.',
        choice_text_1=' I love coffee, and never heard about blueberries.',
        choice_text_2='I tend to prefer coffee, but sometimes go for blueberry smoothie.',
        choice_text_3='I alternate between blueberry smoothies and coffee.',
        choice_text_4='I prefer blueberry smoothies but sometimes give up due to peer pressure',
        choice_text_5='I absolutely go for blueberry smoothie. I don\'t care about coffee',
    )

    Question.objects.create(
        section=frozen_fruit,
        question='I always have a fruit sorbet as dessert at dinner.',
        choice_text_1='The thought of a fruit sorbet makes me sick.',
        choice_text_2='I had a sorbet once and liked it, but then I never remember to take one again.',
        choice_text_3='I have a fruit sorbet once a month.',
        choice_text_4='I really like sorbets, but sometimes can\'t resist a creme brulee.',
        choice_text_5='Fruit sorbet for dessert is my religion.',
    )

    Question.objects.create(
        section=frozen_fruit,
        question='You use frozen fruit as ice cubes in your drinks.',
        choice_text_1='Never. I wouldn\'t change the .',
        choice_text_2='Sometimes, but only when I run out of ice cubes.',
        choice_text_3='I like it but only when drinking water.',
        choice_text_4='I prefer frozen fruit but wouldn\'t say no to ice cubes.',
        choice_text_5='Always. In my house is forbidden to buy anything else.',
    )
