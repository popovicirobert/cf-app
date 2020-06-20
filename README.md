
### This is a command line application that helps you solve problems on codeforces
<br>
<br>
Cf-app documentation:

1) Download the repository and necessary libraries using the install.sh script. This will initialize a directory named cf-app with all necessary files.


    **chmod +x install.sh**   
    **source install.sh**
    
    
2) Go in the cf-app directory and add 3 files username, password and browser that contain your codeforces username, password and the webbrowser you want to use(only Firefox and Chrome and currently available). This step is optional. If you don't make these files you need to insert the fields each time you start the app.




3) To start the application run cf-app.


    **cf-app**
    
    
    
    
4) Commands:

    - **contest {contest_name}**: initialize a directory with the same name as {contest_name} and prepare the tasks and test samples(e.g. **contest 900**)
    
    
    - **check {task_id}**: check the task {task_id} and report the verdict on the samples(e.g. **check A**)
    
    
    - **submit {task_id}**: submits main.cpp from directory {task_id} and reports the evaluation result(e.g. **submit A**)
    
    
    - **quit**: exit the application
    
    
