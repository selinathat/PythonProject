import os
import xml.etree.ElementTree as ET

path = "\\\\txgcv3sql\\Texas_Production\\LSNTicketImporter\\20161026"
count1 = 0
count2 = 0
for filename in os.listdir(path):	
    root = ET.parse(path + "\\" + filename)
    for elem in root.findall("./Ticket/Header"):
        print elem.text            
        if(elem.text == "NOTI-UPDATE"):
            count2 = count2+1
        else:
            count1 = count1+1        
print count1
print count2