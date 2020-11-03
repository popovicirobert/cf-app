
# Cf-app

CLI that automates the process of testing and submitting problems on www.codeforces.com.

## Installation

Download the repository and necessary libraries using the install.sh script.<br>
This will initialize a directory named cf-app with all necessary files.

```bash
 chmod +x install.sh
 sudo source install.sh
 ```


Go in the cf-app directory and add 3 files username, password and browser that contain your codeforces username, password and the webbrowser you want to use(only Firefox and Chrome and currently available).<br>
If you don't make these files you need to insert the fields each time you start the app.


## Running the app

To start the application run cf-app.

```bash
cf-app
```
    
## Usage

- **contest {contest_name}**: initialize a directory with the same name as {contest_name} and prepare the tasks and test samples(e.g. **contest 900**)

- **check {task_id}**: check the task {task_id} and report the verdict on the samples(e.g. **check A**)

- **submit {task_id}**: submits main.cpp from directory {task_id} and reports the evaluation result(e.g. **submit A**)

- **quit**: exit the application
    
    
