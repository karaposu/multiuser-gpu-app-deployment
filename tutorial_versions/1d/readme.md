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


1. **Run your already existing app.py and take notes of system and GPU loads**
2. **Abstract the Data Access Layer**
3. **Redesign your app.py to use env variables as feature flags** (local, cloud, test, prod...)
   a.List all env variables you need
   b.create a .env file to handle env variables locally
   c.use python-dotenv package to load these variables into your environment
   d.use ```from dotenv import load_dotenv``` and ```environment = os.getenv('APP_ENVIRONMENT')``` to load the variables.
   e.control your app logic according the values of env variables
4. **Design and document an API, create a stub, convert stub to implementation**
5. **Wrap your application logic with FastAPI**
6. **Create class initialization and data access layer integration tests inside test_app.py**
7. **Create mocks in test_app.py for external Data Access Layer components and connect them**
8. **Create simple tests for API calls and app logic**
9. **Use Postman to test if all systems are working**
10. **Implement Celery to manage tasks asynchronously**
11. **Use Redis to manage the queue of tasks that Celery will process**
12. **Use Postman to test if all systems are working again**



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
 
