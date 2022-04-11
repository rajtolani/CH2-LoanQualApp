# Project Title
Loan Qualfier Application : Instaneously matches avialable loan programs to Client needs to allow our loand analysts to process and fund loans quickly.

---

## Technologies

This application has been implemented using interpetive language Python. Python has a powerful set of pre built libraries which allows rapid development of financial applications. The Loan Qualifier Application uses the following available python packages
    CSV : This has all the functions to read, write and manipulate Comma Seprated files.
    Fire : Powerful library of functions for file i/o
    Questionary : allows interactive communication using Commant Line Interface with the user of the application
The development was done using the VS Code IDE.
    
---

## Installation Guide

This application is written in python. To run this application you need to have python installed on your computer.It is recomended that python version 3.9.7 or higher is installed
This application relies on python libraries Fire and Questionary. This packages need to be installed. To check and install the packages do the following
>
  > - Open Command Window
  > - type pip freeze

>This will list the packages installed. If fire and questionary are not listed do the following
> - type pip install fire
> - type pip install questionary

>Check to see if the installs were succesfull

> - type pip freeze

Copy the file app.py and the Qualify subfolder to the working directory/folder you are going to work in.

Make sure you have the daily rate sheet in the working folder of a folder where you know the relative path from the working folder

---

## Usage

Before running this application, make sure you have access to the daily_rate_sheet.csv

Open terminal. Confirm you have the correct version of python and libraries as shown in the installation section

type python app.py

You will be prompted "Enter a file path to a rate-sheet (.csv)" : <path/name-of-daily_rate_sheet>

This will be followed by series of prompts to get the loand applicant info

> "What's your credit score?" <applicant's credit score>

> "What's your current amount of monthly debt?" <applicant's current monthly debt>

> "What's your total monthly income?" <applicant's monthly income>

> "What's your desired loan amount?" <Loan amount on application>

> "What's your home value?" <Value of home for which the loan is needed>

This application will then calculate and print the monthly debt/income ration and loan/value ratio

It will compare the requirements againt the list of loans available and filter the loans which the meet the criterion

If no loans are found to meet the criterion the CLI will print a message saying no loans

Else it will be print the number of loans which do meet the Criterion

At this point it will prompt if output file with the list of qualified loans is need. If the answer is year it will prompt for name of the output file and then create a csv file with the list of qualified loans

---

## Contributors

The starters files which did most of the heavy lifting were provided by the Bootcamp staff. Thank You

The remainder including save_csv function and save_qualifying_loans functions were written by

     Raj Tolani
     admin@tolanicollection.com

---

## License

Use of this application and underlying software is governed by Academic Free License which is a variant of the Open Software License. This license can be reviewed at https://choosealicense.com/licenses/afl-3.0/

