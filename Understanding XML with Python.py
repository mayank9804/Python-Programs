# XML stands for eXtensible Markup Language.
# XML was designed to store and transport data. XML was designed to be both human- and machine-readable


# Why Study XML?
# XML plays an important role in many different IT systems.
#
# XML is often used for distributing data over the Internet.
#
# It is important (for all types of software developers!) to have a good understanding of XML.


import xml.etree.ElementTree as ET


# XML Trees
data = '''
<person>
<name>Chuck</name>
<phone type="intl">+1 734 303 4456</phone>
<email hide="yes"/>
</person>
'''

data1 = '''
<stuff>
    <users>
        <user x="2">
            <name>Mayank</name>
            <id>001</id>
        </user>
        <user x="3">
            <name>Chuck</name>
            <id>002</id>
        </user>
    </users>
</stuff>
'''

# Converting to a form python could parse it.(Basically a well defined Tree)
tree = ET.fromstring(data)
tree1 = ET.fromstring(data1)
users = tree1.findall('users/user')
print("###############Data1#############")
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
print("###############Data2#############")
print('User Count',len(users))
for user in users:
    print(user.find('name').text)
    print(user.find('id').text)
    print(user.get('x'))
