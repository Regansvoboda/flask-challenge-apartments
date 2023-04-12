from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Apartment, Tenant, Lease

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )

api = Api(app)

@app.route('/')
def index():
    response = make_response(
        {
            "message": "Hey girl!"
        },
        200
    )
    return response

@app.route('/apartments', methods=['GET', 'POST'])
def apartment():

    if request.method == 'GET':
        apartments = []
        for apartment in Apartment.query.all():
            apartment_dict = {
                'id': apartment.id,
                "number": apartment.number,
            }
            apartments.append(apartment_dict)

        response = make_response(
            apartments,
            200,
        )


    elif request.method == 'POST':
        new_apartment = Apartment(
                number=request.form.get("number"),
            )
        
        db.session.add(new_apartment)
        db.session.commit()

        apartment_dict = new_apartment.to_dict()

        response = make_response(
            apartment_dict,
            201
        )

    return response

@app.route('/apartments/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def apartment_by_id(id):
    apartment = Apartment.query.filter(Apartment.id == id).first()

    if request.method == 'GET':
        apartment_dict = apartment.to_dict()

        response = make_response(
            apartment_dict,
            200
        )
    
    elif request.method == 'PATCH':
        apartment = Apartment.query.filter(Apartment.id == id).first()
        for attr in request.form:
            setattr(apartment, attr, request.form.get(attr))

        db.session.add(apartment)
        db.session.commit()

        apartment_dict = apartment.to_dict()
        response = make_response(
            apartment_dict,
            200
        )

    elif request.method == 'DELETE':
        db.session.delete(apartment)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Apartment deleted."    
        }
        response = make_response(
            response_body,
            200
        )
    return response


@app.route('/tenants', methods=['GET', 'POST'])
def tenant():

    if request.method == 'GET':
        tenants = []
        for tenant in Tenant.query.all():
            tenant_dict = {
                'id': tenant.id,
                "name": tenant.name,
                "age": tenant.age,
            }
            tenants.append(tenant_dict)

        response = make_response(
            tenants,
            200,
        )


    elif request.method == 'POST':
        new_tenant = Tenant(
                name=request.form.get("name"),
                age=request.form.get("age"),
            )
        
        db.session.add(new_tenant)
        db.session.commit()

        tenant_dict = new_tenant.to_dict()

        response = make_response(
            tenant_dict,
            201
        )

    return response

@app.route('/tenants/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def tenant_by_id(id):
    tenant = Tenant.query.filter(Tenant.id == id).first()

    if request.method == 'GET':
        tenant_dict = tenant.to_dict()

        response = make_response(
            tenant_dict,
            200
        )
    
    elif request.method == 'PATCH':
        tenant = Tenant.query.filter(Tenant.id == id).first()
        for attr in request.form:
            setattr(tenant, attr, request.form.get(attr))

        db.session.add(tenant)
        db.session.commit()

        tenant_dict = tenant.to_dict()
        response = make_response(
            tenant_dict,
            200
        )

    elif request.method == 'DELETE':
        db.session.delete(tenant)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Tenant deleted."    
        }
        response = make_response(
            response_body,
            200
        )
    return response

@app.route('/leases')
def leases():

    leases = []
    for lease in Lease.query.all():
        lease_dict = lease.to_dict()
        leases.append(lease_dict)

    response = make_response(
        leases,
        200
    )

    return response

@app.route('/leases/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def lease_by_id(id):
    lease = Lease.query.filter(Lease.id == id).first()

    if request.method == 'GET':
        lease_dict = lease.to_dict()

        response = make_response(
            lease_dict,
            200
        )
    
    elif request.method == 'PATCH':
        lease = Lease.query.filter(Lease.id == id).first()
        for attr in request.form:
            setattr(lease, attr, request.form.get(attr))

        db.session.add(lease)
        db.session.commit()

        lease_dict = lease.to_dict()
        response = make_response(
            lease_dict,
            200
        )

    elif request.method == 'DELETE':
        db.session.delete(lease)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Lease deleted."    
        }
        response = make_response(
            response_body,
            200
        )
    return response
if __name__ == '__main__':
    app.run( port = 3000, debug = True )