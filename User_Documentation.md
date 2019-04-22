# Psychiatric Prescribing Guide: User Support
---
[Developer Documentation](https://github.com/Brick7Face/psychiatric-guide-app/blob/development/README.md)
can be found by clicking on the link.

# 1. Web Application Overview


---


## 1.1 Project Description

Prescribing the right medicine and treatment is difficult, and most medical professionals depend on prescribing
pocket guides to help ensure the best treatment plan possible is given to their patients. One major issue psychiatric
prescribers have is that there is no electronic version of the clinical practice guidelines they use every day. They
 must find the needed information by looking through paper copies, which can add unnecessary time and frustration to
 both the prescribers and the patient's experience. This projects aim is to provide an electronic intuitive guide and
 tool to help psychiatric prescribers give the best care they possibly can to their patients.      

The web application designed to accomplish this task will help simplify and organize the psychiatric prescription
process. Having all the prescribing guidelines stored in a digital format also allows the provided information to
be easily updated and immediately distributed. This helps medical professionals provide more accurate treatment
plans to the people that need it. The information provided on this application is based on the "Prescribing Pocket
Guide 2012", which deals with prescribing in the domain of both Depression and Bipolar disorder. In the future,
this app could be expanded into other medical domains. The website provides a central location for doctors to
reference information in the pocket guide as well as track patient progress through the different treatment processes.


## 1.2 Before Getting Started


Only certified psychiatric prescribers are permitted to create an account to view and track patient information.  
Anyone can view the information provided in the general Prescribing Pocket Guide on our website.

> This pocket guide is intended for the use of licensed medical care providers only. Patients and/or individuals
who are not licensed medical care providers who come into possession of this guide should confirm any information
obtained from or through this guide with other sources, and review all information regarding any medical condition
or treatment with a physician.

> Although every effort has been made to ensure that drug doses and other information are presented accurately in
this guide, the ultimate responsibility rests with the prescribing physician. Neither the publisher, the sponsor,
nor the authors can be held responsible for errors or for any consequences arising from the use of information
contained herein. Readers are strongly urged to consult any relevant primary literature. No claims or endorsements
are made for any drug or compound currently under clinical investigation.  

> The information provided herein is not intended or implied to be a substitute for professional medical advice,
diagnosis or treatment. All content, including text, graphics, images and information contained on or available
through this guide is for general information purposes only.  You are encouraged to confirm any information obtained
from or through this guide with other sources and review all information regarding any medical condition or treatment
as you deem is appropriate in your medical judgment. The publisher does not advise or recommend to its reader's
treatment or action with regard to matters relating to a patient's health or well-being other than to suggest
that readers consult appropriate health-care materials in such matters. No action should be taken based solely
on the content of this guide.

> NEVER DISREGARD YOUR (OR ANOTHER'S) PROFESSIONAL MEDICAL OPINION OR TRAINING BECAUSE OF SOMETHING YOU HAVE READ
IN THIS POCKET GUIDE."

*   _Prescribing Pocket Guide 2012_ - Carla Cobb, Pharm.D., BCPP; Leanna Donner, Pharm.D.; D'Anne Holley, RPh


# 2. Getting Started


---


## 2.1 How To Visit the Webpage

Obtaining the software is as easy as visiting a website. There are no downloads necessary, as it is a web-hosted
application that can be accessed anywhere by following The link below.


## [Psychiatric Prescribing Pocket Guide](https://psychiatric-guide.appspot.com/)


# 3. How to Use the Web App



---


You must be registered as a prescriber to login and use the site. When logged in, a prescriber may access a list of patients, treatment overview information for the treatment options available, and a list of medications for those treatments. Under the patient list, the prescriber may select a patient and view information about them, including visit history, treatment algorithm and corresponding step, medications, PHQ-9/MDQ results, and other personal information necessary. The prescriber also has the option register a new patient from the patients list. From a patient's home page, a prescriber may allow for a patient to take the PHQ-9 or MDQ form and update their score. A patient's information can be edited manually by clicking the Edit Patient button.


## 3.1 Admin Actions

Administrators of the Psychiatric App have more privileges than those who are not. Administrators can create new users through the "Admin Actions" dropdown menu available in the site navigation. All software related administrator actions are described in the [Developer Documentation](https://github.com/Brick7Face/psychiatric-guide-app/blob/development/README.md) for the project.

## 3.2 Patients

Accessible from the site navigation is the "Patients" page. Here you can find a full list of all patients in the app database along with all their individual profiles.

From the Patients List page, you can click on any patient in the list to access their full profile, delete a patient using the garbage can symbol on the right hand side of each patient, and finally create a new patient using the button at the bottom of the page.

### 3.2.1 Creating New Patient

Upon clicking the "New Patient" button on the Patients List page, you are directed to a form to fill out regarding patient information. On this screen you must fill out all form fields. The "Current Step" field is already populated by all the possible options outlined in the Prescribing Pocket Guide.

### 3.2.2 Edit Current Patients

After clicking on a patient from the Patient List page, you will be directed to that patients profile. This profile contains all information that was entered into the form when the patient profile was created, along with any information from previous visits including test results from the PHQ-9 and MDQ, dates of previous visits, and treatment recommendations. On this page you also have the option to "Edit Patient". Once clicking on this button, you will be shown a form similar to the one that you saw when the patient was created. From here you can change any field in the patient profile aside from test scores, and previous visits.

### 3.2.3 Taking New PHQ-9 or MDQ

In any patient profile there are two sections, one for PHQ-9 results, and another for MDQ results. Alongside these results and recommendations are the options to take new tests. When you click on either of these buttons you will be sent to the corresponding test where the patient can answer questions which will determine a score, results, and treatment recommendations that will then be saved to that patients profile upon completion. The PHQ-9 and MDQ forms only require that a prescriber turn the screen toward the patient and let them select answers based on the questions asked. The prescriber could also just ask the patient the questions and record their answer.

## 3.3 Algorithm

The Algorithm tab contains the steps laid out for the Depression, Bipolar Depressed, and Bipolar Manic treatment algorithms as shown in the Prescribing Pocket Guide 2012. The default display is the Depression algorithm, but the Select Algorithm button in the top left can be used to choose among the three. In the case of the layout needing to be changed, an administrator could login and see another button here that says "Edit Layout". This opens up options for moving the steps around in a drag-and-drop manner and rearranging links to steps. So, if a treatment had a few steps that needed to be changed or rearranged, there would not be a lot of overhead to do so.

## 3.4 Treatment Overview

The Treatment Overview page shows general information about the treatment types that a patient may need to be aware of. This page is designed to be printed by the prescriber and given to the patient if they would like. It contains miscellaneous information that is not located elsewhere on the site.

## 3.5 Medications

The Medications page displays relevant medications used in the three treatment algorithms. These contain information such as generic and brand names, dosing, titration, comments, and side effects. Information from this page could also be printed and given to a patient if necessary.

## 3.6 Reporting a Bug

Reporting a bug in the application can be done very simply through the "Report a Bug" option found in the site navigation. On this page you will see a text box where you simply describe the problem or bug you found, which will automatically be visible to the developer of the application. More information regarding bugs on the developer side can be found in the developer documentation.

## 3.7 Viewing Documentation

From the site you may view both the User, and Developer documentation. Located in the site navigation is a "Documentation" link that you will find links to both documents.


# 4. Updates and Bugs



---



## 4.1 Check For Updates And Bug Fixes

At this point the project is intended to be released publically. There are not currently more features planned in the short term, but we will continue to maintain the code through the Github Issues list and by individual request. The code is in the process of being submitted to Cerner for review and is intended to be released there. As always, the source code is available on the [Github site](https://github.com/Brick7Face/psychiatric-guide-app).

## 4.2 Report New Bug

On the website, there is a link on the left side in the navigation bar to report a bug. You can fill out this form or submit a bug manually on [https://github.com/Brick7Face/psychiatric-guide-app](https://github.com/Brick7Face/psychiatric-guide-app).
When submitting a bug, be specific about exactly what you were trying to do, what you did to trigger it (as best of
your knowledge), what error messages you received if any, and if you were able to resolve it or not through alternative
means. You may also be interested in following this process:
[How to write good bug reports](https://musescore.org/en/handbook/developers-handbook/getting-started/how-write-good-bug-report-step-step-instructions).
We greatly appreciate any sort of feedback.
