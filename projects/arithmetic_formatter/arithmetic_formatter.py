def arithmetic_arranger(problems, show_answers=False):
  top = ''
  bottom = ''
  all_ds = ''
  ans = ''

  if len(problems) > 5:
    return "Error: Too many problems."
  p_count = 0
  for p in problems:
    p_count += 1
    split_problem = p.split()
    if not split_problem[0].isnumeric() or not split_problem[2].isnumeric():
      return "Error: Numbers must only contain digits."
    if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    if not (split_problem[1] == "+" or split_problem[1] == "-"):
      return "Error: Operator must be '+' or '-'."

    left_num = split_problem[0]
    right_num = split_problem[2]
    operator = split_problem[1]
    problem_answer = int(left_num) + int(right_num)
    if operator == "-":
      problem_answer = int(left_num) - int(right_num)

    mx_num = max(len(left_num), len(right_num))
    dashes = ""
    c = 0
    while c < mx_num + 2:
      dashes += "-"
      c = c + 1

    alNum = len(dashes)
    opr = alNum - len(right_num)
    b_op = f"{operator:<{opr}}{right_num}"

    sepr = '\n' if p_count == len(problems) else "    "
    ans_sepr = '' if p_count == len(problems) else "    "
    d_sepr = ''
    if p_count == len(problems):
      if show_answers:
        d_sepr = '\n'
    else:
      d_sepr = "    "

    top += f"{left_num:>{alNum}}{sepr}"
    bottom += f"{b_op:>{alNum}}{sepr}"
    all_ds += f"{dashes}{d_sepr}"
    ans += f"{problem_answer:>{alNum}}{ans_sepr}"

    ans = "" if not show_answers else ans

  return f"{top}{bottom}{all_ds}{ans}"

  
print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))