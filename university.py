file = open('applicant_list_7.txt', 'r')

math_apps, phys_apps, bio_apps, chem_apps, eng_apps, second_prio, third_prio, accepted, applicants = ([] for i in range(9))
def files_init():
    file = open('physics.txt', 'w', encoding='utf-8')
    # file.write('Physics\n')
    file.close()
    file = open('mathematics.txt', 'w', encoding='utf-8')
    # file.write('Mathematics\n')
    file.close()
    file = open('chemistry.txt', 'w', encoding='utf-8')
    # file.write('Chemistry\n')
    file.close()
    file = open('engineering.txt', 'w', encoding='utf-8')
    # file.write('Engineering\n')
    file.close()
    file = open('biotech.txt', 'w', encoding='utf-8')
    # file.write('Biotech\n')
    file.close()

def files_append(app_list,dep):
    app_list.sort(key = lambda x: x[0])
    app_list.sort(reverse = True, key = lambda x: x[1])
    print('\n' + dep.capitalize())
    file = open(dep + '.txt', 'a', encoding='utf-8')
    for applicant in app_list:
        file.write(applicant[0] + ' ' + applicant[1] + '\n')
        print(applicant[0], applicant[1])
    file.close()

def priority(dep,name,exam):
    global accepted
    if name not in accepted:
        if dep == 'Engineering':
            if len(eng_apps) < max_app:
                eng_apps.append([name, exam])
                accepted.append(name)
                return 1
        elif dep == 'Mathematics':
            if len(math_apps) < max_app:
                math_apps.append([name, exam])
                accepted.append(name)
                return 1
        elif dep == 'Physics':
            if len(phys_apps) < max_app:
                phys_apps.append([name, exam])
                accepted.append(name)
                return 1
        elif dep == 'Biotech':
            if len(bio_apps) < max_app:
                bio_apps.append([name, exam])
                accepted.append(name)
                return 1
        elif dep == 'Chemistry':
            if len(chem_apps) < max_app:
                chem_apps.append([name, exam])
                accepted.append(name)
                return 1
        return 0

def applicant_sorter(applicants, prio_val):
    for i in range(2,7):
        applicants.sort(key = lambda x: x[0])
        applicants.sort(reverse = True, key = lambda x: (x[i]))
        for val in applicants:
            name = val[0] + ' ' + val[1]
            if i == 2 and val[prio_val] == 'Physics':
                priority('Physics',name,val[i])
            elif i == 3 and val[prio_val] == 'Chemistry':
                priority('Chemistry',name,val[i])
            elif i == 4 and val[prio_val] == 'Mathematics':
                priority('Mathematics',name,val[i])
            elif i == 5 and val[prio_val] == 'Engineering':
                priority('Engineering',name,val[i])
            elif i == 6 and val[prio_val] == 'Biotech':
                priority('Biotech',name,val[i])
        if len(math_apps) == max_app and len(phys_apps) == max_app and len(eng_apps) == max_app and len(bio_apps) == max_app and len(chem_apps) == max_app:
            break

max_app = int(input())
old_applicants = file.read()
file.close()
old_applicants = old_applicants.splitlines()
old_applicants = [val.split() for val in old_applicants]
for val in old_applicants:
    phys_test = round((float(val[2])+float(val[4]))/2,1)
    engin_test = round((float(val[4])+float(val[5]))/2,1)
    bio_test = round((float(val[2])+float(val[3]))/2,1)
    applicants.append([val[0],val[1],str(max(phys_test,float(val[6]))), str(max(float(val[3]),float(val[6]))), str(max(float(val[4]),float(val[6]))), str(max(engin_test,float(val[6]))), str(max(bio_test,float(val[6]))), val[7], val[8], val[9]])

applicant_sorter(applicants, 7)
for val in applicants:
    name = val[0] + ' ' + val[1]
    if name not in accepted:
        second_prio.append(val)

applicant_sorter(second_prio, 8)
for val in applicants:
    name = val[0] + ' ' + val[1]
    if name not in accepted:
        third_prio.append(val)
applicant_sorter(third_prio, 9)

files_init()
files_append(bio_apps, 'biotech')
files_append(chem_apps, 'chemistry')
files_append(eng_apps, 'engineering')
files_append(math_apps, 'mathematics')
files_append(phys_apps, 'physics')
