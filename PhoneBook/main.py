import json

import contact
import contact_book


with open("test.json","r") as read_file:
    developer = json.load(read_file)


item= contact.contact(1, "artem","laptev","ram","8904494434")
