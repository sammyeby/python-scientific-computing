import xml.etree.ElementTree as ET
import json

# XML - eXtensible Markup Language
def xml_web_service():
    data = '''<person>
        <name>Sammy</name>
        <phone type="intl">+1 735 709 6654</phone>
        <email hide="yes"/>
    </person>'''

    tree = ET.fromstring(data)
    print('Name:', tree.find('name').text)
    print('Email Attr:', tree.find('email').get('hide'))
    print('Phone Attr:', tree.find('phone').get('type'))

# JSON - JavaScript Object Notation
def json_web_service():
    data = '''
        [
            { "id" : "001",
            "x" : "2",
            "name" : "Quincy"
            } ,
            { "id" : "009",
            "x" : "7",
            "name" : "Mrugesh"
            }
        ]
    '''
    infos = json.loads(data)
    print('Data Length:', len(infos))
    for info in infos:
        print(info['name'])


# xml_web_service()
json_web_service()