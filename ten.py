def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # avoiding whitespace characters
        while i < n and s[i] == ' ':
            i += 1

        # check weather the number is positive or negative because we need signed integer
        sign = 1
        if i < n and s[i] in ['-', '+']:
            if s[i] == '-':
                sign = -1
            i += 1

        # first converting digits into an integer
        num = 0
        while i < n and s[i].isdigit():
            # get character to its integer value
            digit = ord(s[i]) - ord('0')

            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            # build a number digit by digit
            num = num * 10 + digit
            i += 1

        # add the sign and retuen
        return sign * num

# time Complexity is O(n) - have to explore each character from the string
# space complexity is O(1) - have fixed numbers of variables

#It is very similar to last problem where I operated on 32 bit charater range. Likewise in this problem I am operating on 32 bit signed integer. The logic is to get each character and convert it into integer, and then using that build a number digit by digit
