from wordle import Wordle
import time
import concurrent.futures

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
wordle = Wordle()
letters = []

def solve_letter(p: int) -> dict:

    def create_word(position: int, letter: int) -> str:
        w = []
        for i in range(0,5):
            if i == position:
                w.append(letter)
            else:
                w.append('x')
        return ''.join(w)
    
    for l in alphabet:
        guess = create_word(p, l)
        result = list(wordle.guess(guess))
        r = []
        for item in result: # handles weird blank charcters in split
            if item == ' ': continue
            else: r.append(item)

        if r[p] == "🟩": 
            return {p: l}
        else:
            continue
    
def order_word(stuff: list)-> str:
    w = []
    for i in range(0,5):
        for item in stuff:
            if i in item:
                w.append(item[i])
                break
        continue
    return ''.join(w)

# Solve letter by letter
start = time.time()
for i in range(0,5):
    letters.append(solve_letter(i))
solution = order_word(letters)
t = round((time.time() - start),5)
print(f"Solution is: {solution}")
print(f"Iterative time taken: {t}")

# Solve letter by letter but all letters concurrently
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(solve_letter, i) for i in range(0,5)]
    concurrent.futures.wait(futures)
solution = order_word([future.result() for future in futures])
t = round((time.time() - start),5)
print(f"Parallel time taken: {t}")