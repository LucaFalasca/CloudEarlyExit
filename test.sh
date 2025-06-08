case $1 in
    "PlanGeneration") 
        docker exec -e PYTHONPATH=../../proto_compiled/:../../ cloud_early_exit-deployer-1 python3 PlanGenerationTest.py
        docker exec cloud_early_exit-deployer-1 /bin/sh -c "PYTHONPATH=../../proto_compiled/:../../ python3 PlanGenerationTest.py
        ;;
    "Deployment")
        docker exec cloud_early_exit-deployer-1 PYTHONPATH=../../proto_compiled/:../../ python3 DeploymentTest.py
        ;;
    "Inference")
        docker exec cloud_early_exit-client-1 ./start.sh ClientMain.py 
        ;;
    "ALL")
        docker exec cloud_early_exit-deployer-1 PYTHONPATH=../../proto_compiled/:../../ python3 PlanGenerationTest.py
        docker exec cloud_early_exit-deployer-1 PYTHONPATH=../../proto_compiled/:../../ python3 DeploymentTest.py
        docker exec cloud_early_exit-client-1 ./start.sh ClientMain.py
        ;;
    *) #Default case
        echo "Invalid argument. Please use one of the following: PlanGeneration, Deployment, Inference, ALL"
        exit 1
        ;;
esac
