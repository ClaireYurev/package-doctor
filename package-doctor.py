import json

def update_package_dependencies(filepath="package.json"):
    """
    Scans a package.json file, checks for specific dependencies and updates their versions if needed.
    Outputs descriptive changes to the console with emojis.

    Args:
        filepath (str): The path to the package.json file. Defaults to "package.json".
    """

    desired_dependencies = {
        "date-fns": "^3.0.0",
        "next": "14.2.23"
    }

    try:
        with open(filepath, 'r') as f:
            package_json_content = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: package.json file not found at '{filepath}'. Please ensure the file exists.")
        return
    except json.JSONDecodeError:
        print(f"❌ Error: Could not parse package.json. Please ensure it is valid JSON format.")
        return

    updated = False

    # Check and update dependencies section
    if "dependencies" in package_json_content:
        print("🔍 Checking 'dependencies' section...")
        for dep_name, desired_version in desired_dependencies.items():
            if dep_name in package_json_content["dependencies"]:
                current_version = package_json_content["dependencies"][dep_name]
                if current_version != desired_version:
                    print(f"🔄 Updating dependency '{dep_name}' in 'dependencies':")
                    print(f"   - Old version: ❌ '{current_version}'")
                    print(f"   - New version: ✅ '{desired_version}'")
                    package_json_content["dependencies"][dep_name] = desired_version
                    updated = True
                else:
                    print(f"✅ Dependency '{dep_name}' in 'dependencies' is already at the desired version '{desired_version}'.")
            else:
                print(f"ℹ️ Dependency '{dep_name}' not found in 'dependencies' section. Skipping.")

    # Check and update devDependencies section
    if "devDependencies" in package_json_content:
        print("🔍 Checking 'devDependencies' section...")
        for dep_name, desired_version in desired_dependencies.items():
            if dep_name in package_json_content["devDependencies"]:
                current_version = package_json_content["devDependencies"][dep_name]
                if current_version != desired_version:
                    print(f"🔄 Updating dependency '{dep_name}' in 'devDependencies':")
                    print(f"   - Old version: ❌ '{current_version}'")
                    print(f"   - New version: ✅ '{desired_version}'")
                    package_json_content["devDependencies"][dep_name] = desired_version
                    updated = True
                else:
                    print(f"✅ Dependency '{dep_name}' in 'devDependencies' is already at the desired version '{desired_version}'.")
            else:
                print(f"ℹ️ Dependency '{dep_name}' not found in 'devDependencies' section. Skipping.")

    if updated:
        try:
            with open(filepath, 'w') as f:
                json.dump(package_json_content, f, indent=2)  # indent=2 for pretty formatting
            print("🎉 package.json updated successfully! 🎉")
        except IOError:
            print(f"❌ Error: Could not write to package.json file at '{filepath}'. Please check file permissions.")
    else:
        print("👍 No dependency updates needed in package.json. 👍")

if __name__ == "__main__":
    update_package_dependencies() # By default, it checks "package.json" in the current directory.
    # To check a different file, you can pass the filepath as an argument:
    # update_package_dependencies("path/to/your/package.json")
