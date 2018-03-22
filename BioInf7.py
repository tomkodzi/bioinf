from random import shuffle
import copy
from Tools.scripts.treesync import raw_input

#wczytanie słów z pliku i usunięcie białych znaków
def read_input(file_name):
    file = open(file_name, encoding='utf-8',mode= "r")
    words = file.readlines()
    words = [w.strip() for w in words]
    return words

#funkcja usuwajaca duplikaty(zostają tylko unikalne wierzchołki) i dopisuje możliwe końcówki dla wierzchołków
def remove_duplicates_verticles(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:
        if lst[i][0] == lst[i - 1][0]:
            lst[i-1][1]=lst[i-1][1] + lst[i][1]
            lst.pop(i)
        i -= 1
    return lst

def remove_duplicates_verticles_ver2(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:
        if lst[i][0] == lst[i - 1][0]:
            lst[i-1][1]=lst[i-1][1] + lst[i][1]
            lst.pop(i)
        i -= 1
    return lst

def remove_duplicates_from_list(list):
    list.sort()
    i = len(list) - 1
    while i > 0:
        if list[i] == list[i - 1]:
            list.pop(i)
        i -= 1
    return list

#funkcja do tworzenia list indeksów - pomocnicza
def create_list_index(list):
    list_of_index=[]
    i=0
    for x in list:
        list_of_index.append(i)
        i+=1
#funkcja zliczająca liczbę końcowek (to jest maksymalna liczba możliwych łuków-połączeń między wierzchołkami)
def count_suffix(list):
    count=0
    for x in range(0,len(list)):
        count += len(list[x][1])
    return count
#funkcja do sprawdzania indeksu itemu w liście zagnieżdżonej
def search_nested(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            for z in range(len(mylist[i][j])):
                if mylist[i][j][z] == val:
                    return i


def find_path_ver3(list,list_with_suffix):
    result_word = ''
    verticles_path = []
    list_before_shuffle=copy.deepcopy(list)
    shuffle(list)
    verticle_from_list = 0
    help_list=[None]*len(list)
    var_x = list[verticle_from_list]
    for n in range(50):
        shuffle(list)
        index_of_verticle_to_check = list_before_shuffle.index(var_x)
        if not verticles_path:
            verticles_path.append(var_x)
        # dodanie do slowa litery z pierwszego wierzchołka
        if not result_word:
            result_word = var_x
        for ver in list:
            var_y = ver
            if var_x[len(var_x)-1] == var_y[0]:
                if search_nested(list_with_suffix,var_x)==None:
                    break
                if search_nested(list_with_suffix,var_x)==None and help_list[index_of_verticle_to_check]==None:
                    result_word=result_word+var_y[1:len(var_y)]
                    verticles_path.append(var_y)
                    help_list[index_of_verticle_to_check] = [var_y]
                    break
                elif search_nested(list_with_suffix,var_x)==None and not any(var_y in used for used in help_list[index_of_verticle_to_check]):
                    result_word = result_word + var_y[1:len(var_y)]
                    verticles_path.append(var_y)
                    if help_list[index_of_verticle_to_check]==None:
                        help_list[index_of_verticle_to_check] = [var_y]
                    else:
                        help_list[index_of_verticle_to_check].append(var_y)
                    break
                elif (not help_list or help_list[index_of_verticle_to_check]==None) and any(var_y[len(var_y)-1] in suffix for suffix in list_with_suffix[search_nested(list_with_suffix,var_x)][1]):
                    result_word = result_word + var_y[1:len(var_y)]
                    verticles_path.append(var_y)
                    help_list[index_of_verticle_to_check]=[var_y]
                    # usunięcie z listy końcówek tej która już została zużyta
                    list_with_suffix[search_nested(list_with_suffix,var_x)][1].remove(var_y[len(var_y) - 1])
                    var_x=var_y
                    break
                elif help_list[index_of_verticle_to_check]!= None and not any(var_y in used for used in help_list[index_of_verticle_to_check]) and any(var_y[len(var_y)-1] in suffix for suffix in list_with_suffix[search_nested(list_with_suffix,var_x)][1]):
                    result_word = result_word + var_y[1:len(var_y)]
                    verticles_path.append(var_y)
                    help_list[index_of_verticle_to_check].append(var_y)
                    #usunięcie z listy końcówek tej która już została zużyta
                    list_with_suffix[search_nested(list_with_suffix,var_x)][1].remove(var_y[len(var_y)-1])
                    var_x=var_y
                    break
    return result_word






#funkcja tworząca listę słów (trójek) występujących sekwencja
def get_words_from_sequence(seq):
    list=[]
    for i in range(len(seq)-(k-1)):
        list.append(seq[i:i+k])
    return list

#funkcja do usuwania duplikatów z listy utworzonych sekwencji
def check_duplicates_in_seq(list):
    list.sort()
    new_list=[]
    i = len(list) - 1
    while i > 0:
        if list[i] == list[i - 1]:
            new_list.append(list[i])
        i -= 1
    return new_list

#usuwanie dulikujących się elementów w liście
def remove_duplicates_in_list(list):
    list.sort()
    i = len(list) - 1
    while i > 0:
        if list[i] == list[i - 1]:
            list.pop(i)
        i -= 1
    return list



########################################## POCZĄTEK PROGRAMU ##############################################

#wczytanie zakresu błędów
error_range= int(raw_input("Podaj zakres błędów:" ))


#wczytanie inputu(słów wejściowch) z pliku
words=read_input("testow2.txt")
verticles=[]
verticles_with_suffix=[]
#pobranie długosci słów wejściowych
k=len(words[0])
print("K: ",k)
#wpisanie wszystkich wierzchołków do listy (razem z końcówkami)
for w in words:
    verticles.append([w[0:len(w) - 1], w[1:len(w)]])
    verticles_with_suffix.append([[w[0:len(w)-1]],[w[len(w)-1:]]])
print("Wierzchołki stworzone ze słów wejściowych",verticles)
var_string=[]
#przerobienie listy tak aby występowały w niej wierzchołki w postaci stringów
for x in range(0, len(verticles)):
    for y in range(0, len(verticles[x])):
        var_string.append(str(verticles[x][y]).strip('[]\'\''))

verticles=copy.deepcopy(var_string)
#usunięcie duplikujących się wierzchołków
verticles_with_suffix=remove_duplicates_verticles(verticles_with_suffix)
print("Wierzchołki z przyrostkami",verticles_with_suffix)
print("Verticles", verticles)
verticles=remove_duplicates_from_list(verticles)
print("Dostępne wierzchołki (bez duplikatów): ",verticles)


max_word_size=count_suffix(verticles)+k-1
#lista użytych słów wejściowych(trójek) do budowy sekwencji
list_of_used_word=[]
#lista słów wejściowych które nie zostały użyte do budowy sekwencji
list_of_unused_word=[]
#lista gdzie wpiswane są sekwencje utworzone podczas kolejnych iteracji
found_sequences =[]
#pętla w której tworzona jest lista sekwencji wyjściowych
for z in range(1500):
    path = find_path_ver3(verticles,verticles_with_suffix)
    found_sequences.append(path)

maxlength_of_found_sequences = max(len(s) for s in found_sequences)
#wybór najdłuższych utworzonych sekwencji
longest_found_sequences = [s for s in found_sequences if len(s) == maxlength_of_found_sequences]

#Wyświetlenie najdłuższych ułożonych sekwencji
longest_found_sequences=remove_duplicates_from_list(longest_found_sequences)
print("Najdłuższe sekwencje:",longest_found_sequences)

#badanie stworzonych (najdłuższych) sekwencji pod kątem użytych do ich budowy słów
for i in range(len(longest_found_sequences)):
    list_of_used_word.clear()
    list_of_unused_word.clear()
    print("\n\n\nIteracja numer: ",i)
    check_sequence = longest_found_sequences[i]

    words_of_sequence = get_words_from_sequence(check_sequence)

    #sprawdzenie liczby błędów negatywnych
    #sprawdzenie duplikatów słów w sekwencji
    negative_errors=len(check_duplicates_in_seq(words_of_sequence))
    #sprawdzenie czy w sekwencji występują słowa niewystępujące w zbiorze wejściowym
    for s in words_of_sequence:
        if not any(s in w for w in words):
            negative_errors+=1

    #sprawdzenie liczby błędów pozytywnych
    for w in words:
        if any(w in s for s in words_of_sequence):
            list_of_used_word.append(w)
        else:
            list_of_unused_word.append(w)


    #suma wszystkich znalezionych błędów (negatywne + pozytywne)
    sum_of_errors= len(list_of_unused_word)+negative_errors

    if sum_of_errors<=error_range:
        print("\nWYNIK: \n")
        print("Badana sekwencja: ", check_sequence)
        print("Słowa jakie zawiera sekwencja: ", words_of_sequence)
        print("Słowa wejściowe: ",words)
        print("Lista słów wejściowch użytych przy budowie sekwencji: ",list_of_used_word, "\nlista nieużytych słów wejściowych (błędy pozytywne): ", list_of_unused_word,
              "\nIlość błędów negatywnych: ", negative_errors, "\nIlość błędów pozytywnych: ", len(list_of_unused_word))
    else: print("Liczba błędów była większa niż się spodziewałeś.")

