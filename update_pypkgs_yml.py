import yaml


def get_package_names(requirements_file):
    package_names = []
    with open(requirements_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            package_name = line.split("==")[0]
            package_names.append(package_name)

    return package_names


def get_allowed_packages(yaml_file):
    with open(yaml_file, "r") as file:
        yaml_data = yaml.safe_load(file)

    allowed_packages = yaml_data.get("allowedPythonPackages", [])
    return allowed_packages


def update_yaml_file(yaml_file, allowed_packages_list, disallowed_packages):
    with open(yaml_file, "r") as file:
        yaml_data = yaml.safe_load(file)

    yaml_data["allowedPythonPackages"] = allowed_packages_list + disallowed_packages

    with open(yaml_file, "w") as file:
        yaml.dump(yaml_data, file, default_flow_style=False)


requirements_file = "./requirements.txt"
package_list = get_package_names(requirements_file)
yaml_file = "./appian-proxy-config-internal.yml"
allowed_packages_list = get_allowed_packages(yaml_file)

disallowed_packages = [pkg for pkg in package_list if pkg not in allowed_packages_list]
print(disallowed_packages)

update_yaml_file(yaml_file, allowed_packages_list, disallowed_packages)
