import textwrap

import pyperclip


def tempalte(title: str, question: str, answer: str) -> str:
    return f'''
??? note "{title.strip()}"
    === "题目"
        ```
{textwrap.indent(question.strip(), '        ')}
        ```
    === "答案"
        ```
{textwrap.indent(answer.strip(), '        ')}
        ```
    '''.strip()


keys = ['title', 'question', 'answer']
kwargs = {}
for ith, key in enumerate(keys):
    input(f'{key} >>> ')
    kwargs[key] = pyperclip.paste().replace('\r', '')
    print(kwargs[key])
with open('crawler.md', 'a+') as f:
    f.write(tempalte(**kwargs))
    f.write('\n\n')
