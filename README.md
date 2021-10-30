

# Pacemaker Device Controller-Monitor (DCM)

##### 10/30/2021 Revision 1

##### This software is written in Python 3.8.8 and uses multiple open source libraries. 

#### Module gui2.py

This module contains GUI functions and global members that build the front end of the DCM user program. gui2 uses tkinter to design the layout and different windows of the DCM user program. Moreover it uses a theme wrapper that applies a different theme than the default tkinter colorway which enhances the user experience. 

This module only executes one function which is called initial_screen()  which instatiates the welcome screen. which calls other functions described in the table below to accomplish requirements for Assignment 1 as of 10/30/2021

| Global Variable (State Variable) | Description |
| -------------------------------- | ----------- |
| login_status                     |             |
| messags_status                   |             |
| num_users                        |             |

| Function                                            | Level of Scope | Black-Box Behavior                                           | Internal Behavior                                            |
| --------------------------------------------------- | -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| def programmable()                                  | Public         |                                                              |                                                              |
| def set_communication()                             | Public         |                                                              | Checks serial communication port at 'COMX' and reads a byte of code to recognizes unique pacemaker controllers. |
| def getdetails(username, password, retypedpassword) | Public         | returns 1 if successful and 0 if registration fails.         | gets called when the 'New Account' Button is pressed. Open file 'User_data.txt' to first check if username already exists within the file. If it does have that name the messags_status global variable updates to the corresponding message. If it does not exist it checks if the user limit num_users global variable is over 10 and updates messags_status accordingly. Which then finally writes to the file the user data if password and retypedpassword match. Closes file at the end. |
| def checkdetails()                                  | Public         | returns 1 if successfully logs in and 0 if wrong username or password. | gets called when the 'Log in' Button is pressed. Open file 'User_data.txt' to first check if username exists within the file. If it does not have that name the login_status global variable updates to the corresponding message. Then it checks if the password matches the username that exists and will update the login_status global variable to the corresponding message (whether the password is correct or not) |
| def register_new_user()                             | Public         |                                                              |                                                              |
| def intial_screen()                                 | Public         |                                                              |                                                              |



| UI Button | Called Function |
| --------- | --------------- |
|           |                 |
|           |                 |
|           |                 |

* Module Secret: LRL array and pulse_width_values which stores the possible allowed values for the entry to accept.
* Module Secret: We applied a theme we found on Github [here](https://github.com/rdbende/Forest-ttk-theme) which writes over the default tkinter theme.



#### Requirements Changes that are Likely to Change

 

#### Design decisions that are likely to change:



##### TO DO LIST:

- [ ] Design a new Database which saves corresponding programmable parameters for each user registered in the system.
- [ ] Fix input of 'space' in username and password entries. 

