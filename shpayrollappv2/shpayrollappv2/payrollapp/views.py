from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *
from django.contrib import messages
from django.utils import timezone
from datetime import *
from .taxEmployee_salary import *
from .ModifierDBchanges import *
#'%d/%m/%Y
#"%Y-%m-%d"
# Create your views here.

def dashboard(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/dashboard.html',{'user':user} )

def login(request):
    if(request.method=="POST"):
        
        username = request.POST.get('userlogin')
        password = request.POST.get('pwlogin')
        account = USER_ACCOUNT.objects.filter(username=username, password=password)

        if(account.exists()):
            return redirect(f'dashboard/{account.first().pk}') 
        else:
            messages.error(request, "Invalid login")
            return render(request, 'payrollapp/login.html')
            
    else:
        return render(request, 'payrollapp/login.html')

def employee_database(request, UID):
    a = Employee.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/employee_database.html', {'user':user, 'a':a})

def add_employee(request, UID):
    #If form is submitted
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
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
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            first_name = request.POST.get('inputFstName')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            middle_name = request.POST.get('inputMidName')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        
        
        
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
                return render(request, 'payrollapp/add_employee.html', {'user':user})


        try:
            pnumber = int(request.POST.get('inputPhone'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            email = str(request.POST.get('inputEmail4'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        
        
        try:
            department  = str(request.POST.get('inputDept'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            status  = str(request.POST.get('inputEmpStat'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            position = str(request.POST.get('inputPosition'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            joindate = request.POST.get('inputJoinDate')
            #messages.success(request, str(joindate))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        
        
        
        try:
            # Convert the date string to a datetime object
            joindate = datetime.strptime(joindate, "%Y-%m-%d").date()
        
        except ValueError:
            # Handle the case where the date string is not in the correct format
            messages.warning(request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, 'payrollapp/add_employee.html', {'user':user})


        try:
            banknumber = str(request.POST.get('inputBankAccNo'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})
        try:
            salary = float(request.POST.get('inputSalary'))
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/add_employee.html', {'user':user})

        

        
        
        
        
        


        #Check if employee exists or if the ID is in use(This can be an and if you want to allow same name employees but different IDs but RAW its name or ID)
        if Employee.objects.filter(Last_name=last_name, 
                                        First_name=first_name, 
                                        Middle_name=middle_name ).exists():
            #Message warning, Employee exists/ID in use
            messages.warning(request, "Employee/ID Number Already Exists!")
            #Render create employee
            return render(request, 'payrollapp/add_employee.html', {'user':user})
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
                return redirect('employee_database', {'user':user})
            except:#None Type
                #Message warning, Employee exists/ID in use
                messages.warning(request, "Empty field/Incorrect inputs detected!"+" Employee "  + str(type(last_name)) +str(last_name) + " ID "  +str(type(idnumber)) +str(idnumber) + " Status " +str(status) + " Department " +str(department) + " Role " +str(position) + " Date " +str(joindate) + " PN " +str(pnumber) + " Email " +str(email) + "Join Date " + str(type(joindate)) + str(joindate))
                #Render create employee
                return render(request, 'payrollapp/add_employee.html', {'user':user})
    else:
        return render(request, 'payrollapp/add_employee.html', {'user':user})

def generate_page(request, UID):
    a = Employee.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    if (request.method == "POST"):
        #Get the department type
        try:
        #    department  = request.POST.get('inputDept')
            employee = request.POST.get('inputID')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html' , {'user':user, 'a':a})
        #Get Start Date
        try:
            start  = request.POST.get('inputStartDate')
            try:
            # Convert the date string to a datetime object
                start = datetime.strptime(start, "%Y-%m-%d").date()
        
            except ValueError:
            # Handle the case where the date string is not in the correct format
                messages.warning(request, "Invalid date format. Please use YYYY-MM-DD.")
                return render(request, 'payrollapp/generate_page.html' , {'user':user, 'a':a})
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html' , {'user':user, 'a':a})
        #Get End Date
        try:
            end  = request.POST.get('inputEndDate')
            try:
            # Convert the date string to a datetime object
                end = datetime.strptime(end, "%Y-%m-%d").date()
        
            except ValueError:
            # Handle the case where the date string is not in the correct format
                messages.warning(request, "Invalid date format. Please use YYYY-MM-DD.")
                return render(request, 'payrollapp/generate_page.html', {'user':user, 'a':a})
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html', {'user':user, 'a':a})
        
        #Tax inputs

        try:
        #    department  = request.POST.get('inputDept')
            ULD_AM = request.POST.get('inputULD')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html', {'user':user, 'a':a})
        try:
        #    department  = request.POST.get('inputDept')
            ULD_T = request.POST.get('inputULDT')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html', {'user':user, 'a':a})
        try:
        #    department  = request.POST.get('inputDept')
            CA_AM = request.POST.get('inputCA')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html', {'user':user, 'a':a})
        try:
        #    department  = request.POST.get('inputDept')
            COOP_AM = request.POST.get('inputCOOP')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html', {'user':user, 'a':a})
        try:
        #    department  = request.POST.get('inputDept')
            COLA_AM = request.POST.get('inputCOLA')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html', {'user':user}, {'a':a})
        try:
        #    department  = request.POST.get('inputDept')
            ADDE_AM = request.POST.get('inputADDE')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html' , {'user':user, 'a':a})
        try:
        #    department  = request.POST.get('inputDept')
            ADDE_T = request.POST.get('inputADDET')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/generate_page.html' , {'user':user, 'a':a})
        #Get all
        #employee_list = Employee.objects.filter(Department=department)
        #Run the calculation for values
        #for x in employee_list:
        #    calculateSALARY(x.id_number)
        total, absenceDues, SSS_RATE_ID, PH_ID, HDMF_ID,  WITH_ID = calculateSALARY(employee, start, end, ULD_AM, ULD_T, CA_AM, COOP_AM, COLA_AM, ADDE_AM, ADDE_T)
        try:
            LatestPayslip = Payslip_Transaction.objects.last()
            PayslipID = LatestPayslip.Transaction_ID+ 1
        except:
            PayslipID = 1
        
        try:
            Payslip_Transaction.objects.create(Transaction_ID = PayslipID,
            Date_Distributed = datetime.now().date(),
            Start_Date = start,
            End_Date = end,
            Net_Pay = total,
            Absence_Deductions = absenceDues,
            Employee_ID = get_object_or_404(Employee, pk=employee),
            SSS_Rate_ID = get_object_or_404(SSS, pk=SSS_RATE_ID),
            PhilHealth_Rate_ID = get_object_or_404(PhilHealth, pk=PH_ID),
            HDMF_Rate_ID = get_object_or_404(HDMF, pk=HDMF_ID),
            WTAX_Rate_ID = get_object_or_404(WitholdingTax, pk=WITH_ID),
            HMO_Rate_ID = get_object_or_404(HMO, pk=employee),
            ULDeductions_Rate_ID = UNIFORMLAPTOPDEDUCTIONS.objects.last(),
            CA_Rate_ID = CA.objects.last(),
            COOP_Rate_ID = COOP.objects.last(),
            COLA_Rate_ID = COLA.objects.last(),
            AddtlEarning_Rate_ID = ADDITIONAL_EARNINGS.objects.last()
            )
        except:
            print("Soemthing fked up")
        return render(request, 'payrollapp/generate_page.html' , {'user':user,'a':a})
    else:
        return render(request, 'payrollapp/generate_page.html' , {'user':user,'a':a})

def employee_info(request, UID, EID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    if(request.method=="POST"):
        a = get_object_or_404(Employee, pk = EID)
        try:
            last_name  = request.POST.get('inputLtName')
        except:
            messages.warning(request, "Error missing values Last Name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            first_name = request.POST.get('inputFstName')
        except:
            messages.warning(request, "Error missing values first_name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            middle_name = request.POST.get('inputMidName')
        except:
            messages.warning(request, "Error missing values middle_name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user, 'a':a})
        try:#Need to fix in case of changing name if the ID will change as well
            idnumber = request.POST.get('inputID')
        except:
            messages.warning(request, "Error missing values idnumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            pnumber = request.POST.get('inputPhone')
        except:
            messages.warning(request, "Error missing values pnumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            email = str(request.POST.get('inputEmail4'))
        except:
            messages.warning(request, "Error missing values email") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        
        try:
            department  = str(request.POST.get('inputDept'))
        except:
            messages.warning(request, "Error missing values department") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            status  = str(request.POST.get('inputEmpStat'))
        except:
            messages.warning(request, "Error missing values status") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            position = str(request.POST.get('inputPosition'))
        except:
            messages.warning(request, "Error missing values position") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user, 'a':a})
        try:
            joindate = request.POST.get('inputJoinDate')
        except:
            messages.warning(request, "Error missing values joindate") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            # Convert the date string to a datetime object
            joindate = timezone.datetime.strptime(joindate, "%b. %d, %Y").date()
        except ValueError:
            # Handle the case where the date string is not in the correct format
            messages.warning(request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, 'payrollapp/employee_info.html', {'user':user,'a':a})
        try:
            banknumber = str(request.POST.get('inputBankAccNo'))
        except:
            messages.warning(request, "Error missing values banknumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user, 'a':a})
        try:
            salary = float(request.POST.get('inputSalary'))
        except:
            messages.warning(request, "Error missing values salary") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/employee_info.html', {'user':user, 'a':a})
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
            return redirect('employee_database', {'user':user})
        except:#None Type
                #Message warning, Employee exists/ID in use
            messages.warning(request, "Empty field/Incorrect inputs detected!" + str(type(last_name)) + str(type(first_name)) + str(type(middle_name)) + str(type(idnumber)) + str(type(status)) + str(type(department)) + str(type([position]))  + str(type(joindate)) + str(type(pnumber)) + str(type(email)) + str(type(banknumber)) + str(type(salary)))
                #Render create employee
            return render(request, 'payrollapp/employee_info.html', {'user':user, 'a':a})
    else:
        a = get_object_or_404(Employee, pk = EID)
        return render(request, 'payrollapp/employee_info.html', {'user':user , 'a':a})

def attendance_db(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/attendance_db.html', {'user':user})

def employee_attendance(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/employee_attendance.html', {'user':user})

def tax_module(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/tax_module.html', {'user':user})

def encode_page(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/encode_page.html', {'user':user})

#GO BACK TO BREAKDOWN AND ENCODE
def payroll_breakdown(request, UID, EID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    EID = get_object_or_404(Employee, id_number=EID)
    payrolls =  get_object_or_404(Payslip_Transaction, Employee_ID=EID)
    if(request.method=="POST"):
        try:
            inputULD = request.POST.get('inputULD')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
        try:
            inputULDT = request.POST.get('inputULDT')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
        try:
            inputCA = request.POST.get('inputCA')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
        try:
            inputCOOP = request.POST.get('inputCOOP')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
        try:
            inputCOLA = request.POST.get('inputCOLA')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
        try:
            inputADDE = request.POST.get('inputADDE')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
        try:
            inputADDET = request.POST.get('inputADDET')
        except:
            messages.warning(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            return render(request, 'payrollapp/payroll_breakdown.html' , {'user':user, 'EID':EID})
    else:
        return render(request, 'payrollapp/payroll_breakdown.html', {'user':user})

def HMO_DB(request, UID):
    a = HMO.objects.all()
    c = Employee.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)


    if (request.method=='POST'):
    #Get the values
        EID = request.POST.get('A_EID')
        A_HMOA = request.POST.get('A_HMOA')
        if a.filter(HMO_ID=EID).exists():#If we selected new item, Create new entry
            HMO.objects.filter(HMO_ID=EID).update(HMO_ID=EID, HMO_Amount=A_HMOA)
        else:#Update path
            HMO.objects.create(HMO_ID=EID, HMO_Amount=A_HMOA)
            messages.success(request, "Updated successfully!")
        return redirect(reverse('HMO_DB', kwargs={'UID': user.id}))#No idea why it works, the mysterious forums solved this one
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/HMO_DB.html',{'user':user, 'a':a, 'c':c} )
        