# CloudEarlyExit

This project provide an extension for a Early Exit feature in an existing project that provide a model partition in multiple server based on multiple criteria.

## How to start

Go in the src folder and run the following command:
`docker compose up --build`

## Preliminar steps

You need to generate model files first. You can execute this command for doing it:
    ```bash
    bash test.sh 
    ```
But you need to be in right environment. Use a devContainer for this or install all the dependencies.

## How to run tests

You need to run it from your command line and pass a specific argument indicating which test you want to execute, or nothing for executes all of them
    ```bash
    bash test.sh 
    ```

### Available Arguments:

* **`PlanGeneration`**: Executes the plan generation test inside the `Deployer` container.

  ```bash
  bash test.sh PlanGeneration
    ```

* **`Deployment`**: Executes the deployment test inside the `Deployer` container.

  ```bash
  bash test.sh Deployment
    ```

* **`Inference`**: Executes the inference test inside the `Client` container.
    ```bash
    bash test.sh Inference
    ```
