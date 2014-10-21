#Not quite working. Only working on test account, not more complex ones.
#For some reason, "message" doesn't exist in line 22-23....
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

def thank():
    token="CAACEdEose0cBAEWb2jPapUwT0AchEL3tctpQa7JABZCJKZBspeiGznqOlSEnP6FIGqO3sJzYqeulE5vBHhb9Cq15eBM58ZBYh4e4EBpFvAkMpOOZAgVapXeoYuKcatI75tEQ1qwVpePHBcHLu9vns0dSSr4oyGHcB4KcpKBjtpTueM8jx9w6BQe4ZAlT4kHmIJQdmPKF4DvjBSqSSxgZBamx38GxQeESEZD"
    facebook=fb.graph.api(token)
    graph1 = GraphAPI(token)
    
    vid=input("Enter your Facebook id: ")
    query=str(vid)+"/feed?fields=id&limit=5000000000"
    r=graph1.get(query)
    tempidlist = []
    idlist = []
    messagelist = []
    for x in r['data']: #for each post on feed
        tempidlist.append(x['id']) #list of ids
        postquery = "/" + str(x['id'])
        m=graph1.get(postquery)
        if(m['message']):
            messagelist.append(m['message'].lower())
    print tempidlist
    print messagelist
    for message in messagelist:
        if ("birthday" in message) or ("happy" in message):
            idlist.append(tempidlist[messagelist.index(message)])
        else:
            continue
    print("There are "+ str(len(idlist)) +" birthday posts.")

    char1=raw_input("Do you want to proceed? (y/n) ")
    count=0
    if char1=='y':
        nos=input("Enter number of posts to thank: ")
        mess=raw_input("Enter the thank you message: ")
        if nos<=len(idlist):
           for indid in (idlist[(len(idlist)-nos):]):
        
              facebook.publish(cat="comments",id=indid,message=mess) #Comments on each post
              facebook.publish(cat="likes",id=indid)                 #Likes each post
              count=count+1
              print("Notification number: "+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])
        else: 
              print("Not that many birthday posts.")
    else :
      print("Okay.")

thank()