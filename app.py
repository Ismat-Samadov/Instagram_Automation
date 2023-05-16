from instapy import InstaPy
from instapy import smart_run
# Set up your account credentials
username = '<your_username>'
password = '<your_password>'

# Create an InstaPy session
session = InstaPy(username=username, password=password)
# Set up the automation settings
with smart_run(session):
    session.set_relationship_bounds(enabled=True, potency_ratio=1.5)
    session.set_do_follow(True, percentage=100)
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')

    # Set up specific target accounts or keywords
    session.follow_by_tags(['python', 'programming'], amount=10, interact=True)
