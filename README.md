# JS-Probe
Do you want to keep looking for modifications in the js scripts of your targets? The JS Probe can do this to you!

PLEASE READ THIS!

*JS PROBE* is a tool made with python, that has the ability to search for modifications in the js files

# HOW IT WORKS?

The script will get a list containing the JS URLS. So, the code will start requesting all the JS urls and analyzing if any change happened

If a modification is detected, an email will be sent to you, including a notification in your desktop

![2](https://github.com/user-attachments/assets/03f9af5a-7251-4490-b9ba-d48e0a3c58fa)


# HOW TO INSTALL IT?

First, clone the repository

```sudo git clone https://github.com/HeyTenebrisVenator/JS-Probe.git```

Then, you install the requirement to the script work properly

```sudo pip install -r requirements.txt```

# GETTING STARTED

The Reporistory have two scripts, and both need to be runned.

THE SCRIPTS:

The first script is the *JS_PROBE*

```sudo python3 JS_PROBE```

This first script is the probe configurator. He'll be used to create and delete probes.

When you run it, he'll enter in the *User interactor mode*.

COMMANDS:
help - help to the user

create - used to create a probe that wll be used by the script to determine if the application changed the js file

delete - delete an probe

clear - used to clean the terminal

# CREATING A PROBE:

To create a probe you can, in the user interactor mode, use the command create

>>  create

After that, the script will do some questions to you. 


First, he'll ask you the name of the probe

Secondly, the file containing the JS URLS

Third, he'll ask if you want to configure an Email sending.

If you put 'n' or 'N', you'll not configure the email.

But, if you put 'y' or 'Y', you'll need to answer some questions

FROM >>  - from the X email. 

TO >>    - To the X email.

API KEY >> - The Key to send emails. You can create your here: https://myaccount.google.com/u/2/apppasswords


EX:

Welcome!

Starting interation with user

  >>  create

Name of the probe >> MY_PROBE

Location of the file  >>  /home/user/Documents/urls

FOUND!

generating a copy

OK!

Want to configure email sendings? Y/n >> y

FROM >> myemail@gmail.com

TO >> mysecondemail@gmail.com

API KEY >> xxxxxxxxxxx

DONE!

# DELETING A PROBE:

To delete a probe, you need to be in the user interactor mode, and put the command

>> delete

After that, put the name of the Probe

EX:

Welcome!

Starting interation with user

  >>  delete

Name of the probe  >>  MY_PROBE


# RUNNING THE PROBE

!IMPORTANT! BEFORE YOU RUN THE SCRIPT, GO TO THE DIRECTORY *Modules/job* AND MODIFY THE LINE *User=YOUR USER HERE* TO YOUR USER.

![3](https://github.com/user-attachments/assets/39e65c1b-5053-4de5-b410-5ee050957b0c)


To start the probe, you need to run the script *start_probe.py*

```sudo python3 start_probe.py```

The first thing that you need to know is that the code work with systemctl. So you can control all the features with it

When you run the start_probe.py, a module in the directory *Modules/probe* will be cloned to the */usr/bin/probe_for_js*

After this, the *Modules/job* will be cloned to the */usr/lib/systemd/system/js_probe.service*

REMEMBER TO MODIFY THE *job* WITH YOUR USER

![1](https://github.com/user-attachments/assets/285f0e23-db82-41b5-a117-a2b3450b8cf3)


# CONFIGURATING SYSTEMCTL

When you run the start_probe.py, a job is created, and it's automatically created to run every time you boot the computer.

If you want to stop the script, you can use the command:

```sudo systemctl stop js_probe.service```

If you want to restart the script, you can use the command:

```sudo systemctl restart js_probe.service```


If you want to start the script, you can use the command:

```sudo systemctl start js_probe.service```

If you want to enable it to start the script in the boot, you can use the command:

```sudo systemctl enable js_probe.service```

If you want to disable it to start the script in the boot, you can use the command:

```sudo systemctl disable js_probe.service```
