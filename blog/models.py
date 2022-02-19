from blog import dbase


class Users(dbase.Model):
    """ Users Table """
    __tablename__ = 'users'
    id = dbase.Column(dbase.Integer, primary_key=True)
    username = dbase.Column(dbase.String(80), unique=True, nullable=False)
    email = dbase.Column(dbase.String(120), unique=True, nullable=False)
    passwd = dbase.Column(dbase.String(80), nullable=False)

    def __repr__(self):
        return 'Nom d\'utilisateur %r' % self.username
