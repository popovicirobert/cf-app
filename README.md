
### This is a command line application that helps you solve problems on codeforces<br/><br/><br/>






This is the cf-app documentation<br/><br/>

1) Download the repository and necessary libraries using the install.sh script(see README.md).<br/>
<pre>**chmod +x install.sh**<pre/>
<pre>**source install.sh**<pre/>
2) Go in the cf-app directory and add 3 files username, password and browser that contain your codeforces username, password and the webbrowser you want to use(Firefox and Chrome and currently available).<br/>
3) To start the application run cf-app.<br/><br/>

Commands:<br/>
	- contest {contest_name}: initialize a directory with the same name as {contest_name} and prepare the tasks and test samples<br/>
	- check {task_id}: check the task {task_id} and report the verdict on the samples<br/>
	- submit {task_id}: submits main.cpp from directory {task_id} and reports the evaluation result<br/>
	- quit: exit the application<br/>
