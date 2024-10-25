

def are_anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print('anagram')
    else:
        print('not')
are_anagram("listen","silent")


def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
