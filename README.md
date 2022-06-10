# Email_Label

## Description
A teacher is currently receiving many emails from students and would like to have an app which would automattically analyse those messages and help classify the intentions behind the messages.
This is a python project which helps do just that, by taking the email message as input, analysing the presence or absence of the word "share" in order to determine if the student is confirming to have shared the contact detail(email address) of the teacher to their friends, or if the student is requesting for permission to share the contact details (email address) to their friends.The __email_labeler.py__ script contains the code to analyse and classify these emails.

To test the code, and be sure it returns the outputs expected, the __test_email_labeler.py__ file uses the unnittest package in python to run assert statements and provide results if the tests are Ok or if the tests failed.

Finally, because no external packages were used, just basic inbuilt functions and modules in python, the __requirements.txt__ file is empty and so it will be an easy install-and-run in the next section.


## How to Install and run the Program
The first thing is to ensure you have python installed in your machine.
You can verify this by running the following command in your command prompt (if using a windows system) or in the bash shell (if using a mac system)

```log
python --version
```
If you do not have python installed, you can follow these [instrutions](https://phoenixnap.com/kb/how-to-install-python-3-windows) (if using a windows system) or these [instuctions](https://www.dataquest.io/blog/installing-python-on-mac/) (if using a mac system).
* Download the code:
  While on GitHub, and go to the main page of the project's repository and above the list of the 03 files, click on the green __Code__ button.Copy the url that appears (the default is HTTPS).
* Downloading to your local destination folder:
  Open Git Bash, ensure you change your current working directory to the destination folder you intend to clone the code into. Then type the following command and then press __Enter__
```log
$ git clone https://github.com/Bandolo/Email_Label.git
```
 * Run the script
  To run the code locally then, all you need to do is type the folowing commmand in your Git Bash
```log
 $ python email_labeler.py
```
  * To run test code , you need to type this command
```log
 $ python test_email_labeler.py
```

## A few possible modifications
  1. An input prompt could be added to the __email_labeler.py__ script, which would ask the user to input an email message, and then the script will return a label  with the classification of the email.
  So adding the 02 lines below will prompt the user to input an email and also call the __email_labeler.py__ function to return the results of the classification.
 ```log
    email = input("Please copy and paste the email here: ")
    print(f'Label Results: {email_label("share",email)}')
 ```
   2. A third label could be added to classify future intentions to share the teacher's email. The third label could be "Student will share". Phrases like "I shall share" or "I will share" would fit into this third class.
