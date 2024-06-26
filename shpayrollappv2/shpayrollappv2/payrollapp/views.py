from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *
from django.contrib import messages
from django.utils import timezone
from datetime import *
from .taxEmployee_salary import *
from .ModifierDBchanges import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import FileResponse


#'%d/%m/%Y
#"%Y-%m-%d"
# Create your views here.

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

def reset_pw(request):
    return render(request, 'payrollapp/reset_pw.html')



def dashboard(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    a = BANK_FILES.objects.all()
    count_emp=Employee.objects.all().count()
    count_payrolls=Payslip_Transaction.objects.all().count()
    current_hmo=HMO.objects.all().filter().count()
    count_hmo=count_emp-current_hmo
    current_date = datetime.now()
    if current_date.day < 10:
        target_date = datetime(current_date.year, current_date.month, 10)
    else:
        if current_date.month == 12:  # Handle December case
            target_date = datetime(current_date.year + 1, 1, 10)
        else:
            target_date = datetime(current_date.year, current_date.month + 1, 10)
    countdown = (target_date-current_date)
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Format into a string
    formatted_str = f"{days} days, {hours} hours, {minutes} minutes" 
    print(type(formatted_str))
    print((formatted_str))
    return render(request, 'payrollapp/dashboard.html',{
        'user':user,
        'count_emp':count_emp,
        'count_payrolls':count_payrolls,
        'count_hmo':count_hmo,
        'countdown':formatted_str,
        'a':a
        } )

##@login_required
def employee_database(request, UID):
    a = Employee.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/employee_database.html', {'user':user, 'a':a})

##@login_required
def add_employee(request, UID):
    #If form is submitted
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    a = Department.objects.all()
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
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            first_name = request.POST.get('inputFstName')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            middle_name = request.POST.get('inputMidName')
        except:
            pass
        
        
        try:
            idnumber = first_name[0].upper() + middle_name[0].upper() + last_name[0].upper()
        except:
            idnumber = first_name[0].upper() +'_' + last_name[0].upper()
        id_no = id_no.zfill(3)
        idnumber = idnumber + id_no

        #In the rare chance we've have 999 employees total with the same starting first middle and last names
        emergency = 0
        if Employee.objects.filter(id_number=idnumber).exists():
            while Employee.objects.filter(id_number=idnumber).exists() or emergency<999:
                emergency +=1
                idnumber = idnumber[:3]
                print(id_no)
                id_no = int(id_no)
                if id_no == 999:
                    id_no = 0
                id_no += 1
                id_no = str(id_no)
                id_no = id_no.zfill(3)
                idnumber = idnumber + id_no
                print(idnumber)
            if emergency == 999:
                messages.error(request, "ERROR, 999 employee records hold the same starting letters and number. Please contact IT to upgrade") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
                path = '/add_employee/' + str(user.pk)
                return redirect(path)


        try:
            pnumber = str(request.POST.get('inputPhone'))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            email = str(request.POST.get('inputEmail4'))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        
        
        try:
            department  = str(request.POST.get('inputDept'))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            status  = str(request.POST.get('inputEmpStat'))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            position = str(request.POST.get('inputPosition'))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            joindate = request.POST.get('inputJoinDate')
            #messages.success(request, str(joindate))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        
        
        
        try:
            # Convert the date string to a datetime object
            joindate = datetime.strptime(joindate, "%Y-%m-%d").date()
        
        except ValueError:
            # Handle the case where the date string is not in the correct format
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            path = '/add_employee/' + str(user.pk)
            return redirect(path)


        try:
            banknumber = request.POST.get('inputBankAccNo')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        try:
            salary = float(request.POST.get('inputSalary'))
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/add_employee/' + str(user.pk)
            return redirect(path)

        

        
        
        
        
        


        #Check if employee exists or if the ID is in use(This can be an and if you want to allow same name employees but different IDs but RAW its name or ID)
        if Employee.objects.filter(Last_name=last_name, 
                                        First_name=first_name, 
                                        Middle_name=middle_name ).exists():
            #Message warning, Employee exists/ID in use
            messages.error(request, "Employee/ID Number Already Exists!")
            #Render create employee
            path = '/add_employee/' + str(user.pk)
            return redirect(path)
        else:
            try:
                if status == 'Probationary':
                    vl = 0
                    sl = 0
                else:
                    vl = 15
                    sl = 15
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
                                        Salary=salary,
                                        Vacation_Leaves=vl,
                                        Sick_Leaves=sl)
                messages.success(request, "Employee created successfully!")
                path = '/add_employee/' + str(user.pk)
                return redirect(path)
            except:#None Type
                #Message warning, Employee exists/ID in use
                messages.error(request, "Empty field/Incorrect inputs detected!")
                #Render create employee
                path = '/add_employee/' + str(user.pk)
            return redirect(path)
    else:
        return render(request, 'payrollapp/add_employee.html', {'user':user, 'a':a})

def generate_page(request, UID):
    a = Employee.objects.all()
    payslip=Payslip_Transaction.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    if (request.method == "POST"):
        #Get the department type
        try:
        #    department  = request.POST.get('inputDept')
            employee = request.POST.get('inputID')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        #Get Start Date
        try:
            start  = request.POST.get('inputStartDate')
            try:
            # Convert the date string to a datetime object
                start = datetime.strptime(start, "%Y-%m-%d").date()
        
            except ValueError:
            # Handle the case where the date string is not in the correct format
                messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
                path = '/generate_page/' + str(user.pk)
                return redirect(path)
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        #Get End Date
        try:
            end  = request.POST.get('inputEndDate')
            try:
            # Convert the date string to a datetime object
                end = datetime.strptime(end, "%Y-%m-%d").date()
        
            except ValueError:
            # Handle the case where the date string is not in the correct format
                messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
                path = '/generate_page/' + str(user.pk)
                return redirect(path)
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        
        #Tax inputs

        try:
        #    department  = request.POST.get('inputDept')
            ULD_AM = request.POST.get('inputULD')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        try:
        #    department  = request.POST.get('inputDept')
            ULD_T = request.POST.get('inputULDT')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        try:
        #    department  = request.POST.get('inputDept')
            CA_AM = request.POST.get('inputCA')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        try:
        #    department  = request.POST.get('inputDept')
            COOP_AM = request.POST.get('inputCOOP')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        try:
        #    department  = request.POST.get('inputDept')
            COLA_AM = request.POST.get('inputCOLA')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        try:
        #    department  = request.POST.get('inputDept')
            ADDE_AM = request.POST.get('inputADDE')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        try:
        #    department  = request.POST.get('inputDept')
            ADDE_T = request.POST.get('inputADDET')
        except:
            messages.error(request, "Error missing values") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        #Get all
        #employee_list = Employee.objects.filter(Department=department)
        #Run the calculation for values
        #for x in employee_list:
        #    calculateSALARY(x.id_number)
        emp = get_object_or_404(Employee, id_number = employee)
        total_hours = ATTENDANCE_HISTORY.objects.filter(Employee_ID=emp, Date__range=(start, end))
        if not total_hours.exists():
            messages.error(request, "Warning: No History records found for employee during payroll period")
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        HMO_EXIST = HMO.objects.all()
        if not HMO_EXIST.exists():
            messages.error(request, "Warning: No HMO in System")
            path = '/generate_page/' + str(user.pk)
            return redirect(path)
        else:
            pass
        total, absenceDues, SSS_RATE_ID, PH_ID, HDMF_ID,  WITH_ID, OT, NightIncrease , Holiday_Comp, Total_Deductions = calculateSALARY(employee, start, end, ULD_AM, ULD_T, CA_AM, COOP_AM, COLA_AM, ADDE_AM, ADDE_T)
#        try:
 #           LatestPayslip = Payslip_Transaction.objects.last()
  #          PayslipID = LatestPayslip.Transaction_ID+ 1
   #     except:
    #        PayslipID = 1
        
        try:
            if Payslip_Transaction.objects.filter(Employee_ID=emp, End_Date=end).exists():
                print('error already exists')
                messages.error(request, "Error: Already Exists")

            else:
                xyz = get_object_or_404(HMO, pk=1)
                Payslip_Transaction.objects.create(
                Date_Distributed = datetime.now().date(),
                Start_Date = start,
                End_Date = end,
                Net_Pay = total,
                Total_Deductions= Total_Deductions,
                Absence_Deductions = absenceDues,
                OT= OT,
                NightShift = NightIncrease,
                Holiday_Comp = Holiday_Comp,
                Employee_ID = get_object_or_404(Employee, pk=employee),
                SSS_Rate_ID = SSS_RATE_ID,
                PhilHealth_Rate_ID = PH_ID,
                HDMF_Rate_ID = HDMF_ID,
                WTAX_Rate_ID = WITH_ID,
                HMO_Rate_ID = xyz.HMO_Amount,
                ULDeductions_Rate_ID = UNIFORMLAPTOPDEDUCTIONS.objects.last(),
                CA_Rate_ID = CA.objects.last(),
                COOP_Rate_ID = COOP.objects.last(),
                COLA_Rate_ID = COLA.objects.last(),
                AddtlEarning_Rate_ID = ADDITIONAL_EARNINGS.objects.last()
                )
                messages.success(request, "Payroll successfully generated!")

        except:
            print("Soemthing fked up")
        path = '/generate_page/' + str(user.pk)
        return redirect(path)
    else:
        return render(request, 'payrollapp/generate_page.html' , {'user':user,'a':a, 'payslip':payslip})

##@login_required
def employee_info(request, UID, EID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    b = Department.objects.all()

    if(request.method=="POST"):
        a = get_object_or_404(Employee, pk = EID)
        try:
            last_name  = request.POST.get('inputLtName')
        except:
            messages.error(request, "Error missing values Last Name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            first_name = request.POST.get('inputFstName')
        except:
            messages.error(request, "Error missing values first_name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            middle_name = request.POST.get('inputMidName')
        except:
            messages.error(request, "Error missing values middle_name") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:#Need to fix in case of changing name if the ID will change as well
            idnumber = request.POST.get('inputID')
        except:
            messages.error(request, "Error missing values idnumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            pnumber = str(request.POST.get('inputPhone'))
        except:
            messages.error(request, "Error missing values pnumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            email = str(request.POST.get('inputEmail4'))
        except:
            messages.error(request, "Error missing values email") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        
        try:
            department  = str(request.POST.get('inputDept'))
        except:
            messages.error(request, "Error missing values department") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            status  = str(request.POST.get('inputEmpStat'))
        except:
            messages.error(request, "Error missing values status") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            position = str(request.POST.get('inputPosition'))
        except:
            messages.error(request, "Error missing values position") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            joindate = request.POST.get('inputJoinDate')
            print(type(joindate))
            print(joindate)
        except:
            messages.error(request, "Error missing values joindate") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            # Convert the date string to a datetime object
            joindate = datetime.strptime(joindate, "%Y-%m-%d").date()
        except ValueError:
            # Handle the case where the date string is not in the correct format
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD. " + joindate)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            banknumber = request.POST.get('inputBankAccNo')
        except:
            messages.error(request, "Error missing values banknumber") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        try:
            salary = float(request.POST.get('inputSalary'))
        except:
            messages.error(request, "Error missing values salary") #VERY NIECHE EDGE CASE(I took a look and the chances are incredibly slim but if in a miracle the company lasts THAT long, reallistically we should have migrated or upgraded but error code just in case)
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
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
                                        Phone_Number=pnumber, 
                                        Email=email, 
                                        BankNumber=banknumber, 
                                        Salary=salary)
            messages.success(request, "Employee updated successfully!")
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
        except:#None Type
                #Message warning, Employee exists/ID in use
            messages.error(request, "Empty field/Incorrect inputs detected!" + str(type(last_name)) + str(type(first_name)) + str(type(middle_name)) + str(type(idnumber)) + str(type(status)) + str(type(department)) + str(type([position]))  + str(type(joindate)) + str(type(pnumber)) + str(type(email)) + str(type(banknumber)) + str(type(salary)))
                #Render create employee
            path = '/employee_info/' + str(user.pk)
            return redirect(path)
    else:
        a = get_object_or_404(Employee, pk = EID)
        return render(request, 'payrollapp/employee_info.html', {'user':user , 'a':a, 'b':b})

##@login_required
def attendance_db(request, UID):
    a =  Employee.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    b = ATTENDANCE_HISTORY.objects.values('Employee_ID').annotate(OT__sum=Sum('OT'), HoursWorked=Sum('HoursWorked'), leaves_left=15-Count('Leave_ID'))


    return render(request, 'payrollapp/attendance_db.html', {'user':user, 'a':a, 'b':b})

##@login_required
def employee_attendance(request, UID, EID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    a = get_object_or_404(Employee, pk=EID)
    attendance_record = ATTENDANCE_HISTORY.objects.filter(Employee_ID=a).order_by('-Date').values()

    if(request.method=="POST"):
        Over_hrs = request.POST.get('empOT')
        Night_hrs = request.POST.get('empNightShft')
        Attendance_entry = request.POST.get('entryid')
        Attendance_entry=get_object_or_404(ATTENDANCE_HISTORY, History_ID=Attendance_entry)
        Attendance_entry.OT=Over_hrs
        Attendance_entry.NightShift=Night_hrs
        Attendance_entry.save()
        
        messages.success(request, "Employee attendance updated successfully!")
        path = '/employee_attendance/' + str(user.pk)
        return redirect(path)
    
    return render(request, 'payrollapp/employee_attendance.html', {'user':user, 'a':a, 'attendance_record':attendance_record})

def tax_module(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    return render(request, 'payrollapp/tax_module.html', {'user':user})

def encode_page(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    z = Payslip_Transaction.objects.values_list('End_Date', flat=True).distinct()
    a = BANK_FILES.objects.all()
    if (request.method == "POST"):
        #companyaccountnumber = 1234567890
        #companycode="WT9"
        current_date = datetime.now()
        current_date = current_date.strftime('%Y%m%d')
        try:
            inputDate = request.POST.get('inputDate')
            IDD = inputDate
            inputDate = datetime.strptime(inputDate, '%Y%m%d')
            #messages.success(request, str(joindate))
        except:
            pass
        payslip_match = Payslip_Transaction.objects.filter(End_Date=inputDate)
        current_date = datetime.now()#It broke so this is being redone again
        formatted_date = current_date.strftime("%Y%m%d")
        filename = 'EX' + formatted_date + ".txt"
        startDate = 0
        if BANK_FILES.objects.filter(BANK_FILE_NAME=filename).exists():
            with open(filename, 'w') as file:
                for x in payslip_match:
                    startDate = x.Start_Date
                    if x.Employee_ID.BankNumber != 000000000000:
                        file.write(str(x.Employee_ID.BankNumber) +"\t" + str(x.Net_Pay)+'\n')
                    else:
                        file.write(str(x.Employee_ID.BankNumber) +"\t" + str(x.Net_Pay)+' TO BE MANUALLY ADDED \n')
                startDate = startDate.strftime("%Y-%m-%d")
                period = startDate + '-'+IDD
                current_date = datetime.now().date()
                existingFile = BANK_FILES.objects.filter(BANK_FILE_NAME=filename, BANK_FILE=filename ,PAYROLL_PERIOD=period, Date=current_date)
                existingFile.update(BANK_FILE_NAME=filename, BANK_FILE=filename ,PAYROLL_PERIOD=period)
                messages.success(request, "Bank File Successfully Encoded!")
        else:
            with open(filename, 'w') as file:
                for x in payslip_match:
                    startDate = x.Start_Date
                    print(x.Employee_ID.BankNumber)
                    print(type(x.Employee_ID.BankNumber))
                    if x.Employee_ID.BankNumber != '000000000000':
                        file.write(str(x.Employee_ID.BankNumber) +"\t" + str(x.Net_Pay)+'\n')
                    else:
                        file.write(str(x.Employee_ID.BankNumber) +"\t" + str(x.Net_Pay)+' TO BE MANUALLY ADDED \n')
                startDate = startDate.strftime("%Y-%m-%d")
                period = startDate + '-'+IDD
                current_date = datetime.now().date()
                BANK_FILES.objects.create(BANK_FILE_NAME=filename, BANK_FILE=filename ,PAYROLL_PERIOD=period, Date=current_date)
                messages.success(request, "Bank File Successfully Encoded!")

        path = '/encode_page/' + str(user.pk)
        return redirect(path)
    else:
        return render(request, 'payrollapp/encode_page.html', {'user':user, 'a':a, 'z':z})

#GO BACK TO BREAKDOWN AND ENCODE
##@login_required
def payroll_breakdown(request, UID, TID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    #EID = get_object_or_404(Employee, id_number=EID)
    payrolls =  get_object_or_404(Payslip_Transaction, Transaction_ID=TID)#Swap to Payroll ID later
    employee = payrolls.Employee_ID
    name = employee.Last_name+', '+employee.First_name+' '+employee.Middle_name
    start = payrolls.Start_Date.strftime('%Y-%m-%d')
    end = payrolls.End_Date.strftime('%Y-%m-%d')
    if(request.method=="POST"):
        uld = float(request.POST.get('uld'))
        ca = float(request.POST.get('ca'))
        coop = float(request.POST.get('coop'))
        cola = float(request.POST.get('cola'))
        adde = float(request.POST.get('adde'))
        payrolls.Total_Deductions = payrolls.Total_Deductions - payrolls.ULDeductions_Rate_ID.ULDeductions_Amount - payrolls.CA_Rate_ID.CA_Amount - payrolls.COOP_Rate_ID.COOP_Amount 
        payrolls.Net_Pay = payrolls.Net_Pay + payrolls.ULDeductions_Rate_ID.ULDeductions_Amount + payrolls.CA_Rate_ID.CA_Amount + payrolls.COOP_Rate_ID.COOP_Amount - payrolls.COLA_Rate_ID.COLA_Amount - payrolls.AddtlEarning_Rate_ID.ADD_EARNINGS

        ULD_E = get_object_or_404(UNIFORMLAPTOPDEDUCTIONS, ULDeductions_ID=payrolls.ULDeductions_Rate_ID.getID())
        ULD_E.ULDeductions_Amount = uld
        ULD_E.save()

        CA_E = get_object_or_404(CA, CA_ID=payrolls.CA_Rate_ID.getID())
        CA_E.CA_Amount = ca
        CA_E.save()

        COOP_E = get_object_or_404(COOP, COOP_ID=payrolls.COOP_Rate_ID.getID())
        COOP_E.COOP_Amount = coop
        COOP_E.save()

        COLA_E = get_object_or_404(COLA, COLA_ID=payrolls.COLA_Rate_ID.getID())
        COLA_E.COLA_Amount = cola
        COLA_E.save()

        ADDITIONAL_EARNINGS_E = get_object_or_404(ADDITIONAL_EARNINGS, AddtlEarning_ID=payrolls.AddtlEarning_Rate_ID.getID())
        ADDITIONAL_EARNINGS_E.ADD_EARNINGS = adde
        ADDITIONAL_EARNINGS_E.save()
        
        payrolls.ULDeductions_Rate_ID.ULDeductions_Amount = uld
        payrolls.CA_Rate_ID.CA_Amount = ca
        payrolls.COOP_Rate_ID.COOP_Amount = coop
        payrolls.COLA_Rate_ID.COLA_Amount = cola
        payrolls.AddtlEarning_Rate_ID.ADD_EARNINGS = adde
        payrolls.Total_Deductions = payrolls.Total_Deductions + payrolls.ULDeductions_Rate_ID.ULDeductions_Amount + payrolls.CA_Rate_ID.CA_Amount + payrolls.COOP_Rate_ID.COOP_Amount
        payrolls.Net_Pay = payrolls.Net_Pay - payrolls.ULDeductions_Rate_ID.ULDeductions_Amount - payrolls.CA_Rate_ID.CA_Amount - payrolls.COOP_Rate_ID.COOP_Amount + payrolls.COLA_Rate_ID.COLA_Amount + payrolls.AddtlEarning_Rate_ID.ADD_EARNINGS 
        try: 
            payrolls.save()
        except:
            print('fail')
        path = '/payroll_breakdown/' + str(user.pk) + '/' + str(payrolls.Transaction_ID)
        return redirect(path)




    return render(request, 'payrollapp/payroll_breakdown.html', {'user':user , 'payrolls':payrolls, 'name':name, 'start':start, 'end':end})

#@login_required
def HMO_DB(request, UID):
    a = HMO.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)


    if (request.method=='POST'):
    #Get the values
        A_HMOA = request.POST.get('A_HMOA')
        if a.filter(HMO_ID=1).exists():#If we selected new item, Create new entry
            HMO.objects.filter(HMO_ID=1).update(HMO_Amount=A_HMOA)
            messages.success(request, "Updated successfully!")
        else:#Update path
            HMO.objects.create(HMO_Amount=A_HMOA)
            messages.success(request, "Updated successfully!")
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/tax_module.html', {'user':user})

def payslip(request, UID, TID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    payrolls =  get_object_or_404(Payslip_Transaction, Transaction_ID=TID)#Swap to Payroll ID later
    employee = payrolls.Employee_ID
    name = employee.Last_name+', '+employee.First_name+' '+employee.Middle_name
    start = payrolls.Start_Date.strftime('%Y-%m-%d')
    end = payrolls.End_Date.strftime('%Y-%m-%d')

    return render(request, 'payrollapp/payslip.html', {'user':user, 'payrolls':payrolls, 'name':name, 'start':start, 'end':end})


def settings(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    a = Department.objects.all()
    current_month = datetime.now().month
    return render(request, 'payrollapp/settings.html', {'user':user, 'a':a, 'current_month':current_month})

def download_file(request, file_id):
    file_instance = get_object_or_404(BANK_FILES, BANK_FILE_NAME=file_id)
    file_path = file_instance.BANK_FILE.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)