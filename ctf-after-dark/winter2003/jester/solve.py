import requests
import re
import math


def solve_quadratic_equation(a, b, c):
    d = (b**2) - (4*a*c)

    if d < 0:
        print("The roots are complex")
    else:
        root1 = (-b - math.sqrt(d)) / (2*a)
        root2 = (-b + math.sqrt(d)) / (2*a)

        return (round(root1), round(root2))


addition_regex = r"What is (\d* [+\-*\/] \d*) \?"
quadratic_regex = r"What are the roots of (\d*) x\^2 \+ (\d*) x \+ (\d*) \?"
flag_regex = r"flag{.*}"
url = "https://jester.acmcyber.com/"

s = requests.Session()

r = s.get(url)

matches = re.findall(addition_regex, r.text)
eval_match = eval(matches[0])

r = s.post(url+"/validate", data={"answer": eval_match}, headers={
    "Content-Type": "application/x-www-form-urlencoded"})

if "Sorry" in r.text:
    print("Timing is off")
    exit(-1)

quadratic_matches = re.findall(quadratic_regex, r.text)
quadratic_solve = solve_quadratic_equation(int(quadratic_matches[0][0]), int(
    quadratic_matches[0][1]), int(quadratic_matches[0][2]))

data = {
    "answer1": str(quadratic_solve[0]),
    "answer2": str(quadratic_solve[1])
}

r = s.post(
    url+"/validate",
    data=data,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

flag = re.findall(flag_regex, r.text)
print(flag[0])
