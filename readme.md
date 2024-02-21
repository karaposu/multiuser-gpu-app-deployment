# MULTIUSER-GPU-APP-DEPLOYMENT

Our aim is to deploy an existing GPU-accelerated application, app.py, in a manner that ensures scalability, the capability to handle heavy traffic, and aligns with professional product deployment practices for multi-user access.
Here's an overview of the solution in bullet points. 
After each bullet point we will be testing the last state of the 
application with all the added features

We divide the full deployment process into 3 cycles. 
In the end of first cycle, 
- you will create local deployment with a container for your app
- and then you deployed it on the cloud in a simple way


# 1.First cycle 
## 1.1 App Modernization (local development)

- **a) Run your already existing app.py and take notes of system and GPU loads**
- **b) Abstract the Data Access Layer** Ensure your application interacts with its data storage, cache, and any external state through an abstract data access layer. This means your application code should not directly call specific databases or caching systems. Instead, use interfaces or abstract classes that can be implemented for different backends
- **c) Create mocks to use with Data Access Layer and connect them**
- **d) Test if the app logic is working without any problems**
- **e) Redesign your app.py in a way to use env variables as feature flags**(local, cloud, test, prod...)
- **f) Design an api and create a basic documentation** 
- **g) Wrap it with fastapi**
- **h) Create simple tests for api calls and app logic**
- **i) Use postman test if all systems are working**
- **j) Implement Celery to manage tasks asynchronously**
- **k) Use Redis**  to manage the queue of tasks that Celery will process.
- **l) use postman test if all systems are working**

## 1.2 Deployment Readiness  (local development)
- **Run a Redis container locally to mimic Memorystore and a PostgreSQL container as a stand-in for Cloud SQL**
- **Connect the Data Access Layer to mock_redis and mock_cloud_SQL containers**
- **Add basic CI/CD pipelines for automated testing and container image building**
- **Containerization with GPU Support**
- **Test the container app**
 
## 1.3 Staging Deployment 
- **Create a DockerHub and GCP account**
- **Create Memorystore, PostgreSQL accounts** (if needed)
- **Rebuild the container with correct environment variables and feature flags**
- **Upload your container to dockerhub**
- **Create compute engine(VM) instance in GCP**
- **Install docker in this VM**
- **Pull the app inside the VM and run it**
- **Test if all is okay with postman**


# 2. Second cycle
- **Implement IaC (terraform)**
- **Enhanced CI/CD pipeline to include IaC deployment with Terraform**
- **Deploy on GCP using terraform**

# 3. Third cycle
- **Deploy on GKE using terraform**
- **Refine CI/CD process to support deployments to GKE using Terraform**


Define Interfaces for Data Access

First, define interfaces or abstract classes that encapsulate the operations your application needs to perform on data stores or caches.

 Implement the Interfaces
 
Next, provide concrete implementations of these interfaces for specific backends (e.g., file system storage, cloud storage):

 Use the Abstraction in Your Application
 
