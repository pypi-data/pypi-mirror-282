from globus_compute_sdk import Client, Executor


def task(image_file_path):

    def srun_wrapper(cmd):
        import textwrap
        log_path = ""  # custom log file path
        cmd = textwrap.dedent(cmd.strip())  # remove newlines and indentations
        return f"(srun -n 8 apptainer exec --nv {image_file_path} {cmd}) 2>&1 | tee {log_path}"

    import os
    cmd = f"""
    python /opt/openfold/train_openfold.py \
        /scratch1/00946/zzhang/datasets/openfold/openfold/ls6-tacc/pdb_mmcif/mmcif_files \
        /scratch1/00946/zzhang/datasets/openfold/openfold/ls6-tacc/alignment_openfold \
        /scratch1/00946/zzhang/datasets/openfold/openfold/ls6-tacc/pdb_mmcif/mmcif_files \
        full_output \
        2021-10-10 \
        --val_data_dir /scratch1/00946/zzhang/datasets/openfold/openfold/cameo/mmcif_files \
        --val_alignment_dir /scratch1/00946/zzhang/datasets/openfold/openfold/cameo/alignments \
        --template_release_dates_cache_path=/scratch1/00946/zzhang/datasets/openfold/openfold/ls6-tacc/mmcif_cache.json \
        --precision=32 \
        --train_epoch_len 128000 \
        --gpus=4 \
        --num_nodes=2 \
        --accumulate_grad_batches 8 \
        --replace_sampler_ddp=True \
        --seed=7152022 \
        --deepspeed_config_path=/scratch1/00946/zzhang/frontera/openfold/deepspeed_config.json \
        --checkpoint_every_epoch \
        --obsolete_pdbs_file_path=/scratch1/00946/zzhang/datasets/openfold/openfold/ls6-tacc/pdb_mmcif/obsolete.dat \
        --train_chain_data_cache_path=/scratch1/00946/zzhang/datasets/openfold/openfold/ls6-tacc/chain_data_cache.json
    """
    os.system(srun_wrapper(cmd))
    return 'Done'
                    

def main():
    endpoint = ""  # endpoint for running multi-node GPU task
    gcc_client = Client()
    container_id = "a20b806c-29a8-44b4-97b6-591434ca9365"  # container id for the task

    print("The endpoint status:")
    print(gcc_client.get_endpoint_status(endpoint))
    print("The container info:")
    container_info = gcc_client.get_container(container_id, 'singularity')
    print(container_info)
    image_file_path = container_info['location']

    with Executor(endpoint_id=endpoint) as ex:
        fut = ex.submit(task, image_file_path)
        print(fut.result())


if __name__ == '__main__':
    main()

