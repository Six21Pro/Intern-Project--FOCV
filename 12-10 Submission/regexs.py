class Regexs:
    
    #regex = '<a .*? href="[^"]*?.*?">.*?Community.*?</a>'  #works to check the text, but not the link
    #regex0 = '<a .*? href="[^"]*?.*?">.*?Aca.*?</a>'  #only for testing
    regex1 = '<a .*? href="[^"]*?.*?">.*?Purpose.*?</a>'
    
    #legex means: link-regular expression
    wendysex = '<a .*? href="[^"]*?.menu.*?">.*?</a>'  #this will return just 'menu' #for testing    
    wendyex2 = '<a .*? href="[^"]*?.what-we-value.*?">.*?</a>'#for testing
    wendyex3 = 'menu'  #for testing
    
    legex0 = '<a .*? href="[^"]*?.purpose.*?">.*?</a>'
    legex1 = '<a .*? href="[^"]*?.communit.*?">.*?</a>'
    legex2 = '<a .*? href="[^"]*?.donat.*?">.*?</a>'
    legex3 = '<a .*? href="[^"]*?.philantropy.*?">.*?</a>'
    legex4 = '<a .*? href="[^"]*?.charit.*?">.*?</a>'
    legex5 = '<a .*? href="[^"]*?.giving.*?">.*?</a>'
    legex6 = '<a .*? href="[^"]*?.sustainability.*?">.*?</a>'
    legex7 = '<a .*? href="[^"]*?.stewardship.*?">.*?</a>'
    legex8 = '<a .*? href="[^"]*?.our-planet.*?">.*?</a>'
    legex9 = '<a .*? href="[^"]*?.enviro.*?change.*?">.*?</a>'
    legex10 = '<a .*? href="[^"]*?.enviro.*?impact.*?">.*?</a>'
    legex11 = '<a .*? href="[^"]*?.enviro.*?footprint.*?">.*?</a>'
    legex12 = '<a .*? href="[^"]*?.global.*?impact.*?">.*?</a>'
    legex13 = '<a .*? href="[^"]*?.green.*?globe.*?">.*?</a>'
    legex14 = '<a .*? href="[^"]*?.green.*?planet.*?">.*?</a>'
    legex15 = '<a .*? href="[^"]*?.responsibility.*?">.*?</a>'
    legex16 = '<a .*? href="[^"]*?.conserv.*?">.*?</a>'
    legex17 = '<a .*? href="[^"]*?.educat.*?">.*?</a>'
    legex18 = '<a .*? href="[^"]*?.preserv.*?">.*?</a>'
    legex19 = '<a .*? href="[^"]*?.cultural.*?resourc.*?">.*?</a>'
    legex20 = '<a .*? href="[^"]*?.rural.*?character.*?">.*?</a>'
    
    corpSiteex = '<a .*? href="[^"].*?corporate.*?">.*?</a>'
    foundationSiteex = '<a .*? href="[^"]*?.foundation.*?">.*?</a>'
    
    listOfRegexs = [        legex0, legex1, legex2, legex3, legex4, legex5, legex6, legex7,legex8, legex9, legex10, legex11,        legex12, legex13, legex14, legex15,legex16,legex17,legex18,legex19,legex20,corpSiteex, foundationSiteex   ]  
    
    listOfKWords = ["purpose","community","donation","philantropy","charity","giving","sustainability","stewardship","our planet","environmental change","environmental impact","environmental footprint","global impact","green globe","green planet","responsibility","conservation","education","preservation","cultural resources","rural character","corporate","foundation"]
    
    def Regexs(self):
      return self.listOfRegexs

    def KWords(self):
        return self.listOfKWords
    