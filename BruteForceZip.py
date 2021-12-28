from os import path
import zipfile
import time

folderpath = "/Users/vanshbafna/Desktop/module5/PROJ223/CrackPassword.zip"
zipf = zipfile.ZipFile(folderpath)
tried = 0

if not zipf:           #Checks if the file is password encrypted
    print('The zipped file/folder is not password protected! You can successfully open it!')  #Notifies if the zipped file/folder is not password encrypted

else:
    starttime = time.time()             #Save the start time
    result = 0                          #Intialize a variable result with zero. '0' will indicate Failure, while '1' will idicate Success
    c = 0                               #Initialize a variable c to keep the count of passwords tried

    #Build a character array including all numbers,lowercase letter, uppercase letters and special haracters. Total 10+26+26+33 = 95 characters
    characters =['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']

    
    print("Brute Force Started...")
    
    #If still the password is not found i.e. result = 0, the below loop will try four character passwords. 81450625 Possible Combinations        
    if(result == 0):
        print("Checking for 4 character password...")
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess = str(i) + str(j) + str(k) + str(l)
                        password=guess.encode('utf8').strip()
                        print("Trying to decode password by: " + guess)
                        c=c+1
                        tried += 1
                        print("password tried: " + str(tried))
                        try:
                            with zipfile.ZipFile(folderpath,'r') as zf:
                                zf.extractall(pwd=password)
                                print("\t\t\t\t    __xxxxxxxxxxxxxxxx___.\n \t                      _gxXXXXXXXXXXXXXXXXXXXXXXXX!x_\n \t                   __x!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!x_\n \t                ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx_\n \t              ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!_\n \t            _!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.\n \t          gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs\n \t        ,!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.\n \t       g!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t      iXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t     ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx\n \t     !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx\n \t   ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx\n \t   !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi\n \t  dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t  !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n \t   XXXXXXXXXXXXXXXXXXXf~~~VXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvvvvXXXXXXXXXXXXXX!\n \t   !XXXXXXXXXXXXXXXf`       'XXXXXXXXXXXXXXXXXXXXXf`          '~XXXXXXXXXXP\n \t    vXXXXXXXXXXXX!            !XXXXXXXXXXXXXXXXXX!              !XXXXXXXXX\n \t     XXXXXXXXXXv`              'VXXXXXXXXXXXXXXX                !XXXXXXXX!\n \t     !XXXXXXXXX.                 YXXXXXXXXXXXXX!                XXXXXXXXX\n \t      XXXXXXXXX!                 ,XXXXXXXXXXXXXX                VXXXXXXX!\n \t      'XXXXXXXX!                ,!XXXX ~~XXXXXXX               iXXXXXX~\n \t       'XXXXXXXX               ,XXXXXX   XXXXXXXX!             xXXXXXX!\n \t        !XXXXXXX!xxxxxxs______xXXXXXXX   'YXXXXXX!          ,xXXXXXXXX\n \t         YXXXXXXXXXXXXXXXXXXXXXXXXXXX`    VXXXXXXX!s. __gxx!XXXXXXXXXP\n \t          XXXXXXXXXXXXXXXXXXXXXXXXXX!      'XXXXXXXXXXXXXXXXXXXXXXXXX!\n \t          XXXXXXXXXXXXXXXXXXXXXXXXXP        'YXXXXXXXXXXXXXXXXXXXXXXX!\n \t          XXXXXXXXXXXXXXXXXXXXXXXX!     i    !XXXXXXXXXXXXXXXXXXXXXXXX\n \t          XXXXXXXXXXXXXXXXXXXXXXXX!     XX   !XXXXXXXXXXXXXXXXXXXXXXXX\n \t          XXXXXXXXXXXXXXXXXXXXXXXXx_   iXX_,_dXXXXXXXXXXXXXXXXXXXXXXXX\n \t          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXP\n \t          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t           ~vXvvvvXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf\n \t                    'VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvv~\n \t                      'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX~\n \t                  _    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`\n \t                 -XX!  !XXXXXXX~XXXXXXXXXXXXXXXXXXXXXX~   Xxi\n \t                  YXX  '~ XXXXX XXXXXXXXXXXXXXXXXXXX`     iXX`\n \t                  !XX!    !XXX` XXXXXXXXXXXXXXXXXXXX      !XX\n \t                  !XXX    '~Vf  YXXXXXXXXXXXXXP YXXX     !XXX\n \t                  !XXX  ,_      !XXP YXXXfXXXX!  XXX     XXXV\n \t                  !XXX !XX           'XXP 'YXX!       ,.!XXX!\n \t                  !XXXi!XP  XX.                  ,_  !XXXXXX!\n \t                  iXXXx X!  XX! !Xx.  ,.     xs.,XXi !XXXXXXf\n \t                  XXXXXXXXXXXXXXXXX! _!XXx  dXXXXXXX.iXXXXXX\n \t                   VXXXXXXXXXXXXXXXXXXXXXXXxxXXXXXXXXXXXXXXX!\n \t                   YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXV\n \t                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!\n \t                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf\n \t                       VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf\n \t                         VXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`\n \t                          ~vXXXXXXXXXXXXXXXXXXXXXXXf`\n \t                              ~vXXXXXXXXXXXXXXXXv~\n \t                                 '~VvXXXXXXXV~~\n \t                                       ~~")
                                print(" _                _            _\n | |              | |          | |\n | |__   __ _  ___| | _____  __| |\n | '_ \ / _` |/ __| |/ / _ \/ _` |\n | | | | (_| | (__|   <  __/ (_| |\n |_| |_|\__,_|\___|_|\_\___|\__,_|\n")
                                print("Success! The password is: "+ guess)
                                endtime = time.time()            #Save the end time
                                result = 1                       #Set result variable to 1 on success
                                break                            #If the password is found break from i for loop
                        except:
                            pass
                    if result == 1:
                        break                           #If the password is found break from j for loop
                if result == 1:
                    break                               #If the password is found break from k for loop
            if result == 1:
                break                                   #If the password is found break from l for loop

    #Finally, if the password is not found even after appying all possile combination of characters upto 4 character length, notify the user as below, else print congratulations
    if(result == 0):

        print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
    else:
        duration = endtime - starttime
        print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
