# TODO Найдите количество книг, которое можно разместить на дискете
info_disk = 1.44 #Mb
num_pgs_bk = 100 # Pgs
num_lns_pg = 50 # lines
num_sym_ln = 25 # symbols
size_one_symbol = 4 #b
size_of_1_bk =(size_one_symbol*num_sym_ln*num_lns_pg*num_pgs_bk)/(1024*1024)#Mb
num_of_bks = info_disk/size_of_1_bk
num_of_bks =int(num_of_bks)
#print(num_of_bks)
print("Количество книг, помещающихся на дискету:", int(num_of_bks))
