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
    Phone_Number = models.IntegerField()
    Email = models.CharField(max_length=255)
    BankNumber = models.IntegerField()
    Salary   = models.FloatField()



    
    #ColaEarnings  = models.FloatField()
    #CAdeductions   = models.FloatField()
    #COOPdeductions  = models.FloatField()
    #ULdeductions   = models.FloatField()
    def getID(self):
        return self.id_number
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    
class HMO(models.Model):
    HMO_ID = models.IntegerField(primary_key=True)
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
    COLA_Amount = models.IntegerField()
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
    End_Date = models.DateField(blank=True, null=True)
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
    Type = models.CharField(max_length=255)
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
    Absence_Deductions = models.FloatField()
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    SSS_Rate_ID = models.ForeignKey(SSS, on_delete=models.CASCADE)
    PhilHealth_Rate_ID = models.ForeignKey(PhilHealth, on_delete=models.CASCADE)
    HDMF_Rate_ID = models.ForeignKey(HDMF, on_delete=models.CASCADE)
    WTAX_Rate_ID = models.ForeignKey(WitholdingTax, on_delete=models.CASCADE)
    HMO_Rate_ID = models.ForeignKey(HMO, on_delete=models.CASCADE)
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
    Leave_ID = models.ForeignKey(Leave, on_delete=models.CASCADE)
    Holiday_ID = models.ForeignKey(HOLIDAY, on_delete=models.CASCADE)
    Transaction_ID = models.ForeignKey(Payslip_Transaction, on_delete=models.CASCADE)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Time = models.TimeField()
    IN_OUT = models.CharField(max_length=255)
    Date = models.DateField(blank=True, null=True)
    def getID(self):
        return self.History_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z

class ATTENDANCE_RECORD(models.Model):
    Attendance_ID = models.IntegerField(primary_key=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    History_ID = models.ForeignKey(ATTENDANCE_HISTORY, on_delete=models.CASCADE)
    Time = models.TimeField()
    IN_OUT = models.CharField(max_length=255)
    Date = models.DateField(blank=True, null=True)
    def getID(self):
        return self.Attendance_ID
    def __str__(self):
        z = str(self.pk)+':'+str(self.getID())
        return z
    

    