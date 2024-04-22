from .models import *
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


def HDMF_UPLOAD(file_path):
    # Create a tkinter window
    print(1)
    root = tk.Tk()
    print(1)
    #root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a file")
    print(1)
    if file_path:
    # Load data from the selected file into a pandas DataFrame
        print(file_path)
        
        df = pd.read_excel(file_path)  # Assuming the file is CSV, adjust if needed
        file_path = file_path.split('/')[-1]
        print(file_path)
    
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
        print("Data imported and database cleared successfully.")
        root.destroy()
        return HttpResponse("Data imported and database cleared successfully.")
    else:
        print("No file selected.")
        root.destroy()
        return HttpResponse("Data imported and database cleared unsuccessfully.")
    
def SSS_UPLOAD(file_path):
    # Create a tkinter window
    print(1)
    root = tk.Tk()
    print(1)
    #root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a file")
    print(1)
    if file_path:
    # Load data from the selected file into a pandas DataFrame
        print(file_path)
        df = pd.read_excel(file_path)  # Assuming the file is CSV, adjust if needed
    
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
        print("Data imported and database cleared successfully.")
        root.destroy()
        return HttpResponse("Data imported and database cleared successfully.")
    else:
        print("No file selected.")
        root.destroy()
        return HttpResponse("Data imported and database cleared unsuccessfully.")

def PH_UPLOAD(file_path):
    # Create a tkinter window
    print(1)
    root = tk.Tk()
    print(1)
    #root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a file")
    print(1)
    if file_path:
    # Load data from the selected file into a pandas DataFrame
        print(file_path)
        df = pd.read_excel(file_path)  # Assuming the file is CSV, adjust if needed
    
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
        print("Data imported and database cleared successfully.")
        root.destroy()
        return HttpResponse("Data imported and database cleared successfully.")
    else:
        print("No file selected.")
        root.destroy()
        return HttpResponse("Data imported and database cleared unsuccessfully.")
    
def WitholdingTax_UPLOAD(file_path):
    # Create a tkinter window
    print(1)
    root = tk.Tk()
    print(1)
    #root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a file")
    print(1)
    if file_path:
    # Load data from the selected file into a pandas DataFrame
        print(file_path)
        df = pd.read_excel(file_path)  # Assuming the file is CSV, adjust if needed
    
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
        print("Data imported and database cleared successfully.")
        root.destroy()
        return HttpResponse("Data imported and database cleared successfully.")
    else:
        print("No file selected.")
        root.destroy()
        return HttpResponse("Data imported and database cleared unsuccessfully.")
    
def A_UPLOAD(file_path):
    # Create a tkinter window
    print(1)
    root = tk.Tk()
    print(1)
    #root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a file")
    print(1)
    if file_path:
    # Load data from the selected file into a pandas DataFrame
        print(file_path)
        Employee_check = Employee.objects.all
        holiday_check = HOLIDAY.objects.all
        Leave_check = Leave.objects.all
        holiday_true = ''
        leave_true = ''
        workinghours_df = pd.read_excel(file_path, sheet_name='cleaned data')  # Assuming the file is CSV, adjust if needed
    # Add data from the DataFrame into the database
        for _, row in workinghours_df.iterrows():
            #Data cleaning
            new_ID = ATTENDANCE_HISTORY.objects.latest('History_ID') + 1
            for x in Employee_check:
                if x.id_number == row['Name']:
                    Employee= get_object_or_404(Employee, id_number=x.id_number)
            for x in holiday_check:
                if x.date == row['Date']:
                    holiday_true = get_object_or_404(HOLIDAY, HOLIDAY_ID=x.Holiday_ID)
            for x in Leave_check:
                if x.date == row['Date']:
                    leave_true = get_object_or_404(Leave, Leave_ID=x.Leave_ID)
            try:
                TimeIn = datetime.strptime(row['In'], "%H:%M").time()
            except:
                pass
            try:
                TimeOut  = datetime.strptime(row['Out'], "%H:%M").time()
            except:
                pass
            try:
                TimeIn_2 = datetime.strptime(row['In_2'], "%H:%M").time()
            except:
                pass
            try:
                TimeOut_2 = datetime.strptime(row['Out_2'], "%H:%M").time()
            except:
                pass
            
            
            current_date_str = datetime.now().strftime('%d/%m/%Y')
            date = row['Date'][:-4] + current_date_str[-4:]#10BIT: Check this again

            try:
                OT_IN = datetime.datetime.strptime(row['OT_IN'], "%H:%M")
                OT_OUT = datetime.datetime.strptime(row['OT_OUT'], "%H:%M")
                OT = OT_OUT - OT_IN
                OT_Total = OT.seconds / 3600.0
            except:
                OT_Total = 0

            HoursWorked = 0
            HoursWorked_2 = 0
            try:
                HoursWorked = TimeOut - TimeIn
                HoursWorked_2 = TimeOut_2 - TimeIn_2
            except:
                try:
                    HoursWorked = TimeOut_2 - TimeIn
                except:
                    HoursWorked = TimeOut_2 - TimeIn_2
            HoursWorked = HoursWorked+HoursWorked_2

            ATTENDANCE_HISTORY.objects.create(History_ID=new_ID, Employee_ID=Employee, Date=date, OT=OT_Total, HoursWorked=HoursWorked)
            if TimeIn:
                ATTENDANCE_HISTORY.objects.latest('History_ID').update(TimeIn=TimeIn)
            if TimeOut:
                ATTENDANCE_HISTORY.objects.latest.latest('History_ID').update(TimeOut=TimeOut)
            if TimeIn_2:
                ATTENDANCE_HISTORY.objects.latest('History_ID').update(TimeIn_2=TimeIn_2)
            if TimeOut_2:
                ATTENDANCE_HISTORY.objects.latest('History_ID').update(TimeOut_2=TimeOut_2)

            #10BIT:Go back to fixing this
            if holiday_true != '':
                ATTENDANCE_HISTORY.objects.latest.latest('History_ID').update(Holiday_ID=holiday_true)
            if leave_true != '':
                ATTENDANCE_HISTORY.objects.latest.latest('History_ID').update(Leave_ID=leave_true)

        print("Data imported and database cleared successfully.")
        root.destroy()
        return HttpResponse("Data imported and database cleared successfully.")
    else:
        print("No file selected.")
        root.destroy()
        return HttpResponse("Data imported and database cleared unsuccessfully.")