# Diamond

## Tutorial

### Set up globus compute endpoint
Before we start, we need to create a globus compute endpoint in a HPC. Config samples can be find in `endpoint_configs`.
Run the following commands in target HPC to initialize the endpoint
```
pip install globus-compute-endpoint
globus-compute-endpoint configure {{ endpoint_name }} Diamond/endpoint_configs/{{ HPC }}/{{ config_file }}
globus-compute-endpoint start endpoint_name
```

### Run scripts in remote hpc via diamond

#### login
Run
```
diamond-hpc get-oauth2-url-and-login
```
This cli will return an oauth2 url and wait for the user input, open the url in your broswer and follow the authorization process, finally you will get a token.
Copy the token and input it back to the terminal, finish the authorization process

#### register container
1. create an container build endpoint by configure and start custom-image-builder-config.yaml in the globus endpoint server
2. run the following command(substitude the relevent text with your config)
```
diamond-hpc register-container --endpoint_id e099b614-c95e-4148-8ed9-6bd4684b92bc --work_path /work/09912/haotianxie/frontera --image_file_name 
openfold --base_image gcyang/openfold:0.1
```
This process may take a long time.

#### submit task via script file
1. create an container build endpoint by start endpoint in the globus endpoint server
2. run the following command(substitude the relevent text with your config)
```
diamond-hpc run-task-from-script --cmd_script /home/hotine/work/Diamond/example/sample_task/openfold_single_node_task --endpoint_id fb1ffeec-aa63-4136-8a49-f3f24608d36f --container_id a20b806c-29a8-44b4-97b6-591434ca9365 --log_path /work/09912/haotianxie/frontera/openfold_demo_single_node.log
```
