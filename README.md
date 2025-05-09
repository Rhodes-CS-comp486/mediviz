## Project Description

Mediviz is an application that allows medical professionals to identify areas of the brain that are at high risk for Posterior Fossa Syndrome, a behavior deficit caused by the presence of lesions. 

Given a patient's brain scan and diagnosis, the system aims to identify correlations between patient diagnoses and the location of their lesions. The system prompts users to upload patient brain data and select which trained model they would like to use for identifying the high risk area. Areas of high risk are identified and visualized on the patient’s brain scan. The resulting image can be saved directly to the user’s file system, allowing for streamlined accessibility. 

## Major Features 

Patient Data Generation:

* Artificial patient data is generated based on parameters selected by the user  
* Parameters can be adjusted for each generation and past selections will be saved between uses  
* End user can visualize individual patients’ lesions

Train and Test Algorithm:

* Various visualization tools (heat map, confusion matrix, et cetera)  
* Save trained algorithm  
* Re-test saved algorithm

## Systems Diagram 
<img width="458" alt="systems_diagram" src="https://github.com/user-attachments/assets/3af3a41a-a82b-4d41-82d7-ade9ac90ea4d" />

Dependencies: 

* Listed in requirements.txt

## 

## Quick Start Guide

### Development Team: 

* Clone the repository using ‘git clone’ in the terminal, in your favorite IDE that runs Python.    
  * Ex: git clone [https://github.com/Rhodes-CS-comp486/](https://github.com/Rhodes-CS-comp486/coursewise.git)mediviz.git  
* Create/activate a virtual environment, if preferred.  
* Install dependencies  
  * Install the packages stated in requirements.txt through your Python IDE

### End User:

1. Download mediviz.exe (if connected to the github, install PyInstaller, and proceed).    
2. Two options:  
   1. Double click file  
   2. Open command line and type in “start mediviz.exe”, after navigating to correct file systemHome

## Front End of Application Examples

## ***Home Page***

![image](https://github.com/user-attachments/assets/fbcc9eb3-e9f6-4c8c-82d4-8af09f809dbb)


## ***Data Generation Page***

![image](https://github.com/user-attachments/assets/ab56d6f7-9239-4948-bce3-536ad14cab8b)


## ***Visualization Page***

![image](https://github.com/user-attachments/assets/1988c282-3631-4fa9-a38b-43b74cee9cba)
