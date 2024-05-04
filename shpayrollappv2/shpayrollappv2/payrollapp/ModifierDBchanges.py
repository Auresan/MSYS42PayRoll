from .models import *
from .models import Employee
from django.shortcuts import  render, redirect, get_object_or_404
from datetime import *
from django.db.models import Sum
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

def HDMF_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['hdmf_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)
    
    # Export the current Django database into a CSV file
        print(1)
        df_db = pd.DataFrame(HDMF.objects.all().values())
        print(1)
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_HDMF'+date_str+'.csv', index=False)
    
    # Clear out the database
        print(1)
        HDMF.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            HDMF.objects.create(HDMF_Rate_ID=row['HDMF_Rate_ID'], Employer_Rate=row['Employer_Rate'], Employee_Rate=row['Employee_Rate'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])  # Adjust column names as needed
        messages.success(request, "Data imported and database cleared successfully.")
        print("Data imported and database cleared successfully.")
        messages.success(request, "Employee created successfully!")
        
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    else:
        print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def SSS_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['sss_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)
    
    
    # Export the current Django database into a CSV file
        print(1)
        df_db = pd.DataFrame(SSS.objects.all().values())
        print(1)
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_SSS'+date_str+'.csv', index=False)
    
    # Clear out the database
        print(1)
        SSS.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            SSS.objects.create(SSS_Rate_ID=row['SSS_Rate_ID'], Regular_SS_Employer_Rate=row['Regular_SS_Employer_Rate'], Regular_SS_Employee_Rate=row['Regular_SS_Employee_Rate'], EC_Contribution=row['EC_Contribution'], WISP_Employer_Rate=row['WISP_Employer_Rate'], WISP_Employee_Rate=row['WISP_Employee_Rate'], Total_Contribution=row['Total_Contribution'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])  # Adjust column names as needed
        messages.success(request, "Data imported and database cleared successfully.")
        print("Data imported and database cleared successfully.")
        messages.success(request, "Employee created successfully!")
        
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    else:
        print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})

def PH_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['PH_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)
    
    # Export the current Django database into a CSV file
        print(1)
        df_db = pd.DataFrame(PhilHealth.objects.all().values())
        print(1)
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_PH'+date_str+'.csv', index=False)
    
    # Clear out the database
        print(1)
        PhilHealth.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            PhilHealth.objects.create(PhilHealth_Rate_ID=row['PhilHealth_Rate_ID'], Employer_Rate=row['Employer_Rate'], Employee_Rate=row['Employee_Rate'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])
        messages.success(request, "Data imported and database cleared successfully.")
        print("Data imported and database cleared successfully.")
        messages.success(request, "Employee created successfully!")
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    else:
        print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def WitholdingTax_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['WT_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)
    
    # Export the current Django database into a CSV file
        print(1)
        df_db = pd.DataFrame(WitholdingTax.objects.all().values())
        print(1)
        today_date = datetime.now().date()

        # Convert date to string
        date_str = today_date.strftime("%Y-%m-%d")

        df_db.to_csv('backup_WT'+date_str+'.csv', index=False)
    
    # Clear out the database
        print(1)
        WitholdingTax.objects.all().delete()
    
    # Add data from the DataFrame into the database
        for _, row in df.iterrows():
            WitholdingTax.objects.create(WTAX_Rate_ID=row['WTAX_Rate_ID'], Fix_Tax_Amount=row['Fix_Tax_Amount'], Tax_Rate_On_Excess=row['Tax_Rate_On_Excess'], Start_Range=row['Start_Range'], End_Range=row['End_Range'])
        messages.success(request, "Data imported and database cleared successfully.")
        print("Data imported and database cleared successfully.")
        messages.success(request, "Employee created successfully!")
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    else:
        print("No file selected.")
        #
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def A_UPLOAD(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)

    print(1)
    if request.method == 'POST':
        file = request.FILES['A_xls']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        workinghours_df = pd.read_excel(path)  # Assuming the file is CSV, adjust if needed
        print(workinghours_df)
        Employee_check = Employee.objects.all()
        holiday_check = HOLIDAY.objects.all()
        Leave_check = Leave.objects.all()
        holiday_true = ''
        leave_true = ''
        Employee_t = ''
        
    # Add data from the DataFrame into the database
        for _, row in workinghours_df.iterrows():
            if row['Date'] == 'NaT':
                print('Fail')
                continue
            else:
            

            #Data cleaning
                current_date_str = datetime.now().strftime('%d/%m/%Y')
                print(type(row['Date']))
                date = str(row['Date'])
                print(date)
                date = date.split(' ')
                print(date)
                date = date[0]
                date = date[4:]
                date = current_date_str[-4:] + date #10BIT: Check this again
                date = datetime.strptime(date, "%Y-%m-%d")

            id = row['NAME']
            id = id.upper()
            print('ID: ' + str(id))
            for x in Employee_check:
                if x.id_number == id:
                    Employee_t= get_object_or_404(Employee, id_number=x.id_number)

            xms = ATTENDANCE_HISTORY.objects.filter(Date=date, Employee_ID=Employee_t)
            print(date)
            print(xms)
            print(type(xms))
            print(xms==None)
            print(xms.exists())
            print(not xms.exists())
            print('Benis')

            if not xms:
                

                for x in holiday_check:
                    if x.date == date:
                        holiday_true = get_object_or_404(HOLIDAY, HOLIDAY_ID=x.Holiday_ID)
                for x in Leave_check:
                    if x.date == date:
                        leave_true = get_object_or_404(Leave, Leave_ID=x.Leave_ID)
                print("HELP")
                print(type(row['In']))
                print(row['In'])
                try:
                    TimeIn = row['In'] 
                    print(TimeIn)
                    print(type(TimeIn))
                except:
                    pass
                try:
                    TimeOut  = row['Out']
                    print(TimeOut)
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
            
            
            
                Night_In = 0
                Night_out = 0
                NightShift_Total=0
                try:
                    OT_IN = row['OT_IN']
                    OT_OUT = row['OT_OUT']

                    #if no OT At all
                    if (OT_IN == 'NaT') and (OT_OUT == 'NaT'):
                        print(1) 
                        OT_IN = time(18,0)
                        OT_OUT = time(18,0)
                        Night_In = time(18,0)
                        Night_out = time(18,0)

                    #If no OT_IN but OT_OUT
                    if (OT_IN == 'NaT') and (OT_OUT != 'NaT'):
                        print(2) 
                        OT_IN = time(18, 0)

                    #If no OT_OUT but OT_IN
                    if (OT_IN != 'NaT') and (OT_OUT == 'NaT'):
                        print(3) 
                        OT_OUT = time(22,0)
                    
                    #If OT_IN earlier than 6
                    if OT_IN <= time(18, 0):
                        print(4) 
                        OT_IN = time(18, 0)
                        print(OT_IN)
                        print(OT_OUT)
                        print(Night_In)
                        print(Night_out)

                    #IF OT_IN at 10pm onwards NIGHT SHIFT
                    if OT_IN >= time(22, 0):#A check to see if they worked night shift and is not OT
                        print(5) 
                        Night_In = OT_IN
                        OT_IN = time(18, 0)
                        OT_OUT = time(18, 0)

                    #IF Late Night Shift Start
                    if (OT_IN >= time(0,0)) and (OT_IN <= time(7,0)):#If starts late nightshift
                        print(6) 
                        Night_In = OT_IN
                        OT_IN = time(18,0)
                    

                    #If Late Night end
                    if (OT_OUT >= time(0,0)) and (OT_OUT <= time(7,0)):#If ends late nightshift
                        print(7) 
                        Night_out = OT_OUT
                        print(7.5)
                        OT_OUT = time(22,0)
                        print(7.9)
                        print(OT_IN)
                        print(OT_OUT)
                        print(Night_In)
                        print(Night_out)
                        
                    #Overnight 
                    if (OT_OUT >= time(22,0) and Night_out == 0): #OT_In is declared and normal range but not OT_OUT or Night_In or Out
                        print(8) 
                        Night_out = OT_OUT
                        Night_In = time(22,0)
                        OT_OUT = time(22,0)
                    
                    #Cap NightShift
                    if (OT_OUT >= time(7,0)) and (OT_OUT != time(22,0)) and (Night_In != 0):
                        print(9) 
                        Night_out = time(7,0)

                    #No Nightshift
                    if Night_In == 0:
                        print(10) 
                        Night_In = time(22,0)
                    if Night_out == 0:    
                        print(11) 
                        Night_out = time(22,0)
                    

                    seconds_Night_In = (Night_In.hour * 3600) + (Night_In.minute * 60)
                    seconds_Night_out = (Night_out.hour * 3600) + (Night_out.minute * 60)
                    if seconds_Night_out < seconds_Night_In:
                        seconds_Night_out += 24 * 3600
                    night_shift_seconds = seconds_Night_out - seconds_Night_In
                    print(12) 
                    NightShift_Total = night_shift_seconds / 3600.0
                    print(13) 

                    
                    OT = (OT_OUT.hour * 60 + OT_OUT.minute) - (OT_IN.hour * 60 + OT_IN.minute)
                    print(14) 
                    OT_Total = OT / 60.0 
                    print(OT_Total)
                except:
                    OT_Total = 0
                

                HoursWorked = 0
                HoursWorked_2 = 0
                try:
                # Calculate the difference in minutes
                    HoursWorked = (TimeOut.hour * 60 + TimeOut.minute) - (TimeIn.hour * 60 + TimeIn.minute)
                    print(1)
                    print(HoursWorked)
                    # Convert minutes to hours (float)
                    HoursWorked = HoursWorked / 60.0
                    print(2)
                    # Calculate the difference in minutes
                    HoursWorked_2 = (TimeOut_2.hour * 60 + TimeOut_2.minute) - (TimeIn_2.hour * 60 + TimeIn_2.minute)
                    print(3)
                    print(HoursWorked_2)
                    # Convert minutes to hours (float)
                    HoursWorked_2 = HoursWorked_2 / 60.0
                    print(4)
                except:
                    try:
                        # Calculate the difference in minutes
                        HoursWorked = (TimeOut_2.hour * 60 + TimeOut_2.minute) - (TimeIn.hour * 60 + TimeIn.minute)
                        print(5)
                        # Convert minutes to hours (float)
                        HoursWorked = HoursWorked / 60.0
                        print(6)
                    except:
                        # Calculate the difference in minutes
                        HoursWorked_2 = (TimeOut_2.hour * 60 + TimeOut_2.minute) - (TimeIn_2.hour * 60 + TimeIn_2.minute)
                        print(7)
                        # Convert minutes to hours (float)
                        HoursWorked_2 = HoursWorked_2 / 60.0
                        print(8)
                print('Hours Worked: '+ str(HoursWorked))
                print('Hours Worked: '+ str(HoursWorked_2))
                HoursWorked = HoursWorked+HoursWorked_2
                OT = OT + (HoursWorked-8)
                
                x=0#Code bugs if I dont declare this
                ATTENDANCE_HISTORY.objects.create(Employee_ID=Employee_t, Date=date, OT=OT_Total, NightShift=NightShift_Total, HoursWorked=HoursWorked)
                if TimeIn:
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.TimeIn = TimeIn
                    x.save()
                    print("WOOHOO")
                if TimeOut:
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.TimeOut = TimeOut
                    x.save()
                    print("WOOHOO")
                if TimeIn_2:
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.TimeIn_2 = TimeIn_2
                    x.save()
                    print("WOOHOO")
                if TimeOut_2:
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.TimeOut_2 = TimeOut_2
                    x.save()
                    print("WOOHOO")

                #10BIT:Go back to fixing this
                if holiday_true != '':
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.Holiday_ID = holiday_true
                    x.save()
                    print("WOOHOO")
                if leave_true != '':
                    x = ATTENDANCE_HISTORY.objects.latest('History_ID')
                    x.Leave_ID = leave_true
                    x.save()
                    print("WOOHOO")
            else:
                pass
        messages.success(request, "Data imported and database cleared successfully.")
        print("Data imported and database cleared successfully.")
        messages.success(request, "Employee created successfully!")
        return render(request, 'payrollapp/attendance_db.html', {'user':user})
    else:
        print("No file selected.")
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
            date = datetime.strptime(row['Date'], "%Y-%m-%d")
            HOLIDAY.objects.create(Holiday_ID=row['Holiday_ID'], Type=row['Type'], Date=date)
        messages.success(request, "Data imported and database cleared successfully.")
        print("Data imported and database cleared successfully.")
        messages.success(request, "Employee created successfully!")
        return render(request, 'payrollapp/tax_module.html', {'user':user})
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
            emp = get_object_or_404(Employee, id_number = row['Employee_ID'])
            date = datetime.strptime(row['Date'], "%Y-%m-%d")
            
            if row['Type'] == 'Sick' and emp.Sick_Leaves > 0:
                Leave.objects.create(Employee_ID=emp, Type=row['Type'], Start_Date=date, End_Date=date)
                emp.Sick_Leaves -= 1
                emp.save()
            if row['Type'] == 'Vacation' and emp.Vacation_Leaves > 0:
                Leave.objects.create(Employee_ID=emp, Type=row['Type'], Start_Date=date, End_Date=date)
                emp.Sick_Leaves -= 1
                emp.save()
            if (row['Type'] != 'Sick') or (row['Type'] == 'Vacation'):
                print(str(row['Type'])+str(row['Employee_ID'])+str(row['Start_Date'])+'Not Added')
            
        messages.success(request, "Employee created successfully!")
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
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/tax_module.html', {'user':user})
    
def Department_add(request, UID):
    a = Department.objects.all()
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    if (request.method=='POST'):
    #Get the values
        A_DEP = request.POST.get('A_DEP')
        Department.objects.create(Department_ID=A_DEP)
        messages.success(request, "Created successfully!")
        return render(request, 'payrollapp/settings.html', {'user':user})
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
        return render(request, 'payrollapp/settings.html', {'user':user})
    else:#First time viewing/non-form open
        return render(request, 'payrollapp/settings.html', {'user':user})
    
def Reset_Leaves(request, UID):
    user = get_object_or_404(USER_ACCOUNT, pk=UID)
    a = Employee.objects.all()
    for x in a:
        x.Vacation_Leaves = x.Vacation_Leaves + 15
        x.Sick_Leaves = 15
        x.save()
    return render(request, 'payrollapp/settings.html', {'user':user})