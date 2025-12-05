import subprocess

def execute_git_command(command):
    try:
        result = subprocess.run(['git'] + command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

if __name__ == '__main__':
    # Example usage: list all branches
    print(execute_git_command('branch'))
