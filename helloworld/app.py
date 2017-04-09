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

REGISTERED_PATIENTS = {}

INVENTORY = {}

PATIENTS = {}

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



#
@app.route('/patient/{register}', methods=['POST','PUT', 'GET']  )
def registered_patient(register):

    request = app.current_request
    if request.method == 'PUT' or request.method == 'POST':
        REGISTERED_PATIENTS[register] = "Patient Identifier: " + str(uuid.uuid4())
    elif request.method == 'GET':
        try:
            # return {register: REGISTERED_PATIENTS[register]}
            return {register: REGISTERED_PATIENTS}
        except KeyError:
            raise NotFoundError(register)
    return {register: REGISTERED_PATIENTS[register]}
    # return {register: "Patient Identifier: " + str(uuid.uuid4())}




#
@app.route('/add/{inventory}', methods=['POST','PUT', 'GET'])
def add_inventory(inventory):
    request = app.current_request
    if request.method == 'PUT' or request.method == 'POST':
        INVENTORY[inventory] = request.json_body
    elif request.method == 'GET':
        try:
            return {inventory: INVENTORY[inventory]}
        except KeyError:
            raise NotFoundError(inventory)
    return {inventory: INVENTORY[inventory]}






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



DISPENSARIES = [
    {
        "Organization": "Bloomfield Industries",
        "Facility": "Williamsville (Buffalo area)",
        "Address": "52 South Union Road, Suite 102,Wiliamsville, NY 14221",
        "Phone": "716-810-5219",
        "Email": "patients.williamsville@bloomfieldindustries.com",
        "Payment Type": "currently n/a",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (15% off), disability",
        "Price Range w/ Examples": "Oil Example: the product that yields 30 doses (30mL) costs about $45.48. Syrup Example: the product that yields 14 doses (7oz) costs about $21.22.",
        "Product Inventory": "Offers: oils and syrups; Coming Soon: vaporization, expected to debut in January",
        "Solution Ratios Offered": "currently n/a",
        "Days of Operation": "Mon, Tues, Fri",
        "Impressions": "friendly, willing to answer in depth questions",
        "Extras": "1) replied by email"
    },
    {
        "Organization": "Bloomfield Industries",
        "Facility": "Salina (Syracuse area)",
        "Address": "1304 Buckley Road, Suite 106, Salina,NY 13212",
        "Phone": "315-295-3531",
        "Email": "patients.salina@bloomfieldindustries.com",
        "Payment Type": "currently n/a",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (15% off), disability",
        "Price Range w/ Examples": "Oral Serum Example: the amount of product that yields 30 doses costs about $22, lasts 5-15 days. 1:1 and 1:2 solution variations available",
        "Product Inventory": "Offers: sublingual tinctures, oral serums, and oils",
        "Solution Ratios Offered": "Oral Serum Ratios:  1T:1C; 1T:2C",
        "Days of Operation": "Wed, Thurs, Fri",
        "Impressions": "friendly, willing to answer less in depth questions, seemed pressed for time",
        "Extras": ""
    },
    {
        "Organization": "Bloomfield Industries",
        "Facility": "Lake Success",
        "Address": "2001 Marcus Avenue, Lake Success, NY 11042",
        "Phone": "516-444-3452",
        "Email": "patients.lakesuccess@bloomfieldindustries.com",
        "Payment Type": "currently n/a",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (15% off), disability",
        "Price Range w/ Examples": "Sublingual Example: the amount of product that yields 20 doses costs about $30. Oral Serum Example: the amount of product that yields 14 doses costs about $22.",
        "Product Inventory": "Offers: sublingual tinctures and oral serums; Coming Soon: capsules and inhalation, debut in January",
        "Solution Ratios Offered": "currently n/a",
        "Days of Operation": "Mon, Tues, Thurs, Fri, Sat",
        "Impressions": "very friendly, patient, said I could call back anytime, willing to give detailed explanations",
        "Extras": ""
    },
    {
        "Organization": "Columbia Care NY LLC",
        "Facility": "New York City (Manhattan)",
        "Address": "212 E 14th Street, New York, NY 1003",
        "Phone": "646-453-7178",
        "Email": "NYC@col-care.com",
        "Payment Type": "Accepts: cash or debit card w/ pin number",
        "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
        "Price Range w/ Examples": "Sublingual Usage Example: 7mL lasts a week with a Rx for .5mL b.i.d; Capsule Usage Example: 14 capsules per bottle lasts a week with Rx for 1cap b.i.d; Vape Usage Example: 90 inhalations per cartridge lasts a month with Rx for 3 inhalations q.d. Vape Price Example: cartridge costs $100, one time battery fee costs $10.",
        "Product Inventory": "Offers: sublingual tinctures, capsules, and vapes.",
        "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C",
        "Days of Operation": "Mon, Wed, Fri, Sat",
        "Impressions": "extremely friendly, very patient, very helpful, very in depth explanations",
        "Extras": "1) explained that most prices/products across the Columbia Care collective were the same because all of Columbia Care's products are cultivated in Rochester, NY. 2) personal line for Julie, Columbia Care's Patient Services Coordinator,  585-678-8391."
    },
    {
        "Organization": "Columbia Care NY LLC",
        "Facility": "Riverhead",
        "Address": "13333 E Main Street, Riverhead, NY 11901",
        "Phone": "631-861-4114",
        "Email": "riverhead@col-care.com",
        "Payment Type": "Accepts: cash or debit card w/ pin number",
        "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
        "Price Range w/ Examples": "Vape Price Example: $100 for a month supply; Tinctures and Capsules Price Example: $53.50 for a  week supply",
        "Product Inventory": "Offers: tintcures, oils, and vapes",
        "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C",
        "Days of Operation": "Wed, Thurs, Fri, Sat",
        "Impressions": "willing to answer less in depth questions",
        "Extras": ""
    },
    {
        "Organization": "Columbia Care NY LLC",
        "Facility": "Plattsburgh",
        "Address": "345 Cornelia Street, Plattsburgh, NY 120901",
        "Phone": "518-930-4340",
        "Email": "plattsburgh@col-care.com",
        "Payment Type": "Accepts: cash or debit card w/ pin number",
        "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
        "Price Range w/ Examples": "Vape Price Example: $100 for a month supply; Tinctures and Capsules Price Example: $53.50 for a  week supply",
        "Product Inventory": "Offers: sublingual tinctures, capsules, and vapes",
        "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C",
        "Days of Operation": "Mon, Tues",
        "Impressions": "reluctant to give specifics on dosage and size; friendly, willing to give in depth discritptions",
        "Extras": ""
    },
    {
        "Organization": "Columbia Care NY LLC",
        "Facility": "Rochester",
        "Address": "200 West Ridge Road, Rochester, NY 14615",
        "Phone": "585-678-8390",
        "Email": "rochester@col-care.com",
        "Payment Type": "Accepts: cash or debit card w/ pin number",
        "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
        "Price Range w/ Examples": "Vape Price Example: $100; Tinctures and Capsules Price Example: $53.50",
        "Product Inventory": "Offers: sublingual tinctures, capsules, and vapes",
        "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C",
        "Days of Operation": "Mon, Fri",
        "Impressions": "reluctant to give specifics on dosage and size; friendly, willing to answer less in depth questions",
        "Extras": ""
    },
    {
        "Organization": "Etain, LLC",
        "Facility": "Albany",
        "Address": "402 North Pearl Street, Albany, NY 12207",
        "Phone": "914-437-7898",
        "Email": "info@etainhealth.com",
        "Payment Type": "Accepts: cash and debit card",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
        "Price Range w/ Examples": "currently n/a",
        "Product Inventory": "Offers: tinctures, capsules, vape, and oral spray",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Wed, Thurs, Fri",
        "Impressions": "",
        "Extras": ""
    },
    {
        "Organization": "Etain, LLC",
        "Facility": "Kingston",
        "Address": "445 State Route 28, Kingston, NY 12401",
        "Phone": "914-437-7898",
        "Email": "info@etainhealth.com",
        "Payment Type": "Accepts: cash and debit card",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
        "Price Range w/ Examples": "currently n/a",
        "Product Inventory": "Offers: tinctures, capsules, vape, and oral spray",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Tues, Wed, Thurs, Sat",
        "Impressions": "friendly, willing to answer less in depth questions",
        "Extras": ""
    },
    {
        "Organization": "Etain, LLC",
        "Facility": "Syracuse",
        "Address": "2140 Erie Boulevard E, Syracuse, NY 13224",
        "Phone": "914-437-7898",
        "Email": "info@etainhealth.com",
        "Payment Type": "Accepts: cash and debit card",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
        "Price Range w/ Examples": "currently n/a",
        "Product Inventory": "Offers: oils, vaporizers, tinctures, solutions, and oral spray",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Tues, Wed, Thurs, Sat",
        "Impressions": "friendly, willing to answer less in depth questions",
        "Extras": "only 10 diseases qualify for treatment, curently considering chronic pain as 11th ailment, explicitly said this facility doesn't currently accommodate cases for chronic pain"
    },
    {
        "Organization": "Etain, LLC",
        "Facility": "Yonkers",
        "Address": "55 Main Street, Yonkers, NY 10701",
        "Phone": "914-437-7898",
        "Email": "info@etainhealth.com",
        "Payment Type": "Accepts: cash and debit card",
        "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
        "Price Range w/ Examples": "currently n/a",
        "Product Inventory": "Offers: oils, vaporizers, tinctures, solutions, and oral spray",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Tues, Wed, Thurs, Fri",
        "Impressions": "",
        "Extras": ""
    },
    {
        "Organization": "PharmaCann, LLC",
        "Facility": "Amherst",
        "Address": "25 North Pointe Parkway, Suite 30, Amherst, NY 14228",
        "Phone": "716-636-0420",
        "Email": "contact@pharmacannis.com",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%)",
        "Price Range w/ Examples": "Oral and Sublingual Example: a 20:1 solution in a bottle (?mL), lasts for a week, costs $75.44. Inhalation/E-pen Example: a 1:1 solution in a cartridge (?mL), lasts for a month to 2 months, costs $19 per cartridge, $120 total with e-pen purchase",
        "Product Inventory": "Offers: oral, sublingual, inhalation",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Tues, Wed, Thurs, Fri, Sat",
        "Impressions": "very friendly, very patient, very in depth explanation with little prompting or inquiry",
        "Extras": "1) gave detailed explanation of application process for a medical marijuana card. 2) must have card, photo ID, and doctor recommendation every time you enter the facility regardless if you're a returning pt or not"
    },
    {
        "Organization": "PharmaCann, LLC",
        "Facility": "Liverpool",
        "Address": "642 Old Liverpool Road, Liverpool, NY 13088",
        "Phone": "315-457-0425",
        "Email": "contact@pharmacannis.com",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%). Rewards: uses a \"value system\"; you get a certain percentage off for any sales over one item",
        "Price Range w/ Examples": "Vape Usage Example:  130-150 inhalations per cartridge (?mL). Vape Price Example: USB chargeable, whole vape kit only $19.99 *resale online is $50.",
        "Product Inventory": "Offers: tincture and vape",
        "Solution Ratios Offered": "Equal Parts (1T:1C): tincture. THC Dominant (20T:1C): tincture and vape.",
        "Days of Operation": "Tues, Wed, Thurs, Fri, Sat",
        "Impressions": "very friendly, very patient, very in depth explanation with little prompting or inquiry",
        "Extras": ""
    },
    {
        "Organization": "PharmaCann, LLC",
        "Facility": "Albany",
        "Address": "10 Executive Park Drive, Albany, NY 12203",
        "Phone": "518-459-2161",
        "Email": "contact@pharmacannis.com",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%). Rewards: uses a \"value system\"; you get a certain percentage off for any sales over one item",
        "Price Range w/ Examples": "Vape Usage Example:  130-150 inhalations per cartridge (?mL). Vape Price Example: USB chargeable, whole vape kit only $19.99 *resale online is $50.",
        "Product Inventory": "currently n/a",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Tues, Wed, Thurs, Fri, Sat",
        "Impressions": "",
        "Extras": ""
    },
    {
        "Organization": "PharmaCann, LLC",
        "Facility": "Bronx",
        "Address": "405 Huntspoint Avenue, Bronx, NY 10474",
        "Phone": "718-842-2001",
        "Email": "contact@pharmacannis.com",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%). Rewards: uses a \"bulk discount\"; you get a certain percentage off for any sales over 3 items",
        "Price Range w/ Examples": "Vape Usage Example:  130-150 inhalations per cartridge (?mL). Vape Price Example: USB chargeable, whole vape kit only $19.99 *resale online is $50.",
        "Product Inventory": "Offers: tincture, capsules, and vape",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C.",
        "Days of Operation": "Mon, Tues, Wed, Thurs, Fri, Sat",
        "Impressions": "very friendly, very patient, very in depth explanation with little prompting or inquiry",
        "Extras": ""
    },
    {
        "Organization": "Vireo Health of New York LLC",
        "Facility": "White Plains Dispensary",
        "Address": "221-223 E Post Road, WhitePlains, NY 10601",
        "Phone": "844-484-7366",
        "Email": "n/a",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: financial aid and disability (10%)",
        "Price Range w/ Examples": "currently n/a",
        "Product Inventory": "Offers: oral solution, capsules, vape",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C.",
        "Days of Operation": "Wed, Thurs, Fri, Sat",
        "Impressions": "",
        "Extras": ""
    },
    {
        "Organization": "Vireo Health of New York LLC",
        "Facility": "Queens Dispensary",
        "Address": "89-55 Queens Boulevard, Elmhurst, NY 11373",
        "Phone": "844-484-7366",
        "Email": "n/a",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: financial aid and disability (10%)",
        "Price Range w/ Examples": "Vape Example: product yields about 100 puffs per cartridge. Capsule Example: product yields 30 caps per bottle. *usually distributes a month long supply at a time",
        "Product Inventory": "Offers: oral solution, capsules, vape",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C.",
        "Days of Operation": "Sun, Mon, Tues, Fri, Sat",
        "Impressions": "extremely friendly, very patient, very helpful, very in depth explanations",
        "Extras": "1) provided long explanation of how you apply for a caregiver card"
    },
    {
        "Organization": "Vireo Health of New York LLC",
        "Facility": "Binghamton Dispensary",
        "Address": "59 Harry L Drive, Johnson City, NY 13790",
        "Phone": "844-484-7366",
        "Email": "n/a",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: financial aid and disability (10%)",
        "Price Range w/ Examples": "Capsule Example: This type of medicine, like liquids, take a long time to enter your system and take effect. They also last for a long time. As a general rule, patients should wait at least 3 hours before taking another dose. Oil - Tincture  Example: It can take up to 2-3 hours for these medicines to take full effect, so you should wait three hours before taking another dose. Too often, patients do not believe the first dose is working due to the delay in effect. Be aware that these doses add up over time so please wait the recommended amount so as not to over-dose.  *procured from facility website",
        "Product Inventory": "Offers: oral solution, capsules, vape",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C.",
        "Days of Operation": "Wed",
        "Impressions": "",
        "Extras": ""
    },
    {
        "Organization": "Vireo Health of New York LLC",
        "Facility": "Albany Dispensary",
        "Address": "38 Fuller Road, Albany, NY 12205",
        "Phone": "844-484-7366",
        "Email": "n/a",
        "Payment Type": "Accepts: cash payments only",
        "Discounts": "Discounts for: financial aid and disability (10%)",
        "Price Range w/ Examples": "Oral Solution Example: 25mL bottle offered in most ratios. Capsule Example: 30 capsules per bottle offered in 1:1 ratio. Vape Example: 0.5mL, preloaded cartridge; 1mL, bulk liquid used w/ e-liquid, lasts anywhere from a week to one month dependant upon Rx from physician.",
        "Product Inventory": "Offers: oral solution, capsules, vape",
        "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C.",
        "Days of Operation": "Sun",
        "Impressions": "extremely friendly, very patient, very helpful, very in depth explanations",
        "Extras": ""
    }
]


#
@app.route('/dispensary')
def list_dispensary():
    return {'list_of_dispensaries' : DISPENSARIES}

QUALITY_RESULTS = {
    "AK-47": "PASSES: Department of Health's Wadsworth quality checks for contaminants and pesticides.  Potency: THC=25.6% CBP=1.2% ",
    "BlueLighning": "FAILS: This failed DoH testing for pesticides. Potency: THC=25.6% CBP=1.2%",
    "Gorilla": "FAILS: This failed DoH testing for pesticides. Potency: THC=22.6% CBP=0.2%",
    "GirlScoutCookies": "Passes: This passes DoH testing for pesticides. Potency: THC=0.6% CBP=22.2%",
}


#
@app.route('/quality/{rating}')
def document_quality(rating):
    return {rating: QUALITY_RESULTS[rating]}



ONCALL_DOCTORS = {
    "Bob": "http://aws.chime.com/meetup-1234",
    "Mary": "http://aws.chime.com/meetup-4567",
    "Wendel": "http://aws.chime.com/meetup-2222",
    "Doug": "http://aws.chime.com/meetup-1847"
}

#
@app.route('/meet/{doctor}')
def meet(doctor):
    return {doctor : ONCALL_DOCTORS[doctor]}

#
@app.route('/doctors')
def lookup_doctors():
    return "https://www.marijuanadoctors.com/medical-marijuana-doctors/NY"

