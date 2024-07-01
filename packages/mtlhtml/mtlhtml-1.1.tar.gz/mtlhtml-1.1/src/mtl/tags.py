def htm(kwrgs: str, *contents, props: list, ref: str) -> str:
    temp_content = ""
    temp_props = ""

    for content in contents:
        temp_content += content

    for prop in props:
        temp_props += f"{prop}"

    return f'''<{kwrgs} {temp_props}>{temp_content}</{kwrgs}>'''
