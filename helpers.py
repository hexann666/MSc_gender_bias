from pandas import DataFrame, read_csv, option_context, crosstab
import time
import random

def print_all(text):
    with option_context('display.max_rows', None, 'display.max_columns', None):  
        # more options can be specified also
        print(text)

def write_csv(data, filename):
    with open(filename, 'w', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(data)

def id_separator(paperURL):
    """Splits the paper URL into address and ID and saves ID
    
    :param: paper URL
    :return: paper ID
    """
    paperURL = str(paperURL)
    name = paperURL.rsplit('/', 1)[-1]
    return name

def id_separator(paperURL):
    """Splits the paper URL into address and ID and saves ID
    
    :param: paper URL
    :return: paper ID
    """
    paperURL = str(paperURL)
    name = paperURL.rsplit('/', 1)[-1]
    return name

def update_names_from_RG(paper_title, surname,webdriver='dr', name=None):
    time.sleep(random.randint(1,10))
    query = paper_title.replace(' ', '+') + '+' + surname
    url = f"https://www.researchgate.net/search.Search.html?query={query}&type=publication"
    paper_title = re.sub('[^0-9a-zA-Z ]+', '', paper_title).lower()
    #print('Search for:', paper_title)
    dr.get(url)
    soup = BeautifulSoup(dr.page_source,"lxml")

    results = soup.find_all('div', class_="nova-legacy-v-publication-item__stack nova-legacy-v-publication-item__stack--gutter-m")
        
    for result in results:
        result_title = result.find_all("a", class_="nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare")
        for result_t in result_title:
            result_t = re.sub('[^0-9a-zA-Z ]+', '', result_t.text).lower()
            #print(result_t)
            #print('Found:', re.sub('[^0-9a-zA-Z ]+', '', result_t),         
            if result_t == paper_title:
                results_name = result.find_all('a', class_='nova-legacy-v-person-inline-item')
                for name in results_name:
                    full_name = name.text.split(' ')
                    #print(surname, full_name[-1])
                    if surname.lower() == full_name[-1].lower():
                        if not full_name[0].replace('.', '').isupper():
                            if (full_name[0] not in ['Mr.', 'Dr.', 'Miss., Md.']):
                                first_name = full_name[0]
                                #print(first_name)
                                return first_name
                            
def calculate_metrics(gender_true, gender_pred):
    conf_mat = crosstab(gender_pred, gender_true)
    if 'unknown' in conf_mat.index:
        TN = conf_mat['female']['female']
        TP = conf_mat['male']['male']
        FN = conf_mat['female']['male'] + conf_mat['female']['unknown']
        FP = conf_mat['male']['female'] + conf_mat['male']['unknown']
    else:
        TN = conf_mat['female']['female']
        TP = conf_mat['male']['male']
        FN = conf_mat['female']['male']
        FP = conf_mat['male']['female']

    acc = (TN + TP)/(TP + FP + TN + FP)
    prec = TP / (TP + FP)
    rec = TP / (TP + FN)
    return acc, prec, rec
                            
