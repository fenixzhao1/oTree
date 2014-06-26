from ptree.session import SessionType


def session_types():
    return [
        SessionType(
            name="Prisoner Dilemma",
            base_pay=400,
            num_participants=2,
            subsession_apps=['prisoner_minimal',],
            doc="""Demo"""
        ),
        SessionType(
            name='Trust Game',
            base_pay=10,
            num_participants=2,
            subsession_apps=['trust',],
            doc="""Demo"""
        ),
        SessionType(
            name='Public Goods',
            base_pay=10,
            num_participants=4,
            subsession_apps=['public_goods',],
            doc="""Demo"""
        ),
        SessionType(
            name='Dictator',
            base_pay=100,
            num_participants=2,
            subsession_apps=['dictator',],
            doc="""Demo"""
        ),
        SessionType(
            name='Matching Pennies',
            base_pay=100,
            num_participants=2,
            subsession_apps=['matching_pennies',],
            doc="""Demo"""
        ),
    ]


def show_on_demo_page(session_type_name):
    return True

demo_page_intro_text = 'Click on one of the below sessions to play.'