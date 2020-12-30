brackets = '{}[}{]}{]'
# brackets = '[][][]{}'
stack = []
match = []
index_stack = []
bracket_match = {'[': ']', '{': '}'}
bracket_match_right = {']': '[', '}': '{'}
index = 0
for bracket in brackets:
    if not stack:
        stack.append(bracket)
        index_stack.append(index)
        match.append(0)
    elif stack[-1] in bracket_match and bracket_match[stack[-1]] == bracket:
        match.pop()
        match.append(stack.pop())
        index_stack.pop()
        match.append(bracket)
    else:
        stack.append(bracket)
        index_stack.append(index)
        match.append(0)
    index += 1
if not stack:
    print(''.join(match))
else:
    left = 0
    right = len(stack) - 1
    while left <= right:
        if stack[left] in bracket_match and bracket_match[stack[left]] == stack[right]:
            match[index_stack[left]] = stack[left]
            match[index_stack[right]] = stack[right]
            left += 1
            right -= 1
        elif stack[left] in bracket_match_right:
            if stack[left] == ']':
                match[index_stack[left]] = '1'
            else:
                match[index_stack[left]] = '2'
            left += 1
        elif stack[right] in bracket_match:
            if stack[right] == '[':
                match[index_stack[right]] = '1'
            else:
                match[index_stack[right]] = '2'
            right -= 1
        elif stack[left] in bracket_match and bracket_match[stack[left]] != stack[right]:
            if stack[left] == '[':
                match[index_stack[left]] = '1'
            else:
                match[index_stack[left]] = '2'
            left += 1
        if left == right:
            if stack[left] == '[' or stack[left] == ']':
                match[index_stack[left]] = '1'
            else:
                match[index_stack[left]] = '2'
    print(''.join(match).replace('2', '{}').replace('1', '[]'))
