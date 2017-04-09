# HackUpstate9 Project - 

## Overview:

The primary purpose of this project was to identify a problem within a vertical industry & challenge myself to start rapidly prototyping using emerging technologies & cloud solutions.  

This project aims to initially publish a open dataset of information for Patients & CareGivers  I believe this offering of data will allow others to find, engage, & intereact w/ Doctors & Dispensaries within the communities of NYS 
  

### Problem Statement:

* NYS has implemented one of the worst Medical Marijuana programs in the country.  In terms of innovation - NYS is again well behind our constituents in other cities, counties, and states.  
* NYS does not provide public data for patients to easily find a network of registered doctors.  
* Dispensaries within NYS have many regulations & restrictions which do not allow marketing.  There are no online menus with options/prices as a result
* NYS Dept. of Health is involved in price-fixing & openly discuss it on their site. The cost of 'approved' medical marijuana in NYS is unaffordable as a result

As a result,
* Patients are struggling to gain access to variety of reasonably-cost medicine
* Dispensaries have not been profitable due to a low number of registered patients
* the estimated yearly cost of a patient includes high out-of-pocket costs for both doctors and medicines



## Initial Scope:
- build a blockchain ecosystem which emulates the transfer of data within a trusted public ledger
- build a serverless application to transmit the data between participants & the ledger ecosystem
- Integrate the 2 & automate testing



### Technologies Used

AWS Lambda:

* The serverless API framework  
* The lambda functions are deployed using an automation tool called Chalice.  
* Lambda functions allow you to interact with an API(retrieve/post) 


Ethereum: 
Note: Due to complexity/timing the block chain implementation has been pushed off to a latter phase of development
* A blockchain tooling which can be used to create a decentralized public ledger.


## Accomplishments:
* AWS Lambda API endpoints:
    - created 12 basic lambda functions and automatically deployed them to AWS using Chalice
    - automated sanity testing of API for  PUT/POST/GET scenarios for each API 
    - researched blockchain development 
    
* Ethereum:
  - a contract was created to support a new ecosystem
  - a local development server was built
  - a lot of research into implementation
  


## Future (things to do):
* AWS Lambda API's require additional logic
* Ethereum development requires additional research to be performed


## Testing / Validation:

```shell 
(python2.7)m1ZZ3Nc0nTr0:helloworld cappetta$ ./tests/cli_tests.sh
display dispensary information
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 16726
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:47 GMT
Via: 1.1 f9fbbda041fd5d6cd566e39ed217c7d1.cloudfront.net (CloudFront)
X-Amz-Cf-Id: psNqvV6IMhuU9tLFv_U55mEASV5y3XQ7BZDcqpYPj1cyJzfQNOUfxA==
X-Amzn-Trace-Id: Root=1-58ea4b73-ba68e1030cb1b8b084f77f69
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9da8ce65-1d34-11e7-97f7-ab8333e89595

{
    "list_of_dispensaries": [
        {
            "Address": "52 South Union Road, Suite 102,Wiliamsville, NY 14221",
            "Days of Operation": "Mon, Tues, Fri",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (15% off), disability",
            "Email": "patients.williamsville@bloomfieldindustries.com",
            "Extras": "1) replied by email",
            "Facility": "Williamsville (Buffalo area)",
            "Impressions": "friendly, willing to answer in depth questions",
            "Organization": "Bloomfield Industries",
            "Payment Type": "currently n/a",
            "Phone": "716-810-5219",
            "Price Range w/ Examples": "Oil Example: the product that yields 30 doses (30mL) costs about $45.48. Syrup Example: the product that yields 14 doses (7oz) costs about $21.22.",
            "Product Inventory": "Offers: oils and syrups; Coming Soon: vaporization, expected to debut in January",
            "Solution Ratios Offered": "currently n/a"
        },
        {
            "Address": "1304 Buckley Road, Suite 106, Salina,NY 13212",
            "Days of Operation": "Wed, Thurs, Fri",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (15% off), disability",
            "Email": "patients.salina@bloomfieldindustries.com",
            "Extras": "",
            "Facility": "Salina (Syracuse area)",
            "Impressions": "friendly, willing to answer less in depth questions, seemed pressed for time",
            "Organization": "Bloomfield Industries",
            "Payment Type": "currently n/a",
            "Phone": "315-295-3531",
            "Price Range w/ Examples": "Oral Serum Example: the amount of product that yields 30 doses costs about $22, lasts 5-15 days. 1:1 and 1:2 solution variations available",
            "Product Inventory": "Offers: sublingual tinctures, oral serums, and oils",
            "Solution Ratios Offered": "Oral Serum Ratios:  1T:1C; 1T:2C"
        },
        {
            "Address": "2001 Marcus Avenue, Lake Success, NY 11042",
            "Days of Operation": "Mon, Tues, Thurs, Fri, Sat",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (15% off), disability",
            "Email": "patients.lakesuccess@bloomfieldindustries.com",
            "Extras": "",
            "Facility": "Lake Success",
            "Impressions": "very friendly, patient, said I could call back anytime, willing to give detailed explanations",
            "Organization": "Bloomfield Industries",
            "Payment Type": "currently n/a",
            "Phone": "516-444-3452",
            "Price Range w/ Examples": "Sublingual Example: the amount of product that yields 20 doses costs about $30. Oral Serum Example: the amount of product that yields 14 doses costs about $22.",
            "Product Inventory": "Offers: sublingual tinctures and oral serums; Coming Soon: capsules and inhalation, debut in January",
            "Solution Ratios Offered": "currently n/a"
        },
        {
            "Address": "212 E 14th Street, New York, NY 1003",
            "Days of Operation": "Mon, Wed, Fri, Sat",
            "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
            "Email": "NYC@col-care.com",
            "Extras": "1) explained that most prices/products across the Columbia Care collective were the same because all of Columbia Care's products are cultivated in Rochester, NY. 2) personal line for Julie, Columbia Care's Patient Services Coordinator,  585-678-8391.",
            "Facility": "New York City (Manhattan)",
            "Impressions": "extremely friendly, very patient, very helpful, very in depth explanations",
            "Organization": "Columbia Care NY LLC",
            "Payment Type": "Accepts: cash or debit card w/ pin number",
            "Phone": "646-453-7178",
            "Price Range w/ Examples": "Sublingual Usage Example: 7mL lasts a week with a Rx for .5mL b.i.d; Capsule Usage Example: 14 capsules per bottle lasts a week with Rx for 1cap b.i.d; Vape Usage Example: 90 inhalations per cartridge lasts a month with Rx for 3 inhalations q.d. Vape Price Example: cartridge costs $100, one time battery fee costs $10.",
            "Product Inventory": "Offers: sublingual tinctures, capsules, and vapes.",
            "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C"
        },
        {
            "Address": "13333 E Main Street, Riverhead, NY 11901",
            "Days of Operation": "Wed, Thurs, Fri, Sat",
            "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
            "Email": "riverhead@col-care.com",
            "Extras": "",
            "Facility": "Riverhead",
            "Impressions": "willing to answer less in depth questions",
            "Organization": "Columbia Care NY LLC",
            "Payment Type": "Accepts: cash or debit card w/ pin number",
            "Phone": "631-861-4114",
            "Price Range w/ Examples": "Vape Price Example: $100 for a month supply; Tinctures and Capsules Price Example: $53.50 for a  week supply",
            "Product Inventory": "Offers: tintcures, oils, and vapes",
            "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C"
        },
        {
            "Address": "345 Cornelia Street, Plattsburgh, NY 120901",
            "Days of Operation": "Mon, Tues",
            "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
            "Email": "plattsburgh@col-care.com",
            "Extras": "",
            "Facility": "Plattsburgh",
            "Impressions": "reluctant to give specifics on dosage and size; friendly, willing to give in depth discritptions",
            "Organization": "Columbia Care NY LLC",
            "Payment Type": "Accepts: cash or debit card w/ pin number",
            "Phone": "518-930-4340",
            "Price Range w/ Examples": "Vape Price Example: $100 for a month supply; Tinctures and Capsules Price Example: $53.50 for a  week supply",
            "Product Inventory": "Offers: sublingual tinctures, capsules, and vapes",
            "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C"
        },
        {
            "Address": "200 West Ridge Road, Rochester, NY 14615",
            "Days of Operation": "Mon, Fri",
            "Discounts": "Discounts for: disability, Medicaid, SSI, and social security carriers (15% off); also offers discount for seniors (65yr+) at 15% off",
            "Email": "rochester@col-care.com",
            "Extras": "",
            "Facility": "Rochester",
            "Impressions": "reluctant to give specifics on dosage and size; friendly, willing to answer less in depth questions",
            "Organization": "Columbia Care NY LLC",
            "Payment Type": "Accepts: cash or debit card w/ pin number",
            "Phone": "585-678-8390",
            "Price Range w/ Examples": "Vape Price Example: $100; Tinctures and Capsules Price Example: $53.50",
            "Product Inventory": "Offers: sublingual tinctures, capsules, and vapes",
            "Solution Ratios Offered": "Sublingual Ratios: 20T:1C, 1T:1C, 1T:20C;  Vape Oil Ratios: 20T:1C, 1T:1C, 1T:20C; Oral Capsule Ratios: 20T:1C, 1T:1C, 1T:20C"
        },
        {
            "Address": "402 North Pearl Street, Albany, NY 12207",
            "Days of Operation": "Wed, Thurs, Fri",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
            "Email": "info@etainhealth.com",
            "Extras": "",
            "Facility": "Albany",
            "Impressions": "",
            "Organization": "Etain, LLC",
            "Payment Type": "Accepts: cash and debit card",
            "Phone": "914-437-7898",
            "Price Range w/ Examples": "currently n/a",
            "Product Inventory": "Offers: tinctures, capsules, vape, and oral spray",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "445 State Route 28, Kingston, NY 12401",
            "Days of Operation": "Tues, Wed, Thurs, Sat",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
            "Email": "info@etainhealth.com",
            "Extras": "",
            "Facility": "Kingston",
            "Impressions": "friendly, willing to answer less in depth questions",
            "Organization": "Etain, LLC",
            "Payment Type": "Accepts: cash and debit card",
            "Phone": "914-437-7898",
            "Price Range w/ Examples": "currently n/a",
            "Product Inventory": "Offers: tinctures, capsules, vape, and oral spray",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "2140 Erie Boulevard E, Syracuse, NY 13224",
            "Days of Operation": "Tues, Wed, Thurs, Sat",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
            "Email": "info@etainhealth.com",
            "Extras": "only 10 diseases qualify for treatment, curently considering chronic pain as 11th ailment, explicitly said this facility doesn't currently accommodate cases for chronic pain",
            "Facility": "Syracuse",
            "Impressions": "friendly, willing to answer less in depth questions",
            "Organization": "Etain, LLC",
            "Payment Type": "Accepts: cash and debit card",
            "Phone": "914-437-7898",
            "Price Range w/ Examples": "currently n/a",
            "Product Inventory": "Offers: oils, vaporizers, tinctures, solutions, and oral spray",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "55 Main Street, Yonkers, NY 10701",
            "Days of Operation": "Tues, Wed, Thurs, Fri",
            "Discounts": "Discounts for: hardships, veterans, Medcaid (10% off), disability",
            "Email": "info@etainhealth.com",
            "Extras": "",
            "Facility": "Yonkers",
            "Impressions": "",
            "Organization": "Etain, LLC",
            "Payment Type": "Accepts: cash and debit card",
            "Phone": "914-437-7898",
            "Price Range w/ Examples": "currently n/a",
            "Product Inventory": "Offers: oils, vaporizers, tinctures, solutions, and oral spray",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "25 North Pointe Parkway, Suite 30, Amherst, NY 14228",
            "Days of Operation": "Tues, Wed, Thurs, Fri, Sat",
            "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%)",
            "Email": "contact@pharmacannis.com",
            "Extras": "1) gave detailed explanation of application process for a medical marijuana card. 2) must have card, photo ID, and doctor recommendation every time you enter the facility regardless if you're a returning pt or not",
            "Facility": "Amherst",
            "Impressions": "very friendly, very patient, very in depth explanation with little prompting or inquiry",
            "Organization": "PharmaCann, LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "716-636-0420",
            "Price Range w/ Examples": "Oral and Sublingual Example: a 20:1 solution in a bottle (?mL), lasts for a week, costs $75.44. Inhalation/E-pen Example: a 1:1 solution in a cartridge (?mL), lasts for a month to 2 months, costs $19 per cartridge, $120 total with e-pen purchase",
            "Product Inventory": "Offers: oral, sublingual, inhalation",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "642 Old Liverpool Road, Liverpool, NY 13088",
            "Days of Operation": "Tues, Wed, Thurs, Fri, Sat",
            "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%). Rewards: uses a \"value system\"; you get a certain percentage off for any sales over one item",
            "Email": "contact@pharmacannis.com",
            "Extras": "",
            "Facility": "Liverpool",
            "Impressions": "very friendly, very patient, very in depth explanation with little prompting or inquiry",
            "Organization": "PharmaCann, LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "315-457-0425",
            "Price Range w/ Examples": "Vape Usage Example:  130-150 inhalations per cartridge (?mL). Vape Price Example: USB chargeable, whole vape kit only $19.99 *resale online is $50.",
            "Product Inventory": "Offers: tincture and vape",
            "Solution Ratios Offered": "Equal Parts (1T:1C): tincture. THC Dominant (20T:1C): tincture and vape."
        },
        {
            "Address": "10 Executive Park Drive, Albany, NY 12203",
            "Days of Operation": "Tues, Wed, Thurs, Fri, Sat",
            "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%). Rewards: uses a \"value system\"; you get a certain percentage off for any sales over one item",
            "Email": "contact@pharmacannis.com",
            "Extras": "",
            "Facility": "Albany",
            "Impressions": "",
            "Organization": "PharmaCann, LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "518-459-2161",
            "Price Range w/ Examples": "Vape Usage Example:  130-150 inhalations per cartridge (?mL). Vape Price Example: USB chargeable, whole vape kit only $19.99 *resale online is $50.",
            "Product Inventory": "currently n/a",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "405 Huntspoint Avenue, Bronx, NY 10474",
            "Days of Operation": "Mon, Tues, Wed, Thurs, Fri, Sat",
            "Discounts": "Discounts for: $25 off for new patients; also offers discounts to disability, Medicaid, SSI, and social security carriers (10%). Rewards: uses a \"bulk discount\"; you get a certain percentage off for any sales over 3 items",
            "Email": "contact@pharmacannis.com",
            "Extras": "",
            "Facility": "Bronx",
            "Impressions": "very friendly, very patient, very in depth explanation with little prompting or inquiry",
            "Organization": "PharmaCann, LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "718-842-2001",
            "Price Range w/ Examples": "Vape Usage Example:  130-150 inhalations per cartridge (?mL). Vape Price Example: USB chargeable, whole vape kit only $19.99 *resale online is $50.",
            "Product Inventory": "Offers: tincture, capsules, and vape",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 20T:1C. CBD Dominant: 1T:20C."
        },
        {
            "Address": "221-223 E Post Road, WhitePlains, NY 10601",
            "Days of Operation": "Wed, Thurs, Fri, Sat",
            "Discounts": "Discounts for: financial aid and disability (10%)",
            "Email": "n/a",
            "Extras": "",
            "Facility": "White Plains Dispensary",
            "Impressions": "",
            "Organization": "Vireo Health of New York LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "844-484-7366",
            "Price Range w/ Examples": "currently n/a",
            "Product Inventory": "Offers: oral solution, capsules, vape",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C."
        },
        {
            "Address": "89-55 Queens Boulevard, Elmhurst, NY 11373",
            "Days of Operation": "Sun, Mon, Tues, Fri, Sat",
            "Discounts": "Discounts for: financial aid and disability (10%)",
            "Email": "n/a",
            "Extras": "1) provided long explanation of how you apply for a caregiver card",
            "Facility": "Queens Dispensary",
            "Impressions": "extremely friendly, very patient, very helpful, very in depth explanations",
            "Organization": "Vireo Health of New York LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "844-484-7366",
            "Price Range w/ Examples": "Vape Example: product yields about 100 puffs per cartridge. Capsule Example: product yields 30 caps per bottle. *usually distributes a month long supply at a time",
            "Product Inventory": "Offers: oral solution, capsules, vape",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C."
        },
        {
            "Address": "59 Harry L Drive, Johnson City, NY 13790",
            "Days of Operation": "Wed",
            "Discounts": "Discounts for: financial aid and disability (10%)",
            "Email": "n/a",
            "Extras": "",
            "Facility": "Binghamton Dispensary",
            "Impressions": "",
            "Organization": "Vireo Health of New York LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "844-484-7366",
            "Price Range w/ Examples": "Capsule Example: This type of medicine, like liquids, take a long time to enter your system and take effect. They also last for a long time. As a general rule, patients should wait at least 3 hours before taking another dose. Oil - Tincture  Example: It can take up to 2-3 hours for these medicines to take full effect, so you should wait three hours before taking another dose. Too often, patients do not believe the first dose is working due to the delay in effect. Be aware that these doses add up over time so please wait the recommended amount so as not to over-dose.  *procured from facility website",
            "Product Inventory": "Offers: oral solution, capsules, vape",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C."
        },
        {
            "Address": "38 Fuller Road, Albany, NY 12205",
            "Days of Operation": "Sun",
            "Discounts": "Discounts for: financial aid and disability (10%)",
            "Email": "n/a",
            "Extras": "",
            "Facility": "Albany Dispensary",
            "Impressions": "extremely friendly, very patient, very helpful, very in depth explanations",
            "Organization": "Vireo Health of New York LLC",
            "Payment Type": "Accepts: cash payments only",
            "Phone": "844-484-7366",
            "Price Range w/ Examples": "Oral Solution Example: 25mL bottle offered in most ratios. Capsule Example: 30 capsules per bottle offered in 1:1 ratio. Vape Example: 0.5mL, preloaded cartridge; 1mL, bulk liquid used w/ e-liquid, lasts anywhere from a week to one month dependant upon Rx from physician.",
            "Product Inventory": "Offers: oral solution, capsules, vape",
            "Solution Ratios Offered": "Equal Parts: 1T:1C. THC Dominant: 6T:1C; 19T:1C. CBD Dmoinant: 1T:6C; 1T:19C."
        }
    ]
}

Display OnCall Doctors - Bob
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 43
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:48 GMT
Via: 1.1 1d43f56d3213a63608863fd0e49585b9.cloudfront.net (CloudFront)
X-Amz-Cf-Id: iXuWh60L4D6joX1o_hudz6pof3fF7wY1i1QPa3F-86dhmcL7y4z-Nw==
X-Amzn-Trace-Id: Root=1-58ea4b74-2cc51fa09c66ad9461f130de
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9ddd7281-1d34-11e7-9e01-8f184c530b15

{
    "Bob": "http://aws.chime.com/meetup-1234"
}

Display OnCall Doctors - Mary
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 44
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:48 GMT
Via: 1.1 ac34121093afdc7c5e89263bece028e1.cloudfront.net (CloudFront)
X-Amz-Cf-Id: I60OIjcEEGj0UZoOml_cGrl13ZZMcH0kvx0vVZkSMd2iR0WZfYL1JQ==
X-Amzn-Trace-Id: Root=1-58ea4b74-00296337cf458dba49b04c0f
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9e0b8751-1d34-11e7-bcb4-85ff6e176af3

{
    "Mary": "http://aws.chime.com/meetup-4567"
}

Display OnCall Doctors - Wendel
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 46
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:48 GMT
Via: 1.1 20710af5b67bb4f49570084055f06277.cloudfront.net (CloudFront)
X-Amz-Cf-Id: YlD6fOdcd4tItNYe5Rs2LfWICxPa2s6cpR1jZ9HVotxgUiwSSwD7Pg==
X-Amzn-Trace-Id: Root=1-58ea4b74-843dc62058dc0fb796e0b245
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9e3b4a05-1d34-11e7-988a-5be709eae10c

{
    "Wendel": "http://aws.chime.com/meetup-2222"
}

Display OnCall Doctors - Doug
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 44
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:49 GMT
Via: 1.1 1d43f56d3213a63608863fd0e49585b9.cloudfront.net (CloudFront)
X-Amz-Cf-Id: c-Rs4kLKZTxfsXa22hrJtDMN93L-3DTpsZ-qQS2erYqNVBvIe4QOkQ==
X-Amzn-Trace-Id: Root=1-58ea4b75-08db1413816d92705a8a54bc
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9e6a22c2-1d34-11e7-a847-6f255884ac8f

{
    "Doug": "http://aws.chime.com/meetup-1847"
}

Display Doctors List
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 61
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:49 GMT
Via: 1.1 1c618ea0f595386e66803b2a07e0f4dc.cloudfront.net (CloudFront)
X-Amz-Cf-Id: NRUlLyNH5q9lKvidn1xHUQBfD2KDr9rH5NY1atEwEwFYdqkkWc1Mkg==
X-Amzn-Trace-Id: Root=1-58ea4b75-24c6a2f058f22a6a5e294479
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9e9f8aa3-1d34-11e7-b0f4-2771f1220774

https://www.marijuanadoctors.com/medical-marijuana-doctors/NY

Display Quality Testing Results - AK-47
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 131
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:49 GMT
Via: 1.1 0f02b0042bcba00911e5a40240b699d3.cloudfront.net (CloudFront)
X-Amz-Cf-Id: EPg53t30xF4ZjmWxtEqNDEnULy75JjfbbuKhijyW9dA7fOHsgKCxQg==
X-Amzn-Trace-Id: Root=1-58ea4b75-344658e5efd7ea2655dea323
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9ed28171-1d34-11e7-8e17-6fb0711cf94c

{
    "AK-47": "PASSES: Department of Health's Wadsworth quality checks for contaminants and pesticides.  Potency: THC=25.6% CBP=1.2% "
}

Display Quality Testing Results - BlueLighning
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 94
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:50 GMT
Via: 1.1 a536f7c9dbedc2b462a158901fcd8254.cloudfront.net (CloudFront)
X-Amz-Cf-Id: sfqNXZGlbdadihptxJHesFI-dc6qJdG-6dtkz5KfBH-I2LyeElTc7g==
X-Amzn-Trace-Id: Root=1-58ea4b76-75c2c6cae764d52bc3460dcf
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9f09be11-1d34-11e7-8caa-cfce5cc52da3

{
    "BlueLighning": "FAILS: This failed DoH testing for pesticides. Potency: THC=25.6% CBP=1.2%"
}

Display Quality Testing Results - Gorilla
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 89
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:50 GMT
Via: 1.1 1d43f56d3213a63608863fd0e49585b9.cloudfront.net (CloudFront)
X-Amz-Cf-Id: tOffw1WLt21ytlxHVt9BH89CKr9QwjjQpG21kKr2wZAFDYSjQbyg5A==
X-Amzn-Trace-Id: Root=1-58ea4b76-3cab9af5e9d57616adbb61f4
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9f3dc5a8-1d34-11e7-8dcf-71943f1c20d9

{
    "Gorilla": "FAILS: This failed DoH testing for pesticides. Potency: THC=22.6% CBP=0.2%"
}

Display Quality Testing Results - GirlScoutCookies
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 99
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:50 GMT
Via: 1.1 2ebc0bd350ce03ac7549d526b72cae8e.cloudfront.net (CloudFront)
X-Amz-Cf-Id: WVScOYJ3IXirOi8KLJN0CuAX6kGz5fRKOEKSbyiCAbe6TJf9i2EHYg==
X-Amzn-Trace-Id: Root=1-58ea4b76-7fc51973c3b8931d25514d0f
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9f6e4bc4-1d34-11e7-96f2-43965d9061df

{
    "GirlScoutCookies": "Passes: This passes DoH testing for pesticides. Potency: THC=0.6% CBP=22.2%"
}

Testing Inventory Lookup - Hybrid
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 59
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:51 GMT
Via: 1.1 ac34121093afdc7c5e89263bece028e1.cloudfront.net (CloudFront)
X-Amz-Cf-Id: SFL8fiu-UkHFTR0HN3UzdYS-T_pOCj7VH2xmknsGsA38oSiC4hcGcg==
X-Amzn-Trace-Id: Root=1-58ea4b77-78240e0427105f6ea296635d
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9fa07f13-1d34-11e7-9016-71297b23a633

{
    "Inventory": [
        "Diseal Kush",
        "Ak-Man",
        "GirlScout Dream"
    ]
}

Testing Inventory Lookup - Sativa
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 63
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:51 GMT
Via: 1.1 044470188efe7aea5c8537e1416e3d92.cloudfront.net (CloudFront)
X-Amz-Cf-Id: XtJ2SSURv845xkYTUgSSTAF80n-u5EnmX2Rn07q3v4Rw2zRwC1H4cw==
X-Amzn-Trace-Id: Root=1-58ea4b77-bc343cd24584a89bed3d0846
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9fd1051c-1d34-11e7-afee-f95438fa688b

{
    "Inventory": [
        "AK-47",
        "Blue Lightning",
        "GirlScout Cookies"
    ]
}

Testing Inventory Lookup - Indica
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 58
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:51 GMT
Via: 1.1 829eee129e6b5002d6c1a37f04888da1.cloudfront.net (CloudFront)
X-Amz-Cf-Id: WhHqTYZHAKos_8OtUTCeN4sVUw7rrbBUsDG94DFZNIZD-VIngP3glg==
X-Amzn-Trace-Id: Root=1-58ea4b77-4d82b953392118c40235fbc4
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9ffecbd0-1d34-11e7-aa5d-b16c5004daad

{
    "Inventory": [
        "Sleepy Man",
        "Blue Dream",
        "Sour Diseal"
    ]
}

testing place 1st order
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 77
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:53 GMT
Via: 1.1 a536f7c9dbedc2b462a158901fcd8254.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 04gKSFCoZM6cXfs0Bt51qPJgHSqvE_8YfYr4YqRibyUd8VP7Rt2Qyg==
X-Amzn-Trace-Id: Root=1-58ea4b78-f6e029c1b1197eea533b0d77
X-Cache: Miss from cloudfront
x-amzn-RequestId: a02da45d-1d34-11e7-b98b-b36963ee222c

{
    "order placed": [
        "(3g) Diseal Kush",
        "(3g) Ak-Man",
        "(3g) GirlScout Dream"
    ]
}

testing place 2nd order
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 76
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:53 GMT
Via: 1.1 f417319e2be16229be3a4f373f919466.cloudfront.net (CloudFront)
X-Amz-Cf-Id: DhYCHpHDsx3IzpEGZytKVQNwYxXcxlGZL8ENocD6HotV91r67uG_Hg==
X-Amzn-Trace-Id: Root=1-58ea4b79-3cea55b7a4d1a7ddc8154d80
X-Cache: Miss from cloudfront
x-amzn-RequestId: a0f97fdc-1d34-11e7-9c0e-f309745e41dc

{
    "order placed": [
        "(3g) Sleepy Man",
        "(3g) Blue Dream",
        "(3g) Sour Diseal"
    ]
}

testing place 3rd order
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 83
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:53 GMT
Via: 1.1 0cd6949155fdc875b62d453c5f6c0005.cloudfront.net (CloudFront)
X-Amz-Cf-Id: Q1O9zBcMGBZFa5d-R9kANB51nt69sD1atQuJkenv9MQJ6IBVS3Yfug==
X-Amzn-Trace-Id: Root=1-58ea4b79-c8acd187659bf5c3d99dc6c5
X-Cache: Miss from cloudfront
x-amzn-RequestId: a129b76b-1d34-11e7-bb7b-5961e36eff8c

{
    "order placed": [
        "(1QP) AK-47",
        "(1oz) Blue Lightning",
        "(3g) GirlScout Cookies"
    ]
}

testing retrieve 1st order
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 80
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:54 GMT
Via: 1.1 7ea42c16b0af66858eb9302f2f610cd6.cloudfront.net (CloudFront)
X-Amz-Cf-Id: zbs1-LjWKbReYWz-rtRWgvgh6ADrI3aVqv2F95Di_hv9ofImo2ualw==
X-Amzn-Trace-Id: Root=1-58ea4b7a-b8a77df511b51114e71bd6a7
X-Cache: Miss from cloudfront
x-amzn-RequestId: a15e8339-1d34-11e7-9f6f-e545b4f6247b

{
    "order retrieved": [
        "(3g) Diseal Kush",
        "(3g) Ak-Man",
        "(3g) GirlScout Dream"
    ]
}

testing retrieve 2nd order
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 79
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:54 GMT
Via: 1.1 f19281f08e79aa6c6634266c50732dd5.cloudfront.net (CloudFront)
X-Amz-Cf-Id: bV-PsAnZZPikVRY2pvAeHYdX1S07QMYDQ2H2XFFWb7YRS0oAPKzGVA==
X-Amzn-Trace-Id: Root=1-58ea4b7a-3646d7ab436653d8bfe1b2a9
X-Cache: Miss from cloudfront
x-amzn-RequestId: a193eb81-1d34-11e7-a2de-f192b46f4775

{
    "order retrieved": [
        "(3g) Sleepy Man",
        "(3g) Blue Dream",
        "(3g) Sour Diseal"
    ]
}

testing retrieve 3rd order
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 86
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:54 GMT
Via: 1.1 9ce63d3af60e77462dfef1ebe1eea8f0.cloudfront.net (CloudFront)
X-Amz-Cf-Id: qpfnpTr0dKuVUtS6s5mN0SXLgxfm35ejwWzlExOmybtsunWswmINFQ==
X-Amzn-Trace-Id: Root=1-58ea4b7a-3656ce237ee1a05e238ac2f6
X-Cache: Miss from cloudfront
x-amzn-RequestId: a1c2c3af-1d34-11e7-acf6-bfaf48002ee7

{
    "order retrieved": [
        "(1QP) AK-47",
        "(1oz) Blue Lightning",
        "(3g) GirlScout Cookies"
    ]
}

testing register 1st device
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:55 GMT
Via: 1.1 f417319e2be16229be3a4f373f919466.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 3i8frZPiBZV8J2qlhv7vrfkRXWfuB8ruKZZLyb7E9vG9oUnCzXeafQ==
X-Amzn-Trace-Id: Root=1-58ea4b7b-7bf55319d771f69a7496f85c
X-Cache: Miss from cloudfront
x-amzn-RequestId: a1f174e9-1d34-11e7-acf6-bfaf48002ee7

{
    "Mary": [
        "iPhone6",
        "585-565-9665",
        "windows 10",
        "00:84:80:90:50"
    ]
}

testing register 2nd device
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 37
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:55 GMT
Via: 1.1 1c618ea0f595386e66803b2a07e0f4dc.cloudfront.net (CloudFront)
X-Amz-Cf-Id: V7UDyry71mv-WKobCFifbZpfrFkeYQkhqPoq5DkJ4TVPQ7bSpGsbRA==
X-Amzn-Trace-Id: Root=1-58ea4b7b-58aa415d1d6943c8cc7f4110
X-Cache: Miss from cloudfront
x-amzn-RequestId: a221103d-1d34-11e7-b056-dd785d46ff24

{
    "John": [
        "Android",
        "315-488-8998"
    ]
}

testing register 3rd device
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 55
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:55 GMT
Via: 1.1 0f0049492e2872b6e133c50b6cc7be4b.cloudfront.net (CloudFront)
X-Amz-Cf-Id: Ekd3cdrltXPdH-go-q6She5VwtXTs3wn87FZHIBBnnuNaMsXZF5TOA==
X-Amzn-Trace-Id: Root=1-58ea4b7b-5008b8dc57be84b5f76707dd
X-Cache: Miss from cloudfront
x-amzn-RequestId: a25517f1-1d34-11e7-a847-6f255884ac8f

{
    "Tom": [
        "home",
        "315-488-8998",
        "computer",
        "laptop"
    ]
}

testing posting inventory - Mary
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 25
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:56 GMT
Via: 1.1 2ebc0bd350ce03ac7549d526b72cae8e.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 3lZKtO7IS4WFI3kcPWbrr2_OKGKjG7_qSa4bRLHdtW8xomMLP00EBw==
X-Amzn-Trace-Id: Root=1-58ea4b7c-1c7591e7aece10f9f93e840a
X-Cache: Miss from cloudfront
x-amzn-RequestId: a28883d6-1d34-11e7-8890-9f62dc341a81

{
    "Mary": {
        "AK-47": "5g"
    }
}

testing posting inventory - John
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 36
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:56 GMT
Via: 1.1 0f0049492e2872b6e133c50b6cc7be4b.cloudfront.net (CloudFront)
X-Amz-Cf-Id: k0x3jBZzERycb9hnynhbBoDiOGXbO4Y9cf0mcbBogBgfP4WFMG2rPQ==
X-Amzn-Trace-Id: Root=1-58ea4b7c-53dda176eebd40f77920540c
X-Cache: Miss from cloudfront
x-amzn-RequestId: a2bf99f1-1d34-11e7-8ed7-bd152c287c3a

{
    "John": {
        "Blue Lightning": "112g"
    }
}

testing posting inventory - Tom
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 46
Content-Type: application/json
Date: Sun, 09 Apr 2017 14:55:56 GMT
Via: 1.1 440cbcb26e69761b0c95e97cad505b77.cloudfront.net (CloudFront)
X-Amz-Cf-Id: WMQ1SJk63bZuCZI6RweLSnM7YSu-pM9iqTTTSgDOHmEEkgEzCkH-fg==
X-Amzn-Trace-Id: Root=1-58ea4b7c-cfdbb2c9124016533230d0a2
X-Cache: Miss from cloudfront
x-amzn-RequestId: a2f2b774-1d34-11e7-bfeb-7d87418aae08

{
    "Tom": {
        "Cartridges": "10",
        "Cookies": "20"
    }
}
```



