import re

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value
        self.left = left
        self.right = right

def create_rule(rule_string):
    tokens = re.split(r'(\s+|AND|OR)', rule_string)
    tokens = [token.strip() for token in tokens if token.strip()]

    def parse(tokens):
        stack = []
        for token in tokens:
            if token in ('AND', 'OR'):
                if len(stack) < 2:
                    print(f"Error: Not enough operands for operator '{token}'")
                    return None  # Not enough operands
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(type='operator', value=token, left=left, right=right))
            else:
                match = re.match(r'(\w+)\s*(==|!=|>=|<=|>|<)\s*(\d+)', token)
                if match:
                    left_operand = match.group(1)
                    operator = match.group(2)
                    right_operand = match.group(3)
                    stack.append(Node(type='operand', value=f"{left_operand} {operator} {right_operand}"))
                else:
                    print(f"Invalid condition: {token}")
        return stack[0] if stack else None

    return parse(tokens)


def combine_rules(rules, combine_operator='AND'):
    if not rules:
        return None  # Return None if there are no rules

    combined_root = create_rule(rules[0])
    
    for rule_string in rules[1:]:
        new_root = create_rule(rule_string)
        
        if not new_root:
            print(f"Invalid rule: {rule_string}")
            continue  # Skip invalid rules
        
        combined_root = Node(type='operator', value=combine_operator, left=combined_root, right=new_root)
    
    return combined_root

def evaluate_rule(root, json_data):
    if root is None:
        return False
    
    if root.type == 'operand':
        try:
            left_operand, operator, right_operand = root.value.split()
            left_value = json_data.get(left_operand)
            right_value = int(right_operand) if right_operand.isdigit() else json_data.get(right_operand)

            if operator == '>':
                return left_value > right_value
            elif operator == '<':
                return left_value < right_value
            elif operator == '>=':
                return left_value >= right_value
            elif operator == '<=':
                return left_value <= right_value
            elif operator == '==':
                return left_value == right_value
            elif operator == '!=':
                return left_value != right_value
        except ValueError:
            print(f"Invalid operand format: {root.value}")
            return False

    elif root.type == 'operator':
        left_result = evaluate_rule(root.left, json_data)
        right_result = evaluate_rule(root.right, json_data)

        if root.value == 'AND':
            return left_result and right_result
        elif root.value == 'OR':
            return left_result or right_result

    return False
