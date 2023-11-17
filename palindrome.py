def palindrome(str: str, i) -> bool:
    local_str = str if i == 0 else str[i:-i]
    if len(local_str) == 0 or len(local_str) == 1:
        return True
    if str[i] == str[-(i + 1)] or i == 0 and str[i] == str[-1]:
        return palindrome(str, i+1)
    else:
        return False


cases = ["racecar", "radar", "google"]
truth = [True, True, False]
for (i, case) in enumerate(cases):
    if palindrome(case, 0) != truth[i]:
        print("Error")
    else:
        print("Pass")
