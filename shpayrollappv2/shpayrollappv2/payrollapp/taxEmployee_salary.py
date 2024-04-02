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
    HMO_M = get_object_or_404(HMO, HMO_ID = y)
    HMO_M_Amount = HMO_M.HMO_Amount
    return HMO_M_Amount
def calculateULD(x,z):
    #Retrive all of the tables
    ULD_E = UNIFORMLAPTOPDEDUCTIONS.objects.last()
    ULD_E_ID = ULD_E.AddtlEarning_ID +1
    UNIFORMLAPTOPDEDUCTIONS.objects.create(ULDeductions_ID=ULD_E_ID, Type=z,Amount=x)
    return x
def calculateCA(x):#DEPENDS IF CA is Used to add to that payslips value or if that's a deduction from last week's CA
    #Retrive all of the tables
    CA_M = COLA.objects.last()
    CA_M_ID = CA_M.AddtlEarning_ID +1
    CA.objects.create(CA_ID=CA_M_ID, CA_Amount=x)
    return x
def calculateCOOP(x):#CLARIFY HERE
    #Retrive all of the tables
    COOP_M = COOP.objects.last()
    COOP_M_ID = COOP_M.AddtlEarning_ID +1
    COOP.objects.create(COOP_M=COOP_M_ID, COOP_Amount=x)
    return x
def calculateCOLA(x):
    #Retrive all of the tables
    COLA_M = COLA.objects.last()
    COLA_M_ID = COLA_M.AddtlEarning_ID +1
    COLA.objects.create(COLA_ID=COLA_M_ID, COLA_Amount=x)
    return x
def calculateADDE(x,z): #Remember to ADD this
    #Retrive all of the tables
    ADD_E = ADDITIONAL_EARNINGS.objects.last()
    ADD_E_ID = ADD_E.AddtlEarning_ID +1
    ADDITIONAL_EARNINGS.objects.create(AddtlEarning_ID=ADD_E_ID, Type=z,Amount=x)
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
            SSS_EE = row.Regular_SS_Employer_Rate
            SSS_EC = row.EC_Contribution
            #SSS_WISP_ER = row.WISP_Employer_Rate
            SSS_WISP_EE = row.WISP_Employee_Rate
    #return SSS_ER, SSS_EE, SSS_EC, SSS_WISP_ER, SSS_WISP_EE
    return  SSS_EE, SSS_EC,  SSS_WISP_EE
def calculatePH(x):
    #Retrive all of the tables
    PhilHealth_Table = PhilHealth.objects.all()
    #compare to all values to find the appropriate range
    for row in PhilHealth_Table:
        if x > row.Start_Range:
            PH_EE = (x * row.Employee_Rate)/2
    return PH_EE
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
    return HDMF_EE, HDMF_ER, HDMF_EE_R, HDMF_ER_R
def calculateWithTax(x): #ASK FOR ASSISTANCE HERE
    #Retrive all of the tables
    WITHTAX = WitholdingTax.objects.all()
    #compare to all values to find the appropriate range
    for row in WITHTAX:
        if x > row.Start_Range:
            FIXTAX = row.Fix_Tax_Amount
            EXCESS = row.Tax_Rate_On_Excess * x
    return FIXTAX, EXCESS

def calculateSALARY(employeeID, ULD_AM, ULD_Type, CA_AM, COOP_AM, COLA_AM,  ADDE_AM, ADDE_TYPE, WITHTAX_AM):
    #Get Employee ID
    emp = get_object_or_404(Employee, id_number = employeeID)
    #Get Daily rate
    emp_DR = emp.Salary*2*12/314
    #Get Basic Pay
    emp_BP = emp.Salary/2
    #Get Absences
    end_date = date.now()
    start_date = end_date - timedelta(days=14)
    abse = ATTENDANCE_HISTORY.objects.filter(date__range=(start_date, end_date), absent="Yes").count()
    
    #Do all modifiers
    HMO_Amount = calculateHMO(employeeID)
    ULD_Amount = calculateULD(ULD_AM, ULD_Type)
    CA_Amount = calculateCA(CA_AM)
    COOP_Amount = calculateCOOP(COOP_AM)
    COLA_Amount = calculateCOLA(COLA_AM)
    ADDE_Amount = calculateADDE(ADDE_AM, ADDE_TYPE)
    SSS_Amount, SSS_EC, SSS_WISP_Amount = calculateSSS(emp.Salary)
    PH_Amount = calculatePH(emp.Salary)
    HDMF_Amount = calculateHDMF(emp.Salary)
    WithTax_Amount, WithTax_Excess = calculateWithTax(emp_BP)#FIX THIS
    #lateDues = (emp_DR*((LATEHERE/8)/60))*-1 Currently not in use due to how the office does it(Culmulative time = Absence)
    absenceDues = emp_BP*2*12/314*-abse
    OT = ATTENDANCE_HISTORY.objects.filter(date__range=(start_date, end_date)).aggregate(sum=Sum('OT'))['sum']
    OT = emp_DR/8*1.25*OT

    #total = emp_BP + HMO_Amount+ ULD_Amount + CA_Amount + COOP_Amount+ COLA_Amount+ ADDE_Amount- SSS_Amount- SSS_EC- SSS_WISP_Amount- PH_Amount - HDMF_Amount - WithTax_Amount - WithTax_Excess- absenceDues + OT
    total = emp_BP + HMO_Amount- ULD_Amount - CA_Amount - COOP_Amount+ COLA_Amount+ ADDE_Amount- SSS_Amount- SSS_WISP_Amount- PH_Amount - HDMF_Amount - WithTax_Amount - WithTax_Excess- absenceDues + OT
    return total