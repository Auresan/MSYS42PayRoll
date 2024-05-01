from django.db import models

# Create your models here.
class Employee(models.Model):
    Last_name = models.CharField(max_length=255)
    First_name = models.CharField(max_length=255)
    Middle_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=6, primary_key=True)
    Status  = models.CharField(max_length=255)
    Department  = models.CharField(max_length=255)
    Role   = models.CharField(max_length=255)
    Join_Date = models.DateField(blank=True, null=True)
    Phone_Number = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    BankNumber = models.IntegerField()
    Salary   = models.FloatField()



    
    #ColaEarnings  = models.FloatField()
    #CAdeductions   = models.FloatField()
    #COOPdeductions  = models.FloatField()
    #ULdeductions   = models.FloatField()
    def getID(self):
        return self.id_number
    
    def getFullName(self):
        full_name = self.Last_name + ", " + self.First_name + " "+ self.Middle_name
        return full_name

    def __str__(self):
        z = str(self.getID())
        return z
    
class HMO(models.Model):
    HMO_ID = models.CharField(max_length=6, primary_key=True)
    HMO_Amount = models.IntegerField()
    def getID(self):
        return self.HMO_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class UNIFORMLAPTOPDEDUCTIONS(models.Model):
    ULDeductions_ID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)
    ULDeductions_Amount = models.IntegerField()
    def getID(self):
        return self.ULDeductions_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class CA(models.Model):
    CA_ID = models.IntegerField(primary_key=True)
    CA_Amount = models.IntegerField()
    def getID(self):
        return self.CA_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class COOP(models.Model):
    COOP_ID = models.IntegerField(primary_key=True)
    COOP_Amount = models.IntegerField()
    def getID(self):
        return self.COOP_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class COLA(models.Model):
    COLA_ID = models.IntegerField(primary_key=True)
    COLA_Amount = models.IntegerField()
    def getID(self):
        return self.COLA_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class ADDITIONAL_EARNINGS(models.Model):
    AddtlEarning_ID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)
    ADD_EARNINGS = models.IntegerField()
    def getID(self):
        return self.AddtlEarning_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class HOLIDAY(models.Model):
    Holiday_ID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)
    Date = models.DateField(blank=True, null=True)
    def getID(self):
        return self.Holiday_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class Leave(models.Model):
    Leave_ID = models.IntegerField(primary_key=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Type = models.CharField(max_length=255)
    Leaves_Left = models.IntegerField()
    Start_Date = models.DateField(blank=True, null=True)
    End_Date = models.DateField(blank=True, null=True)#10BIT: TO BE REMOVED Why did we even add this
    def getID(self):
        return self.Leave_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class SSS(models.Model):
    SSS_Rate_ID = models.IntegerField(primary_key=True)
    Regular_SS_Employer_Rate = models.FloatField()
    Regular_SS_Employee_Rate = models.FloatField()
    EC_Contribution = models.FloatField()
    WISP_Employer_Rate = models.FloatField()
    WISP_Employee_Rate = models.FloatField()
    Total_Contribution = models.FloatField()
    Start_Range = models.FloatField()
    End_Range = models.FloatField()
    def getID(self):
        return self.SSS_Rate_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class PhilHealth(models.Model):
    PhilHealth_Rate_ID = models.IntegerField(primary_key=True)
    Employer_Rate = models.FloatField()
    Employee_Rate = models.FloatField()
    Start_Range = models.FloatField()
    End_Range = models.FloatField()
    def getID(self):
        return self.PhilHealth_Rate_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class HDMF(models.Model):
    HDMF_Rate_ID = models.IntegerField(primary_key=True)
    Employer_Rate = models.FloatField()
    Employee_Rate = models.FloatField()
    Start_Range = models.FloatField()
    End_Range = models.FloatField()
    def getID(self):
        return self.HDMF_Rate_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class WitholdingTax(models.Model):
    WTAX_Rate_ID = models.IntegerField(primary_key=True)
    Fix_Tax_Amount = models.FloatField()
    Tax_Rate_On_Excess = models.FloatField()
    Start_Range = models.FloatField()
    End_Range = models.FloatField()
    def getID(self):
        return self.WTAX_Rate_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class Payslip_Transaction(models.Model):
    Transaction_ID = models.IntegerField(primary_key=True)
    Date_Distributed = models.DateField(blank=True, null=True)
    Start_Date = models.DateField(blank=True, null=True)
    End_Date = models.DateField(blank=True, null=True)
    Net_Pay = models.FloatField()
    Total_Deductions = models.FloatField()
    Absence_Deductions = models.FloatField()
    OT = models.FloatField()
    Holiday_Comp = models.FloatField()
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    SSS_Rate_ID = models.FloatField()
    PhilHealth_Rate_ID = models.FloatField()
    HDMF_Rate_ID = models.FloatField()
    WTAX_Rate_ID = models.FloatField()
    HMO_Rate_ID = models.FloatField()
    ULDeductions_Rate_ID = models.ForeignKey(UNIFORMLAPTOPDEDUCTIONS, on_delete=models.CASCADE)
    CA_Rate_ID = models.ForeignKey(CA, on_delete=models.CASCADE)
    COOP_Rate_ID = models.ForeignKey(COOP, on_delete=models.CASCADE)
    COLA_Rate_ID = models.ForeignKey(COLA, on_delete=models.CASCADE)
    AddtlEarning_Rate_ID = models.ForeignKey(ADDITIONAL_EARNINGS, on_delete=models.CASCADE)

    def getID(self):
        return self.Transaction_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class ATTENDANCE_HISTORY(models.Model):
    History_ID = models.IntegerField(primary_key=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    Leave_ID = models.ForeignKey(Leave, on_delete=models.CASCADE, blank=True, null=True)#Here null blank=true
    Holiday_ID = models.ForeignKey(HOLIDAY, on_delete=models.CASCADE, blank=True, null=True)
    TimeIn = models.TimeField(blank=True, null=True)
    TimeOut = models.TimeField(blank=True, null=True)
    TimeIn_2 = models.TimeField(blank=True, null=True)
    TimeOut_2 = models.TimeField(blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    OT = models.FloatField()
    #OT = models.FloatField()
    HoursWorked = models.FloatField()
    def getID(self):
        return self.History_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class USER_ACCOUNT(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()

    def getUsername(self):
        return str(self.username)
    
    def getPassword(self):
        return str(self.password)
    
    def __str__(self):
        return str(self.pk) + ": " + self.getUsername() + " " + self.getPassword()
    
class BANK_FILES(models.Model):
    BANK_ENTRY_ID = models.IntegerField(primary_key=True)
    BANK_FILE_NAME = models.CharField(max_length=250)
    PAYROLL_PERIOD = models.CharField(max_length=250)
    def __str__(self):
        return str(self.BANK_FILE_NAME)