# first step: converting file types of .txt to .patch
import os
import re
def convert_txt_to_patch(folder):
    for filename in os.listdir(folder):
        new_filename = filename.replace(".txt", ".patch")
        prev_name = folder + "/" + filename
        new_name = folder + "/" + new_filename
        os.rename(prev_name, new_name)

convert_txt_to_patch('./Bears-Patches')
convert_txt_to_patch('./QuickBugs-Patches')

# second step: splitting all patches
def slice_patch2(path, folder_name):
    cnt = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.patch'):
                project = root.split('/')[-1]
                name = file.split('.')[0]
                id = name
                number_diff = 0
                number_AT = 0
                patch = ''
                content = False
                try:
                    with open(os.path.join(root, file)) as f:
                        for line in f:
                            if line.startswith('--- '):
                                minus_line = line
                            elif line.startswith('+++ '):
                                plus_line = line
                            elif line.startswith('diff '):
                                if number_diff > 0:
                                    # save previous patch
                                    new_path = path.replace(folder_name, folder_name + 'Processed') + project + '/' + id
                                    new_name = id+'_'+str(number_AT)+'.patch'
                                    if not os.path.exists(new_path):
                                        os.makedirs(new_path)
                                    with open(os.path.join(new_path, new_name), 'w+') as f:
                                        f.write(minus_line + plus_line + patch)

                                    content = False
                                else:
                                    number_diff += 1
                                    continue
                            elif line.startswith('@@ '):
                                if content:
                                    # save previous patch
                                    new_path = path.replace(folder_name, folder_name + 'Processed') + project + '/' + id
                                    new_name = id+'_'+str(number_AT)+'.patch'
                                    if not os.path.exists(new_path):
                                        os.makedirs(new_path)
                                    with open(os.path.join(new_path, new_name), 'w+') as f:
                                        f.write(minus_line + plus_line + patch)

                                    patch = line
                                    number_AT += 1
                                    content = True
                                else:
                                    # first @@
                                    patch = line
                                    number_AT += 1
                                    content = True
                            elif content:
                                patch += line
                            else:
                                continue
                except Exception as e:
                    print(e)

                # save last patch
                new_path = path.replace(folder_name, folder_name + 'Processed') + project + '/' + id
                new_name = id + '_' + str(number_AT) + '.patch'
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                with open(os.path.join(new_path, new_name), 'w+') as f:
                    f.write(minus_line + plus_line + patch)

# slice_patch(path)
path_list = ['./Bears-Patches', './Bugs.jar-Patches', './D4J-Patches', './ManySStuBs4Jsmall', './QuickBugs-Patches']
name_list = ['Bears-Patches', 'Bugs.jar-Patches', 'D4J-Patches', 'ManySStuBs4Jsmall', 'QuickBugs-Patches']

for i in range(len(path_list)):
    slice_patch2(path_list[i], name_list[i])

# thrid step: converting patches to buggy and fixed strings
def get_only_change(path_patch, type='patched'):
    with open(path_patch, 'r') as file: # changing from r+ to r
        lines = ''
        p = r"([^\w_])"
        # try:
        for line in file:
            line = line.strip()
            if line != '':
                if line.startswith('diff') or line.startswith('index'):
                    continue
                elif line.startswith('--- ') or line.startswith('-- ') or line.startswith('PATCH_DIFF_ORIG=---') or line.startswith('+++ ') or line.startswith('++ '):
                    continue
                elif type == 'buggy':
                    if line.startswith('@@'):
                        # retain the part after @@
                        line = re.sub("@@.*@@", "", line)
                        lines += line.strip() + ' '
                    elif line.strip().startswith('*'):
                        continue
                    elif line.strip().startswith('/*'):
                        continue
                    elif line.startswith('+'):
                        continue
                    elif line.startswith('-'):
                        if line[1:].strip() == '':
                            continue
                        if line[1:].strip().startswith('//'):
                            continue
                        lines += line[1:].strip() + ' '
                    else: # context lines
                        if line.strip().startswith('//'):
                            continue
                        if line.strip() == '':
                            continue
                        lines += line.strip() + ' '
                elif type == 'patched':
                    if line.startswith('@@'):
                        # retain the part after @@
                        line = re.sub("@@.*@@", "", line)
                        lines += line.strip() + ' '
                    elif line.strip().startswith('*'):
                        continue
                    elif line.strip().startswith('/*'):
                        continue
                    elif line.startswith('-'):
                        continue
                    elif line.startswith('+'):
                        if line[1:].strip() == '':
                            continue
                        if line[1:].strip().startswith('//'):
                            continue
                        lines += line[1:].strip() + ' '
                    else: # context lines
                        if line.strip().startswith('//'):
                            continue
                        if line.strip() == '':
                            continue
                        lines += line.strip() + ' '
    lines = re.sub("\n", " ", lines)
    lines = re.sub("\s{2,}", " ", lines)
    lines = lines.strip()
    return lines

path = './Processed_5_datasets'
with open('./Final_data/bugfix.buggy', 'a') as buggy, open('./Final_data/bugfix.fixed', 'a') as fixed:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.patch'):
                file_path = root + '/' + file
                print(file_path)
                buggy_string = get_only_change(file_path, 'buggy')
                fixed_string = get_only_change(file_path, 'patched')

                if buggy_string != fixed_string: # only store meaningful data
                    buggy.write(buggy_string)
                    buggy.write('\n')
                    fixed.write(fixed_string)
                    fixed.write('\n')

print("end")