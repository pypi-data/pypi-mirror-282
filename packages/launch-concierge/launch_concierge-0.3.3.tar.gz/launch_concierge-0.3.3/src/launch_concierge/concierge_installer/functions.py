import subprocess
import os
import shutil
from script_builder.util import require_admin, get_lines, prompt_install
from script_builder.argument_processor import ArgumentProcessor


def init_arguments(install_arguments):
    require_admin()
    argument_processor = ArgumentProcessor(install_arguments)
    argument_processor.init_args()
    print("\n\n\nConcierge: AI should be simple, safe, and amazing.\n\n\n")
    return argument_processor


def clean_up_existing():
    # If Docker isn't present, there's no point in proceeding
    if not shutil.which("docker"):
        print(
            "Docker isn't installed. You will need it to be able to proceed, please install Docker or use a machine which has it installed!"
        )
        exit()

    # check if docker is running
    process_info = subprocess.run(
        ["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    # if it's not running we can't check anything docker related
    if process_info.returncode == 1:
        print("Docker isn't running.")
        print(
            "This script requires the Docker daemon to be running. Please start it and rerun the script once it's up and running."
        )
        exit()

    # Check if Concierge is already configured
    if os.path.isfile(".env"):
        concierge_root = ""
        # read .env file manually because we don't necessarily have the pip requirements installed yet
        with open(".env") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("DOCKER_VOLUME_DIRECTORY="):
                    concierge_root = stripped.replace("DOCKER_VOLUME_DIRECTORY=", "")
                    break

        # if the Concierge docker directory is configured, we take that to mean it has previously been installed
        if concierge_root:
            print("Concierge instance discovered.")
            print("This script can help reset your system for a re-install.\n")

            # option to remove volumes directory
            concierge_volumes = os.path.join(concierge_root, "volumes")
            print(
                "Removing the Concierge volumes will delete all ingested data and any language models you downloaded."
            )
            print("Remove Concierge volumes?")
            approve_to_delete = input(
                f"Type 'yes' to delete {concierge_volumes} or press enter to skip: "
            )
            print("\n")
            if approve_to_delete == "yes":
                shutil.rmtree(concierge_volumes)

            def check_dependencies(check_command, label, remove_command):
                result = get_lines(check_command)
                if result:
                    print(f"The following docker {label} were discovered:")
                    print(" ".join(result))

                    print("\nWould you like to have the installer remove any for you?")
                    to_remove = input(
                        f"Please give a space separated list of the {label} you would like removed or press enter to skip: "
                    )
                    print("\n")

                    if to_remove != "":
                        subprocess.run(
                            [*remove_command, to_remove], stdout=subprocess.DEVNULL
                        )
                else:
                    print(f"No existing docker {label} were found.\n")

            # docker containers
            check_dependencies(
                ["docker", "container", "ls", "--all", "--format", "{{.Names}}"],
                "containers",
                ["docker", "container", "rm"],
            )
            # docker networks
            check_dependencies(
                ["docker", "network", "ls", "--format", "{{.Name}}"],
                "networks",
                ["docker", "network", "rm"],
            )


def prompt_for_parameters(argument_processor):
    print("Welcome to the Concierge installer.")
    print("Just a few configuration questions and then some download scripts will run.")
    print("Note: you can just hit enter to accept the default option.\n\n")

    argument_processor.prompt_for_parameters()

    print("Concierge setup is almost complete.\n")
    print(
        "If you want to speed up the deployment of future Concierge instances with these exact options, save the command below.\n"
    )
    print(
        "After git clone or unzipping, run this command and you can skip all these questions!\n\n"
    )
    print(
        "\npython install.py" + argument_processor.get_command_parameters() + "\n\n\n"
    )

    print("About to make changes to your system.\n")
    # TODO make a download size variable & update based on findings
    # print("Based on your selections, you will be downloading aproximately X of data")
    # print("Depending on network speed, this may take a while")
    print(
        'No changes have yet been made to your system. If you stop now or answer "no", nothing will have changed.'
    )


def docker_compose_helper(environment, compute_method, dir, rebuild=False):
    filename = "docker-compose"
    if environment == "development":
        filename = f"{filename}-dev"
    if compute_method == "GPU":
        filename = f"{filename}-gpu"
    full_path = os.path.abspath(os.path.join(dir, f"{filename}.yml"))
    if rebuild:
        # pull latest versions
        subprocess.run(["docker", "compose", "-f", full_path, "pull"])
        # build local concierge image
        subprocess.run(["docker", "compose", "-f", full_path, "build"])
    subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            full_path,
            "up",
            "-d",
        ]
    )


def prompt_concierge_install():
    prompt_install(
        "Ready to apply settings and start downloading?",
        "Install cancelled. No changes were made. Have a nice day! :-)",
    )


def install_docker(argument_processor, docker_compose_dir, environment="production"):
    # setup .env (needed for docker compose files)
    with open(".env", "w") as env_file:
        # write .env info needed
        env_file.writelines(
            "\n".join(
                [
                    "DOCKER_VOLUME_DIRECTORY="
                    + argument_processor.parameters["docker_volumes"],
                    "ENVIRONMENT=" + environment,
                    "WEB_PORT=" + argument_processor.parameters["port"],
                ]
            )
        )
    # docker compose
    if argument_processor.parameters["compute_method"] == "GPU":
        docker_compose_helper(environment, "GPU", docker_compose_dir, True)
    elif argument_processor.parameters["compute_method"] == "CPU":
        docker_compose_helper(environment, "CPU", docker_compose_dir, True)
    else:
        # need to do input check to prevent this condition (and others like it)
        print("You have selected an unknown/unexpected compute method.")
        print("you will need to run the docker compose file manually")
        exit()
    # ollama model load
    subprocess.run(
        [
            "docker",
            "exec",
            "-it",
            "ollama",
            "ollama",
            "pull",
            argument_processor.parameters["language_model"],
        ]
    )
