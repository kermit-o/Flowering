import os
import json

def create_module(module_name, base_path="Modules"):
    """
    Creates a new module folder with a README and a config file.

    Parameters:
    - module_name (str): Name of the module to create.
    - base_path (str): Base directory where modules are stored.
    """
    module_path = os.path.join(base_path, module_name)
    try:
        # Create the module directory
        os.makedirs(module_path, exist_ok=False)

        # Create a README file
        readme_path = os.path.join(module_path, "README.md")
        with open(readme_path, "w") as readme_file:
            readme_file.write(f"# {module_name}\n\nThis is the {module_name} module.")

        # Create a config.json file
        config_path = os.path.join(module_path, "config.json")
        config_content = {
            "module_name": module_name,
            "created_by": "Outman",
            "version": "1.0.0",
            "description": f"Configuration for {module_name} module"
        }
        with open(config_path, "w") as config_file:
            json.dump(config_content, config_file, indent=4)

        print(f"Module '{module_name}' created successfully at '{module_path}'.")
    except FileExistsError:
        print(f"Error: Module '{module_name}' already exists at '{module_path}'.")
    except Exception as e:
        print(f"An error occurred while creating the module: {e}")

if __name__ == "__main__":
    print("Welcome to the Module Generator!\n")
    base_directory = "Modules"

    # Ensure the base directory exists
    os.makedirs(base_directory, exist_ok=True)

    while True:
        module_name = input("Enter the name of the new module (or type 'exit' to quit): ").strip()

        if module_name.lower() == 'exit':
            print("Exiting the Module Generator. Goodbye!")
            break

        if module_name:
            create_module(module_name, base_path=base_directory)
        else:
            print("Module name cannot be empty. Please try again.")
