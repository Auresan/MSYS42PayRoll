from .models import *
from django.shortcuts import  get_object_or_404
from datetime import *
from django.db.models import Sum
#HMO, COOP*, WithTax

#X is the base value we are basing off of
#Y is any need for ID passthrough/Assignment
#Z is for any string passed
def calculateHMO(y):#CLARIFY HERE
    #Retrive all of the tables
    print(y)
    HMO_M = get_object_or_404(HMO, pk = y)
    HMO_M_Amount = HMO_M.HMO_Amount
    
    return HMO_M_Amount
def calculateULD(x,z):
    #Retrive all of the tables
    ULD_E = UNIFORMLAPTOPDEDUCTIONS.objects.last()
    try:
        ULD_E_ID = ULD_E.ULDeductions_ID +1
    except:
        ULD_E_ID = 1
    UNIFORMLAPTOPDEDUCTIONS.objects.create(ULDeductions_ID=ULD_E_ID, Type=z,ULDeductions_Amount=x)
    return x
def calculateCA(x):#DEPENDS IF CA is Used to add to that payslips value or if that's a deduction from last week's CA
    #Retrive all of the tables
    CA_M = CA.objects.last()
    try:
        CA_M_ID = CA_M.CA_ID +1
    except:
        CA_M_ID = 1
    CA.objects.create(CA_ID=CA_M_ID, CA_Amount=x)
    return x
def calculateCOOP(x):#CLARIFY HERE
    #Retrive all of the tables
    COOP_M = COOP.objects.last()
    try:
        COOP_M_ID = COOP_M.COOP_ID +1
    except:
        COOP_M_ID = 1
    COOP.objects.create(COOP_ID=COOP_M_ID, COOP_Amount=x)
    return x
def calculateCOLA(x):
    #Retrive all of the tables
    COLA_M = COLA.objects.last()
    try:
        COLA_M_ID = COLA_M.COLA_ID +1
    except:
        COLA_M_ID = 1
    COLA.objects.create(COLA_ID=COLA_M_ID, COLA_Amount=x)
    return x
def calculateADDE(x,z): #Remember to ADD this
    #Retrive all of the tables
    ADD_E = ADDITIONAL_EARNINGS.objects.last()
    try:
        ADD_E_ID = ADD_E.AddtlEarning_ID +1
    except:
        ADD_E_ID = 1
    ADDITIONAL_EARNINGS.objects.create(AddtlEarning_ID=ADD_E_ID, Type=z,ADD_EARNINGS=x)
    return x
def calculateSSS(x): #SUBTRACT THIS
    #Retrive all of the tables
    sss = SSS.objects.all()

    #compare to all values to find the appropriate range
    for row in sss:
        #We look through all the ranges and if the X is bigger than Start replace the variables; This works since if the start is higher we don't update variables
        #Note: Look into how the rows are indexed, that way we can instead remember the index number and overwrite the variables once to cut down on process time
        if row.Start_Range < x:
            #SSS_ER = row.Regular_SS_Employer_Rate
            SSS_EE = row.Regular_SS_Employee_Rate*x
            SSS_EC = row.EC_Contribution
            #SSS_WISP_ER = row.WISP_Employer_Rate
            SSS_WISP_EE = row.WISP_Employee_Rate
            SSS_RATE_ID = row.SSS_Rate_ID
    #return SSS_ER, SSS_EE, SSS_EC, SSS_WISP_ER, SSS_WISP_EE
    return  SSS_EE, SSS_EC,  SSS_WISP_EE, SSS_RATE_ID
def calculatePH(x):
    #Retrive all of the tables
    PhilHealth_Table = PhilHealth.objects.all()
    #compare to all values to find the appropriate range
    for row in PhilHealth_Table:
        if x > row.Start_Range:
            PH_EE = (x * row.Employee_Rate)/2
            PH_ID = row.PhilHealth_Rate_ID
    return PH_EE, PH_ID
def calculateHDMF(x): #SUBTRACT THIS
    #Retrive all of the tables
    HDMF_Table = HDMF.objects.all()
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
    #compare to all values to find the appropriate range
    for row in WITHTAX:
        if x > row.Start_Range:
            FIXTAX = row.Fix_Tax_Amount
            EXCESS = row.Tax_Rate_On_Excess * (x- row.Start_Range)
            WITH_ID = row.WTAX_Rate_ID
    return FIXTAX, EXCESS,  WITH_ID

def calculateSALARY(employeeID, start, end, ULD_AM, ULD_Type, CA_AM, COOP_AM, COLA_AM,  ADDE_AM, ADDE_TYPE):
    #Get Employee ID
    emp = get_object_or_404(Employee, id_number = employeeID)
    #Get Daily rate
    emp_DR = emp.Salary*2*12/314
    #Get Basic Pay
    emp_BP = emp.Salary/2
    #Get Absences
    total_days = (end - start).days + 1
    existing_records_count = ATTENDANCE_RECORD.objects.filter(
    Date__range=[start, end]).count()
    abse = total_days - existing_records_count
    holidays = HOLIDAY.objects.filter(Date__range=[start, end])
    for holiday in holidays:
        abse -= 1

    #Do all modifiers
    HMO_Amount = calculateHMO(employeeID)
    ULD_Amount = calculateULD(ULD_AM, ULD_Type)
    CA_Amount = calculateCA(CA_AM)
    COOP_Amount = calculateCOOP(COOP_AM)
    COLA_Amount = calculateCOLA(COLA_AM)
    ADDE_Amount = calculateADDE(ADDE_AM, ADDE_TYPE)
    SSS_Amount, SSS_EC, SSS_WISP_Amount, SSS_RATE_ID = calculateSSS(emp.Salary)
    PH_Amount, PH_ID = calculatePH(emp.Salary)
    HDMF_Amount, HDMF_ER, HDMF_EE_R, HDMF_ER_R, HDMF_ID = calculateHDMF(emp.Salary)
    WithTax_Amount, WithTax_Excess,  WITH_ID = calculateWithTax(emp_BP)#FIX THIS
    #lateDues = (emp_DR*((LATEHERE/8)/60))*-1 Currently not in use due to how the office does it(Culmulative time = Absence)
    absenceDues = emp_BP*2*12/314*-abse
    OT = ATTENDANCE_RECORD.objects.filter(Date__range=(start, end)).aggregate(sum=Sum('OT'))['sum']
    if OT == None:
        OT = 0
    OT = emp_DR/8*1.25*OT

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
    #total = emp_BP + HMO_Amount+ ULD_Amount + CA_Amount + COOP_Amount+ COLA_Amount+ ADDE_Amount- SSS_Amount- SSS_EC- SSS_WISP_Amount- PH_Amount - HDMF_Amount - WithTax_Amount - WithTax_Excess- absenceDues + OT
    total = emp_BP + HMO_Amount- float(ULD_Amount) - float(CA_Amount) - float(COOP_Amount)+ float(COLA_Amount)+ float(ADDE_Amount)- float(SSS_Amount)- float(SSS_EC)- float(SSS_WISP_Amount)- float(PH_Amount) - float(HDMF_Amount) - float(WithTax_Amount) - float(WithTax_Excess)+ float(absenceDues) + float(OT)
    print(total)
    return total, absenceDues, SSS_RATE_ID, PH_ID, HDMF_ID,  WITH_ID