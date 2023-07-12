#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jul 11, 2023 06:58:25 AM CEST  platform: Windows NT

import sys
import requests
import tkinter.scrolledtext as sc
from tkinter import filedialog
import os
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import AdminGet_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    AdminGet_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    AdminGet_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x610+383+49")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Get Admin Banel ")
        top.configure(background="#d9d9d9")
        admin_list = ['admin.php',
                'admin.html',
                'index.php',
                'login.php',
                'login.html',
                'administrator',
                'adminpanel',
                'admin',
                'cpanel',
                'login',
                'wp-login.php',
                'administrator',
                'admins','Admin/Login.aspx',
                'logins',
                'login.asp',
                'admin.asp',
                'adm/',
                'admin/',
                'admin/account.html',
                'admin/login.html',
                'admin/login.htm',
                'admin/controlpanel.html',
                'admin/controlpanel.htm',
                'admin/adminLogin.html',
                'admin/adminLogin.htm',
                'admin.htm',
                'admin.html',
                'adminitem/',
                'adminitems/',
                'administrator/',
                'administrator/login.%EXT%',
                'administrator.%EXT%',
                'administration/',
                'administration.%EXT%',
                'adminLogin/',
                'adminlogin.%EXT%',
                'admin_area/admin.%EXT%',
                'admin_area/',
                'admin_area/login.%EXT%',
                'manager/',
                'superuser/',
                'superuser.%EXT%',
                'access/',
                'access.%EXT%',
                'sysadm/',
                'sysadm.%EXT%',
                'superman/',
                'supervisor/',
                'panel.%EXT%',
                'control/',
                'control.%EXT%',
                'member/',
                'member.%EXT%',
                'members/',
                'user/',
                'user.%EXT%',
                'cp/',
                'uvpanel/',
                'manage/',
                'manage.%EXT%',
                'management/',
                'management.%EXT%',
                'signin/',
                'signin.%EXT%',
                'log-in/',
                'log-in.%EXT%',
                'log_in/',
                'log_in.%EXT%',
                'sign_in/',
                'sign_in.%EXT%',
                'users/',
                'users.%EXT%',
                'accounts/',
                'accounts.%EXT%',
                'bb-admin/login.%EXT%',
                'bb-admin/admin.%EXT%',
                'bb-admin/admin.html',
                'administrator/account.%EXT%',
                'relogin.htm',
                'relogin.html',
                'check.%EXT%',
                'relogin.%EXT%',
                'blog/wp-login.%EXT%',
                'users/admin.%EXT%',
                'registration/',
                'user/admin.%EXT%',
                'processlogin.%EXT%',
                'checklogin.%EXT%',
                'checkuser.%EXT%',
                'checkadmin.%EXT%',
                'isadmin.%EXT%',
                'authenticate.%EXT%',
                'authentication.%EXT%',
                'authuser.%EXT%',
                'auth.%EXT%',
                'authuser.%EXT%',
                'authadmin.%EXT%',
                'cp.%EXT%',
                'modelsearch/login.%EXT%',
                'moderator.%EXT%',
                'moderator/',
                'controlpanel/',
                'controlpanel.%EXT%',
                'admincontrol.%EXT%',
                'adminpanel.%EXT%',
                'fileadmin/',
                'fileadmin.%EXT%',
                'sysadmin.%EXT%',
                'admin1.%EXT%',
                'admin1.html',
                'admin1.htm',
                'admin2.%EXT%',
                'admin2.html',
                'yonetim.%EXT%',
                'yonetim.html',
                'yonetici.%EXT%',
                'yonetici.html',
                'phpmyadmin/',
                'myadmin/',
                'ur-admin.%EXT%',
                'ur-admin/',
                'Server.%EXT%',
                'Server/',
                'wp-admin/',
                'administr8.%EXT%',
                'administr8/',
                'webadmin/',
                'webadmin.%EXT%',
                'administratie/',
                'admins/',
                'admins.%EXT%',
                'administrivia/',
                'Database_Administration/',
                'useradmin/',
                'sysadmins/',
                'admin1/',
                'system-administration/',
                'administrators/',
                'pgadmin/',
                'directadmin/',
                'staradmin/',
                'ServerAdministrator/',
                'SysAdmin/',
                'administer/',
                'LiveUser_Admin/',
                'sys-admin/',
                'typo3/',
                'panel/',
                'cpanel/',
                'cpanel_file/',
                'platz_login/',
                'rcLogin/',
                'blogindex/',
                'formslogin/',
                'autologin/',
                'manuallogin/',
                'simpleLogin/',
                'utility_login/',
                'showlogin/',
                'memlogin/',
                'login-redirect/',
                'sub-login/',
                'wp-login/',
                'login1/',
                'dir-login/',
                'login_db/',
                'xlogin/',
                'smblogin/',
                'customer_login/',
                'UserLogin/',
                'acct_login/',
                'bigadmin/',
                'project-admins/',
                'phppgadmin/',
                'pureadmin/',
                'sql-admin/',
                'radmind/',
                'openvpnadmin/',
                'wizmysqladmin/',
                'vadmind/',
                'ezsqliteadmin/',
                'hpwebjetadmin/',
                'adminpro/',
                'newsadmin/',
                'Lotus_Domino_Admin/',
                'bbadmin/',
                'vmailadmin/',
                'Indy_admin/',
                'ccp14admin/',
                'irc-macadmin/',
                'banneradmin/',
                'sshadmin/',
                'phpldapadmin/',
                'macadmin/',
                'administratoraccounts/',
                'admin4_account/',
                'admin4_colon/',
                'radmind-1/',
                'Super-Admin/',
                'AdminTools/',
                'cmsadmin/',
                'SysAdmin2/',
                'globes_admin/',
                'cadmins/',
                'phpSQLiteAdmin/',
                'navSiteAdmin/',
                'server_admin_small/',
                'logo_sysadmin/',
                'power_user/',
                'system_administration/',
                'ss_vms_admin_sm/',
                'bb-admin/',
                'panel-administracion/',
                'instadmin/',
                'memberadmin/',
                'administratorlogin/',
                'adm.%EXT%',
                'admin_login.%EXT%',
                'panel-administracion/login.%EXT%',
                'pages/admin/admin-login.%EXT%',
                'pages/admin/',
                'acceso.%EXT%',
                'admincp/login.%EXT%',
                'admincp/',
                'adminarea/',
                'admincontrol/',
                'affiliate.%EXT%',
                'adm_auth.%EXT%',
                'memberadmin.%EXT%',
                'administratorlogin.%EXT%',
                'modules/admin/',
                'administrators.%EXT%',
                'siteadmin/',
                'siteadmin.%EXT%',
                'adminsite/',
                'kpanel/',
                'vorod/',
                'vorod.%EXT%',
                'vorud/',
                'vorud.%EXT%',
                'adminpanel/',
                'PSUser/',
                'secure/',
                'webmaster/',
                'autologin.%EXT%',
                'webmaster.%EXT%',
                'userlogin.%EXT%',
                'userlogin.%EXT%',
                'cmsadmin.%EXT%',
                'usr/',
                'root/',
                'secret/',
                'admin/login.%EXT%',
                'admin/adminLogin.%EXT%',
                'moderator.php',
                'moderator.html',
                'moderator/login.%EXT%',
                'moderator/admin.%EXT%',
                'yonetici.%EXT%',
                '0admin/',
                '0manager/',
                'aadmin/',
                'cgi-bin/login%EXT%',
                'login1%EXT%',
                'login_admin/',
                'login_admin%EXT%',
                'login_out/',
                'login_out%EXT%',
                'login_user%EXT%',
                'loginerror/',
                'loginok/',
                'loginsave/',
                'loginsuper/',
                'loginsuper%EXT%',
                'login%EXT%',
                'logout/',
                'logout%EXT%',
                'secrets/',
                'super1/',
                'super1%EXT%',
                'super_index%EXT%',
                'super_login%EXT%',
                'supermanager%EXT%',
                'superman%EXT%',
                'superuser%EXT%',
                'supervise/',
                'supervise/Login%EXT%',
                'super%EXT%','admin/login.php','adm/login.php',
        'painel/login.php','admin/login.asp','admin_login.asp']
        #for i in admin_list:
        #    p = 'https://www.facebook.com/'+i
        #    ck = requests.get(p)
        #    if ck.status_code == 200:
        #        print(p)
        #    else:
        #        print("+===> i ")
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=51, width=604)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Coded By {SAID AYADY} [ Hackers Maroc ]''',font='-family {Showcard Gothic} -size 18 -weight bold')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.082, relheight=0.172
                , relwidth=0.975)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.017, rely=0.086, height=25, width=564)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Get Info For Bread Forss''',font='-family {Showcard Gothic} -size 16 -weight bold')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.017, rely=0.381, height=17, width=124)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Enter Word List''',font='-family {Showcard Gothic} -size  8 -weight bold')

        self.Label3_1 = tk.Label(self.Frame1)
        self.Label3_1.place(relx=0.017, rely=0.667, height=17, width=124)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#d9d9d9")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Enter Web Site''',font='-family {Showcard Gothic} -size  8 -weight bold')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.239, rely=0.381, height=20, relwidth=0.605)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry1_1 = tk.Entry(self.Frame1)
        self.Entry1_1.place(relx=0.239, rely=0.667, height=20, relwidth=0.503)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.872, rely=0.286, height=34, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse''',font='-family {Showcard Gothic} -size  8 -weight bold')

        self.Button1_1 = tk.Button(self.Frame1)
        self.Button1_1.place(relx=0.769, rely=0.667, height=24, width=127)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Start bread''',font='-family {Showcard Gothic} -size  8 -weight bold')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.017, rely=0.279, relheight=0.713
                , relwidth=0.975)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.017, rely=0.115, relheight=0.494
                , relwidth=0.966)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Frame4 = tk.Frame(self.Frame2)
        self.Frame4.place(relx=0.017, rely=0.641, relheight=0.333
                , relwidth=0.966)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")

        br = ttk.Treeview(self.Frame3,selectmode='browse')
        br.place(x=0,y=0,width=556,height=205)
        br['columns'] = ('1')
        br.column('0',width=546,anchor='c' )
        br.column('1',width=10,anchor='c' )


        br.heading('#0',text='Link',anchor='c')
        br.heading('#1',text='Statis Code',anchor='c')

        scrol = sc.ScrolledText(self.Frame4)
        scrol.place(x=0 , y=0,height=137
                , width=557)
        scrol.tag_config('erorr',foreground='red')
        scrol.tag_config('true',foreground='green')
        scrol.tag_config('strat',foreground='white',background='blue')
        def checkFile():
            fileWorlList = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                title="open Worl List file",
                                                filetype=(('Text File','.txt'),
                                                        ('TEXT File','TXT'),
                                                        ('XML File','.xml'),
                                                        ('XML File','XML'),
                                                        ('All File','ALL')
                                                        )
                                                )
            self.Entry1.insert(0, fileWorlList)
        self.Button1.configure(command=checkFile)
        def startG():
            url = self.Entry1_1.get()
            scrol.insert('end', f'Start Bred Fors For Admin Banel : {url}','strat')
            for i in admin_list:
                p = f'{url}/{i}'
                chek = requests.get(p)
                self.Label4 = tk.Label(self.Frame2)
                self.Label4.place(relx=0.051, rely=0.023, height=31, width=534)
                self.Label4.configure(background="#d9d9d9")
                self.Label4.configure(disabledforeground="#a3a3a3")
                self.Label4.configure(foreground="green")
                self.Label4.configure(text=f'''Start Scan : {p}''',font={'Arial',16})
                if chek.status_code == 200:
                    br.insert(parent='',index=0, text=(p),values=('200'))
                    scrol.insert('end', f'\n ✅   valud   : {p}','true')
                else:
                    scrol.insert('end', f'\n ❌ No Valude : {p}','erorr')
                    continue
            scrol.insert('end', f'Finesh Bred Fors For Admin Banel : {url}','strat')
            self.Label4 = tk.Label(self.Frame2)
            self.Label4.place(relx=0.051, rely=0.023, height=31, width=534)
            self.Label4.configure(background="#d9d9d9")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(foreground="red")
            self.Label4.configure(text=f'''\n Finesh Scan : {url}''',font={'Arial',16})
        import threading
        def geStart():
            threading.Thread(target=startG).start()
        self.Button1_1.configure(command=geStart)

if __name__ == '__main__':
    vp_start_gui()





