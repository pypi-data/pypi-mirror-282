'''
Pylines moudule will give you all management and powers to store in an organized way and retrieve data in a smooth and efficient way\n
the Pylines module stores data in the form of rows and in an odd number system such as 1,3,5,9...\n
The dump() func is the func with which you will add data\n
The load() func is the func that will take data,whether in the form of a list or a dict\n
The rest of the func are explained
'''

def dump(obj : list , file , clean : bool = False):
    '''
    Args : obj : [] , file : FileName , Clean \n
    obj = your data (list or big list(2D)) you want put it in your txt file 'you can pass list only'\n
    file = FileName 
    clean = default False if you put your data like this [1,2,3,4] don't change clean to true
    if your data like this [[1,2,3],[4,5,6]...] change clean to true cuz sort data to give a row his value \n
    ex:
    input :dump(obj= [1,2,3] , file = 'file_txt' ) 
    out in file : row 1 = [1,2,3]\n
    another ex :
    input :dump(obj= [1,2,3] , file = 'file_txt' , clean = True ) 
    out in file : row 1 = 1\n
    row 3 = 2\n
    row 5 = 3
    '''
    if  not clean:
        try:
            load = open(file,'r').readlines()

            with open(file,'a') as f:
                f.write(f'{len(load)+1}: {obj}\n')
                f.write('\n')

        except FileNotFoundError as f:
            with open(file,'a') as f:
                f.write(f'1: {obj}\n')
                f.write('\n')
    else:
        for item in range(len(obj)):
            try:
                load = open(file,'r').readlines()

                with open(file,'a') as f:
                    f.write(f'{len(load)+1}: {obj[item]}\n')
                    f.write('\n')

            except FileNotFoundError as f:
                with open(file,'a') as f:
                    f.write(f'1: {obj[item]}\n')
                    f.write('\n')

def load(file , type : str = 'dict') -> dict[str,list] | list[list | str] :
    '''
    Args : file : FileName , type : dict{default} | list | both
    this func you cant using it with any file txt just with our txt and his data was dumping by our func(dump)
    file = FileName
    type = if you want data return to you like dict [key[row_number] , value[row_data]] dont  change anything\n
    if you want data return to you like list [data[row1] , data [row2].....] change type to list\n
    if you want both change type to both wiil return list & dict

    '''
    try:
        main_dict = {}
        main_list = []
        with open(file,'r') as f:
            it = f.readlines()
            with_out_n = [list_[0:-1] for list_ in it if list_ != '\n']
            for list , num  in zip(with_out_n,range(1,len(with_out_n)*2,2)):
                    main_dict[num] = eval(list[3:])
                    main_list.append(eval(list[3:]))
    except FileNotFoundError as f:
        print(f'{f}\n you should create a new file by our func (dump)')
    if type == 'dict':
        return main_dict
    elif type == 'list':
        return main_list
    elif type == 'both':
        return main_list , main_dict

def fetchall_rows_numbers(file) -> list[int] : 
    '''
    Args : file : FileName
    return all rows number like [1,3,5,7,9........]
    '''
    with open(file , 'r') as f:
        data = f.readlines()
    all_numbers_row = [row_n.split(':')[0] for row_n in data if row_n != '\n']
    return all_numbers_row
    
def fetch_by_row(row_number: str , file) -> str | None :
    '''
    Args : row : str[row_number] file : FileName\n
    this you will give number of row and it will return row data
    '''
    with open(file,'r') as f:
        data = f.readlines()
        for ckh_row in data:
            num_row = ckh_row.split(':')[0]
            if str(row_number) == num_row:
                return eval(ckh_row[3:-1])
        return None
        
def replace_row(row_number : str, new_row_value : str | list | dict | set , file ) -> None:
    '''
    Args : row_number : str[rown_number] , new_row_value : str | list | dict | set , file ;FileName
    you will give it number_row and new value and it will edit him in txt file
    '''
    copy_data = []
    with open(file , 'r') as f:
        data = f.readlines()
        for row in data:
            if str(row_number) == row.split(':')[0]:
                copy_data.append(f'{row_number}: {new_row_value}\n')
                continue
            else:
                copy_data.append(row)
    with open(file,'w') as fl:
        fl.writelines(copy_data)

def replace_rows(from_ : int , to : int ,file,values) -> None:
    '''
    Args : from : int , to : int , file :FileName , values : [data[to row from start],.,.,data[till last row]]
    for ex:
    if this your data :\n
    old data:
    row1 = 1
    row3 = 2
    row5 = 3
    row7 = 4
    row9 = 5
    row11 = 6\n
    replace_rows(1,9 , FILENAME , [9,8,7,6])\n
    new data:
    row1 = 9
    row3 = 8
    row5 = 7
    row7 = 6
    row9 = 5
    row11 = 6
    \nif we foucs we will find row9 it's still the same if you wanna change it also 'replace(1,11 or 9+2 ....)

    '''
    increase = 0
    for row in fetchall_rows_numbers(file):
        if int(row) == int(to):
            break
        if int(from_) <= int(row):
            replace_row(row , values[increase] , f)
            increase += 1


