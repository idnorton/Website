from ..flask_admin_base import VolunteerModelView

from main import volunteer_admin, db
from models.volunteer.volunteer import Volunteer


class VolunteerUserModelView(VolunteerModelView):
    can_delete = False
    action_disallowed_list = ['delete']
    can_set_page_size = True
    can_view_details = True
    column_filters = ["trained_roles", "allow_comms_during_event"]
    column_list = (
        "user",
        "planned_arrival",
        "planned_departure",
        "nickname",
        "banned",
    )
    column_searchable_list = ("nickname", "volunteer_email")
    create_modal = True
    details_modal = True
    edit_modal = True
    form_excluded_columns = ("versions")
    page_size = 50  # the number of entries to display on the list view


# Add menu item Volunteers
volunteer_admin.add_view(
    VolunteerUserModelView(
        Volunteer,
        db.session,
        name="Volunteers"
    )
)
