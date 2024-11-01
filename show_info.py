def read_members(file_name):
    members = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        member_data = {}
        for line in file:
            line = line.strip()
            if line.startswith("Ism:"):
                member_data['Ism'] = line.split(": ")[1]
            elif line.startswith("Yosh:"):
                member_data['Yosh'] = line.split(": ")[1]
            elif line.startswith("Qiziqishlari:"):
                member_data['Qiziqishlari'] = line.split(": ")[1]
            elif line == "":
                # Bo'sh qator kelganda ma'lumotlarni lug'atga qo'shamiz
                if 'Ism' in member_data:
                    members[member_data['Ism']] = member_data
                member_data = {}
    return members

def print_member_info(members, name):
    # A'zolar haqida ma'lumotni chiqarish
    if name in members:
        print(f"Ism: {members[name]['Ism']}")
        print(f"Yosh: {members[name]['Yosh']}")
        print(f"Qiziqishlari: {members[name]['Qiziqishlari']}")
    else:
        print(f"{name} ismi bilan a'zo topilmadi.")


