from .models import *
from django.shortcuts import  get_object_or_404
from datetime import *
from django.db.models import Sum, Count
#HMO, COOP*, WithTax

#X is the base value we are basing off of
#Y is any need for ID passthrough/Assignment
#Z is for any string passed
def calculateHMO(y):#CLARIFY HERE
    #Retrive all of the tables
    print(y)
    HMO_M = get_object_or_404(HMO, pk = 1)
    HMO_M_Amount = HMO_M.HMO_Amount
    
    return HMO_M_Amount
def calculateULD(x,z):
    #Retrive all of the tables
#    ULD_E = UNIFORMLAPTOPDEDUCTIONS.objects.last()
 #   try:
  #      ULD_E_ID = ULD_E.ULDeductions_ID +1
   # except:
    #    ULD_E_ID = 1
    #UNIFORMLAPTOPDEDUCTIONS.objects.create(ULDeductions_ID=ULD_E_ID, Type=z,ULDeductions_Amount=x)
    UNIFORMLAPTOPDEDUCTIONS.objects.create(Type=z,ULDeductions_Amount=x)
    return x
def calculateCA(x):#DEPENDS IF CA is Used to add to that payslips value or if that's a deduction from last week's CA
    #Retrive all of the tables
#    CA_M = CA.objects.last()
 #   try:
  #      CA_M_ID = CA_M.CA_ID +1
   # except:
    #    CA_M_ID = 1
    #CA.objects.create(CA_ID=CA_M_ID, CA_Amount=x)
    CA.objects.create(CA_Amount=x)
    return x
def calculateCOOP(x):
    #Retrive all of the tables
#    COOP_M = COOP.objects.last()
 #   try:
  #      COOP_M_ID = COOP_M.COOP_ID +1
   # except:
    #    COOP_M_ID = 1
    #COOP.objects.create(COOP_ID=COOP_M_ID, COOP_Amount=x)
    COOP.objects.create(COOP_Amount=x)
    return x
def calculateCOLA(x):
    #Retrive all of the tables
#    COLA_M = COLA.objects.last()
 #   try:
  #      COLA_M_ID = COLA_M.COLA_ID +1
   # except:
    #    COLA_M_ID = 1
    #COLA.objects.create(COLA_ID=COLA_M_ID, COLA_Amount=x)
    COLA.objects.create(COLA_Amount=x)
    return x
def calculateADDE(x,z): #Remember to ADD this
    #Retrive all of the tables
#    ADD_E = ADDITIONAL_EARNINGS.objects.last()
 #   try:
  #      ADD_E_ID = ADD_E.AddtlEarning_ID +1
   # except:
    #    ADD_E_ID = 1
    #ADDITIONAL_EARNINGS.objects.create(AddtlEarning_ID=ADD_E_ID, Type=z,ADD_EARNINGS=x)
    ADDITIONAL_EARNINGS.objects.create(Type=z,ADD_EARNINGS=x)
    return x
def calculateSSS(x): #SUBTRACT THIS
    #Retrive all of the tables
    sss = SSS.objects.all()
    SSS_EE =0 
    SSS_EC=0
    SSS_WISP_EE=0
    SSS_RATE_ID=0

    #compare to all values to find the appropriate range
    for row in sss:
        #We look through all the ranges and if the X is bigger than Start replace the variables; This works since if the start is higher we don't update variables
        #Note: Look into how the rows are indexed, that way we can instead remember the index number and overwrite the variables once to cut down on process time
        if row.Start_Range < x:
            #SSS_ER = row.Regular_SS_Employer_Rate
            SSS_EE = row.Regular_SS_Employee_Rate
            SSS_EC = row.EC_Contribution
            #SSS_WISP_ER = row.WISP_Employer_Rate
            SSS_WISP_EE = row.WISP_Employee_Rate
            SSS_RATE_ID = row.SSS_Rate_ID
    #return SSS_ER, SSS_EE, SSS_EC, SSS_WISP_ER, SSS_WISP_EE
    return  SSS_EE, SSS_EC,  SSS_WISP_EE, SSS_RATE_ID
def calculatePH(x):
    #Retrive all of the tables
    PhilHealth_Table = PhilHealth.objects.all()
    PH_EE =0 
    PH_ID=0
    #compare to all values to find the appropriate range
    for row in PhilHealth_Table:
        if x > row.Start_Range:
            PH_EE = (x * row.Employee_Rate)/2
            PH_ID = row.PhilHealth_Rate_ID
    return PH_EE, PH_ID
def calculateHDMF(x): #SUBTRACT THIS
    #Retrive all of the tables
    HDMF_Table = HDMF.objects.all()
    HDMF_EE_R = 0
    HDMF_ER_R = 0
    HDMF_EE = 0
    HDMF_ER = 0
    HDMF_ID = 0
    #compare to all values to find the appropriate range
    for row in HDMF_Table:
        if x > row.Start_Range:
            HDMF_EE_R = row.Employee_Rate
            HDMF_ER_R = row.Employer_Rate
            HDMF_EE = x * row.Employee_Rate
            HDMF_ER = x * row.Employer_Rate
            HDMF_ID = row.HDMF_Rate_ID
    return HDMF_EE, HDMF_ER, HDMF_EE_R, HDMF_ER_R, HDMF_ID
def calculateWithTax(x): #ASK FOR ASSISTANCE HERE
    #Retrive all of the tables
    WITHTAX = WitholdingTax.objects.all()
    FIXTAX = 0
    EXCESS = 0
    WITH_ID = 0
    #compare to all values to find the appropriate range
    for row in WITHTAX:
        if x > row.Start_Range:
            FIXTAX = row.Fix_Tax_Amount
            EXCESS = row.Tax_Rate_On_Excess * (x- row.Start_Range)
            WITH_ID = row.WTAX_Rate_ID
    return FIXTAX, EXCESS,  WITH_ID


def calculateSALARY(employeeID, start, end, ULD_AM, ULD_Type, CA_AM, COOP_AM, COLA_AM,  ADDE_AM, ADDE_TYPE):
    abse = 0
    total_OT = 0
    total_days = 0
    total_NH = 0
    






    date_range = [start + timedelta(days=x) for x in range((end - start).days + 1)]

    #Get Employee ID
    emp = get_object_or_404(Employee, id_number = employeeID)
    #Get Daily rate
    emp_DR = emp.Salary*2*12/314
    #Get Basic Pay
    emp_BP = emp.Salary/2
    #Get Absences 10BIT:Remove the ='' if it doesn't work probs
    #print(date_range)

    total_days = (end - start).days + 1
    #

    try:
        print(type(date_range))
        print(type(start))
        noShow_records_count = ATTENDANCE_HISTORY.objects.filter(Employee_ID=emp, Date__in=date_range,TimeIn__isnull=True,TimeOut__isnull=True, TimeIn_2__isnull=True, TimeOut_2__isnull=True).count()
    except:
        print('Wumpus WOMP')
        noShow_records_count = ATTENDANCE_HISTORY.objects.filter(Employee_ID=emp, Date__range=(start, end),TimeIn__isnull=True,TimeOut__isnull=True, TimeIn_2__isnull=True, TimeOut_2__isnull=True).exclude(Date__week_day=7).count()
    abse = noShow_records_count#Gets the amount of times they didn't show
    
    
    total_hours = ATTENDANCE_HISTORY.objects.filter(Employee_ID=emp, Date__range=(start, end))
    print(total_hours)
    for o in total_hours:
        print(o.Date)
        print(end)
        print(o.Date == end)
    try:
        total_hours_worked = total_hours.aggregate(HoursWorked=Sum('HoursWorked'))['HoursWorked']
    except:
        print('WOMP WOMP')
    total_OT = total_hours.aggregate(OT=Sum('OT'))['OT']
    total_NH = total_hours.aggregate(NightShift=Sum('NightShift'))['NightShift']

    #Resolve Absences
    holidays = HOLIDAY.objects.filter(Date__range=(start, end))
    for holiday in holidays:
        abse -= 1
        total_days = total_days - 1
    leaves = Leave.objects.filter(Start_Date__range=(start, end), Employee_ID=emp)
    for leave in leaves:
        abse -= 1
        total_days = total_days - 1
    sd = start  
    edd = end
    wekend_c = 0
    while sd <= edd:
        if sd.weekday() in (5, 6):
            wekend_c += 1
        sd += timedelta(days=1)
    total_days = total_days - (wekend_c / 4)
    


    #Total Hours needed:
    totalHours_needed = total_days * 8
    totalHours_needed = (totalHours_needed - (total_hours_worked)) * 60 #Get how much wasn't done then convert to minutes for late
    if totalHours_needed > 0 and totalHours_needed< total_OT:
        total_OT -= totalHours_needed
        totalHours_needed = 0


    #Holiday Pay for emergency calls(ADD TO THE END ANOTHER CALC WITH 2x BASIC COLA)
    holidayWork = ATTENDANCE_HISTORY.objects.filter(Employee_ID=emp, Date__range=(start, end), Holiday_ID__isnull=False)
    holidayWork_n = holidayWork.filter(Holiday_ID__Type='NORMAL')#unsure if this will work
    holidayWork_s = holidayWork.filter(Holiday_ID__Type='SPECIAL')#unsure if this will work
    holidayHours = holidayWork_n.aggregate(HoursWorked=Sum('HoursWorked'))['HoursWorked']# 10BIT We will assume no OT is allowed on holidays please lang
    holidayHours_s = holidayWork_s.aggregate(HoursWorked=Sum('HoursWorked'))['HoursWorked']

    if holidayHours is None:
        holidayHours = 0
    if holidayHours_s is None:
        holidayHours_s = 0
    #holidayHours = holidayWork_n.aggregate(total_amount=Sum('total_amount'))['total_amount']
    #holidayHours_s = holidayWork_s.aggregate(total_amount=Sum('total_amount'))['total_amount']
    #Do all modifiers
    #ATTENDANCE_HISTORY.objects.filter=()

    HMO_Amount = calculateHMO(employeeID)
    ULD_Amount = calculateULD(float(ULD_AM), ULD_Type)
    CA_Amount = calculateCA(float(CA_AM))
    COOP_Amount = calculateCOOP(float(COOP_AM))
    COLA_Amount = calculateCOLA(float(COLA_AM))
    ADDE_Amount = calculateADDE(float(ADDE_AM), ADDE_TYPE)
    SSS_Amount, SSS_EC, SSS_WISP_Amount, SSS_RATE_ID = calculateSSS(emp.Salary)
    PH_Amount, PH_ID = calculatePH(emp.Salary)
    HDMF_Amount, HDMF_ER, HDMF_EE_R, HDMF_ER_R, HDMF_ID = calculateHDMF(emp.Salary)
    print(SSS_Amount)
    SSS_Amount =  float(SSS_Amount)+ float(SSS_EC)+ float(SSS_WISP_Amount)
    print('BAU BAU')
    print(SSS_Amount)
    print(SSS_EC)
    print(SSS_WISP_Amount)
    
    current_date = datetime.now()

    # Set the day to 17
    end_check = current_date.replace(day=27).date()
    start_check = current_date.replace(day=23).date()

    cycle2 = [start_check + timedelta(days=x) for x in range((end_check - start_check).days + 1)]

    if end in cycle2:
        SSS_Amount = 0
    else:
        HDMF_Amount = 0
        PH_Amount = 0


    lateDues = (emp_DR*((totalHours_needed/8)/60))*-1 #LATEHERE is replaced with minutes late
    absenceDues = emp_BP*2*12/314*-abse
    NightIncrease = emp_DR*1.25*1.1*total_NH
    OT = emp_DR/8*1.25*total_OT
    holidayPay = emp_DR/8*2*holidayHours
    holidayPay_s = emp_DR+(.3*emp_DR)/8*holidayHours_s
    #Compute BP+Holi+OT+NS -SSS-PH-HDMF
    GroTaxInc = emp_BP + holidayPay + holidayPay_s + OT + NightIncrease #https://www.eezi.com/withholding-taxes-in-the-philippines-everyones-responsibility/
    Tot_Ded_1 = SSS_Amount + HDMF_Amount + PH_Amount - absenceDues - lateDues
    taxInc= GroTaxInc-Tot_Ded_1
    WithTax_Amount, WithTax_Excess,  WITH_ID = calculateWithTax(taxInc)#FIX THIS
    WithTax_Amount = float(WithTax_Amount) + float(WithTax_Excess)
    tot_ded_2 = ULD_Amount + CA_Amount + COOP_Amount + HMO_Amount + WithTax_Amount
    tot_cred = COLA_Amount + ADDE_Amount
    total = taxInc - tot_ded_2 + tot_cred
    
    Holiday_Comp = float( holidayPay + holidayPay_s )
    print('START')
    print(emp_BP)
    print(HMO_Amount)
    print(ULD_Amount)
    print(CA_Amount)
    print(COOP_Amount)
    print(COLA_Amount)
    print(ADDE_Amount)
    print(SSS_Amount)
    print(SSS_EC)
    print(SSS_WISP_Amount)
    print(PH_Amount)
    print(HDMF_Amount)
    print(WithTax_Amount)
    print(WithTax_Excess)
    print(absenceDues)
    print(OT)
    print('END')
    #total = emp_BP + HMO_Amount+ ULD_Amount + CA_Amount + COOP_Amount+ COLA_Amount+ ADDE_Amount- SSS_Amount- SSS_EC- SSS_WISP_Amount- PH_Amount - HDMF_Amount - WithTax_Amount - WithTax_Excess- absenceDues + OT + (DR+COLA)*holiday
    total = round(total, 2)
    absenceDues = round(absenceDues, 2)
    SSS_Amount= round(SSS_Amount, 2)
    PH_Amount= round(PH_Amount, 2)
    HDMF_Amount= round(HDMF_Amount, 2)
    WithTax_Amount= round(WithTax_Amount, 2)
    OT= round(OT, 2)
    NightIncrease= round(NightIncrease, 2)
    Holiday_Comp= round(Holiday_Comp, 2)
    

    Total_Deductions = Tot_Ded_1 + tot_ded_2
    
    return total, absenceDues, SSS_Amount, PH_Amount, HDMF_Amount,  WithTax_Amount, OT, NightIncrease ,Holiday_Comp, Total_Deductions
