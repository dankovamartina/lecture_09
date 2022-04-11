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



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 0))


if __name__ == '__main__':
    main()