import Handler

import contact
import contact_book


# with open("test.json","r") as read_file:
#     developer = json.load(read_file)

# lst=[]
# item= contact.contact(1, "artem","laptev","ram","8904494434")
# lst.append(item)
# item=contact.contact(2,"gena","petrovich","ivanov","2309120748")
# lst.append(item)
# Handler.JsonHandler.export(lst)
data=Handler.JsonHandler.importin(self=None)
print(data)