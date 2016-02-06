from main import db
from datetime import datetime

CFP_STATES = ['new', 'locked', 'rejected', 'to_anonymise']

class CfpStateException(Exception):
    pass


class Proposal(db.Model):
    __versioned__ = {}
    __tablename__ = 'proposal'
    # Admin
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    state = db.Column(db.String, nullable=False, default='new')
    type = db.Column(db.String, nullable=False)  # talk, workshop or installation

    # Core information
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String)
    length = db.Column(db.String)  # only used for talks and workshops
    notice_required = db.Column(db.String)

    # Flags
    needs_help = db.Column(db.Boolean)
    needs_money = db.Column(db.Boolean)
    one_day = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_on': type}

    def set_state(self, state):
        state = state.lower()
        if state not in CFP_STATES:
            raise CfpStateException('"%s" is not a valid state' % state)
        self.state = state


class TalkProposal(Proposal):
    __mapper_args__ = {'polymorphic_identity': 'talk'}
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)


class WorkshopProposal(Proposal):
    __mapper_args__ = {'polymorphic_identity': 'workshop'}
    attendees = db.Column(db.String)
    cost = db.Column(db.String)


class InstallationProposal(Proposal):
    __mapper_args__ = {'polymorphic_identity': 'installation'}
    size = db.Column(db.String)
    funds = db.Column(db.String, nullable=True)


class TalkCategory(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    proposals = db.relationship(TalkProposal, backref='category')

