# 1. Function receives a find string,
# a replace string, and one or more text files.

def replace(find_string, replace_string, *text_files):

# 2. Find the string in the text files. Alert user
# if text string is not found.

    for text_file in text_files:
        text = open(text_file, 'r')
        line = text.readline()
        pos = 0
        while pos > -1:
            pos = line.find(find_string, pos+len(find_string), )
            if pos > -1:
                print('Found \'{}\' at position {} in: '.format(find_string, str(pos)) + text_file)

                # 3. Replace the string in the text file.

                line_list = list(line)
                del line_list[pos:pos + len(find_string)]
                line_list.insert(pos, replace_string)
                new_line = ''.join(line_list)
                print(new_line)
        else:
            print('Done with {}'.format(text_file))
        text.close()

# 4. Save changes to file.

replace('is', 'blah', '/Users/connorodell/python/data/replace.txt', '/Users/connorodell/python/data/another.txt')
