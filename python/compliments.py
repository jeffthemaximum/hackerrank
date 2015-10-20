import pudb

def check_weird_line(line):
    if "p>" not in line and "<br/>&#13" in line:
        temp_line = line
        return temp_line
    return True

def remove_tags(line):
    if line[:17] == '<p class="large">':
        line = line.replace('<p class="large">', '')
    if line[:18] == '<p class="medium">':
        line = line.replace('<p class="medium">', '')
    if line[:17] == '<p class="small">':
        line = line.replace('<p class="small">', '')
    line = line.replace('</p>', "\",")
    if '&#13' in line:
        line = line.replace('<br/>&#13;', '')
        line = line.replace('\n', ' ')
    if check_weird_line(line) != True:
        return line
    return "\"" + line



compliments_input_file = open('compliments.txt', 'r')
compliments_output_file = open('stripped_compliments.txt', 'w')
compliment_dict = {}
temp_line = ""

for i, line in enumerate(compliments_input_file):
    # if i == 78:
    #     pu.db
    if check_weird_line(line) == True:
        line = remove_tags(line)
        if temp_line != "":
            compliment_dict[i] = temp_line + line[1:]
        else:
            compliment_dict[i] = temp_line + line
        print line
        temp_line = ""
    else:
        temp_line = check_weird_line(line)
        temp_line = remove_tags(line)

# compliments_output_file.write(compliment_dict)
print compliment_dict
compliments_output_file.close()
compliments_input_file.close()