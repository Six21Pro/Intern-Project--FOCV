import re
import requests
from regexs import Regexs


class Contexter:
  numberOrigCharS = 0  #number of original charitable sites
  numberOfOrigCon = 0  #number of original context
  urls = [] #list to store URLs
  charSites = [] #list to store charitable sites

  def increment_Char(self):
    Contexter.numberOrigCharS += 1

  def increment_Con(self):
    Contexter.numberOfOrigCon += 1

  def intake(self, added):
    charSites.append(added)


  def addContext2(self, url):

    listex = Regexs()
    #print(listex.Regexs())
    arregex = listex.Regexs()#get the list of regular expressions  
    keyreggex = listex.KWords()

    contextArray = []#return this to add context about charitableness to the websites scraped    

    for y in range(
        len(url)):  #this for loop checks every url passed to this function
      #print("Y: ",y)#for debugging
      notCharitable = True #this boolean will be used to add the context that a website has no indications of being charitable.

      try:
        response2 = requests.get(url[y], timeout=10)
        #print(f"Status code: {response2.status_code}")  # Debug print
        if response2.status_code == 403:
          print("Hit the 403 check!")
          contextArray.append("could not access the website")
          continue

        if response2.status_code == 200:
          print("Successful 200 check!")
          htmltext2 = response2.text

        else:
          print(f"Unexpected status code: {response2.status_code}")
          contextArray.append("could not access the website")
          continue

      except Exception as e:
        print(f"Error with {url[y]}: {e}")
        contextArray.append("could not access the website")
        continue

      if response2.status_code != 200:  #this likely won't happen
        print()
        print("SKIPPING!!!SKIPPING!!!SKIPPING!!!")
        contextArray.append("could not access the website")
        continue

      for x in range(
          len(arregex
              )):  #this for loop to check every regex passed to this function

        arrcomp = arregex[x]  #set arrcomp to one of the regex's
        pattern1 = re.compile(arrcomp)
        if htmltext2 != None:
          #print("htmltext2 is not empty")#for debugging
          here1 = re.findall(pattern1, htmltext2)          
        if htmltext2 == None:
          #print("htmltext2 IS empty")#for debugging
          continue

        contextCategory = " Possibly charitable. Keywords found: "  #every url is given this context #if it matches at least one regex
        if here1:  #if here1 not empty#it certainly shouldn't be
          #print("here1 is not empty")#for debugging
          notCharitable = False          
          tempContext = contextCategory

          for y in range(  
              len(arregex)
          ):  #this for loop is responsible adding keywords to the context
          
            arrcomp = arregex[y]  #set arrcomp to one of the regex's
            pattern2 = re.compile(arrcomp)
            
            here2 = re.findall(pattern2, htmltext2)
            if here2:
              contextCategory2 = keyreggex[y]
              tempContext = tempContext + contextCategory2 +", "
       
          contextArray.append(tempContext) 
          break  #this prevents us from checking the same url twice and adding any unnecessary context
        if notCharitable is True and x == len(arregex) - 1:
          contextArray.append("No indications of being charitable")
    return contextArray