def run():
    my_list=[1,'hello',True,4.5]
    my_dict={'first_name':'oscar', 'last_name':'salas'}

    super_list=[
        {'first_name':'oscar', 'last_name':'salas'},
        {'first_name':'julio', 'last_name':'torres'},
        {'first_name':'carlos', 'last_name':'rodriguez'}
    ]

    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.2,4.5,6.43]
    }

    # for key,value in super_dict.items():
    #     print (key," ",value)

    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()