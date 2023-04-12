from random import choice as rc, randint

# from faker import Faker

from app import app
from models import db, Apartment, Tenant, Lease

# fake = Faker()

def make_this():
    Apartment.query.delete()
    Tenant.query.delete()
    Lease.query.delete()
    a1 = Apartment(number = 1)
    a2 = Apartment(number = 54)
    a3 = Apartment(number = 23)
    a4 = Apartment(number = 7)
    a5 = Apartment(number = 12)

    a = [a1,a2,a3,a4,a5]


    t1 = Tenant(name = 'Andre', age = 27)
    t2 = Tenant(name = 'Regan', age = 23)
    t3 = Tenant(name = 'Vanessa', age = 30)

    t = [t1,t2,t3]

    l1 = Lease(rent = 5743457, apartment = a1, tenant = t3)
    l2 = Lease(rent = 5273457, apartment = a2, tenant = t1)
    l3 = Lease(rent = 4273457, apartment = a4, tenant = t2)
    l4 = Lease(rent = 1343457, apartment = a5, tenant = t1)
    l5 = Lease(rent = 2273457, apartment = a3, tenant = t3)

    l= [l1,l2,l3,l4,l5]

    db.session.add_all(a)
    db.session.add_all(t)
    db.session.add_all(l)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_this()