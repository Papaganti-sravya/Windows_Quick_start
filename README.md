Work in progresss 


Problem Statement :


            For new iphones we use apple quick start to transfer everything(apps, contacts, pictures etc) to transfer the data into new iphone which makes the transition easy and removes the risk 
            of manual transfers, what if we buy a new laptop(windows) we need to use 3rd party tools like nearby share and the corns of this is we have to select the files that needs 
            to be shared and those files only will be share but here the use case is to share all the contents in the old laptop to new laptop with exact file location through images.


Solution: 

        Step 1: we need to collect all the data and form a zip file

        Step 2: we need to create a qr code or dot like images(like apple quick start) which contains entire dataof us laptop, (if the data is large we have to cut the data
        into chunks and then process the data that is a different method in this repository I used smaller data for testing purpose)

        Step 3: Ensure the security of the receiving device 

        Step 4: Transfer the data.



In this repository I have created a path till step2
Notes: Since this is for testing purpose I have mentioned the folders in the code but usually the idea is to collect all data including apps and data in it. 
Collect_data.py -> will collect data and make a zip files
generate_qr -> this will generate the qr code 
main_scrip.py -> this will combine objects of collect_data and generate_qr 

How to run :

just run the main_script.py and it will generate the files

Work in progess:


     1. Since this is for small data the qr is easily generated but for large data we have to divide the data into chunks and create qr code  
     2. Data transfer not yet tested
     3. Code for deleting the zip file after use is not yet included.  
