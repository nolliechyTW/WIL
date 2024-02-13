class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:  # Potential IPv4
            return self.validateIPv4(queryIP)
        elif queryIP.count(':') == 7:  # Potential IPv6
            return self.validateIPv6(queryIP)
        else:
            return 'Neither'

    def validateIPv4(self, IP: str) -> str:
        parts = IP.split('.')
        for part in parts:
            # isdigit() method returns True if all the characters are digits
            if not part.isdigit() or not 0 <= int(part) <= 255 or \
               (part[0] == '0' and len(part) > 1) or len(part) == 0:
                return 'Neither'
        return 'IPv4'

    def validateIPv6(self, IP: str) -> str:
        parts = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for part in parts:
            # all() function returns True if all items in an iterable are true
            if not 1 <= len(part) <= 4 or not all(c in hexdigits for c in part):
                return 'Neither'
        return 'IPv6'
