def parse(s):
    if not type(s) is str:
        return None
    if len(s) < 1:
        return None
    if(('.' in s) and (('E' in s) or ('e' in s))):
        expression1 = '0'
        expression1,expression2 = s.split(".")
        if not expression1:
            expression1 = '0'
        if('0'<=expression1<='9'):
         t = 1
         if('E' in expression2):
            for s in expression2:
                if(s == 'E' and t == 1):
                    t=t+1
                    return None
                else:
                    t=t+1
                    x,y = expression2.split('E')
                    y = int(y)
                    y=y-len(x)
                    break
         elif('e' in expression2):
            for s in expression2:
                if(s == 'e' and t == 1):
                    t=t+1
                    return None
                else:
                    t=t+1
                    x,y = expression2.split('e')
                    y = int(y)
                    y=y-len(x)
                    break
         
         else:
             return None

         result = (expression1+x+'*10**'+str(y))
         return result
        else:
            return None
    if '+' in s:
        s_list = s.split("+")
        n_list = [parse(s) for s in s_list]
        if None in n_list:
            return None
        return sum(n_list)
    if s[0] == '-':
        return(-parse(s[1:]))
    n = 0
    dec = False
    divisor = 1.0
    if s == '.':
        return None
    for c in s:
        if c == '.':
            if dec:
                return None
            dec = True
        elif not dec:
            if not ('0' <= c <= '9'):
                return None
            n = n * 10
            n = n + ord(c) - ord('0')
        else:
            divisor = divisor / 10.0
            v = ord(c) - ord('0')
            n = n + v * divisor
    return n
