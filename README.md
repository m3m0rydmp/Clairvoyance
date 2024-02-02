<!--
![icons8-eye-48](https://github.com/Resonanc3/Clairvoyance/assets/79844632/6e384898-ae65-4181-be36-bf1358684f01)
![icons8-code-48](https://github.com/Resonanc3/Clairvoyance/assets/79844632/d5a9648a-3770-4e99-a40c-32c2f351fadb)
![icons8-feature-100](https://github.com/Resonanc3/Clairvoyance/assets/79844632/5d881271-d70e-4716-ac3d-ca4c42925f4e)
![icons8-google-drive-48](https://github.com/Resonanc3/Clairvoyance/assets/79844632/e59bb1d3-37e5-461e-9957-8034244b578f)
-->


# Clairvoyance <img src="https://github.com/Resonanc3/Clairvoyance/assets/79844632/6e384898-ae65-4181-be36-bf1358684f01">
This project is a keylogger that I made out of boredom. This was inspired through a collective ideas from the internet, and through the exploration and usage of linux tools.
This is just a basic program about keyloggers with added features. I just want to improve myself in the field of hacking and understand how the techniques or methods used works.

# Features <img src="https://github.com/Resonanc3/Clairvoyance/assets/79844632/5d881271-d70e-4716-ac3d-ca4c42925f4e" width=60px>
Clairvoyance is a keylogger with added features, it is a collective idea from the internet. You can make a keylogger with just a few lines but it gets so boring.
So, why not tweak the project like how I would like it. This project currently has the following features:
* Keylogger - captures keyboard strokes
* Screenshot - Takes screenshot every minute
* File Upload - Data files are uploaded to a specific Google Drive
* Extract Info - Extracts the system information of a computer
* Unique Termination - Termination of the program requires to press 'esc' key 5 times
  
I will add more features in the feature. With my current knowledge I still can't comprehend how to make it advance.

# How It Works <img src="https://github.com/Resonanc3/Clairvoyance/assets/79844632/d5a9648a-3770-4e99-a40c-32c2f351fadb">
This repository consist of 3 files. 2 files are for the source code, and one file for the application executable </br>

**SOURCE CODE**
* clairvoyance.pyw
* extract_info.py

**EXECUTABLE**
* clairvoyance

You can just execute the application if you want to test it out.

The application starts by extracting the system info of the computer, where it will then create a '.txt' file and append the data inside it.
It will then start capturing keyboard strokes, and also create a '.txt' file, appending the timestamp on when the program is opened.
Then, the first capture of screenshot takes place, it will take another screenshot in another 60 seconds.
In order for the program to be terminated, it needs to press the 'esc' key 5 times. When it is terminated, the files will be uploaded to google drive which are
the two '.txt' file and the number of screenshots present.

# Setting Up Google Drive <img src="https://github.com/Resonanc3/Clairvoyance/assets/79844632/e59bb1d3-37e5-461e-9957-8034244b578f">
In order for the upload file to work, you need three things and this will be your variables for uploading.
* SCOPES
* SERVICE ACCOUNT FILE
* FOLDER ID

**SCOPES**

**1. Enable the Google Drive API**
* Visit the Google API Console: https://console.developers.google.com/
* Create a new project or select an existing one.
* Search for "Google Drive API" and enable it.

**2. Create Credentials**
* Go to the "Credentials" tab.
* Click "Create Credentials" and choose "OAuth client ID."
* Select "Desktop app" as the application type.
* Give your app a name and click "Create."
* You'll receive a client ID and client secret.

**3. Get The Scopes**
* The scopes define the specific permissions your app needs.
* For file uploading, you'll typically need: ```https://www.googleapis.com/auth/drive.file``` for basic file actions

**SERVICE ACCOUNT FILE**

**1. Creating a Service Account**
* Go to the Google Cloud Console: https://console.cloud.google.com/: https://console.cloud.google.com/
* Select the project where you want to create the service account.
* Go to the "IAM & Admin" section and click on "Service accounts."
* Click "Create Service account."
* Give your service account a name and description, then click "Create."
* Click on the newly created service account and go to the "Keys" tab.
* Click "Add Key" and select "Create new key."
* Choose the JSON format and click "Create."
* Download the JSON file. This file contains the private key and other information needed to authenticate your service account.

**2. Using an Existing Account**
* If you already have a service account in your project, you can use that one instead of creating a new one.
* Go to the "IAM & Admin" section and click on "Service accounts."
* Select the existing service account you want to use.
* Go to the "Keys" tab and click on the key you want to use.
* Click on the "..." menu next to the key and select "Download."

**FOLDER ID**

**1. Inspect the URL**
* Open the folder you want the ID for in Google Drive.
* Look at the URL in your browser's address bar.
* The folder ID is the string that follows "folders/" in the URL. For example, in the URL ```https://drive.google.com/drive/u/0/folders/abcdef123456``` the Folder ID is "abcdef123456"

Look for the Google Drive Upload Variable in the code, and place the necessary info in it.


#
I still want to add more features about this project but I still don't know what feature and how to implement it with my current knowledge. Yet, I won't stop exploring and creating in order to improve myself.
I hope you like this project, as much as I did.
