case $1 in
"PlanGeneration")
	docker exec -e PYTHONPATH=.:./proto_compiled/ cloud_early_exit-deployer-1 python3 -m Deployer.Test.PlanGenerationTest
	;;
"Deployment")
	docker exec -e PYTHONPATH=.:./proto_compiled/ cloud_early_exit-deployer-1 python3 -m Deployer.Test.DeploymentTest
	;;
"Inference")
	docker exec cloud_early_exit-client-1 ./start.sh ClientMain.py
	;;
*) #Default case
	docker exec -e PYTHONPATH=.:./proto_compiled/ cloud_early_exit-deployer-1 python3 -m Deployer.Test.PlanGenerationTest
	docker exec -e PYTHONPATH=.:./proto_compiled/ cloud_early_exit-deployer-1 python3 -m Deployer.Test.DeploymentTest
	docker exec cloud_early_exit-client-1 ./start.sh ClientMain.py
	;;
esac
