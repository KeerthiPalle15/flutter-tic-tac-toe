import re
with open('lib/main.dart.bak', 'r') as f:
    content = f.read()

old = 'body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column('''

new = 'body: Padding(
        padding: const EdgeInsets.all(16),
        child: SingleChildScrollView(
          child: Column('''

content = content.replace(old, new)

pattern_end = '],
        ),
      ),
    );'
replacement_end = '],
        ),
        ),
      ),
    );'

if pattern_end in content:
    content = content.replace(pattern_end, replacement_end)
    with open('lib/main.dart', 'w') as f:
        f.write(content)
    print('Success')
else:
    print('Pattern not found')
