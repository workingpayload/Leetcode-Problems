class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k',
       '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't',
       '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}

        l = []

        for i in range(len(s)-2):
            if s[i] == '#':
                l.append(s[i - 2:i + 1])
            else:
                if s[i + 1] == '#' or s[i + 2] == '#':
                    continue
                else:
                    l.append(s[i])
        if s[-1]=='#':
            l.append(s[-3:])
        elif s[-2]=='#':
            l.append(s[-4:-1])
            l.append(s[-1])
        else:
            l.append(s[-2])
            l.append(s[-1])

        newstring = ""

        for i in range(len(l)):
            if l[i] in dic.keys():
                newstring+=dic[l[i]]


        return newstring
                    
                
        