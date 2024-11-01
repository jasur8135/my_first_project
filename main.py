from enter_info import enter_safe_mem
from show_info import  read_members, print_member_info


file_name='family_list.txt'
enter_safe_mem(file_name)
k=input('siz kirgizgan azolaringizni malumotlarini kormoqchimisiz Y/N \n>>>').lower()
if  k=='y':
    members_data = read_members(file_name)
    name_to_search = input("A'zoning ismini kiriting: ").title()
    print_member_info(members_data, name_to_search)




