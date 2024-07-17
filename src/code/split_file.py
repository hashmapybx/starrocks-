
import os

cur_path = os.getcwd()
print(cur_path)
with open("sqls/sql", 'r') as fin:
    lines = fin.readlines()


idxs = []

for idx, line in enumerate(lines):
    # print("idx:{}, data:{}".format(idx, line))
    if line.startswith("-- query"):
        idxs.append(idx)
        print(idx, line)
        # fout.writelines(line[first_tmp:])

print(idxs)

window_size = 2
result = [idxs[i:i + window_size] for i in range(len(idxs) - window_size + 1)]
print(len(result))

for i in range(len(result)):
    fout = open("sqls/99sql/{}.sql".format(i + 1), 'w')
    id_end = result[i]
    fout.writelines(lines[id_end[0]:id_end[1] - 1])
    fout.close()
