from diamond.container.container import ImageRegistry


def main():
    image_builder_endpoint = ""  # endpoint for building images
    site_config = {
        "endpoint": image_builder_endpoint,
        "work_path": ""  # work path for building images
    }
    ir = ImageRegistry(site_config)
    print("The available containers are:")
    print(ir.list_avail_containers())

    image_file_name = "openfold"
    base_image = "gcyang/openfold:0.1"  # base image url in Docker Hub
    pkg_config = None
    container_id = ir.build(base_image, pkg_config, image_file_name)

    print("The container id is", container_id)

if __name__ == '__main__':
    main()
