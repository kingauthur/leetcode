class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sLen = len(s)
        # for i in range(sLen,0,-1):
        #     for j in range(0,sLen):
        #         if i + j - 1 > sLen - 1:
        #             break
        #         else:
        #             head = j
        #             tail = i + j - 1
        #             isPalindromic = True
        #             while head <= tail:
        #                 if s[head] != s[tail]:
        #                     isPalindromic = False
        #                     break
        #                 head += 1
        #                 tail -= 1
        #             if isPalindromic:
        #                 return s[j:i+j]
        longest = ""
        for i in range(0,len(s)):
            s1 = self.getLongestPalindrome(s,i-1,i+1)
            if len(s1) > len(longest):
                longest = s1

            if i < len(s) - 1 and s[i] == s[i+1]:
                s2 = self.getLongestPalindrome(s,i-1,i+2)
                if len(s2) > len(longest):
                    longest = s2

        return longest

    def getLongestPalindrome(self,s,left,right):
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left+1:right]


solution = Solution()
print(solution.longestPalindrome("kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd"))
