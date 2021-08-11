def run():
    my_list = [1,'hello',True,4.5]
    my_dict = {
        'firstname': 'samuel',
        'lastname':'Narvaez'
    }

    super_list = [
        {
            'firstname': 'Samuel',
            'lastname':'Narvaez'
        },
        {
            'firstname': 'Kim',
            'lastname':'Garces'
        },
        {
            'firstname': 'Camilo',
            'lastname':'Serrano'
        },
        {
            'firstname': 'Stiven',
            'lastname':'Castro'
        },
        {
            'firstname': 'German',
            'lastname':'Alvarez'
        },
    ]

    super_dict = {
        'natural_nums' : [1,2,3,4,5],
        'integer_nums' : [-1,-2,0,1,2],
        'floating_nums' : [1.1,4.5,6.4]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

if __name__ == '__main__':
    run()