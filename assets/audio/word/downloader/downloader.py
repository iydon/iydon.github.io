import pathlib
import requests


words = [
    'access', 'Adobe', 'admin', 'adversarial', 'agile', 'amazon', 'analogy',
    'Angular', 'AJAX', 'alias', 'Apache', 'app', 'archive', 'array', 'ASCII',
    'aspect', 'async', 'avatar', 'Azure', 'bind', 'cache', 'Chrome', 'clang',
    'daemon', 'debt', 'deny', 'deprecate', 'deque', 'digest', 'Django', 'doc',
    'dotnet', 'ephemeral', 'epoch', 'execute', 'executor', 'event', 'facade',
    'fedora', 'format', 'gauge', 'Git', 'GraphQL', 'GUI', 'Haskell', 'height',
    'hidden', 'image', 'implement', 'integer', 'issue', 'Java', 'jpg', 'key',
    'Kubernetes', 'lambda', 'Ldap', 'linear', 'LINQ', 'Linux', 'locale', 'Lucene',
    'main', 'margin', 'matrix', 'maven', 'Microsoft', 'miscellaneous', 'module',
    'null', 'obsolete', 'phantom', 'parameter', 'privilege', 'Prometheus', 'putty',
    'Qt', 'query', 'Realm', 'reconcile', 'Redux', 'resume', 'resolved', 'resort',
    'retina', 'route', 'San Jose', 'safari', 'scheme', 'scala', 'segue', 'suite',
    'thymeleaf', 'tuple', 'typical', 'Vagrant', 'variable', 'verbose', 'vue',
    'width', 'YouTube',
]
others = {
    'Coq': ['https://upload.wikimedia.org/wikipedia/commons/4/47/Fr-coq.ogg', None],
    'Dijkstra': ['https://upload.wikimedia.org/wikipedia/commons/8/85/Dijkstra.ogg', 'https://dict.youdao.com/dictvoice?audio=digest&type=2'],
    'GNU': ['https://upload.wikimedia.org/wikipedia/commons/2/24/En-gnu.ogg', 'https://upload.wikimedia.org/wikipedia/commons/2/24/En-gnu.ogg'],
    'Grafana': ['http://www.howtopronounce.cc/file/e204a97ed1e440c5ab15ea0117beb955.mp3', 'http://www.howtopronounce.cc/file/e204a97ed1e440c5ab15ea0117beb955.mp3'],
    'nginx': [None, None],
    'OS X': [None, None],
    'SQL': [None, None],
    'sudo': [None, None],
    'Ubuntu': ['http://upload.wikimedia.org/wikipedia/commons/b/b5/En-Ubuntu_pronunciation.oga', 'http://upload.wikimedia.org/wikipedia/commons/b/b5/En-Ubuntu_pronunciation.oga'],
}

url = 'https://dict.youdao.com/dictvoice'
types = ['uk', 'us']
root = pathlib.Path('.')
rename = lambda string: string.lower().replace(' ', '_')
# words
for type in types:
    (root/type).mkdir(parents=True, exist_ok=True)
for word in words:
    for ith, type in enumerate(types):
        path = root/type/f'{rename(word)}.mp3'
        if not path.exists():
            response = requests.get(url, params={'audio': word, 'type': ith+1})
            path.write_bytes(response.content)
# others
print('Please download the following link manually:')
for word, (uk, us) in others.items():
    print('-', word)
    if uk is not None and not (root/'uk'/f'{rename(word)}.mp3').exists():
        print('    uk:', uk)
    if us is not None and not (root/'us'/f'{rename(word)}.mp3').exists():
        print('    us:', us)
