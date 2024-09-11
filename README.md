# Kura Labs Cohort 5- Deployment Workload 3


---



## Monitoring Application and Server Resources

Welcome to Deployment Workload 3! The past 2 Workloads have utilized AWS managed services to provision the infrastructure for our application.  Let's start shifting to infrastucture built by us and take a deeper dive into what goes into deploying an application.

Be sure to document each step in the process and explain WHY each step is important to the pipeline.

## Instructions

1. Clone this repo to your GitHub account. IMPORTANT: Make sure that the repository name is "microblog_EC2_deployment"

2. Create an EC2 instance named "Jenkins" and install Jenkins onto it (are you still doing this manually?).  Be sure to configure the security group to allow for SSH and HTTP traffic in addition to the ports required for Jenkins and any other services needed (Security Groups can always be modified afterward)

3. Configure the server by installing 'python3.9',  'python3.9-venv', and 'nginx'. (Hint: There are several ways to install a previous python version. One method was used in Workloads 1 and 2)

4. Clone your GH repository to the server, cd into the directory, create and activate a python virtual environment with: 

```
$python3.9 -m venv venv
$source venv/bin/activate
```

5. While in the python virtual environment, install the application dependencies and other packages by running:

```
pip install -r requirements.txt
pip install gunicorn pymysql cryptography
```

6. Set the ENVIRONMENTAL Variable:

```
FLASK_APP=microblog.py
```
Note: What is this command doing?

7. Run the following commands: 

```
$flask translate compile
$flask db upgrade
```

8. Edit the NginX configuration file at "/etc/nginx/sites-enabled/default" so that "location" reads as below.

```
location / {
proxy_pass http://127.0.0.1:8000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```
Note: What is this config file/NginX responsible for?

9. Run the following command and then put the servers public IP address into the browser address bar

```
gunicorn -b :5000 -w 4 --access-logfile - --error-logfile - microblog:app
```
Note: What is this command doing? You should be able to see the application running in the browser but what is happening "behind the scenes" when the IP address is put into the browser address bar?

10. If all of the above works, stop the application by pressing ctrl+c.  Now it's time to automate the pipeline.  Modify the Jenkinsfile and fill in the commands for the build, test, and deploy stages.

  a. The build stage should include all of the commands required to prepare the environment for the application.  This includes creating the virtual environment and installing all the dependencies, setting variables, and setting up the databases.

  b. The test stage will run pytest.  Create a python script to run a unit test of the application source code. IMPORTANT: Put the script in a directory called "tests/unit/" of the GitHub repository. Note: The complexity of the script is up to you.  Work within your limits.  (Hint: If you don't know where to start, try testing the homepage or log in page.  Want to challenge yourself with something more complicated? Sky's the limit!)

  c. The deploy stage will run the commands required to deploy the application so that it is available to the internet.

11. In Jenkins, install the "OWASP Dependency Checker" plug-in by navigating to "Manage Jenkins" and then "Global Tool Configuration".

NOTE: What is this plug in for?  What is it doing?  Why is it important?

13. Create a MultiBranch Pipeline and run the build.  IMPORTANT: Make sure the name of the pipeline is: "workload_3".

11. After the application has successfully deployed, create another EC2 called "Monitoring".  Install Prometheus and Grafana and then configure it to monitor the activity on the server running the application. 

12. Document! All projects have documentation so that others can read and understand what was done and how it was done. Create a README.md file in your repository that describes:

	  a. The "PURPOSE" of the Workload,

  	b. The "STEPS" taken (and why each was necessary/important),
      NOTE: Were steps 4-9 absolutely necessary for the CICD pipeline? Why or why not?
    
  	c. A "SYSTEM DESIGN DIAGRAM" that is created in draw.io (IMPORTANT: Save the diagram as "Diagram.jpg" and upload it to the root directory of the GitHub repo.),

	  d. "ISSUES/TROUBLESHOOTING" that may have occured,

  	e. An "OPTIMIZATION" section for that answers the question: What are the advantages of provisioning ones own resources over using a managed service like Elastic Beanstalk?  Could the infrastructure created in this workload be considered that of a "good system"?  Why or why not?  How would you optimize this infrastructure to address these issues?

    f. A "CONCLUSION" statement as well as any other sections you feel like you want to include.
