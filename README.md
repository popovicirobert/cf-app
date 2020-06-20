
### This is a command line application that helps you solve problems on codeforces<br/><br/><br/>



Cf-app documentation:<br/><br/>

1) Download the repository and necessary libraries using the install.sh script.<br/>
    **chmod +x install.sh**<br/>
    **source install.sh**<br/><br/>
2) Go in the cf-app directory and add 3 files username, password and browser that contain your codeforces username, password and the webbrowser you want to use(only Firefox and Chrome and currently available).<br/><br/>
3) To start the application run cf-app.<br/>
    **cf-app**<br/><br/>
4) Commands:<br/>
    - **contest {contest_name}**: initialize a directory with the same name as {contest_name} and prepare the tasks and test samples(e.g. **contest 900**)<br/>
    - **check {task_id}**: check the task {task_id} and report the verdict on the samples(e.g. **check A**)<br/>
    - **submit {task_id}**: submits main.cpp from directory {task_id} and reports the evaluation result(e.g. **submit A**)<br/>
    - **quit**: exit the application<br/>
