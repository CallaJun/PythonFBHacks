import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

def spam():
    token="CAACEdEose0cBAIwSg2fo3ip8ScL3YQgM5Q99KEdGZCAv8zfn30bmruqj8hs6eWbMFKJFB8AWqDBWa28LI5YyHjYfTnxPnHrrLhl08WNPdxvA01is9GMVVLZCkZAh2HBPTjXNqxStDnDJr1ZBCealtJIn6huGclco1wgPHYDG4aGO4EORE72eDuAoXe1UA8OB9QDqfjvkwIfCWZA9Hz4RggeUmqgiEyZBkZD"
    facebook=fb.graph.api(token)
    graph1 = GraphAPI(token)
    
    vid=input("Enter victim's id: ")
    query=str(vid)+"/photos/uploaded"
    r=graph1.get(query)
    
    idlist=[x['id'] for x in r['data']]
    idlist.reverse()
    print("There are "+ str(len(idlist)) +" spammable photos.")
    
    char1=raw_input("Do you want to spam? (y/n) ")
    count=0
    if char1=='y':
        nos=input("Enter number of photos to be spammed with comments: ")
        mess=raw_input("Enter the message to be commented: ")
        if nos<=len(idlist):
           for indid in (idlist[(len(idlist)-nos):]):
        
              facebook.publish(cat="comments",id=indid,message=mess) #Comments on each photo
              facebook.publish(cat="likes",id=indid)                 #Likes each photo
              count=count+1
              print("Notification number: "+str(count)+" on www.facebook.com/photo.php?fbid="+str(indid))
        else: 
              print("Not that many spammable photos available. No spam happening.")
    else :
      print("No spam happening then.")

spam()