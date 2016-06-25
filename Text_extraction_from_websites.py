# -*- coding: utf-8 -*-
#This is a task from one company, that offered me a job as python programmer
#It is my first program with usage of classes. It purpose is to extract text from webpages and make links in the text visible,
#after that is saves extracted text from webpage to a .txt file in the same directory, as source code. 
#Width of the text in final file should be 80 characters and long words should not be broken, instead they are moved to a new line
import urllib, textwrap, os
from bs4 import BeautifulSoup
class scraping:
    #Initialize with values
    def __init__(self):
        self.myfile = ""
        self.webpage = ""
      
    def text_parser(self):
        
        def soups(text_soup):
            # This function returns soup
            soup = BeautifulSoup(text_soup, "lxml")
            return soup
        
        title =""
        text = ""
        #Extract all titles of webpage
        for x in soups(self.myfile).findAll("h1" or "h2" or "h3" or "h4" or "h5" or "h6"):
            title+=x.text
        #Extract all source code with text tags
        for node in soups(self.myfile).findAll("p"):
            text+=str(node) 
        
        # Find all links and replace every link with [link] and make them visible in text
        for link in soups(text).findAll("a"):
            text= text.replace(str(link),"[" + link.get("href") +"] " + link.text.encode("utf-8"))
    
        final_text =""
    
        #Extract readable text from text tags
        for readable in soups(text).findAll("p"):
            final_text += readable.text + "\n"
            
        #Wrapping title width 80
        title_wrapper = textwrap.TextWrapper(break_long_words = False, break_on_hyphens = False, replace_whitespace = False, width = 80)
        wrapped_title = title_wrapper.fill(title)
        final =""
        #Wrapping text part width 80 
        for part in final_text.splitlines():
            final +="\n" + '\n'.join(textwrap.wrap(part, break_long_words = False, break_on_hyphens = False, width=80))

        #Erase http and html from web address
        if ".html" == self.webpage[len(self.webpage)-5:]:
            self.webpage=self.webpage.replace(".html", "")
        elif ".htm" == self.webpage[len(self.webpage)-4:]:
            self.webpage=self.webpage.replace(".htm", "")    
        if "https:/" == self.webpage[0:7]:
            self.webpage = self.webpage.replace("https:/", "")
        elif "http:/" == self.webpage[0:6]:
            self.webpage = self.webpage.replace("http:/", "")
        #Filename of .txt file, that should be saved in the same directory as source file
        filename = str((os.path.dirname(os.path.realpath(__file__))))
        #Replacing \ with / to avoid possible errors
        filename = filename.replace("\\", "/")
        #Filename  can't contain / sign
        self.webpage = self.webpage.replace("/", " ")
        #Creating a filename for text file 
        filename = filename + "/" +self.webpage + ".txt"
        #Saving final text to the text file
        file = open(filename, "w")
        file.write(wrapped_title.encode("utf-8")+"\n\n")  
        file.write(final.encode("utf-8"))
        file.close()
def start():
    try:
        #Loop that asks for a webpage, if web address is not valid throws an exception and starts again
        #until user enters empty line
        while True:                
            print "Please enter a web address or press Enter to exit:"
            webpage = raw_input("")
            if webpage == "":
                break
            else:
                site = urllib.urlopen(webpage)           
                myfile = site.read()
                news = scraping()
                news.myfile += myfile
                news.webpage += webpage
                news.text_parser()
    except:
        print "This web address does not exist"
        start()
start()