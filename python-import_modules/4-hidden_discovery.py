#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    import marshal
    import types

    def find_hidden(pyc_file):
        with open(pyc_file, "rb") as f:
            f.read(16)
            code = marshal.load(f)

        def get_names(code_obj):
            for const in code_obj.co_consts:
                if isinstance(const, types.CodeType):
                    yield from get_names(const)
            for name in code_obj.co_names:
                if name.startswith('__') and name.endswith('__'):
                    continue
                yield name

        return sorted(set(get_names(code)))

    if __name__ == "__main__":
        hidden_functions = find_hidden("hidden_4.pyc")
        for name in hidden_functions:
            print(name)
