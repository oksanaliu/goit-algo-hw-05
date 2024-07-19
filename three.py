import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = {}

    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0

    compute_lps_array(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Спроба завантажити файли з різними кодуваннями
def read_file_with_encoding(path, encoding):
    try:
        with open(path, 'r', encoding=encoding) as f:
            return f.read()
    except UnicodeDecodeError:
        return None

# Шляхи до файлів
path1 = '/Users/oksanaluklan/goit-algo-hw-05/стаття 1.txt'
path2 = '/Users/oksanaluklan/goit-algo-hw-05/стаття 2.txt'

encodings = ['utf-8', 'cp1251', 'latin1']

text1, text2 = None, None

for encoding in encodings:
    if text1 is None:
        text1 = read_file_with_encoding(path1, encoding)
    if text2 is None:
        text2 = read_file_with_encoding(path2, encoding)

if text1 is None or text2 is None:
    raise ValueError("Не вдалося завантажити файли з підтримуваними кодуваннями")

# Вибір підрядків
existing_substring = "підрядок"  # Підрядок, який існує в обох текстах
non_existing_substring = "немає"  # Підрядок, якого немає в обох текстах

# Вимірювання часу виконання для статті 1
time_boyer_moore_text1_existing = timeit.timeit(lambda: boyer_moore(text1, existing_substring), number=100)
time_boyer_moore_text1_non_existing = timeit.timeit(lambda: boyer_moore(text1, non_existing_substring), number=100)

time_kmp_text1_existing = timeit.timeit(lambda: kmp_search(text1, existing_substring), number=100)
time_kmp_text1_non_existing = timeit.timeit(lambda: kmp_search(text1, non_existing_substring), number=100)

time_rabin_karp_text1_existing = timeit.timeit(lambda: rabin_karp(text1, existing_substring), number=100)
time_rabin_karp_text1_non_existing = timeit.timeit(lambda: rabin_karp(text1, non_existing_substring), number=100)

# Вимірювання часу виконання для статті 2
time_boyer_moore_text2_existing = timeit.timeit(lambda: boyer_moore(text2, existing_substring), number=100)
time_boyer_moore_text2_non_existing = timeit.timeit(lambda: boyer_moore(text2, non_existing_substring), number=100)

time_kmp_text2_existing = timeit.timeit(lambda: kmp_search(text2, existing_substring), number=100)
time_kmp_text2_non_existing = timeit.timeit(lambda: kmp_search(text2, non_existing_substring), number=100)

time_rabin_karp_text2_existing = timeit.timeit(lambda: rabin_karp(text2, existing_substring), number=100)
time_rabin_karp_text2_non_existing = timeit.timeit(lambda: rabin_karp(text2, non_existing_substring), number=100)

# Результати
print(f"Article 1 - Existing Substring:")
print(f"Boyer-Moore: {time_boyer_moore_text1_existing} seconds")
print(f"KMP: {time_kmp_text1_existing} seconds")
print(f"Rabin-Karp: {time_rabin_karp_text1_existing} seconds")

print(f"\nArticle 1 - Non-existing Substring:")
print(f"Boyer-Moore: {time_boyer_moore_text1_non_existing} seconds")
print(f"KMP: {time_kmp_text1_non_existing} seconds")
print(f"Rabin-Karp: {time_rabin_karp_text1_non_existing} seconds")

print(f"\nArticle 2 - Existing Substring:")
print(f"Boyer-Moore: {time_boyer_moore_text2_existing} seconds")
print(f"KMP: {time_kmp_text2_existing} seconds")
print(f"Rabin-Karp: {time_rabin_karp_text2_existing} seconds")

print(f"\nArticle 2 - Non-existing Substring:")
print(f"Boyer-Moore: {time_boyer_moore_text2_non_existing} seconds")
print(f"KMP: {time_kmp_text2_non_existing} seconds")
print(f"Rabin-Karp: {time_rabin_karp_text2_non_existing} seconds")