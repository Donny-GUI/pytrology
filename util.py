from google_images_download import google_images_download
import fitz # install using: pip install PyMuPDF
from pprint import pprint
from string import ascii_uppercase
from bs4 import BeautifulSoup
import json
import wikipediaapi
import sys
import re
from element import SymbolsList


column_names = 36, 45

cnames = [
    "Name",
    "CNMMN/CNMNC formula",
    "IMA",
    "Status",
    "IMA No.",
    "Year",
    "Country",
    "First reference",
]

def pdf_to_text(path): 
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text 

def get_mineral_info():
    text = pdf_to_text("minlist.pdf")
    lines = text.split("\n")
    counter = 0
    ColumnNames = []
    for line in lines[36:45]:
        ColumnNames.append(line.strip())
    
    minerals = {}
    current_min = ""
    started = False
    for line in lines:
        text = line.strip()
        
        if text == "Abellaite":
            started = True
            
        if started == False:
            continue
        
        if text.startswith("All cells modified after the preceding release (September 2022)"):
            break
        
        if text.startswith(" Neues Jahrbuch für Mineralogie Monatshefte (1978), 134"):
            break
        
        if counter == 0:
            current_min = text
            minerals[text] = {"Name": text}
            counter+=1
            continue
        elif counter < 8:
            minerals[current_min][ColumnNames[counter]] = text
            counter+=1
            continue
        elif counter == 8:
            minerals[current_min][ColumnNames[counter]] = text
            counter = 0
            continue
    
    pprint(minerals)
    return minerals

def find_formula_in_text(text: str):
    formula_pattern = r"\b[A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)*\b"
    fancy_pattern = r"[A-Z][a-z]?[\d\.]*(?:\([A-Za-z\d,]+\))?(?:\{[A-Za-z\d\[\]\(\),]+\})?(?:\[[A-Za-z\d]+\])*(?:\([A-Za-z\d,]+\))?"
    fformulas = re.findall(pattern=fancy_pattern, string=text)
    lengff = len(fformulas)
    if lengff == 1:
        formula = fformulas[0]
        return formula
    elif lengff > 1:
        formula = "-".join(fformulas)
        return formula
    
    if need_formula:
    
        formulas = re.findall(pattern=formula_pattern, string=text)
        formula = ""
        not_chem = ["It", "IMA", "In", "REE", "REEs", "US", "IMA2018", "CNMNC", "BERR", "Dr", "GDP", "NATO", "ARR", "AR", "CIBJO"]
        for chemical in formulas:
            if chemical in not_chem:
                continue
            
            for element in SymbolsList:
                if chemical.startswith(element):        
                    if formula == "":
                        formula+=chemical
                    else:
                        formula+="-"
                        formula+=chemical
                    break
                
def wiki_mineral_list():

    formula_pattern = r"\b[A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)*\b"
    fancy_pattern = r"[A-Z][a-z]?[\d\.]*(?:\([A-Za-z\d,]+\))?(?:\{[A-Za-z\d\[\]\(\),]+\})?(?:\[[A-Za-z\d]+\])*(?:\([A-Za-z\d,]+\))?"
    

    wiki = wikipediaapi.Wikipedia(language='en')

    mineral_list = []
    
    print("getting page...")
    page = wiki.page("List_of_minerals")
    
    links = page.links
    print("getting names....")
    
    counter = 0
    for link in links:
        add = True
        for char in link:
            if char == " ":
                add = False
                break
            elif char == ":":
                add = False
                break
        if add:
            counter+=1
            if counter == 10:
                print(link)
                counter=0
            elif counter != 10:
                print(link, " ", end="")
            mineral_list.append(link)
    
    
    for mineral in mineral_list:
        page = wiki.page(mineral)
        text = page.summary
        need_formula = True
        fformulas = re.findall(pattern=fancy_pattern, string=text)
        lengff = len(fformulas)
        
        if lengff == 1:
            formula = fformulas[0]
            need_formula = False
        elif lengff > 1:
            pass
            
        
        if need_formula:
            
        
            formulas = re.findall(pattern=formula_pattern, string=text)
            formula = ""
            not_chem = ["It", "IMA", "In", "REE", "REEs", "US", "IMA2018", "CNMNC", "BERR", "Dr", "GDP", "NATO", "ARR", "AR", "CIBJO"]
            for chemical in formulas:

                if chemical in not_chem:
                    continue
                
                for element in SymbolsList:
                    if chemical.startswith(element):        
                        if formula == "":
                            formula+=chemical
                        else:
                            formula+="-"
                            formula+=chemical
                        break

            print(formula)    
        
        
    


def all_mineral_names():
    import requests
    url = "https://www.mindat.org/index-A.html"
    allmins = []
    mineral_links = []
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    print("getting mineral names.....")
    for letter in ascii_uppercase:
        urlindexed = "https://www.mindat.org/index-" + letter + ".html"
        response = requests.get(urlindexed, headers=headers)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # find the links 
        links = soup.find_all('a')
        for link in links:
            endlink = link.get('href')
            print(endlink)
            mineral_links.append(f"https://www.mindat.org/{endlink}")
            
        # get the texts of the links
        link_texts = [str(link.text) for link in links]
        texts = [text.encode('latin-1', errors='ignore').decode('latin-1') for text in link_texts]

        # determine if the link starts with the index letter
        for text in texts:
            write = True
            if text.startswith(letter):
                for char in text:
                    if char == " ":
                        write = False
                        break
                if write == True:
                    print(text)
                    allmins.append(text)


    with open("all_mineral_names.py", "w") as wfile:
        wfile.write("AllMineralNames = [\n")
        for miny in allmins:
            mineral = str(miny).encode('latin-1', errors='ignore').decode('latin-1')
            line = "\t" + '"' + str(mineral) + '",\n'
            sline = str(line)
            try:
                wfile.write(sline)
            except:
                pass
            
        wfile.write("]\n")
    print("extracting data....")
    for index, link in enumerate(mineral_links):
        mineral_data = []
        if not link.startswith("https://www.mindat.org/min-"):
            allmins.pop(index)
            continue
        if link == "https://www.mindat.org/None":
            allmins.pop(index)
            continue
        response = requests.get(link, headers=headers)
        response.raise_for_status()
        print(response)
        print(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        mindatah = soup.find_all("div", class_="mindatah")
        mindata2 = soup.find_all("div", class_="mindata2")
        for idx, title in enumerate(mindatah):
            ht = title.text
            dt = mindata2[idx].text
            print(ht, dt)
            mineral_data.append((ht, dt))
        
        fn = allmins[index] + ".json"
        filen = str(fn)
        with open(filen, "w") as jfile:
            json.dump(mineral_data, jfile)

        

def download_images(query, limit=10, output_directory='downloads', chromedriver_path=None):
    """
    Download images from Google Image Search.

    Parameters:
    - query (str): The search query for images.
    - limit (int): The maximum number of images to download. Default is 10.
    - output_directory (str): The directory to save the downloaded images. Default is 'downloads'.
    - chromedriver_path (str): Path to the ChromeDriver executable (optional).

    Returns:
    - downloaded_images (list): List of downloaded image paths.
    """
    response = google_images_download.googleimagesdownload()

    # Set the download arguments
    arguments = {
        'keywords': query,
        'limit': limit,
        'output_directory': output_directory,
        'chromedriver': chromedriver_path
    }

    # Download images
    paths = response.download(arguments)

    # Return the list of downloaded image paths
    return paths[0][query]


petrographic_thin_slides_search = download_images("petrographic thin slides")