class String():

    def __init__(self, str1,rules=[]):
        str1=str(str1)
        self.value = str1
        self.bits = ""
        self.lenght = 0
        self.n=-1
        self.stri_list = []
        self.pair_original = []
        self.rules=rules
        self.val_list=list(str1)
        self.dict_b64 = {}
        self.dict_pair = {}
        self.histogram_dict={}

    def __getitem__(self,item):
        if isinstance(item, slice):
            start, stop, step = item.indices(len(self.value))
            return String([self.value[i] for i in range(start, stop, step)])
        elif isinstance(item, int):
            return String(self.value[item])
        elif isinstance(item, tuple):
            raise NotImplementedError
        else:
            raise TypeError
    def __add__(self, other):
        new_string = (str(self.value) + str(other))

        return String(new_string)

    def __mul__(self, other):
        return String(self.value * int(other))

    def __cmp__(self, other):
        if (self.value == str(other)):
            return True
        else:
            return False
    def count(self,val,start1=0,end1=-1):
        return (self.value.count(val,start1, end1))

    def __iter__(self):
        return self

    def __next__(self):
        if self.n+1<len(self.value):
            self.n+=1
            return String(self.val_list[self.n])
        else:
            raise StopIteration

    def isupper(self):
        return str(self.value).isupper()
    def islower(self):
        return str(self.value).islower()

    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        return (self.value) == (str(other))

    def base64(self) -> 'String':
        '''
        Encode the String (self) to a base64 string
        :return: a new instance of String with the encoded string.
        '''

        self.create_base_64_dict()
        list_8=[]
        b_64=[]
        temp=[]
        encod=[]
        c=0
        list_8=self.convert_string_into_a_sequence_of_bits()
        len_6=6-len(list_8) % 6
        if (len_6!=0):
            for i in range(len_6):
                list_8.append("0")
        for j in range(len(list_8)//6):
            temp=list_8[c:6+c]
            temp2="".join(temp)
            b_64.append(temp2)
            c=c+6
        for i in range(len(b_64)):
            if(b_64[i] in self.dict_b64):
                encod.append(self.dict_b64.get(b_64[i]))
        encod_str=''.join([str(elem) for elem in encod])
        return String(encod_str)


    def byte_pair_encoding(self) -> 'String':
        '''
        Encode the String (self) to a byte pair string
        :return: a new instance of String with the encoded string.
        :exception: BytePairError
        '''
        self.stri_list = list(self.value)
        pair_list2 = []
        self.rules=[]
        others = True
        digit = True
        upper_case = True
        lower_case = True
        # pair_list2 = list(self.value)
        for i in range(len(self.val_list)):
            if others == True and (33 <= ord(self.val_list[i]) <= 47 or 58 <= ord(self.val_list[i]) <= 64 or 91 <= ord(
                    self.val_list[i]) <= 96 or 124 <= ord(self.val_list[i]) <= 126):
                others = False
            if digit == True and 48 <= ord(self.val_list[i]) <= 57:
                digit = False
            if upper_case == True and 65 <= ord(self.val_list[i]) <= 90:
                upper_case = False
            if lower_case == True and 97 <= ord(self.val_list[i]) <= 122:
                lower_case = False

        if others == True:
            count = 33
        elif digit == True:
            count = 48
        elif upper_case == True:
            count = 65
        elif lower_case == True:
            count = 97
        elif others==False and digit==False and upper_case==False and lower_case==False:
            raise BytePairError
        self.pair_list_fix()
        sorted_pairs = sorted(self.dict_pair, key=self.dict_pair.get, reverse=True)
        max_key = sorted_pairs[0]

        while (self.dict_pair[max_key] != 1):
            c = 0
            for i in range(len(self.val_list)):
                if (i + c < len(self.val_list) - 2) and (self.val_list[c + i] + self.val_list[c + i + 1]) == max_key:
                    if others == True:
                        if 48 <= count <= 57:
                            count = 58
                        if 64 <= count <= 90:
                            count = 91
                        if 95 <= count <= 123:
                            count = 124
                        if count>126 and digit==True:
                            count=48
                            others=False
                        if count>126 and digit==False and upper_case==True:
                            count=65
                            others=False
                        if count>126 and digit==False and upper_case==False and lower_case==True:
                            count=97
                            others=False
                        if count>126 and digit==False and upper_case==False and lower_case==False:
                            raise BytePairError
                            others=False
                    elif digit==True:
                        if count>57 and upper_case==True:
                            count=65
                            digit=False
                        if count>57 and upper_case==False and lower_case==True:
                            count=97
                            digit=False
                        if count>57 and upper_case==False and lower_case==False:
                            raise BytePairError
                            digit=False
                    elif upper_case==True:
                        if count>90 and upper_case==True:
                            count=97
                            upper_case=False
                        if count>90 and lower_case==False:
                            raise BytePairError
                            upper_case=False
                    elif lower_case==True:
                        if count>122 :
                            raise BytePairError
                            lower_case=False
                    pair_list2.append(chr(count))
                    c = c + 1
                    if c+i==len(self.val_list) - 2:
                        pair_list2.append(self.val_list[-1])

                elif (i + c < len(self.val_list) - 2) and (
                        self.val_list[c + i] + self.val_list[c + i + 1]) != max_key:  # and (
                    # self.val_list[c + i + 1] + self.val_list[c + i + 2]) != max_key:
                    pair_list2.append(self.val_list[c + i])
                elif (i + c == len(self.val_list) - 2) and self.val_list[len(self.val_list) - 2] + self.val_list[
                    len(self.val_list) - 1] == max_key:
                    pair_list2.append(chr(count))
                elif (i + c == len(self.val_list) - 2) and self.val_list[len(self.val_list) - 2] + self.val_list[
                    len(self.val_list) - 1] != max_key:
                    pair_list2.append(self.val_list[c + i])
                    pair_list2.append(self.val_list[c + i + 1])

            self.dict_pair[chr(count)] = self.dict_pair.pop(max_key)
            self.rules.append(str(chr(count)) + " = " + max_key)
            self.val_list = pair_list2
            self.stri_list = pair_list2
            self.value = "".join(self.stri_list)
            self.pair_list_fix()
            sorted_pairs = sorted(self.dict_pair, key=self.dict_pair.get, reverse=True)
            max_key = sorted_pairs[0]
            pair_list2 = []
            count = count + 1


        return String(self.value,self.rules)


    def cyclic_bits(self, num: int) -> 'String':
        '''
        Encode the String (self) to a cyclic bits string
        :return: a new instance of String with the encoded string.
        '''
        n=num
        b_8 = []
        c = 0
        self.stri_list=self.convert_string_into_a_sequence_of_bits()
        n=n%len(self.stri_list)
        if n>0:
            for i in range(n):
                self.stri_list.append(self.stri_list.pop(0))
        if n<0:
            for i in range(n):
                self.stri_list.insert(0,self.stri_list.pop(-1))
        len_8 = 8 - (len(self.stri_list)) % 8
        if (len_8 != 0):
            for i in range(len_8):
                self.stri_list.append("0")
        for j in range(len(self.stri_list) // 8):
            temp = self.stri_list[c:8 + c]
            temp2 = "".join(temp)
            b_8.append(temp2)
            c = c + 8
        self.stri_list = b_8
        fin_str=self.convert_sequence_of_bits_into_a_string()
        return String(fin_str)


    def cyclic_chars(self, num: int) -> 'String':
        '''
        Encode the String (self) to a cyclic chars string
        :return: a new instance of String with the encoded string.
        :exception: CyclicCharsError
        '''
        n=num
        first=[]
        last=[]
        first=list(self.value)
        for i in range(len(first)):
            if 32>ord(first[i])or ord(first[i])>126:
                raise CyclicCharsError
            if n>0:
                s_cyc=ord(first[i])+n
                if (32<=s_cyc<127):
                    last.append(chr(s_cyc))
                elif s_cyc>126:
                    s_cyc=(n-(127-(s_cyc-n))+32)
                    last.append(chr(s_cyc))
            if n<0:
                new_n=(-1)*n
                return self.decode_cyclic_chars(new_n)
        last_srt=''.join([str(elem) for elem in last])
        return String(last_srt)
        #raise NotImplemented

    def histogram_of_chars(self) -> dict:
        '''
        calculate the histogram of the String (self). The bins are
        "control code", "digits", "upper", "lower" , "other printable"
        and "higher than 128".
        :return: a dictonery of the histogram. keys are bins.
        '''
        other=0
        control_code=0
        digit=0
        upper=0
        lower=0
        higher=0

        for i in range(len(self.val_list)):
            if  (33 <= ord(self.val_list[i]) <= 47 or 58 <= ord(self.val_list[i]) <= 64 or 91 <= ord(
                    self.val_list[i]) <= 96 or 124 <= ord(self.val_list[i]) <= 126):
                other +=1
            if 48 <= ord(self.val_list[i]) <= 57:
                digit +=1
            if  65 <= ord(self.val_list[i]) <= 90:
                upper+=1
            if  97 <= ord(self.val_list[i]) <= 122:
                lower += 1
            if ord(self.val_list[i])==32 or ord(self.val_list[i])==123 or 127<=ord(self.val_list[i])<=128:
                control_code+=1
            if ord(self.val_list[i])>=129:
                higher=+1

        self.histogram_dict["control code"]=control_code
        self.histogram_dict["digits"]=digit
        self.histogram_dict["upper"]=upper
        self.histogram_dict["lower"]=lower
        self.histogram_dict["other printable"]=other
        self.histogram_dict["higher than 128"]=higher
        return self.histogram_dict
        raise NotImplemented

    def decode_base64(self) -> 'String':
        '''
        Decode the String (self) to its original base64 string.
        :return: a new instance of String with the endecoded string.
        :exception: Base64DecodeError
        '''
        dencod=[]
        b_8=[]
        c=0
        stri_1="*"
        fin_list=[]
        self.create_base_64_dict()
        self.stri_list=list(self.value)
        for i in range(len(self.stri_list)):
            for code, char in self.dict_b64.items():
                if char == self.stri_list[i]:
                    dencod.append(code)
        if len(dencod) != len(self.value):
            raise Base64DecodeError
        len_8 = 8 - (len(dencod)*6) % 8
        if (len_8 != 0):
            for i in range(len_8):
                dencod.append("0")
        for i in range(len(dencod)):
            stri_1=stri_1+dencod[i]
        fin_list=list(stri_1)
        fin_list.remove("*")
        dencod=fin_list
        for j in range(len(dencod) // 8):
            temp = dencod[c:8 + c]
            temp2 = "".join(temp)
            b_8.append(temp2)
            c = c + 8
        self.stri_list=b_8
        self.bits = ''.join([str(elem) for elem in b_8])
        decoded=self.convert_sequence_of_bits_into_a_string()
        return String(decoded)


        raise NotImplemented

    def decode_byte_pair(self) -> 'String':
        '''
        Decode the String (self) to its original byte pair string.
        Uses the property rules.
        :return: a new instance of String with the endecoded string.
        :exception: BytePairDecodeError
        '''
        count_swich = 0
        if len(self.rules)==0:
            raise BytePairDecodeError
        self.create_dict_pair_rules()
        self.stri_list = list(self.value)
        while (count_swich < len(self.stri_list)):
            count_swich = 0
            for i in range(len(self.stri_list)):
                val_r = self.dict_pair.get(self.stri_list[i])
                if val_r:
                    self.pair_original.append(list(val_r)[0])
                    self.pair_original.append(list(val_r)[1])

                else:
                    self.pair_original.append(self.stri_list[i])
                    count_swich = count_swich + 1
            self.stri_list = self.pair_original
            self.pair_original = []
        self.value = "".join(self.stri_list)
        return String(self.value)

        #raise NotImplemented

    def decode_cyclic_bits(self, num: int) -> 'String':
        '''
        Decode the String (self) to its original cyclic bits string.
        :return: a new instance of String with the endecoded string.
        '''
        n=(-1)*num
        return (self.cyclic_bits(n))

        #raise NotImplemented

    def decode_cyclic_chars(self, num: int) -> 'String':
        '''
        Decode the String (self) to its original cyclic chars string.
        :return: a new instance of String with the endecoded string.
        :exception: CyclicCharsDecodeError
        '''
        n = num
        first = []
        last = []
        first = list(self.value)
        for i in range(len(first)):
            if 32>ord(first[i])or ord(first[i])>126:
                raise CyclicCharsDecodeError
            if n>0:
                s_cyc = ord(first[i]) - n
                if (32 <= s_cyc <= 127):
                    last.append(chr(s_cyc))
                elif s_cyc < 32:
                    s_cyc = (127 - (n - (s_cyc + n-32)))
                    last.append(chr(s_cyc))
            else:
                new_n=(-1)*n
                return self.cyclic_chars(new_n)

        last_srt = ''.join([str(elem) for elem in last])
        return String(last_srt)

        #raise NotImplemented
    def create_base_64_dict(self):
        base = '000000'
        base_list = list(base)
        for i in range(64):
            if i != 0 and i % 2 != 0:
                base_list[5] = '1'
            if i != 0 and i % 2 == 0:
                base_list[5] = "0"
                if (i == 4):
                    base_list = ["0", "0", "0", "1", "0", "0", ]
                if (i == 8):
                    base_list = ["0", "0", "1", "0", "0", "0", ]
                if (i == 16):
                    base_list = ["0", "1", "0", "0", "0", "0", ]
                if (i == 32):
                    base_list = ["1", "0", "0", "0", "0", "0", ]
                if (i != 4 and i != 8 and i != 16 and i != 32):
                    if base_list[4] == "0":
                        base_list[4] = "1"
                    elif base_list[4] == "1" and base_list[3] == "1" and base_list[2] == "1" and base_list[0] == "1":
                        base_list[4] = "0"
                        base_list[3] = "0"
                        base_list[2] = "0"
                        base_list[1] = "1"
                    elif base_list[4] == "1" and base_list[3] == "1":
                        base_list[4] = "0"
                        base_list[3] = "0"
                        base_list[2] = "1"
                    elif base_list[4] == "1":
                        base_list[4] = "0"
                        base_list[3] = "1"

            base = "".join(base_list)
            if (i <= 25):
                self.dict_b64[base] = chr(65 + i)
            if (25 < i <= 51):
                self.dict_b64[base] = chr(71 + i)
            if (51 < i <= 61):
                self.dict_b64[base] = str(i - 52)
            if (i == 62):
                self.dict_b64[base] = "+"
            if (i == 63):
                self.dict_b64[base] = "/"
        return self.dict_b64
    def convert_string_into_a_sequence_of_bits(self):

        result = []
        for c in self.value:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([str(b) for b in bits])
            self.bits= ''.join([str(elem) for elem in result])
        return result



    def convert_sequence_of_bits_into_a_string(self):
        chars = []
        for b in range(len(self.stri_list)):
            chars.append(chr(int(self.stri_list[b], 2)))
        chars.pop(-1)
        return ''.join(chars)
    def pair_list_fix(self):
        pair_list_fix = []
        self.dict_pair = {}
        c=0
        for i in range(len(self.stri_list) - 1):
            if c < (len(self.stri_list)) - 2 and self.stri_list[c] == self.stri_list[c + 1] == self.stri_list[c + 2]:
                pair_list_fix.append(self.stri_list[c] + self.stri_list[c])
                c = c + 2
            elif c < (len(self.stri_list))-1:
                pair_list_fix.append(self.stri_list[i] + self.stri_list[i + 1])


        c = [0] * len(pair_list_fix)
        for i in range(len(pair_list_fix)):
            if c[i] == 0:
                self.dict_pair[pair_list_fix[i]] = 1
            for j in range(i + 1, len(pair_list_fix)):
                if pair_list_fix[i] == pair_list_fix[j] and c[i] == 0:
                    self.dict_pair[pair_list_fix[i]] = self.dict_pair[pair_list_fix[i]] + 1
                    c[j] = 1
        self.stri_list = pair_list_fix
        return pair_list_fix

    def create_dict_pair_rules(self):
        for i in range(len(self.rules)):
            self.dict_pair[list(self.rules[i])[0]]=list(self.rules[i])[4]+list(self.rules[i])[5]



class Base64DecodeError(Exception):
    """Exception raised for errors in the input string.
    """


class CyclicCharsError(Exception):
    """Exception raised for errors in the input string.
    """


class CyclicCharsDecodeError(Exception):
    """Exception raised for errors in the input string.
    """


class BytePairError(Exception):
    """Exception raised for errors in the input string.
    """


class BytePairDecodeError(Exception):
    """Exception raised for errors in the input string.
    """

#b = String('#d#ac',['! = aa', '“ = !a', '# = “b'])
#print(b.decode_byte_pair())
#print(b.decode_byte_pair().byte_pair_encoding())
