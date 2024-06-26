from .models import *
from .models import Employee
from django.shortcuts import  render, redirect, get_object_or_404
from datetime import *
from django.db.models import Sum, F
import pandas as pd
from django.apps import apps
from django.db import transaction
import tkinter as tk
from tkinter import filedialog
from django import forms
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.conf import settings
import os
from django.contrib import messages
import math

def HDMF_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    #print(1)
    if request.method == 'POST':
        file = request.FILES['hdmf_xls']
        obj = File.objects.create(
            file=file
        )
        path = file
        try:
            df = pd.read_excel(path)  # Assuming the file is CSV, adjust if needed
            #print(df)
        except:
            path = '/tax_module/' + str(user.pk)
            return redirect(path)
    
    # Export the current Django database into a CSV file
        #print(1)
        df_db = pd.DataFrame(HDMF.objects.all().values())
        #print(1)
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_HDMF'+date_str+'.csv', index=False)
    
    # Clear out the database
        #print(1)
        HDMF.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            if ((row['HDMF_Rate_ID'] == 'Nat') or (math.isnan(row['HDMF_Rate_ID']))) :
                continue
            else:
                pass
            if ((row['Employer_Rate'] == 'Nat') or (math.isnan(row['Employer_Rate']))):
                continue
            else:
                pass
            if ((row['Employee_Rate'] == 'Nat') or (math.isnan(row['Employee_Rate']))):
                continue
            else:
                pass
            if ((row['Start_Range'] == 'Nat') or (math.isnan(row['Start_Range']))):
                continue
            else:
                pass
            if ((row['End_Range'] == 'Nat') or (math.isnan(row['End_Range']))):
                continue
            else:
                pass
            HDMF.objects.create(HDMF_Rate_ID=row['HDMF_Rate_ID'], Employer_Rate=row['Employer_Rate'], Employee_Rate=row['Employee_Rate'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])  # Adjust column names as needed
        messages.success(request, "Data imported and database cleared successfully.")
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:
        #print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def SSS_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    #print(1)
    if request.method == 'POST':
        file = request.FILES['sss_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        try:
            df = pd.read_excel(path)  # Assuming the file is CSV, adjust if needed
        except:
            path = '/tax_module/' + str(user.pk)
            return redirect(path)
    
    
    # Export the current Django database into a CSV file
        #print(1)
        df_db = pd.DataFrame(SSS.objects.all().values())
        #print(1)
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_SSS'+date_str+'.csv', index=False)
    
    # Clear out the database
        #print(1)
        SSS.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            if ((row['SSS_Rate_ID'] == 'Nat') or (math.isnan(row['SSS_Rate_ID']))) :
                continue
            else:
                pass
            if ((row['Regular_SS_Employer_Rate'] == 'Nat') or (math.isnan(row['Regular_SS_Employer_Rate']))):
                continue
            else:
                pass
            if ((row['Regular_SS_Employee_Rate'] == 'Nat') or (math.isnan(row['Regular_SS_Employee_Rate']))):
                continue
            else:
                pass
            if ((row['Start_Range'] == 'Nat') or (math.isnan(row['Start_Range']))):
                continue
            else:
                pass
            if ((row['End_Range'] == 'Nat') or (math.isnan(row['End_Range']))):
                continue
            else:
                pass
            if ((row['EC_Contribution'] == 'Nat') or (math.isnan(row['EC_Contribution']))):
                continue
            else:
                pass
            if ((row['WISP_Employer_Rate'] == 'Nat') or (math.isnan(row['WISP_Employer_Rate']))):
                continue
            else:
                pass
            if ((row['WISP_Employee_Rate'] == 'Nat') or (math.isnan(row['WISP_Employee_Rate']))):
                continue
            else:
                pass
            if ((row['Total_Contribution'] == 'Nat') or (math.isnan(row['Total_Contribution']))):
                continue
            else:
                pass
            SSS.objects.create(SSS_Rate_ID=row['SSS_Rate_ID'], Regular_SS_Employer_Rate=row['Regular_SS_Employer_Rate'], Regular_SS_Employee_Rate=row['Regular_SS_Employee_Rate'], EC_Contribution=row['EC_Contribution'], WISP_Employer_Rate=row['WISP_Employer_Rate'], WISP_Employee_Rate=row['WISP_Employee_Rate'], Total_Contribution=row['Total_Contribution'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])  # Adjust column names as needed
        messages.success(request, "Data imported and database cleared successfully.")
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:
        #print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})

def PH_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)


    if request.method == 'POST':
        file = request.FILES['PH_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        try:
            df = pd.read_excel(path)  # Assuming the file is CSV, adjust if needed
            #print(df)
        except:
            path = '/tax_module/' + str(user.pk)
            return redirect(path)
    
    # Export the current Django database into a CSV file

        df_db = pd.DataFrame(PhilHealth.objects.all().values())

        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_PH'+date_str+'.csv', index=False)
    
    # Clear out the database
        PhilHealth.objects.all().delete()
    
    # Add data from the DataFrame into the database
        #print(df)
        for _, row in df.iterrows():
            if ((row['PhilHealth_Rate_ID'] == 'Nat') or (math.isnan(row['PhilHealth_Rate_ID']))) :
                #print('a')
                continue
            else:
                pass
            if ((row['Employer_Rate'] == 'Nat') or (math.isnan(row['Employer_Rate']))):
                #print('b')
                continue
            else:
                pass
            if ((row['Employee_Rate'] == 'Nat') or (math.isnan(row['Employee_Rate']))):
                #print('c')
                continue
            else:
                pass
            if ((row['Start_Range'] == 'Nat') or (math.isnan(row['Start_Range']))):
                #print('d')
                continue
            else:
                pass
            if ((row['End_Range'] == 'Nat') or (math.isnan(row['End_Range']))):
                #print('e')
                continue
            else:
                pass
            #print(1)
            PhilHealth.objects.create(PhilHealth_Rate_ID=row['PhilHealth_Rate_ID'], Employer_Rate=row['Employer_Rate'], Employee_Rate=row['Employee_Rate'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])
        messages.success(request, "Data imported and database cleared successfully.")
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:
        #print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def WitholdingTax_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    #print(1)
    if request.method == 'POST':
        file = request.FILES['WT_xls']
        obj = File.objects.create(
            file=file
        )
        #print(file)
        #print(file.file)
        path = file.file
        try:
            df = pd.read_excel(path)  # Assuming the file is CSV, adjust if needed
            #print(df)
        except:
            path = '/tax_module/' + str(user.pk)
            return redirect(path)
        
    
    # Export the current Django database into a CSV file
        
        df_db = pd.DataFrame(WitholdingTax.objects.all().values())
        
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_WT'+date_str+'.csv', index=False)
    
    # Clear out the database
       
        WitholdingTax.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            #print(df)
            if ((row['WTAX_Rate_ID'] == 'Nat') and (math.isnan(row['WTAX_Rate_ID']))) :
                continue
            else:
                pass
            if ((row['Fix_Tax_Amount'] == 'Nat') and (math.isnan(row['Fix_Tax_Amount']))):
                continue
            else:
                pass
            if ((row['Tax_Rate_On_Excess'] == 'Nat') and (math.isnan(row['Tax_Rate_On_Excess']))):
                continue
            else:
                pass
            if ((row['Start_Range'] == 'Nat') and (math.isnan(row['Start_Range']))):
                continue
            else:
                pass
            if ((row['End_Range'] == 'Nat') and (math.isnan(row['End_Range']))):
                continue
            else:
                pass
            WitholdingTax.objects.create(WTAX_Rate_ID=row['WTAX_Rate_ID'], Fix_Tax_Amount=row['Fix_Tax_Amount'], Tax_Rate_On_Excess=row['Tax_Rate_On_Excess'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])
        messages.success(request, "Data imported and database cleared successfully.")
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:
        #print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def A_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    
    if request.method == 'POST':
        file = request.FILES['A_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        try:
            workinghours_df = pd.read_excel(path)  # Assuming the file is CSV, adjust if needed
        except:
            path = '/attendance_db/' + str(user.pk)
            return redirect(path)
        #print(workinghours_df)
        Employee_check = Employee.objects.all()
        holiday_check = HOLIDAY.objects.all()
        Leave_check = Leave.objects.all()
        holiday_true = ''
        leave_true = ''
        Employee_t = ''
        
    # Add data from the DataFrame into the database
        for _, row in workinghours_df.iterrows():
            if row['Date'] == 'NaT':
                continue
            else:
            

            #Data cleaning
                current_date_str = datetime.now().strftime('%d/%m/%Y')
                #print(type(row['Date']))
                date = str(row['Date'])
                #print(date)
                date = date.split(' ')
                #print(date)
                date = date[0]
                date = date[4:]
                date = current_date_str[-4:] + date #10BIT: Check this again
                date = datetime.strptime(date, "%Y-%m-%d")
                date = date.date()
            if row['NAME'] == 'NaT':
                continue
            else:
                id = row['NAME']
                id = id.upper()
                print('ID: ' + str(id))
                for x in Employee_check:
                    if x.id_number == id:
                        Employee_t= get_object_or_404(Employee, id_number=x.id_number)
                        print(Employee_t)
            print(date)
            xms = ATTENDANCE_HISTORY.objects.filter(Date=date, Employee_ID=Employee_t)
            #print(date)
            #print(xms)
            #print(type(xms))
            #print(xms==None)
            #print(xms.exists())
            #print(not xms.exists())
            #print('Benis')
            #print(not xms.exists() == True)

            if not xms.exists():
                for x in holiday_check:
                    print(str(x.pk) + str(x.Date))
                    print((date==x.Date))
                    print(date)
                    print(x.Date)
                    if x.Date == date:
                        
                        holiday_true = get_object_or_404(HOLIDAY, Holiday_ID=x.Holiday_ID)
                for x in Leave_check:
                    if x.Start_Date == date:
                        leave_true = get_object_or_404(Leave, Leave_ID=x.Leave_ID)
                
                TimeIn =0
                TimeOut=0
                TimeIn_2=0
                TimeOut_2=0

                
                
                try:
                    TimeIn = row['In'] 
                    #print(type(TimeIn))
                    #print(TimeIn)
                except:
                    pass
                try:
                    TimeOut = row['Out'] 
                except:
                    pass
                try:
                    TimeIn_2 = row['In_2'] 
                except:
                    pass
                try:
                    TimeOut_2 = row['Out_2']
                except:
                    pass

                try:
                    OT_IN = row['OT_IN']
                except:
                    pass
                try:
                    OT_OUT = row['OT_OUT']
                except:
                    pass
                
                if (TimeIn  == 'NaT') or (TimeOut  == 'NaT') or (TimeIn_2  == 'NaT') or (TimeOut_2  == 'NaT'):
                    try:
                        if (math.isnan(TimeIn)) or ( math.isnan(TimeOut)  == 'nan') or (math.isnan(TimeIn_2)   == 'nan') or (math.isnan(TimeOut_2)   == 'nan'):
                            #print('benis')
                            continue
                    except:
                        if (isinstance(TimeIn, float)) or (isinstance(TimeOut, float)) or (isinstance(TimeIn_2, float)) or (isinstance(TimeOut_2, float)):
                            #print('benis')
                            continue
                
                Night_In = 0
                Night_out = 0
                NightShift_Total=0
                OT_Total = None
                if ((OT_IN == 'NaT') and (OT_OUT == 'NaT')) or ((isinstance(OT_IN, float)) and (isinstance(OT_OUT, float))):
                    OT_Total = 0
                    NightShift_Total = 0

            

                if ((OT_IN == 'NaT') and (OT_OUT != 'NaT') or (isinstance(OT_IN, float)) and (isinstance(OT_OUT, float) == False)):
                        #print(2) 
                        OT_IN = time(18, 0)


                    
                if ((OT_IN != 'NaT') and (OT_OUT == 'NaT') or (isinstance(OT_IN, float)  == False) and (isinstance(OT_OUT, float))):
                        #print(3) 
                        OT_OUT = OT_IN
                        OT_Total = 0

                if (((OT_IN != 'NaT')) and ((OT_OUT != 'NaT'))) and ((isinstance(OT_IN, float)  == False) and (isinstance(OT_OUT, float) == False)) and (OT_Total == None) :
                    #print(OT_IN)
                    #print(type(OT_IN))
                    if OT_IN <= time(18, 0) and OT_IN > time(7,0):#A check to see if they worked night shift and is not OT
                        #print('a')
                        OT_IN = time(18, 0)
                    if OT_IN >= time(22, 0):#A check to see if they worked night shift and is not OT
                        #print('b')
                        Night_In = OT_IN
                        OT_IN = time(18, 0)
                    NightShiftStart = 0
                    if (OT_IN >= time(0,0)) and (OT_IN <= time(7,0)):#If starts late nightshift
                        #print('c')
                        Night_In = OT_IN
                        OT_IN = time(18,0)
                        NightShiftStart = 1
                    if (OT_OUT >= time(0,0)) and (OT_OUT <= time(7,0)) and (NightShiftStart == 0):#If ends late nightshift
                        #print('d')
                        Night_out = OT_OUT
                        OT_OUT = time(22,0)
                    elif (OT_OUT >= time(0,0)) and (OT_OUT <= time(7,0)) and (NightShiftStart == 1):
                        #print('e')
                        Night_out= OT_OUT
                    #Overnight 
                    
                    if (OT_OUT >= time(22,0) and Night_out == 0): #OT_In is declared and normal range but not OT_OUT or Night_In or Out
                        #print('an')
                        Night_out = OT_OUT
                        OT_OUT = time(22,0)
                    if ((OT_OUT >= time(7,0)) ) and (OT_OUT != time(22,0)) and (Night_In != 0):
                        #print('benis')
                        Night_out = Night_In
                    if Night_In == 0 and Night_out == 0:
                        #print('cin')
                        NightShift_Total=0
                    elif Night_In == 0 and Night_out != 0:
                        #print('den')
                        Night_In = time(22,0)
                        #print('night calc')
                        #print(Night_In)
                        #print(Night_out)
                        seconds_Night_In = (Night_In.hour * 3600) + (Night_In.minute * 60)
                        seconds_Night_out = (Night_out.hour * 3600) + (Night_out.minute * 60)
                        if seconds_Night_out < seconds_Night_In:
                            seconds_Night_out += 24 * 3600
                        night_shift_seconds = seconds_Night_out - seconds_Night_In
                        #print(12) 
                        NightShift_Total = night_shift_seconds / 3600.0
                    else:
                        if NightShiftStart == 1:
                            OT_OUT = time(18,0)
                        #print('fig')
                        #print('night calc')
                        #print(Night_In)
                        #print(Night_out)
                        seconds_Night_In = (Night_In.hour * 3600) + (Night_In.minute * 60)
                        seconds_Night_out = (Night_out.hour * 3600) + (Night_out.minute * 60)
                        if seconds_Night_out < seconds_Night_In:
                            seconds_Night_out += 24 * 3600
                        night_shift_seconds = seconds_Night_out - seconds_Night_In
                        #print(12) 
                        NightShift_Total = night_shift_seconds / 3600.0
                    #print('OT calc')
                    #print(OT_IN)
                    #print(OT_OUT)
                    OT_Total = (OT_OUT.hour * 60 + OT_OUT.minute) - (OT_IN.hour * 60 + OT_IN.minute)
                    OT_Total = OT_Total / 60.0 
                    

                HoursWorked = 0
                HoursWorked_2 = 0
                try:
                # Calculate the difference in minutes
                    HoursWorked = (TimeOut.hour * 60 + TimeOut.minute) - (TimeIn.hour * 60 + TimeIn.minute)
                    #print(1)
                    #print(HoursWorked)
                    # Convert minutes to hours (float)
                    HoursWorked = HoursWorked / 60.0
                    #print(2)
                    # Calculate the difference in minutes
                    HoursWorked_2 = (TimeOut_2.hour * 60 + TimeOut_2.minute) - (TimeIn_2.hour * 60 + TimeIn_2.minute)
                    #print(3)
                    #print(HoursWorked_2)
                    # Convert minutes to hours (float)
                    HoursWorked_2 = HoursWorked_2 / 60.0
                    #print(4)
                except:
                   print(';-;')
                #print('Hours Worked: '+ str(HoursWorked))
                #print('Hours Worked: '+ str(HoursWorked_2))
                HoursWorked = HoursWorked+HoursWorked_2
                if (HoursWorked < 8) and (date.weekday() == 5):
                    diff = 8- HoursWorked
                    if (OT_Total > diff) and (diff>0):
                        OT_Total = OT_Total - diff
                        diff = 0
                        HoursWorked = 8
                    elif (OT_Total > 0) and (diff>0):
                        diff -= OT_Total
                        HoursWorked += OT_Total
                        OT_Total = 0
                    if (NightShift_Total > diff) and (diff>0):
                        NightShift_Total = NightShift_Total - diff
                        diff = 0
                        HoursWorked = 8
                    elif (NightShift_Total > 0) and (diff>0):
                        diff -= NightShift_Total
                        HoursWorked += NightShift_Total
                        NightShift_Total = 0
                else:
                    diff = 4- HoursWorked
                    if (OT_Total > diff) and (diff>0):
                        OT_Total = OT_Total - diff
                        diff = 0
                        HoursWorked = 4
                    elif (OT_Total > 0) and (diff>0):
                        diff -= OT_Total
                        HoursWorked += OT_Total
                        OT_Total = 0
                    if (NightShift_Total > diff) and (diff>0):
                        NightShift_Total = NightShift_Total - diff
                        diff = 0
                        HoursWorked = 4
                    elif (NightShift_Total > 0) and (diff>0):
                        diff -= NightShift_Total
                        HoursWorked += NightShift_Total
                        NightShift_Total = 0
                x=0#Code bugs if I dont declare this prior
                ATTENDANCE_HISTORY.objects.create(Employee_ID=Employee_t, Date=date, OT=OT_Total, NightShift=NightShift_Total, HoursWorked=HoursWorked)
                if TimeIn:
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    print(x)
                    print(TimeIn)
                    x.TimeIn = TimeIn
                    try:
                        x.save()
                        print("Timed in")
                    except:
                        pass
                    
                if TimeOut:
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.TimeOut = TimeOut
                    try:
                        x.save()
                    except:
                        pass
                try:
                    if TimeIn_2:
                        x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                        x.TimeIn_2 = TimeIn_2
                        try:
                            x.save()
                        except:
                            pass
                except:
                    pass
                try:
                    if TimeOut_2:
                        x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                        x.TimeOut_2 = TimeOut_2
                        try:
                            x.save()
                        except:
                            pass

                except:
                    pass
                #10BIT:Go back to fixing this
                print('Hi')
                print(holiday_true)
                if holiday_true != '':
                    print('a')
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    print('b')
                    x.Holiday_ID = holiday_true
                    print('c')
                    try:
                        x.save()
                        print('d')
                    except:
                        print('e')
                        pass
                    print("WOOHOO")
                if leave_true != '':
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.Leave_ID = leave_true
                    try:
                        x.save()
                    except:
                        pass
                    print("WOOHOO")
            else:
                pass
        messages.success(request, "Data imported and database cleared successfully.")
        path = '/attendance_db/' + str(user.pk)
        return redirect(path)
    else:
        return render(request, 'payrollapp/attendance_db.html', {'user':user})
    
def Holiday_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['Holiday_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            if ((row['Date'] == 'Nat') and (isinstance(row['Date'], float))) :
                continue
            else:
                pass
            if ((row['Type'] == 'Nat') and (isinstance(row['Type'], float))):
                continue
            else:
                pass
            date = datetime.strptime(row['Date'], "%Y-%m-%d")
            xms = HOLIDAY.objects.filter(Date=date)
            if not xms.exists():
                HOLIDAY.objects.create(Type=row['Type'], Date=date)
            else:
                a = HOLIDAY.objects.filter(Date=date)
                a.update(Type=row['Type'])
        messages.success(request, "Data imported and database cleared successfully.")
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:
        print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def Leave_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['Leave_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            #Check for any missing if so skip this log
            if ((row['Start_Date'] == 'Nat') and (isinstance(row['Start_Date'], float))) :
                continue
            else:
                pass
            if ((row['Type'] == 'Nat') and (isinstance(row['Type'], float))):
                continue
            else:
                pass
            if ((row['Employee_ID'] == 'Nat') and (isinstance(row['Employee_ID'], float))):
                continue
            else:
                pass
            try:
                emp = get_object_or_404(Employee, id_number = row['Employee_ID'])
            except:
                continue
            date = datetime.strptime(row['Start_Date'], "%Y-%m-%d")
            xms = Leave.objects.filter(Employee_ID=emp, Start_Date=date)
            if row['Type'] == 'Sick' and emp.Sick_Leaves > 0:
                if not xms.exists():
                    Leave.objects.create(Employee_ID=emp, Type=row['Type'], Start_Date=date)
                    emp.Sick_Leaves -= 1
                    emp.save()
                else:
                    a = HOLIDAY.objects.filter(Date=date)
                    a.update(Type=row['Type'])
                    emp.Sick_Leaves += 1
                    emp.Vacation_Leaves -= 1
                    emp.save()
            if row['Type'] == 'Vacation' and emp.Vacation_Leaves > 0:
                if not xms.exists():
                    Leave.objects.create(Employee_ID=emp, Type=row['Type'], Start_Date=date)
                    emp.Vacation_Leaves -= 1
                    emp.save()
                else:
                    a = HOLIDAY.objects.filter(Date=date)
                    a.update(Type=row['Type'])
                    emp.Sick_Leaves -= 1
                    emp.Vacation_Leaves += 1
                    emp.save()            
        messages.success(request, "Leaves updated successfully!")
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    else:
        print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    

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
        path = '/tax_module/' + str(user.pk)
        return redirect(path)
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def Department_add(request, UID):
    a = Department.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    if (request.method=='POST'):
    #Get the values
        A_DEP = request.POST.get('A_DEP')
        xms = Department.objects.filter(Department_ID=A_DEP)
        if not xms.exists():
            Department.objects.create(Department_ID=A_DEP)
            messages.success(request, "Created successfully!")
        else:
            messages.warning(request, "Error: Already exists")
        
        path = '/settings/' + str(user.pk)
        return redirect(path)
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/settings.html', {'user':user})
    
def Department_del(request, UID):
    a = Department.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    if (request.method=='POST'):
    #Get the values
        D_DEP = request.POST.get('D_DEP')
        Department.objects.filter(Department_ID=D_DEP).delete()
        messages.success(request, "Deleted Department successfully!")
        path = '/settings/' + str(user.pk)
        return redirect(path)
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/settings.html', {'user':user})
    
def Reset_Leaves(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    a = Employee.objects.filter(Status='Regular')
    a.update(Vacation_Leaves=15,
             Sick_Leaves=15)
    path = '/settings/' + str(user.pk)
    return redirect(path)