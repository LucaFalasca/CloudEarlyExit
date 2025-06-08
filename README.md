# CloudEarlyExit
This project provide an extension for a Early Exit feature in an existing project that provide a model partition in multiple server based on multiple criteria.

## How to start
Go in the src folder and run the following command:
```docker compose up --build```

## How to run tests
Go in the src folder and run the following command:
```docker exec 


frontend server per componenti fittizione, intermediate per le componenti effettive

# Fa partire uno dei test sul deployer
PYTHONPATH=../../proto_compiled/:../../ python3 <TestName>
# stanno qui i test
src/Deployer/Test

# Fa partire il test dell'inferenza sul client
./start.sh ClientMain.py 

# Per far partire le altre componenti 
./start.sh Main.py 

# oppure per il client 
./start.sh ServerMain.py

# COnfigurazione dei container
src/config/local_config.ini

# Generazione dei modelli da runnare in locale
/workspaces/CloudEarlyExit/src/Other/model_scripts/model_generator.py

# Pre-post processing, da integrare la versione nuova nei test
Analysis/Onnx/YoloPPP.py

# La divisione del piano avviene:
src/ModelDivider/Divide/OnnxModelPartitioner.py

# Qui vengono fatte le rpc per far e il deployement
src/Deployer/DeploymentServer.py