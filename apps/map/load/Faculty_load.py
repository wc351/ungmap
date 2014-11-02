from apps.map.models import Campus, Building, Faculty
import django
django.setup()

faculty_path = 'C:/Users/crlyli0476/Desktop/ungmap_reproject/Faculty/All_Faculty.csv'

f = open(faculty_path, 'r')
data = f.readlines()
f.close()
for line in data[1:]:
    print data[1:]
    campus, building, name, title, office_num, phone_num, email, department = line.strip().split(',')
    campus = Faculty.objects.filter(campus=campus).first()
    building = Faculty.objects.filter(building=building).first()
    title = Faculty.objects.filter(title=title).first()
    office_num = Faculty.objects.filter(office_num=office_num).first()
    phone_num = Faculty.objects.filter(phone_num=phone_num).first()
    email = Faculty.objects.filter(email=email).first()
    department = Faculty.objects.filter(department=department).first()

    faculty = Faculty(campus=campus)
    faculty.save()
    faculty = Faculty(building=building)
    faculty.save()
    faculty = Faculty(name=name)
    faculty.save()
    faculty = Faculty(title=title)
    faculty.save()
    faculty = Faculty(office_num=office_num)
    faculty.save()
    faculty = Faculty(phone_num=phone_num)
    faculty.save()
    faculty = Faculty(email=email)
    faculty.save()
    faculty = Faculty(department=department)
    faculty.save()

    sfaculty = []
    sfaculty.append(name)
    print "name: {0}".format(sfaculty)