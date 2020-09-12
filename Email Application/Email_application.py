#please install PySimpleGUI using pip install PySimpleGUI

import PySimpleGUI as sg
import sys

def send_email(body, subject, recipient,signature, auto=True):
    import win32com.client as win32   

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    
    body=body+'<br>'*2+signature
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
    
    body=body+'<br>'*2+signature
    mail.HtmlBody = body
    if auto:
        mail.display()
    else:
        mail.open
        

sg.theme('DarkBlue1')  # please make your windows colorful

layout = [
            [sg.Text('Lets begin the Show!!! Change the default fields if you feel necessary.',size=(50, 2), key='text')],
            [sg.Text('Mail Content', size=(15, 10)), sg.Multiline('', key='body',size=(50, 10))],
            [sg.Text('Email Address', size=(15, 1)), sg.InputText('vk00489900@techmahindra.com', key='maild',size=(50, 10))],
            [sg.Text('Email Subject', size=(15, 1)), sg.InputText('Daily Status Update', key='subject',size=(50, 10))],
            [sg.Button('Send Mail'),sg.Button('Show Draft'),sg.Button('Signature'),sg.Button('Default Body'),sg.Button('Close')]
            ]

window = sg.Window('Email Application', layout)
signature="default"
try:
  

    while True:
        event, values = window.read()
        if  event == sg.WIN_CLOSED or event == 'Close' :
            break
        if event == 'Send Mail':
            if signature =="default":
                signature="Regards,<br>Vamsi Raju Kadimisetty"
            send_email(values['body'].replace('\n','<br>'),values['subject'],values['maild'],signature)
            sg.popup('Your email is sent out!!!')
            window['text'].update('You have just sent an email!!!')
        elif event == 'Show Draft':
            if signature =="default":
                signature="Regards,<br>Vamsi Raju Kadimisetty."
            show_draft(values['body'].replace('\n','<br>'),values['subject'],values['maild'],signature)
            sg.popup('Your email open in draft now. Please check!!') 
            window['text'].update('You have just created an email draft!!!')
        if event == 'Signature':
            sig_layout=[[sg.Text('Signature', size=(15, 1)), sg.Multiline('', key='Signature',size=(20, 5))],
                       [sg.Button('Save Signarute'),sg.Button('Cancel')]]
            s_window = sg.Window('Enter a signature', sig_layout)
            s_event, s_values = s_window.read()
            if s_event=='Save Signarute':
                signature=s_values['Signature'].replace('\n','<br>')
                s_window.close()
                window['text'].update('You have just updated a signature from default one to a new Signature!!!')
            elif s_event=='Cancel':
                s_window.close()
                
        if event == 'Default Body':
            default_body="""Hello Kejas,<br><br>I have completed all my tasks for today.<br>
            There were no show stoppers. I have also updated my BAU Tracker."""
            default_body=default_body.replace('\n','<br>')
            window['body'].update(default_body)
except:
    print("Some error")
    sys.exit()
window.close()
