import os


path = r'./zz/'

dirFiles = os.listdir(path)
dirFiles.remove('.DS_Store')
dirFiles.sort(key=lambda x: int(os.path.splitext(x)[0]))
dirFiles1 = dirFiles[0:550]
dirFiles2 = dirFiles[550:1100]
dirFiles3 = dirFiles[1100:1650]
dirFiles4 = dirFiles[1650:2200]
dirFiles5 = dirFiles[2220:2750]
dirFiles6 = dirFiles[2750:]


total_words = 0
if __name__ == '__main__':
    for i in range(1, 7):
        subdirFiles = "dirFiles" + str(i)
        print(i, subdirFiles)
        with open('join{}.txt'.format(i), 'a+', encoding='utf-8') as f:
            for file in eval(subdirFiles):
                print(file)
                with open("./zz/{}".format(file), 'r', encoding='utf-8') as j:
                    f.write(os.path.splitext(file)[0])
                    f.write('\n\n')
                    for line in j:
                        line.replace(u'\u3000', '')
                        s1 = line.strip()
                        for ca in s1:
                            if ca == u'\u3000':
                                continue
                            else:
                                f.write(ca)
                                total_words = total_words + 1
                                # print(hex(ord(ca)), ca)
                    f.write('\n\n')
    print("total words ", total_words)
