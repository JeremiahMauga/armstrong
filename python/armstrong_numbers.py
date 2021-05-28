# How can you make this more scalable and reusable later?
def find_armstrong_numbers(list):
    
    armstrong_list = []


    for i in range(len(list)) :
        string = str(i)
        number_list = list(string)
        number_list = []

        for x in number_list :
            number_list.append(int(x))

        sum = 0    

        for y in number_list :
            sum += y ** len(number_list)

        if i == sum :
            armstrong_list.append(i) 

    print(armstrong_list)

    return armstrong_list


find_armstrong_numbers([0, 1, 2, 3, 4, 5, 6, 7])


