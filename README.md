# MISUserRegistry

Goal of this program is to create a user registry for the Minnesota Indonesian Society (MIS)
Should allow for users to register to be part of MIS and keep track of who has signed up and who has paid.

Idea is to just use the google sheets api which will allow for quick additions and changes to the sheet while not needing to setup a lot of extra external tools.

Will allow for member addition, removal, and status changes.
Members should have first name, last name, email, phone, and date joined

Also keep track of if the member has paid dues for the year

Before working, you need to retrieve secrets. Secrets can be found in the google secrets manager
Retrieve the secrets and add them to the respective files

To start work run 
    pip install -r requirements.txt
then should be good to go 
Run from main.py 

Will eventually expand so we can connect to the MIS website

For future, may port to a SQL database which will allow for much better allocation, but that may be out of the scope
of what am currently capable of
