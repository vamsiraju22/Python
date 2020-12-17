import pandas as pd
import PySimpleGUI as sg
import sys
import os
import docx
import time
import win32com.client as win32   


all_data=pd.read_excel('data.xlsx') #Make sure the columns donot contain trailing spaces.
all_data

data=all_data[['Service Line','Service','Type','Task/Service/Reports','Effort','Frequency_Neat','Frequency']]
data.drop(data[data['Service'].isna()==True].index, inplace = True)

def get_nextmonth_date_details():
    import calendar
    import datetime

    current_month=datetime.datetime.today().month
    current_day=datetime.datetime.today().day
    current_year=datetime.datetime.today().year
    
    _, num_days = calendar.monthrange(current_year, current_month)
    first_day = datetime.date(current_year, current_month, 1)
    last_day = datetime.date(current_year, current_month, num_days)
    
    def workdays(d, end, excluded=(6, 7)):
        working_days=[]
        day_week=[]
        working_days_week_dic={}
        day_dict={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday'}
        while d <= end:
            if d.isoweekday() not in excluded:
                working_days.append(str(d))
                working_days_week_dic[str(d)]=day_dict[d.isoweekday()]
                day_week.append(day_dict[d.isoweekday()])
            d += datetime.timedelta(days=1)
        return(working_days,working_days_week_dic,day_week)
    
    working_days,working_days_week_dic,day_week=workdays(first_day,last_day)
    
    ind=list(range(1,len(working_days)+1))
    working_days_dic=dict(zip(ind,working_days))
    ind_day_dic=dict(zip(ind,day_week))
    return(working_days_dic,working_days,working_days_week_dic,ind_day_dic)

def get_date_details():
    import calendar
    import datetime

    current_month=datetime.datetime.today().month
    current_day=datetime.datetime.today().day
    current_year=datetime.datetime.today().year
    
    _, num_days = calendar.monthrange(current_year, current_month)
    first_day = datetime.date(current_year, current_month, 1)
    last_day = datetime.date(current_year, current_month, num_days)
    
    def workdays(d, end, excluded=(6, 7)):
        working_days=[]
        day_week=[]
        working_days_week_dic={}
        day_dict={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday'}
        while d <= end:
            if d.isoweekday() not in excluded:
                working_days.append(str(d))
                working_days_week_dic[str(d)]=day_dict[d.isoweekday()]
                day_week.append(day_dict[d.isoweekday()])
            d += datetime.timedelta(days=1)
        return(working_days,working_days_week_dic,day_week)
    
    working_days,working_days_week_dic,day_week=workdays(first_day,last_day)
    
    ind=list(range(1,len(working_days)+1))
    working_days_dic=dict(zip(ind,working_days))
    ind_day_dic=dict(zip(ind,day_week))
    return(working_days_dic,working_days,working_days_week_dic,ind_day_dic)

working_days_dic,working_days,working_days_week_dic,ind_day_dic=get_date_details()

def get_week_day_dates(working_days_week_dic):
    keys_list,values_list=[],[]
    for i in working_days_week_dic.keys():
        keys_list.append(i)
        values_list.append(working_days_week_dic[i])
        
    monday_indlist=[]
    tuesday_indlist=[]
    wednesday_indlist=[]
    thursday_indlist=[]
    friday_indlist=[]
    for ind,i in enumerate(values_list):
        if i =='Monday':
            monday_indlist.append(ind+1)
        elif i == 'Tuesday':
            tuesday_indlist.append(ind+1)
        elif i == 'Wednesday':
            wednesday_indlist.append(ind+1)
        elif i == 'Thursday':
            thursday_indlist.append(ind+1)
        elif i == 'Friday':
            friday_indlist.append(ind+1)
    #print(monday_indlist,tuesday_indlist,wednesday_indlist,thursday_indlist,friday_indlist)
    total_list=[monday_indlist,tuesday_indlist,wednesday_indlist,thursday_indlist,friday_indlist]
    monday_list=[]
    tuesday_list=[]
    wednesday_list=[]
    thursday_list=[]
    friday_list=[]
    for ind,i in enumerate(total_list):
        #print(ind)
        for j in i:
            #print(keys_list[j-1])
            if ind ==0:
                monday_list.append(keys_list[j-1])
            elif ind == 1:
                tuesday_list.append(keys_list[j-1])
            elif ind == 2:
                wednesday_list.append(keys_list[j-1])
            elif ind == 3:
                thursday_list.append(keys_list[j-1])
            elif ind == 4:
                friday_list.append(keys_list[j-1])
    #print(monday_list,tuesday_list,wednesday_list,thursday_list,friday_list)
    week_day_dict={'Monday':monday_list,
                 'Tuesday':tuesday_list,
                 'Wednesday':wednesday_list,
                  'Thursday':thursday_list,
                  'Friday':friday_list
                 }
    return(week_day_dict)
week_day_dict=get_week_day_dates(working_days_week_dic)
count={
'Daily':len(working_days),
'Monday':len(week_day_dict['Monday']),
'Tuesday':len(week_day_dict['Tuesday']),
'Wednesday':len(week_day_dict['Wednesday']),
'Thursday':len(week_day_dict['Thursday']),
'Friday':len(week_day_dict['Friday'])}

df = pd.DataFrame(columns = data.columns) 
#Values should not contain X+10 or X+9 like that. only one single value.
next_working_days_dic,next_working_days,next_working_days_week_dic,next_ind_day_dic=get_nextmonth_date_details()

for i in data.iterrows():
    #print(i[1]['Frequency_Neat'])
    try:
        if i[1]['Frequency_Neat']=='Daily':
            for j in range(count[i[1]['Frequency_Neat']]):
                #print(j,"--",i[0])
                srs= pd.Series(data.iloc[i[0]])
                srs['Date']=working_days_dic[j+1]
                srs=srs.to_frame().T
                df = df.append(srs)
                
        elif i[1]['Frequency_Neat'] in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
             for j in range(count[i[1]['Frequency_Neat']]):
                #print(j,"--",i[0])
                for p,q in zip(['Monday','Tuesday','Wednesday','Thursday','Friday'],[j for i,j in week_day_dict.items()]):
                    if i[1]['Frequency_Neat'] ==p:
                        srs= pd.Series(data.iloc[i[0]])
                        for k_ind,k in enumerate(q):
                            if j==k_ind:
                                srs['Date']=k
                                srs=srs.to_frame().T
                                df = df.append(srs)
        else:
            if ('+' in i[1]['Frequency_Neat']):
                m,_,_,_=get_date_details()
                if int(i[1]['Frequency_Neat'].split('+')[1]) > max(m.keys()):
                    diff=int(i[1]['Frequency_Neat'].split('+')[1])-max(m.keys())
                    next_working_days_dic,_,_,_=get_nextmonth_date_details()
                    srs= pd.Series(data.iloc[i[0]])
                    srs['Date']=next_working_days_dic[diff]
                    srs=srs.to_frame().T
                    df = df.append(srs)                
                
                elif i[1]['Frequency_Neat'].split('+')[1] != '0':
                    #print(i[1]['Frequency_Neat'].split('+')[1],'  ',working_days_dic[int(i[1]['Frequency_Neat'].split('+')[1])])
                    srs= pd.Series(data.iloc[i[0]])
                    srs['Date']=working_days_dic[int(i[1]['Frequency_Neat'].split('+')[1])]
                    srs=srs.to_frame().T
                    df = df.append(srs)
                elif i[1]['Frequency_Neat'].split('+')[1] == '0':
                    #print(i[1]['Frequency_Neat'].split('+')[1])
                    srs= pd.Series(data.iloc[i[0]])
                    srs['Date']='Adhoc'
                    srs=srs.to_frame().T
                    df = df.append(srs)
                
                
                
                    
            elif ('-' in i[1]['Frequency_Neat']):
                #print("-----",i[1]['Frequency_Neat'].split('-')[1],'=======',str(max(a.keys())-int(i[1]['Frequency_Neat'].split('-')[1])))
                a,_,_,_=get_nextmonth_date_details()
                
                srs= pd.Series(data.iloc[i[0]])
                srs['Date']=working_days_dic[int(max(a.keys())-int(i[1]['Frequency_Neat'].split('-')[1]))]
                srs=srs.to_frame().T
                df = df.append(srs)
        
    except:
        print("exception")
        raise
df.reset_index(drop=True,inplace=True) 




def get_task_details(df,val):    
    temp_df=df.copy()
    temp_df['New Tasks'] = df['Service'].str.cat(df['Type'].astype(str).fillna('No SOP'),sep="-->").str.cat(df['Task/Service/Reports'].astype(str),sep="-->").str.cat(df['Frequency'].astype(str),sep="-->").copy()
    task_details=""
    for i,j in temp_df[temp_df['Date'].isin([val])].filter(items=['New Tasks']).items():
        for k in j:
            task_details+=str(k)
            task_details+='\n'
    return(task_details)



def get_task(df,val):
    temp_df1=df.copy()
    tasks=""
    for i,j in temp_df1[temp_df1['Date'].isin([val])].filter(items=['Task/Service/Reports']).items():
        for k in j:
            #print(k)
            tasks+=str(k)
            tasks+='\n'
    return(tasks)
    
def send_email(body, subject, recipient,signature, auto=True):
    import win32com.client as win32   

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    
    body=body+'<br>'*1+signature
    mail.HtmlBody = body
    if auto:
        mail.send
    else:
        mail.open 
def show_draft(body, subject, recipient,signature, auto=True):
    import win32com.client as win32   

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = body
    
    body=body+'<br>'*1+signature
    mail.HtmlBody = body
    if auto:
        mail.display()
    else:
        mail.open

resources_df=pd.read_excel('resources_list.xlsx')
resources_df
master_service_set=set()
for i,j in resources_df['Service'].items():
    for k in j.split(','):
        master_service_set.add(k)
mail_dic={}
for i,j in resources_df['Service'].items():
    for k in j.split(','):
        if k in list(master_service_set):
            if len(mail_dic)==0:
                mail_dic[k]=[resources_df['Email'][i]]
                #print(mail_dic)
                if len(mail_dic[k])==0:
                    mail_dic[k]=[resources_df['Email'][i]]
            else:
                #print("Dic",mail_dic)
                try:
                    if len(mail_dic[k])==0:
                        mail_dic[k]=[resources_df['Email'][i]]
                    else:
                        mail_dic[k].append(resources_df['Email'][i])
                except:
                    mail_dic[k]=[resources_df['Email'][i]]
                
print('')
          


      

named_tuple = time.localtime()
time_string=time.strftime("%Y-%m-%d",named_tuple)
time_string

sg.theme('DarkBlue17') 

layout = [ 
          [sg.Text('Task Reminder', size=(36, 1), justification='center', font=("Helvetica",20), relief=sg.RELIEF_RIDGE)],    
         
    [sg.Text('Service Line Name: '),sg.InputCombo(list(df['Service Line'].unique()),key='Service Line', size=(20, 2), enable_events=True),
      sg.Text('Service Name: '),sg.InputText('', key='Service',size=(20, 10),enable_events=True)],   
    
    [sg.Text('Date List:', pad=((60,10),(0,0))), (sg.InputCombo(working_days,key='date2', size=(20, 20), enable_events=True)),
                sg.Text('Date:', pad=((61,0),(0,0))),sg.InputText(time_string, key='date',size=(20, 10), pad=((10,50),(0,0)),enable_events=True)],
    
    [sg.Button('Show Details',size=(20,1)),sg.Button('Show Tasks',size=(20,1)),sg.Text('All Tasks:', pad=((20,10),(0,0))),
    sg.InputCombo(list(df['Service Line'].unique()),key='All_Service_Line', size=(20, 2), enable_events=True)],
    
    [sg.Text('Tasks-')],[ sg.Multiline('', key='tasks',size=(80, 25))],       
            
    [sg.Button('Send Mail'),sg.Button('Show Draft'),sg.Button('Update')]
         ]
updated_count=0
window = sg.Window('Remind Me',resizable=True).Layout(layout)
while True:
    event, values = window.read()
    if event == 'Show Tasks':
        if (len(values['Service']) ==0) and (len(values['All_Service_Line'])==0):
            sg.popup("Alert","Please enter a service value before looking for tasks.")
        elif (len(values['Service']) > 0) and (len(values['All_Service_Line'])==0):
            window['tasks'].update(get_task(df[df['Service']==values['Service']],values['date']))
        elif len(values['All_Service_Line'])>0:
            window['tasks'].update(get_task(df[df['Service Line']==values['All_Service_Line']],values['date']))        
        
    if event == 'Show Details':        
        if (len(values['Service']) ==0) and (len(values['All_Service_Line'])==0):
            sg.popup("Alert","Please enter a service value before looking for tasks.")
        elif (len(values['Service']) > 0) and (len(values['All_Service_Line'])==0):
            window['tasks'].update(get_task_details(df[df['Service']==values['Service']],values['date']))
        if len(values['All_Service_Line'])>0:
            window['tasks'].update(get_task_details(df[df['Service Line']==values['All_Service_Line']],values['date']))

    if event == 'Service Line':
        layout2=[ [sg.Text('Service Name: ')
                 ,sg.InputCombo(list(df[df['Service Line']==values['Service Line']]['Service'].unique()),key='Service2', size=(20, 10), enable_events=True)]]
        window2=sg.Window('Choose Service Name',resizable=True).Layout(layout2)
        event2, values2 = window2.read()
        if event2 == 'Service2':
            window['Service'].update(values2['Service2'])
            window2.close()
        window['All_Service_Line'].update('') 
        
    if event == 'date2':
        window['date'].update(values['date2'])
    
    if event == 'All_Service_Line':
        window['Service'].update('')
        window['Service Line'].update('')
        
    if event == 'Show Task Details':
        window['tasks'].update(get_task_details(df[df['Service']==values['Service']],values['date']))
        
        if event2 == 'Service2':
            window['Service'].update(values2['Service2'])
            window2.close()
        window['tasks'].update(get_task_details(df[df['Service Line']==values['All_Service_Line']],values['date']))
    
    if event == 'Show Draft':
        if len(values['Service']) <3:
            sg.popup("Alert","Please enter a service value before looking for tasks.")
        else:
            body="""Hello All,
    
            Please make sure the Reports for """+time_string+""" are delivered by EOD. \nReports for the day are :\n\n"""+get_task(df[df['Service']==values['Service']],values['date'])
            
            subject="Reminder for Tasks "+time_string+" for "+values['Service']+"."
            
            signature="Regards,<br>Asset Management Team"
            recipient=";".join(mail_dic[values['Service']])+";VK00489900@techmahindra.com"
            show_draft(body.replace('\n','<br>'), subject, recipient,signature, auto=True)
    if event == 'Send Mail':
        if len(values['Service']) <3:
            sg.popup("Alert","Please enter a service value before looking for tasks.")
        else:
            body="""Hello All,
    
            Please make sure the tasks for """+time_string+""" are completed by EOD. \nTasks for the day are :\n\n"""+get_task(df[df['Service']==values['Service']],values['date'])
            
            subject="Reminder for Tasks "+time_string+" for "+values['Service']+"."
            
            signature="Regards,<br>Asset Management Team"
            recipient=";".join(mail_dic[values['Service']])+";VK00489900@techmahindra.com"
            send_email(body.replace('\n','<br>'), subject, recipient,signature, auto=True)
    
    if event == 'Update':
        if values['date']==time_string:
           
            if (len(values['Service']) ==0) and (len(values['All_Service_Line'])==0):
                sg.popup("Alert","Please enter a service value before looking for tasks.")
            else:
                def checkbox_data(service,date): 
                    bf=df[df['Service']==service].copy()
                    a=[]
                    for i,j in bf[bf['Date'].isin([date])].filter(items=['Task/Service/Reports']).items():
                        for k in j:
                            a+=[sg.Checkbox(k,key=k)]
                    col=[a]
                    b=[]
                    for i in col:
                        for j in i:
                            b.append([j])
                    return(b)
                
                check_items=checkbox_data(values['Service'],values['date'])
                
                layout4 = [[ sg.Column(check_items,scrollable=True)], [sg.Button('Check'),sg.Button('Confirm'),sg.Button('Save and Close')]]
                window4 = sg.Window('Task Check Boxes ',resizable=True).Layout(layout4)
                
                if updated_count==1:
                    sg.popup('Looks like you have already updated the tasks.')
                    updated_count=0
                
                while True:
                    event4, values4 = window4.read()
                    
                    try:
    
                        if event4 == 'Check':                       
                            if os.path.isfile('Checked_data.xlsx'):
                                checked_df=pd.read_excel('Checked_data.xlsx')
                                if time_string not in  list(checked_df['Task Due Date'].unique()):
                                    os.remove('Checked_data.xlsx')    
                                else:
                                    test_df=pd.DataFrame(values4,index=['Status']).T.reset_index() 
                                    checked_df=pd.read_excel('Checked_data.xlsx')
                                    
                                    
                                    
                                    l1=list(checked_df['index'])
                                    l2=list(test_df['index'])
        
                                    for i_ind,i in enumerate(l1):
                                        for j_ind,j in enumerate(l2):
                                            if i == j :
                                                if checked_df['Status'][i_ind]==True:
                                                    window4[i].Update(disabled=True)
                                    del test_df  
                                    del checked_df
                            else:
                                sg.popup('There is no saved data to perform a check.')
                            
                           
                        if event4 =='Confirm': 
    
                            def confirm():
                                if os.path.isfile('Checked_data.xlsx'):
                                    checked_df= pd.read_excel('Checked_data.xlsx')  
                                    test_df=pd.DataFrame(values4,index=['Status']).T.reset_index()
                                    
                                    filter_cols=['index','Status']
                                    checked_df.reset_index(drop=True,inplace=True)
                                    checked_df=checked_df.filter(items=filter_cols)
                                    checked_df.reset_index(drop=True,inplace=True)
                                    
                                else:
                                    checked_df= pd.DataFrame(values4, index=['Status']).T.reset_index() #revisit
                                    checked_df.reset_index(drop=True,inplace=True)
                                    test_df=pd.DataFrame(values4,index=['Status']).T.reset_index()
                            
    
                                l1=list(checked_df['index'])
                                l2=list(test_df['index'])
                                test_df=pd.DataFrame(values4,index=['Status']).T.reset_index()
                                count=0
                                temp_list_index=[]
                                temp_list_status=[]
                                for j_ind,j in enumerate(l2):
                                    for i_ind,i in enumerate(l1):
                                        if i == j :
                                            #print(i_ind,j_ind,checked_df,test_df)
                                            if checked_df['Status'][i_ind]==False and test_df['Status'][j_ind] == True:
                                                checked_df['Status'][i_ind]=test_df['Status'][j_ind]
                                            if checked_df['Status'][i_ind]==True:
                                                checked_df['Status'][i_ind]=True
                                            if checked_df['Status'][i_ind] not in [True,False]:
                                                checked_df['Status'][i_ind]=False
                                        else:
                                            if test_df['Status'][j_ind] == True:
                                                
                                                temp_list_index.append(j)
                                                temp_list_status.append(True)
                                temp_dic={'index':list(set(temp_list_index)),'Status':[True for i in range(len(set(list(temp_list_index))))]}
                                checked_df=pd.DataFrame(temp_dic).append(checked_df,ignore_index=True)
                                filter_cols=['index','Status']
                                checked_df=checked_df.filter(items=filter_cols)
                                checked_df.append(test_df).reset_index(drop=True)
                                checked_df = checked_df.drop_duplicates(subset='index', keep="last")
                                checked_df.to_excel('Checked_data.xlsx', index=0)
                                
                                def get_check_data_details():
                                    checked_df = pd.read_excel('Checked_data.xlsx')
                                    checked_df = checked_df.reindex(columns=['Service Line', 'Service', 'index', 'Status', 'Task Due Date', 'Task Updated Date'])        
                                
                                    for i_ind,i in enumerate(checked_df['index']):
                                        if len(list(df[df['Task/Service/Reports']==i]['Service'].unique()))>1:
                                            sg.popup('Looks like a same task is present in 2 different Services. Please check the task name.')
                                        else: 
                                            checked_df['Service'][i_ind]=list(df[df['Task/Service/Reports']==i]['Service'].unique())[0]
                                            checked_df['Service Line'][i_ind]=list(df[df['Task/Service/Reports']==i]['Service Line'].unique())[0]
                                            checked_df['Task Due Date'][i_ind]=values['date']
                                            checked_df['Task Updated Date'][i_ind]=time_string
                                                                    
                                    return(checked_df)
                                test_checked_df=checked_df.copy()
                                test_checked_df.to_excel('test_checked_df.xlsx')
                                checked_df=get_check_data_details()
                                checked_df = checked_df.drop_duplicates(subset='index', keep="last")
                                checked_df.to_excel('Checked_data.xlsx', index=0)
                                
                            confirm()    
                            for i,j in values4.items():
                                if i in list(values4.keys()):
                                    if values4[i]==True:
                                        window4[i].Update(disabled=True)
                               
                            
                        if event4 == sg.WIN_CLOSED:
                            break    
                        
                        if event4 =='Save and Close':
                            window4.close()
                            confirm()
                                                    
                    except:
                        sg.popup('Make Sure you closed the Checked_data excel.')
                        raise
                        break
                        
        else:
            sg.popup('You can only update for todays reports')
             
                       
    if event == sg.WIN_CLOSED:
        break