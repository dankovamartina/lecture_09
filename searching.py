import os
import json

#balicek os resi problemy s lomitky pri zadavani cest - podiva se, co mam za operacni system a podle toho tam vlozi potrebna lomitka

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    #napred osetrime, jeslti je pozadovany klic field v MNOZINE pozadovanych reseni

    #tady spojujeme dve cesty dohromady - ziskame absolutni cestu k souboru
    file_path = os.path.join(cwd_path, file_name)

    with open (file_path, mode ="r") as json_file:
        data = json.load(json_file)

 #napred osetrime, jeslti je pozadovany klic field v MNOZINE pozadovanych reseni
 #klice nahazime do mnoziny prikazem set
    if field not in set(data.keys()):
        return None
    return data[field]  # vracime jen kousek toho slovniku podle klice


def linear_search(sekvence, cislo):
    """
    :param sekvence: prohledavana sekvence (seznam)
    :param cislo: hledane cislo (int)
    :return: slovnik se dvema klici, prvni klic je "positions" - seznam pozic, indexu a druhy klic je "count" - pocet vyskytu hledaneho cisla
    """
    positions = []
    count = 0

    for i in range(0, len(sekvence)):
        if sekvence[i] == cislo:
            count = count + 1
            positions.append(i)
   # return {"positions": positions, "count": count}
    #nebo se to dalo delat pres enumerate
    search_res = {"positions": [], "count": 1}
    for index, value in enumerate(sekvence):
        if value == cislo:
            search_res["positions"].append(index)
            search_res["count"] = search_res["count"]+1
    return search_res

    # analyza asymptoticke slozitosti:
    # nejhorsi a nejlepsi scenar vzdykcy vyjsou stejne, protoze hledame vsechny vyskyty a musime to stejne projet cele
    # vzdycky to bude O(n)

#moje reseni, ktere pry slo o krok dopredu :-)
def pattern_search(sekvence, vzor):
    """
    :param sekvence: prohledavana sekvence
    :param vzor: porovnavany vzor, muze mit ruznou delku!
    :return: mnozina ve ktere jsou ulozeny pozice vyskytu v sekvenci
    """
    delka = len(vzor)
    mnozina = set()
    for j in range(0, len(sekvence)-delka + 1):
        pomocna = 0
        for i in range(0, delka):
            if pomocna == 0:
                if sekvence[j+i] != vzor[i]:
                    pomocna = 1
        if pomocna == 0:
            mnozina.add(j)
    return mnozina
#tak jak jsme to v hodine delali vzorove:
def vzorak_pattern_search(sequence, pattern):
    positions = set()
    index = 0
    while index < len(sequence) - len(pattern):
        if sequence[index:index + len(pattern)] == pattern:
            positions.add(index)
        index = index + 1
    return positions



def main():
    sekvenceDNA = read_data("sequential.json", "dna_sequence")
    print(sekvenceDNA)
    print(pattern_search(sekvenceDNA, "ATA"))
    print(vzorak_pattern_search(sekvenceDNA, "ATA"))

if __name__ == '__main__':
    main()


