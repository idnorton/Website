from ..flask_admin_base import FlaskVolunteerAdminAppMixin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules

from main import volunteer_admin, db
from models.volunteer.training import Training

class TrainingModelView(FlaskVolunteerAdminAppMixin, ModelView):

    can_delete = False
    can_view_details = True
    column_list = (
        "role",
        "name",
        "enabled",
    )
    details_modal = True
#    edit_modal = True
    form_columns = (
        "enabled",
        "name",
        "role",
        "pass_auto",
        "pass_mark",
        "url",
    )

volunteer_admin.add_view(TrainingModelView(Training, db.session, category="Settings"))
