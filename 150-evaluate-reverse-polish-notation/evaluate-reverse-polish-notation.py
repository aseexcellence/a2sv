class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _stack = []
        
        for tk in tokens:
            if tk in "/+*-":
                op2 = _stack.pop()
                op1 = _stack.pop()
                exp = f"{op1}{tk}{op2}"
                _stack.append(int(eval(exp)))
            else:
                _stack.append(int(tk))
        
        return _stack[0]