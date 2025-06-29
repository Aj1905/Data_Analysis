import importlib.util
import pathlib
from loaders import base_loader
from utils import result_formatter, logger


def discover_tests(base_dir='tests'):
    for py_file in pathlib.Path(base_dir).rglob('*.py'):
        yield py_file


def run_tests(groups, base_dir='tests'):
    results = []
    for py_file in discover_tests(base_dir):
        spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, 'run'):
            result = module.run(groups)
            results.append((py_file, result))
    return results


def main():
    data_rows = base_loader.load_csv('data/sample_data.csv')
    groups = base_loader.group_by(data_rows, 'group')
    for path, result in run_tests(groups):
        logger.log(f'== {path} ==')
        logger.log(result_formatter.format_result(result))
        logger.log('')


if __name__ == '__main__':
    main()
