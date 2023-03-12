from polls.events_system import dispatch, register_event
from polls.functions import notify_friends, send_email


# services.py
def create_user(username:str,password:str):
    print("user was saved",username,password)

    dispatch('user_registered',username)

# main.py/bootstrap.py
register_event('user_registered',send_email)
register_event('user_registered',notify_friends)


create_user("Santosh","haigeieiwgo")

#  Signal dispatcher , Subscription signal , When to use signals