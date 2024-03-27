from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.utils import timezone


# Create your views here.

def dashboard(request):
    
    
    return render(request, 'payrollapp/dashboard.html')

def login(request):
    return render(request, 'payrollapp/login.html')

def employee_database(request):
    a = Employee.objects.all()
    return render(request, 'payrollapp/employee_database.html', {'a':a})

def add_employee(request):
    #If form is submitted
    if(request.method=="POST"):
        id_no = 1
        id_no = str(id_no)
        #for b in a:
        #    id_no += 1
        #id_no = str(id_no)
        #Get Data
        try:
            last_name  = request.POST.get('inputLtName')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            first_name = request.POST.get('inputFstName')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            middle_name = request.POST.get('inputMidName')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        
        
        
        idnumber = str(request.POST.get('inputFstName'))[0] + str(request.POST.get('inputMidName'))[0] + str(request.POST.get('inputLtName'))[0]
        id_no = id_no.zfill(3)
        idnumber = idnumber + id_no

        #In the rare chance we've have 999 employees total with the same starting first middle and last names
        emergency = 0
        if Employee.objects.filter(id_number=idnumber).exists():
            while Employee.objects.filter(id_number=idnumber).exists() or emergency<999:
                emergency +=1
                id_no = int(id_no)
                if id_no == 999:
                    id_no = 0
                id_no += 1
                id_no = str(id_no)
                id_no = id_no.zfill(3)
                idnumber = idnumber + id_no
            if emergency == 999:
                messages.warning(request, "ERROR, 999 employee records hold the same starting letters and number. Please contact IT to upgrade") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
                return render(request, 'payrollapp/add_employee.html')


        try:
            pnumber = int(request.POST.get('inputPhone'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            email = str(request.POST.get('inputEmail4'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        
        
        try:
            department  = str(request.POST.get('inputDept'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            status  = str(request.POST.get('inputEmpStat'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            position = str(request.POST.get('inputPosition'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            joindate = request.POST.get('inputJoinDate')
            #messages.success(request, str(joindate))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        
        
        
        try:
            # Convert the date string to a datetime object
            joindate = timezone.datetime.strptime(joindate, "%Y-%m-%d").date()
        
        except ValueError:
            # Handle the case where the date string is not in the correct format
            messages.warning(request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, 'payrollapp/add_employee.html')


        try:
            banknumber = str(request.POST.get('inputBankAccNo'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')
        try:
            salary = float(request.POST.get('inputSalary'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html')

        

        
        
        
        
        


        #Check if employee exists or if the ID is in use(This can be an and if you want to allow same name employees but different IDs but RAW its name or ID)
        if Employee.objects.filter(Last_name=last_name, 
                                        First_name=first_name, 
                                        Middle_name=middle_name ).exists():
            #Message warning, Employee exists/ID in use
            messages.warning(request, "Employee/ID Number Already Exists!")
            #Render create employee
            return render(request, 'payrollapp/add_employee.html')
        else:
            try:
                #Attempts to create employee
                Employee.objects.create(Last_name=last_name, 
                                        First_name=first_name, 
                                        Middle_name=middle_name, 
                                        id_number=idnumber, 
                                        Status=status, 
                                        Department=department, 
                                        Role=position, 
                                        Join_Date=joindate, 
                                        Phone_Number=pnumber, 
                                        Email=email, 
                                        BankNumber=banknumber, 
                                        Salary=salary)
                messages.success(request, "Employee created successfully!")
                return redirect('employee_database')
            except:#None Type
                #Message warning, Employee exists/ID in use
                messages.warning(request, "Empty field/Incorrect inputs detected!"+" Employee "  + str(type(employee)) +str(employee) + " ID "  +str(type(idnumber)) +str(idnumber) + " Status " +str(status) + " Department " +str(department) + " Role " +str(position) + " Date " +str(joindate) + " PN " +str(pnumber) + " Email " +str(email) + "Join Date " + str(type(joindate)) + str(joindate))
                #Render create employee
                return render(request, 'payrollapp/add_employee.html')
    else:
        return render(request, 'payrollapp/add_employee.html')

def generate_page(request):
    return render(request, 'payrollapp/generate_page.html')

def employee_info(request, EID):
    if(request.method=="POST"):
        a = get_object_or_404(Employee, pk = EID)
        try:
            last_name  = request.POST.get('inputLtName')
        except:
            messages.warning(request, "Error missing values Last Name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            first_name = request.POST.get('inputFstName')
        except:
            messages.warning(request, "Error missing values first_name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            middle_name = request.POST.get('inputMidName')
        except:
            messages.warning(request, "Error missing values middle_name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:#Need to fix in case of changing name if the ID will change as well
            idnumber = request.POST.get('inputID')
        except:
            messages.warning(request, "Error missing values idnumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            pnumber = request.POST.get('inputPhone')
        except:
            messages.warning(request, "Error missing values pnumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            email = str(request.POST.get('inputEmail4'))
        except:
            messages.warning(request, "Error missing values email") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        
        try:
            department  = str(request.POST.get('inputDept'))
        except:
            messages.warning(request, "Error missing values department") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            status  = str(request.POST.get('inputEmpStat'))
        except:
            messages.warning(request, "Error missing values status") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            position = str(request.POST.get('inputPosition'))
        except:
            messages.warning(request, "Error missing values position") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            joindate = request.POST.get('inputJoinDate')
        except:
            messages.warning(request, "Error missing values joindate") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            # Convert the date string to a datetime object
            joindate = timezone.datetime.strptime(joindate, "%b. %d, %Y").date()
        except ValueError:
            # Handle the case where the date string is not in the correct format
            messages.warning(request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            banknumber = str(request.POST.get('inputBankAccNo'))
        except:
            messages.warning(request, "Error missing values banknumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        try:
            salary = float(request.POST.get('inputSalary'))
        except:
            messages.warning(request, "Error missing values salary") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'a':a})
        #Check if employee exists or if the ID is in use(This can be an and if you want to allow same name employees but different IDs but RAW its name or ID)
#        if Employee.objects.filter.filter(pk=EID).update.exists():
   #         #Message warning, Employee exists/ID in use
    #        messages.warning(request, "Employee/ID Number Already Exists!")
     #       #Render create employee
      #      return render(request, 'payrollapp/employee_info.html', {'a':a})
       # else:
        try:
                #Attempts to create employee
            Employee.objects.filter(pk=EID).update(Last_name=last_name, 
                                        First_name=first_name, 
                                        Middle_name=middle_name, 
                                        id_number=idnumber, 
                                        Status=status, 
                                        Department=department, 
                                        Role=str(position), 
                                        Join_Date=joindate, 
                                        Phone_Number=int(pnumber), 
                                        Email=email, 
                                        BankNumber=int(banknumber), 
                                        Salary=salary)
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_database')
        except:#None Type
                #Message warning, Employee exists/ID in use
            messages.warning(request, "Empty field/Incorrect inputs detected!" + str(type(last_name)) + str(type(first_name)) + str(type(middle_name)) + str(type(idnumber)) + str(type(status)) + str(type(department)) + str(type([position]))  + str(type(joindate)) + str(type(pnumber)) + str(type(email)) + str(type(banknumber)) + str(type(salary)))
                #Render create employee
            return render(request, 'payrollapp/employee_info.html', {'a':a})
    else:
        a = get_object_or_404(Employee, pk = EID)
        return render(request, 'payrollapp/employee_info.html', {'a':a})

def attendance_db(request):
    return render(request, 'payrollapp/attendance_db.html')

def employee_attendance(request):
    return render(request, 'payrollapp/employee_attendance.html')

def tax_module(request):
    return render(request, 'payrollapp/tax_module.html')

def encode_page(request):
    return render(request, 'payrollapp/encode_page.html')

def payroll_breakdown(request):
    return render(request, 'payrollapp/payroll_breakdown.html')