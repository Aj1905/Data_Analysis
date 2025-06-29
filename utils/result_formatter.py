from typing import Dict


def format_result(result: Dict) -> str:
    return '\n'.join(f'{k}: {v}' for k, v in result.items())
