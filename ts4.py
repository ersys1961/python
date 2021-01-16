
f_out = open('test4_1.txt', 'w', encoding="utf-8")
with open('test4.txt', 'r', encoding="utf-8") as f_inp:
    for line in f_inp:
        if line.count('One') > 0:
            line = line.replace('One', 'Один')
        elif line.count('Two') > 0:
            line = line.replace('Two', 'Два')
        elif line.count('Three') > 0:
            line = line.replace('Three', 'Три')
        elif line.count('Four') > 0:
            line = line.replace('Four', 'Четыре')
        f_out.write(line)
f_out.close()

