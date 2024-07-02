from ShellUtilities import Shell
import os
import logging
from pathlib import Path
import sys
import platform
import re
from packaging import version


# This contains python functions which invokes the bash script to determine the version number.

def determine_version_number(repo_path=None, adjust_for_pep_440=True, adjust_for_pypi=False):
    """This function executes a BASH script to determine the CalVer compliant version number of a git repository which is expected to follow the documented Trunk Based Development (TBD) branching strategy.

    Args:
        repo_path (_type_, optional): The absolute path to the repository. Defaults to None.
        adjust_for_pep_440 (bool, optional): Whether the version number should be adjusted to conform to PEP-440 and use local labels ('+' instead of '.') for non-integration branches. Defaults to True.
        adjust_for_pypi (bool, optional): Adjusts for PEP-440 and asjusts version number for integration branches to satisfy PyPI requirements. Raises for non-integration branches. Defaults to False.

    Returns:
        str: Version number compliant with TBD and CalVer strategies.
    """
    # Determine if we are using conda
    try:
        if os.environ["CONDA_DEFAULT_ENV"]:
            logging.info("Detected that a conda environment is being used.")
            using_conda = True
            conda_env_name = os.environ["CONDA_DEFAULT_ENV"]
            conda_env_path = os.environ["CONDA_PREFIX"]
    except:
        using_conda = False
    
    script_name = "determine_tbd_calver_version_number.sh"
    script_installed = False
    
    # Determine the platform
    if platform.system() == "Linux" and not using_conda:
        # Check the environment variable named PATH to see if the script was installed
        logging.debug("Searching PATH for installed bash script.")
        logging.debug(os.linesep + os.environ["PATH"])
        script_installed = False
        for path in os.environ["PATH"].split(":"):
            script_path = os.path.join(path, script_name)
            if os.path.exists(script_path):
                script_installed = True
                logging.debug(f"Found script at '{script_path}'")
                break
        logging.warn("Script not found in environment PATH.")       
    elif platform.system() == "Windows" and not using_conda:
        # On windows, the user is expected to use a bash-like environment
        logging.warn("Script not found in windows environment.")
        pass
    elif using_conda:
        script_path = os.path.join(conda_env_path, "bin", script_name)
        logging.debug(f"Checking conda environment for: {script_path}")
        if os.path.exists(script_path):
            script_installed = True
            logging.debug(f"Found script at '{script_path}'")
        else:
            logging.warn("Script not found in conda environment.")
 
    # If the script is not installed into the PATH, assume we are running from inside the git repo
    # Check if the script can be found locally
    if not script_installed:
        logging.warn("Assuming script is being run from the local git repo instead.")  
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if not repo_path:
            repo_path = os.getcwd()
        logging.debug(f"Repo path set to: {repo_path}")
        src_root_dir = os.path.dirname(current_dir)
        bash_dir = os.path.join(src_root_dir, "bash", "bin")
        script_path = os.path.join(bash_dir, script_name)
        if os.path.exists(script_path):
            script_installed = True
            logging.debug(f"Found script at '{script_path}'")

    if not script_installed:
        raise Exception("Unable to determine location of determine_tbd_calver_version_number.sh.")
    
    # Now that we know where the script is, we can run it
    # Before we can run it however, we need to identify the bash interpreter we will use
    interpreter = ""
    try:
        Shell.execute_shell_command(f"bash --version", cwd=repo_path).Stdout
        interpreter = "bash"
    except:
        pass
    if not interpreter:
        logging.warning("The bash executable was not found or not configured properly. Checking for sh executable.")
        try:
            Shell.execute_shell_command(f"sh --version", cwd=repo_path).Stdout
            interpreter = "sh"
        except:
            pass
    if not interpreter:
        logging.fatal("Unable to find a working bash interpreter")
    
    # Run the shell command
    logging.debug("Running shell script to calculate version number.")
    version_number = Shell.execute_shell_command(f"{interpreter} {script_path}", cwd=repo_path).Stdout
    logging.debug(f"Raw version number determined to be '{version_number}'.")
    
    # Return raw output if user requested it    
    if not adjust_for_pep_440 and not adjust_for_pypi:
        return version_number
    
    # Parse the version number
    parts = version_number.split(".")
    year = parts[0]
    month = parts[1]
    day = parts[2]
    branch_type = parts[3]
    build_or_commit = parts[4]
    
    # Adjust the version number to be compliant with PEP-440
    # This standard is defined here: https://peps.python.org/pep-0440/
    #
    # With PEP 440 version specifier is `<public identifier>[+<local label>]`
    # This means we need to adjust our version numbers to use a + rather than a .
    # for the fourth element in the version number for non release branches
    #
    
    if adjust_for_pep_440 or adjust_for_pypi:
        if branch_type in ["feature", "bug", "patch", "master"]:
            version_number = f"{year}.{month}.{day}+{branch_type}.{build_or_commit}"
        elif branch_type == "release":
            version_number = f"{year}.{month}.{day}.{build_or_commit}"
        else:
            raise Exception(f"Unable to determine version number for a branch of type {branch_type} as it is not compliant with PEP 440. See notes in source code for more details.")

        # Check the official regex to ensure the version number is compliant
        # https://peps.python.org/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions
        # https://stackoverflow.com/questions/37972029/regex-to-match-pep440-compliant-version-strings
        
        _regex = re.compile(
            r"^\s*" + version.VERSION_PATTERN + r"\s*$",
            re.VERBOSE | re.IGNORECASE,
        )
        
        compliant = re.match(_regex, version_number) is not None
        if not compliant:
            raise Exception(f"The version number '{version_number}' was not PEP-440 compliant.")

        logging.debug(f"Adjusted version number to '{version_number}' so that it is PEP-440 compliant.")
    
    # Note that Pypi does not allow local labels to be used. It is very strict
    # that it is a public package repository meant to serve public packages.
    # As such, the version numbers output by this library will not be compliant
    # with pypi (though they will work with other systems like artifactory).
    # 
    # One of the main issues is that the PEP 440 scheme really only allows numbers
    # which it represents with N:
    #
    #        [N!]N(.N)*[{a|b|rc}N][.postN][.devN]
    #
    # This means that only integration branches can have version numbers because 
    # they are synchronous in nature. Asynchronous branches cannot be assigned 
    # sequential numbers because they are non-sequention by nature.
    #
    # We will use rc to denote the master branch artifacts
    #
    
    if adjust_for_pypi:
        if branch_type == "master":
            version_number = version_number.replace("+master.", ".rc")
        elif branch_type == "release":
            version_number = version_number.replace(".release.", ".rc")
        else:
            raise Exception(f"Versions for branch type {branch_type} can not be uploaded to PyPI.")

        logging.debug(f"Adjusted version number for PyPI. New version number: '{version_number}'.")

    return version_number