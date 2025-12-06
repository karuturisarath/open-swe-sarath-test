import logging

# Initialize the logger
def init_logger():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Execute JavaScript code by calling a Node.js subprocess.
def execute_js_code(js_code):
    try:
        init_logger()
        logging.debug('Executing JavaScript code...')
        result = subprocess.run(['node', '-e', js_code], capture_output=True, text=True, check=True)
        logging.debug('Execution completed.')
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error('An error occurred: %s', e.stderr)
        return e.stderr

# Main function for testing.
if __name__ == '__main__':
    js_code = "console.log('Hello, world!');"
    output = execute_js_code(js_code)
    print(output)