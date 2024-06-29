def block_decorator(word, prefix=None, suffix=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            code = ''
            if prefix:
                code += '\n'.join(prefix) + '\n'
            code += f'\\begin{{{word}}}\n'
            code += func(*args, **kwargs)
            code += f'\\end{{{word}}}\n'
            if suffix is not None:
                code += suffix
            return code

        return wrapper

    return decorator


def table_decorator(func):
    def wrapper(*args, **kwargs):
        n, m = args
        code = '\\begin{tabular}'
        code += f'{{{' '.join(['c' for _ in range(n)])}}}\n'
        code += func(*args, **kwargs)
        code += '\\end{tabular}\n'
        return code

    return wrapper


@block_decorator('center')
@table_decorator
def generate_table(n, m):
    content = [' & '.join([str(j + 1) for j in range(i * n, (i + 1) * n)]) + '\\\\' for i in range(m)]
    return '\n'.join(content) + '\n'


@block_decorator('center')
def generate_image(path):
    return f'\\includegraphics[scale=0.4, angle=45]{{{path}}}\n'


@block_decorator('document', prefix=['\\documentclass{article}'])
def generate_document_with_table(n, m):
    return generate_table(n, m)


@block_decorator('document', prefix=['\\documentclass{article}', '\\usepackage{graphicx}'])
def generate_document_with_image(path):
    return generate_image(path)
