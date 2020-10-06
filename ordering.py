import os
import json
from math import pow,log2,ceil


def ordering(wantedlist,inital_penalty = 0):
    if wantedlist == []:
        print("NO enchantment given")
        return
    sortedlist, numlist = enchantment_split(wantedlist)

    total_step = int(log2(len(sortedlist)))+1
    penalty = inital_penalty + total_step 

    # the factor of enchantment (first 16 books, should be enough though), no idea to form an equation or function
    multiplyfactor = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]

    ordering_num = [[] for x in range(total_step)]
    ordering = []
    
    # multiplied enchatment factor
    xp_extra_level = 0
    priority_list = []

    # generate base enchantment level list
    # i.e. add the sum of penalty level by item and merged books
    # also, count the max_step
    total_enchantment = len(numlist)
    xp_list, max_step = enchant_layer(total_step, total_enchantment, inital_penalty)

    if penalty > 6:
        return "Error!Cannot enchant"


    while numlist:
        temp_max_step = []
        
        for x in max_step:
            if x == 0:
                temp_max_step.append(1000)
            else:
                temp_max_step.append(x)

        priority_list = [xp_list[i]*temp_max_step[i] for i in range(len(xp_list))]


        step = priority_list.index(min(priority_list))
        existed_num = len(ordering_num[step])
        tobe_enchanted = max(numlist)

        ordering_num[step].append(tobe_enchanted)
        xp_list[step] += tobe_enchanted
        max_step[step] -= 1

        # combining enchantments cause the level counted more than one times
        if existed_num != 0:
            xp_extra_level += tobe_enchanted * multiplyfactor[existed_num]

        numlist.remove(tobe_enchanted)


    #penalty of merged books
    xp_penalty_book = 0
    for element in ordering_num:
        #penalty for merge book
        xp_penalty_book += merged_penalty_book(len(element))

        #list steps with name
        for j in element:
            for k in sortedlist:
                if k[1] == j:
                    ordering.append(k)
                    sortedlist.remove(k)
                    break

    xp_max = 0
    for i in xp_list:
        if i > xp_max:
            xp_max = i
            
    print(ordering)
    print("max:",xp_max)
    print("penalty:",penalty)
    print("total level:",sum(xp_list)+xp_extra_level+xp_penalty_book)
    return ordering



def list_to_step(wantedlist):
    n = 1
    wantedlist = [i[0] for i in wantedlist]



def enchant_layer(total_step,total_enchantment, inital_penalty):
    xp_list = []
    max_step = []
    for i in range(total_step):
        # add the penalty level by item
        xp_list.append(2** i+inital_penalty -1)
        
        num_of_enchantment = min(2**i, total_enchantment)
        max_step.append(num_of_enchantment)
        total_enchantment -= num_of_enchantment
        merged_books_penalty = 2**ceil(log2(num_of_enchantment)) -1
        # add the penalty level by merged books
        xp_list[i] += merged_books_penalty
    return xp_list,max_step


def merged_penalty_book(num):
    if num == 0:
        return 0
    xp = 0
    p_list = [0 for x in range(num)]
    while len(p_list) != 1 :
        new_list = []
        for i in range(num//2):
            xp += sum([2**x-1 for x in p_list[i*2:i*2+2]])
            new_list.append(max(p_list[i*2:i*2+2])+1)
        if num %2 != 0:
            new_list.append(p_list[-1])
        p_list = new_list[:]
        num = len(p_list)
    
    return xp




def enchantment_split(wantedlist):
    #get the xp required and in（tobe_enchanted it
    numlist = [x[1] for x in wantedlist]
    numlist.sort(reverse=True)
    sortedlist = []
    for num in numlist:
        for element in wantedlist:
            if element[1] == num:
                sortedlist.append(element)
                wantedlist.remove(element)
              
    return sortedlist,numlist
