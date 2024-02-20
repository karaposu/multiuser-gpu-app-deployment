 It's a standard practice in software development to separate production code from test code. 
 This separation is maintained by creating distinct test files (e.g., test_main.py) where mocks and other testing utilities are used to simulate dependencies, external services, or side effects.
 
Benefits:

Isolation: Keeps production code clean from testing artifacts, ensuring that mocks or test-specific logic don't accidentally become part of the production codebase.
Clarity: Makes it easier for developers to understand the structure of the project at a glance, with clear delineations between application logic and tests.
Integration with CI/CD: Automated testing frameworks and Continuous Integration (CI) pipelines typically expect tests to be in separate files or directories, making it straightforward to integrate and automate testing processes.


we want To test the integration of GoogleCloudStorageModelLoader model without actually doing anything with googlecloudstorage. So will mock it's behaviors. 

so inside the test_app.py we will import our main function. and then create 
class TestMainFunction(unittest.TestCase) to test test methods


The @patch decorator from the unittest.mock module in Python is used to temporarily replace the real implementation of a class or function with a mock object during testing. 


1. To mock the behavior of GoogleCloudStorageModelLoader such that it simulates a successful download of the "dreamshaperXL_turboDpmppSDE.safetensors" file, you can use the unittest.mock module's capabilities to set up return values and behaviors for the mocked object. Specifically, you'll configure the mock to return a predefined result when its load_checkpoint 
2. 
in the context of testing, you're interested in mocking the behavior of GoogleCloudStorageModelLoader when used within main.

you would set up a test that patches GoogleCloudStorageModelLoader within main