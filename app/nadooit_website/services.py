import uuid
from .models import Session, Section

session_tick = 5


def create__session():
    session = Session.objects.create(
        session_score=0,
    )
    session.save()
    return session.session_id


def received__session_still_active_signal__for__session_id(session_id):
    session = Session.objects.get(session_id=session_id)
    session.session_duration = session_tick
    session.save()
    return session.session_id


def get__next_section(session_id):
    # check if fist section
    if Session.objects.filter(session_id=session_id).exists():
        session = Session.objects.get(session_id=session_id)
        if session.session_score == 0:
            # get first section
            pass
        else:
            pass
            # get next section


def check__session_id__is_valid(session_id: uuid):
    return Session.objects.filter(session_id=session_id).exists()


def get__first_section():
    # check if there are the last first section tests are done.
    # To find that out take all first section tests and check if they are done.
    # That can be figured out by checking if the session_end_time is futher in the past than the session start_time + session_duration + session_tick.
    # If all first section tests are done, evalualte them.
    # If not create a new competition and get the first section.
    pass
