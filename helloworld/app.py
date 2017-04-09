from chalice import Chalice
from chalice import NotFoundError
import uuid

app = Chalice(app_name='helloworld')
app.debug = True


AVAIL_FLOWER = {
    'sativa': ['AK-47', 'Blue Lightning', 'GirlScout Cookies'],
    'indica': ['Sleepy Man', 'Blue Dream', 'Sour Diseal'],
    'hybrid': ['Diseal Kush', "Ak-Man", "GirlScout Dream"]
}

# AVAIL_CareGivers = {
#     {
#         'patient_1': 'First Patient',
#         'caregivers': ['Mickey Mouse','Minnie Mouse']
#     },
#     {
#         'patient_2': 'Second Patient',
#         'caregivers': ['Donald Duck','Daphy Duck']
#     },
# }



ORDERS_PLACED = {
    '3': ['(1QP) AK-47', '(1oz) Blue Lightning', '(3g) GirlScout Cookies'],
    '2': ['(3g) Sleepy Man', '(3g) Blue Dream', '(3g) Sour Diseal'],
    '1': ['(3g) Diseal Kush', "(3g) Ak-Man", "(3g) GirlScout Dream"]
}

DEVICES_REGISTERED = {
    'Mary': ['iPhone6', '585-565-9665', 'windows 10', '00:84:80:90:50'],
    'John': ['Android','315-488-8998'],
    'Tom': ['home','315-488-8998', 'computer', 'laptop' ]
}



@app.route('/')
def index():
    return {'hello': 'world'}


# type: bud,cartridge,tincure,edible
#  subsearch underneath each at some point
@app.route('/info/{strain}')
def lookup_flowers(strain):
    return {'Inventory': AVAIL_FLOWER[strain]}


#
@app.route('/place/{order}')
def place(order):
    # performs some magic to make sure the order can be placed
    # order is taken down once fulfilled - use device fingerprints to match
    return {'order placed' : ORDERS_PLACED[order]}



#
@app.route('/retrieve/{order}')
def retrieve_order(order):
    # performs some magic to make sure the order can be placed
    # order is taken down once fulfilled - use device fingerprints to match
    return {'order retrieved' : ORDERS_PLACED[order]}


#
@app.route('/register/{device}')
def register(device):
    return {device: DEVICES_REGISTERED[device]}


OBJECTS = {}

#
@app.route('/add/{inventory}', methods=['POST','PUT', 'GET'])
def add_inventory(inventory):
    request = app.current_request
    if request.method == 'PUT' or request.method == 'POST':
        print "post command recieved"
        OBJECTS[inventory] = request.json_body
    elif request.method == 'GET':
        try:
            return {inventory: OBJECTS[inventory]}
        except KeyError:
            raise NotFoundError(inventory)
    return {inventory: OBJECTS[inventory]}



PATIENTS = {}


@app.route('/register_patient/{patientName}', methods=['POST','PUT', 'GET'])
def register_patient(patientName):
    request = app.current_request
    if request.method == 'PUT' or request.method == 'POST':
        print "post command recieved"
        PATIENTS[patientName] = request.json_body
    elif request.method == 'GET':
        try:
            return {patientName: PATIENTS[patientName]}
        except KeyError:
            raise NotFoundError(patientName)
    return {patientName: PATIENTS[patientName]}





# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return {'user_id': user_id}
#
# See the README documentation for more examples.
#
