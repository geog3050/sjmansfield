# define a function
def folded_or_unfolded(climate, temp_list):
    if climate == ('Tropical'):
        threshold = 30
    if climate == ('Continental'):
        threshold = 25
    else:
        threshold = 18

    i = 0
    for i in temp_list:
        if i <= threshold:
            print('F')
        else:
            print('U')