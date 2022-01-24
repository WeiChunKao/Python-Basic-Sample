import xmltodict
import json
def xmltojson(xmlstr):    
    xmlparse = xmltodict.parse(xmlstr)
    jsonstr = json.dumps(xmlparse,indent=1)
    return jsonstr
    #print(jsonstr)
def jsontoxml(jsonstr): 
    xmlstr = xmltodict.unparse(jsonstr)
    return xmlstr
    #print(xmlstr)
if __name__=='__main__':
    jsondata = {'transaction': {'course': {'name': 'math', 'score': '90'},
                        'info': {'sex': 'male', 'name': 'name'}, 'stid': '10213'}}
    print(jsontoxml(jsondata))
    xml ="""         
    <student>
        <stid>10213</stid>
        <info>
            <name>name</name>
            <sex>male</sex>
        </info>
        <course>
            <name>math</name>
            <score>90</score>
        </course>
    </student>
        """
    print(xmltojson(xml))  #
