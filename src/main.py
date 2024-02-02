from utils import get_all_operations, sorting_operations_by_date, get_only_executed, get_output_date
import os
from configurations import ROOT_DIR


OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')

def main():
    all_operations = get_all_operations()
    only_executed = get_only_executed(all_operations)
    sorting_operations = sorting_operations_by_date(only_executed)
    five_operations = sorting_operations[:5]

    for operation in five_operations:
        print(get_output_date(operation))
        print()


if __name__ == '__main__':
    main()