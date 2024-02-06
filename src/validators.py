def process_line(line:str, n:int) -> list:
    data = line.strip().split("::")
    return data[:n]


def validate_lines_num(lines:list[str], allowed_lines:int=2) -> bool:
    return len(lines) <= allowed_lines


def are_all_true(elements:list) -> bool:
    return all(elements)