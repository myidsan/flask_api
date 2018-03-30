from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    # three columns into the users table Model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')
    # we have a relationship with ItemModel
    # finds the foreginkey in ItemModel of store.id
    # --> list of ItemModels
    # lazy=dynamic makes items as a query builder rather than a list of items
    # which could be expensive operation as number of item grows

    def __init__(self, name, price):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    # this should still be a classmethod because it is returning an object of
    # type ItemModel instead of a dictionary
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from __tablename__ name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
