import os
import unicodedata


def fullwidth_to_half_width(s):
    s_normalized = unicodedata.normalize('NFC', s)
    result = ""
    for character in s_normalized:
        code_point = ord(character)

        if code_point == 0x3000:
            result += " "
        elif 0xFF01 <= code_point <= 0xFF5E:
            result += chr(code_point - 0xfee0)
        elif code_point == 0x3002:
            result += "."
        elif code_point == 0x2014:
            result += "-"
        # elif code_point == 0x201d or code_point == 0x201c:
        #     result += "\""
        # elif code_point == 0x2018 or code_point == 0x2019:
        #     result += "\'"
        elif code_point == 0x2026:
            result += ".."
        elif code_point == 0x300a:
            result += "["
        elif code_point == 0x300b:
            result += "]"
        elif code_point == 0x3010:
            result += "["
        elif code_point == 0x3011:
            result += "]"
        elif code_point == 0x3001:
            result += ","
        else:
            result += character
    return result


path = r'./zz/'

dirFiles = os.listdir(path)
dirFiles.remove('.DS_Store')
dirFiles.sort(key=lambda x: int(os.path.splitext(x)[0]))
# dirFiles1 = dirFiles[0:550]
# dirFiles2 = dirFiles[550:1100]
# dirFiles3 = dirFiles[1100:1650]
# dirFiles4 = dirFiles[1650:2200]
# dirFiles5 = dirFiles[2220:2750]
# dirFiles6 = dirFiles[2750:]
subdirFiles = []
for s in range(309, len(dirFiles), 80):
    subdirFiles.append(dirFiles[s:s+80])


if __name__ == '__main__':
    for i in range(0, len(subdirFiles)):
        total_words = 0
        with open('join{}.txt'.format(i), 'a+', encoding='utf-8') as f:
            for file in subdirFiles[i]:
                print(file, end=" ")
                with open("./zz/{}".format(file), 'r', encoding='utf-8') as j:
                    f.write(os.path.splitext(file)[0])
                    f.write('\n\n')
                    for line in j:
                        line = line.replace(u'\u3000', u'')
                        s1 = line.strip()
                        s1 = fullwidth_to_half_width(s1)
                        f.write(s1)
                        for ca in s1:
                            if ca>=u'\u4e00' and ca<=u'\u9fa5':
                                total_words = total_words + 1
                            elif ca>=u'\uff00' and ca<=u'\uffef':
                                total_words = total_words + 1
                            elif ca >= u'\u0020' and ca <= u'\u007f':
                                total_words = total_words + 1
                            else:
                                pass
                                # print(hex(ord(ca)), ca)
                    f.write('\n\n')
            print()
        print(subdirFiles[i], " have total words ", total_words, end='\n')
