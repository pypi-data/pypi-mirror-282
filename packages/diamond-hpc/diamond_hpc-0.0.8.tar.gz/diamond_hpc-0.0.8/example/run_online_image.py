from globus_compute_sdk import Client, Executor


def task(image_uri, num_workers, log_path):

    def srun_wrapper(cmd):
        import textwrap
        cmd = textwrap.dedent(cmd.strip())  # remove newlines and indentations
        return f"(srun -n {num_workers} apptainer run --nv {image_uri} {cmd}) 2>&1 | tee {log_path}"

    import os
    cmd = f"""
    python -c "import torch; print('PyTorch version:', torch.__version__)"
    """
    os.system(srun_wrapper(cmd))
    return 'Done'
                    

def main():
    endpoint = "b317afe2-702f-4074-804b-b93c36d892e4"
    gcc_client = Client()

    print("The endpoint status:")
    print(gcc_client.get_endpoint_status(endpoint))
    image_uri = "docker://nvcr.io/nvidia/pytorch:24.02-py3"
    num_workers = 1
    log_path = '/work2/09849/gcyang/frontera/online_image.log'  # custom log file path

    with Executor(endpoint_id=endpoint) as ex:
        fut = ex.submit(task, image_uri, num_workers, log_path)

    print(fut.result())


if __name__ == '__main__':
    main()

