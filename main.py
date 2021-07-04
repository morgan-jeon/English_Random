import re
import random, sys

with open('book', 'r',-1,encoding='utf-8') as f:
    lines = f.read().replace('\n', ' ')
ps = re.split('#[1-9]+', lines)
ps = list(map(lambda x: x.strip(), ps))
ps = list(filter(lambda x: x != '', ps))
print(f'Total: {len(ps)}')

g = open('result', 'w',encoding='utf-8')
num = 0
for p in ps:
    num = num + 1
    g.write(f'#{num}\n')
    print(f'#{num}')
    ls = p.split('. ')
    n = 0
    for l in ls:
        n = n + 1
        ws = l.split(' ')
        for i in range(0, len(ws) - 1):
            if ws[i] == "(":
                ws[i] = ws[i] + ws[i + 1]
                del (ws[i + 1])
            if ws[i] == ")":
                ws[i] = ws[i - 1] + ws[i]
                del (ws[i - 1])
        print(len(ws))
        try:
            R = random.sample(range(2, len(ws) - 2), int(len(ws) / 3))
        except Exception as e:
            print(e)
            # sys.exit()
        for i in R:
            try:
                ws[i] = ws[i - 1] + ' ' + ws[i]
                del (ws[i - 1])
            except:
                trash = 0
        print(R)
        random.shuffle(ws)
        rl = ' / '.join(ws)
        g.write(f'L{n}. ' + rl + '\n\n')
    g.write('\n')

g.close()
