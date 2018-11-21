import random, string

def import_names(name_file):
    try:
        with open(name_file, 'r') as f_open:
            names = f_open.readlines()
            name_list = [x.strip() for x in names]
    except:
        print("name file not found\n")
    return  name_list

def namegetter(firstnames, lastnames, count):
        for i in range(0,count):
            first_name = random.choice(firstnames)
            last_name = random.choice(lastnames)
            rtn_name = first_name + ' ' + last_name
            print(rtn_name)

def main():
    input_m_first_name = 'maleNAMES.txt'
    input_f_first_name = 'femaleNAMES.txt'
    input_last_name = 'lastNAME.txt'

    while True:
        first_names = []
        last_names = []
        answer = input("\nLet's generate a random Male or Female name.\nPlease answer 'M' or 'F' or Press 'Q' to quit. \n")
        answer = answer.upper()
        if answer in ('M', 'F'):
            if answer == 'M':
                first_names = import_names(input_m_first_name)
            elif answer == 'F':
                first_names = import_names(input_f_first_name)
            last_names = import_names(input_last_name)
        elif answer == 'Q':
            break
        else:
            print("\nInput must be 'M' or 'F' to select a Male or Female name or 'Q' to quit.")
            continue

        count = 0
        while True:
          try:
             count = int(input("\nHow many names do you want? \n"))
          except ValueError:
              print("\nInput must be an integer!\n")
              continue
          if count < 0:
              print("\nInput must be a positive number!\n")
          else:
              print("\n")
              namegetter(first_names, last_names, count)
              break
main()
