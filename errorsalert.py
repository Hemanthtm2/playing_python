#!/usr/bin/python 


error_sys=input('Enter the alert system\n')
error_sev=input('Enter the severity\n')

#error_sys='console'
#error_sev='critical'
error_msg='OMG! something terribly went wrong!'


if error_sys=='console':
   print(error_msg)

elif error_sys=='email':
     if error_sev=='warning':
        print('Something went wrong')
     elif error_sev=='critical':
        print(error_msg)

     else:
        print('Not much to worry,Just make a not of it and fix it in the morning')
