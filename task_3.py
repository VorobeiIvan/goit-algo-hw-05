from collections import defaultdict
import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    last = defaultdict(lambda: -1)
    for i in range(m):
        last[pattern[i]] = i
    
    i = m - 1 
    j = m - 1 
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            i += m - min(j, 1 + last[text[i]])
            j = m - 1
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    j = 0
    
    length, i = 0, 1
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
    
    i = 0  
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            j = lps[j - 1] if j > 0 else 0
            i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    d = 256  
    h = pow(d, m - 1) % prime
    p = 0  
    t = 0  
    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime
    return -1


with open("article_1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()
with open("article_2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()


existing_substring = "алгоритм"
non_existing_substring = "фантастика"


for text, name in [(text1, "Article 1"), (text2, "Article 2")]:
    print(f"Testing on {name}")
    for search_func in [boyer_moore, kmp_search, rabin_karp]:
        for substring in [existing_substring, non_existing_substring]:
            time_taken = timeit.timeit(lambda: search_func(text, substring), number=10)
            print(f"{search_func.__name__} ({substring}): {time_taken:.6f} sec")

'''
Висновки щодо продуктивності алгоритмів пошуку підрядка
Після тестування алгоритмів Бойєра-Мура, Кнута-Морріса-Пратта (KMP) та Рабіна-Карпа на двох статтях із пошуком слів "алгоритм" та "фантастика", отримані такі результати:

Бойєр-Мур (Boyer-Moore)

Найшвидший алгоритм серед трьох, особливо при пошуку коротких слів.
Значно випереджає інші методи для слова "алгоритм" (до 10 разів швидший за KMP і Рабіна-Карпа).
Для слова "фантастика" також демонструє хорошу продуктивність, але перевага над іншими методами менш виражена.
Кнут-Морріс-Пратт (KMP)

Відчутно повільніший за Бойєра-Мура, особливо на довших словах.
Час пошуку для "фантастика" майже в 10 разів гірший, ніж для "алгоритм", що може вказувати на чутливість алгоритму до довжини та розташування підрядка.
Проте все ще швидший за Рабіна-Карпа у більшості випадків.
Рабін-Карп (Rabin-Karp)

Найповільніший серед трьох алгоритмів.
Час пошуку сильно залежить від довжини підрядка.
Для коротких слів (наприклад, "алгоритм") продуктивність порівнянна з KMP, але для довших слів ("фантастика") затримка значна.
Загальні висновки
✅ Бойєр-Мур — найкращий вибір для швидкого пошуку в текстах, особливо коли підрядки не надто довгі.
✅ KMP працює стабільно, але не так швидко, як Бойєр-Мур.
❌ Рабін-Карп менш ефективний, особливо для довших підрядків, і може поступатися навіть KMP.

Якщо потрібен універсальний варіант, варто використовувати Бойєра-Мура або KMP залежно від специфіки даних. 🚀

'''