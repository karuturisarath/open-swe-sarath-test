import subprocess

def execute_git_command(command):
    try:
        result = subprocess.run(['git'] + command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def create_dynamic_session_branch():
    return execute_git_command('checkout -b dynamic-session-branch')

def list_branches():
    return execute_git_command('branch')

if __name__ == '__main__':
    print(create_dynamic_session_branch())
    print(list_branches())
