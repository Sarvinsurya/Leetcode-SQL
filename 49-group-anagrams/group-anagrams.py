class Solution(object):
    def groupAnagrams(self, strs):
        str_dict={}
        for string in strs:
            sorted_String="".join(sorted(string))
            if sorted_String not in str_dict:
                str_dict[sorted_String]=[]
            str_dict[sorted_String].append(string)
        return list(str_dict.values())
        