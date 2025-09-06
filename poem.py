import re
import xml.dom.minidom

filename = "poem.txt"
class Poem:
    def __init__(self, filename):
        fobj = open(filename,"r")
        self.lines = fobj.readlines()
        fobj.close()
        self.cleaned_lines = [line.strip() for line in self.lines] 


    def clean_with_enumerator(self):
        result = []
        for i ,line in enumerate(self.cleaned_lines):
            cleaned = re.sub(r'[^\w\s]',"", line)   
            result.append(cleaned)
        self.cleaned_lines = result

    def clean_with_map(self):
        self.cleaned_lines = list(map(lambda line : re.sub(r'[^\w\s]',"", line), self.cleaned_lines))


    def clean_with_list_comp(self):
        self.cleaned_lines =[re.sub(r'[^\w\s]',"", line) for line in self.cleaned_lines]

    def get_lines(self, word):
        doc = xml.dom.minidom.Document()
        root  = doc.createElement("results")
        doc.appendChild(root)

        for index,line in enumerate(self.cleaned_lines):
            if word.lower() in line.lower():
                line_element = doc.createElement("line")
                line_element.setAttribute("number", str(index+1))
                text_node = doc.createTextNode(line) 
                line_element.appendChild(text_node)
                root.appendChild(line_element)

        return doc.toprettyxml()           
          