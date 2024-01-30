import os.path

OPERATIONS_PATH = os.path.join(ROOT_DIR, 'utils', 'operations.json')
def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    only_executed = get_only_executed(all_operations)
    sorting_operations = sorting_operations_by_date(only_executed)