def explode_text(text: str, target: str) -> str:
    stack_text: list[int] = []
    stack_target: list[int] = [ord(c) for c in target]
    target_len = len(target)

    for char in text:
        stack_text.append(ord(char))  # Into ascii integer
        if len(stack_text) < target_len:
            continue
        tail = stack_text[-target_len:]
        if tail == stack_target:
            for _ in range(target_len):
                stack_text.pop()

    return "".join(chr(i) for i in stack_text)  # From ascii integer


def main():
    text = input()
    target = input()
    result = explode_text(text, target)
    print(result if result else "FRULA")


main()
