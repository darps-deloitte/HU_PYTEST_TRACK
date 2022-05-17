from itertools import combinations

import pytest


class TestStringClass:

    def __init__(self, str):
        self.str = str

    def test_LengthofString(self):
        return len(self.str)

    def test_ConvertToList(self):
        strlist = []
        strlist[:0] = self.str
        return strlist


class TestPairsPossible(TestStringClass):

    def test_PossiblePairsList(self):
        strlist = TestStringClass.test_ConvertToList(self)
        pairList = list(combinations(strlist, 2))
        return pairList


class TestSearchCommonElements(TestPairsPossible):

    def __init__(self, a, b):
        self.StringClass_str = a
        self.PossiblePairs_str = b
        self.common_list = list()

    def test_CommonElements(self):
        dict = {}
        for ele in self.StringClass_str:
            if ele in self.PossiblePairs_str:
                if ele in dict:
                    continue
                else:
                    dict[ele] = 1

        for key in dict:
            self.common_list.append(key)

        return self.common_list


class TestEqualSumPairs(TestSearchCommonElements):

    def __init__(self, str):
        self.str = str

    def test_CountPairs(self, lis):
        dict1 = {}

        for pair in lis:
            pairs_list = list(pair)
            sum = 0
            for num in pairs_list:
                sum = sum + int(num)

            if sum in dict1:
                dict1[sum] = dict1[sum] + 1
            else:
                dict1[sum] = 1

        for key in dict1:
            if dict1[key] == 1:
                print(key, end=" ")


def test_StringClass():
    obj = TestStringClass("12314532")
    print(obj.test_LengthofString())
    print(obj.test_ConvertToList())


def test_PairPossible():
    obj = TestPairsPossible("1357357")
    print(obj.test_PossiblePairsList())


def test_SearchCommonElements():
    obj = TestStringClass("12314532")
    obj2 = TestPairsPossible("1357357")
    obj3 = TestSearchCommonElements(obj.str, obj2.str)
    print(obj3.test_CommonElements())


def test_EqualSumPairs():
    obj1 = TestPairsPossible("1357357")
    lis = obj1.test_PossiblePairsList()
    obj2 = TestEqualSumPairs("12314532")
    obj2.test_CountPairs(lis)
