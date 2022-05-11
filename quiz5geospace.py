# testing the import file funtion

from hw2 import openfile

try:
    f = open(filename, 'r')
    for row in f:
        row = row.strip(",\n")
        row = row.split(",")
        if len(row) == 4:
            print('The row is the correct length!')

        except:
            if len(row) != 4:
                print('The row is too long...')

    # checking that each input is correct
    row[0] = Name
    row[1] = Type
    row[2] = HP
    row[3] = Attack

    try:
        Name == str(row[0])
                   
        except TypeError:
            print('This input must be a string, try again')

    try:
        Type == str(row[1])
    
        except TypeError:
            print('This input must be a string, try again')

    try:
        HP == float(row[2])           

        except TypeError:
            print('This input must be a float value, please try again')

    try:
        Attack == float(row[3])

        except TypeError:
            print('This input must be a float value, please try again')

# close file after ensuring the inputs are correct
finally:
    f.close()

# testing the attack multiplier function

from hw2 import attack_multiplier

try:
    attacker_type == Water
    defender_type == Fire
    result = 2.5

    # calling function

    attack_multiplier(attacker_type, defender_type)

    if result == 2.5:
        print('This function worked!')

    except:
        if result != 2.5:
            print('This function did not work.')

# testing the fight function

from hw2 import fight

try:
    f = openfile('test2.txt', 'r')
    f.readLines()

    participent1 = row1[0]
    participent2 = row2[0]
    first2attack = 1 or 2

    # calling function

    fight(participent1, participent2, first2attack)
    if winner >= 1:
        print('This function completed')

except:
    if winner == 0:
        print('This function did not complete')

# testing the tournament function

from hw2 import tournament

try:
    f = openfile('test2.txt', 'r')
    f.readlines()
    f.splitlines(",")
    participents = row1, row2

    tournament(participents)

    if wins >=1:
        print('This function worked.')

except:
    if wins == 0:
        print('This function did not work.')

    
    
    
    
    
    
                        
            
            

            
