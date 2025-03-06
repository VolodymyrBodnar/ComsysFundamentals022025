import os
import wikipediaapi
from multiprocessing import Pool
from collections import defaultdict
import re

# ---------------------- 1. Завантаження статей з Вікіпедії ----------------------
wiki = wikipediaapi.Wikipedia(
    language="uk",
    user_agent="MyWikipediaBot/1.0 (contact: myemail@example.com)"
)

articles = [
    "Математика",
    "Комп'ютерні науки",
    "Обчислювальна техніка",
    "Штучний інтелект",
    "Богдан Хмельницький",
    "Україна"
]

def fetch_wikipedia_article(title):
    """Отримує текст статті з Вікіпедії"""
    page = wiki.page(title)
    if not page.exists():
        return ""
    text = page.text
    text = re.sub(r'\n+', ' ', text)  # Видаляємо зайві переноси рядків
    text = re.sub(r'[^а-яА-ЯіІїЇєЄґҐa-zA-Z0-9\s]', '', text)  # Видаляємо знаки пунктуації
    return text.lower()

def create_corpus_from_wikipedia():
    """Завантажує статті та створює текстовий корпус"""
    with Pool() as pool:
        texts = pool.map(fetch_wikipedia_article, articles)
    
    corpus_text = " ".join(texts).strip()

    if not corpus_text:
        print("⚠️ ПОМИЛКА: Отримано порожній корпус! Переконайтеся, що статті існують.")
        return False

    with open("corpus.txt", "w", encoding="utf-8") as f:
        f.write(corpus_text)
    
    print(f"✅ Корпус успішно створено! Довжина: {len(corpus_text)} символів.")
    return True

# ---------------------- 2. Читання корпусу ----------------------
def read_corpus():
    """Читає текстовий корпус"""
    if not os.path.exists("corpus.txt"):
        print("⚠️ ПОМИЛКА: Файл corpus.txt не знайдено!")
        return ""
    
    with open("corpus.txt", "r", encoding="utf-8") as f:
        return f.read().strip()

# ---------------------- 3. Фаза Map: Генерація n-грам ----------------------
def generate_ngrams(text, n=2):
    """Генерує n-граму (за замовчуванням біграми)"""
    words = text.split()
    if len(words) < n:
        return []
    ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
    return [(ngram, 1) for ngram in ngrams]

def generate_ngrams_wrapper(args):
    """Обгортка для multiprocessing"""
    text, n = args
    return generate_ngrams(text, n)

# ---------------------- 4. Фаза Shuffle: Групування n-грам ----------------------
def shuffle(mapped_data):
    """Групує n-граму за ключем"""
    grouped_data = defaultdict(list)
    for key, value in mapped_data:
        grouped_data[key].append(value)
    return grouped_data

# ---------------------- 5. Фаза Reduce: Підрахунок частот n-грам ----------------------
def reduce_function(key_values):
    """Обчислює суму частот для кожної n-грами"""
    key, values = key_values
    return (key, sum(values))

# ---------------------- 6. Прогнозування наступного слова ----------------------
def predict_next_word(context, model, n):
    """Прогнозує наступне слово на основі n-грам"""
    words = context.split()
    if len(words) < n - 1:
        print("❌ Введено занадто мало слів для прогнозу!")
        return None

    context_tuple = tuple(words[-(n - 1):])  # Беремо останні n-1 слів
    candidates = {key[-1]: count for key, count in model.items() if key[:-1] == context_tuple}

    if not candidates:
        print(f"❌ Немає прогнозу для контексту: {context_tuple}")
        return None

    return max(candidates, key=candidates.get)  # Найімовірніше слово

# ---------------------- 7. Головна функція ----------------------
if __name__ == "__main__":
    print("📥 Завантаження статей з Вікіпедії...")
    if not create_corpus_from_wikipedia():
        exit(1)

    print("📖 Читання корпусу...")
    text = read_corpus()
    if not text:
        print("⚠️ ПОМИЛКА: Корпус порожній! Завантаження не вдалося.")
        exit(1)

    n = int(input("🔢 Введіть значення n для n-грам (наприклад, 2 для біграм, 3 для триграм): ").strip())

    print("🔨 Обробка тексту...")
    with Pool() as pool:
        mapped_results = pool.map(generate_ngrams_wrapper, [(text, n)])

    flat_mapped = [pair for sublist in mapped_results for pair in sublist]

    if not flat_mapped:
        print("⚠️ ПОМИЛКА: Не знайдено жодної n-грамної пари. Можливо, текст занадто короткий?")
        exit(1)

    print("🔄 Групування n-грам...")
    shuffled = shuffle(flat_mapped)

    print("🧮 Підрахунок частот n-грам...")
    with Pool() as pool:
        reduced_results = pool.map(reduce_function, shuffled.items())

    final_model = dict(reduced_results)

    if not final_model:
        print("⚠️ ПОМИЛКА: Модель порожня! Не вдалося створити n-грамну статистику.")
        exit(1)

    # ---------------------- CLI ----------------------
    print("\n🤖 Simple CLI Chatbot using n-gram Model")
    print("Введіть кілька слів, і бот спрогнозує наступне слово (напишіть 'exit' для виходу).")

    while True:
        user_input = input("\nВведіть слова: ").strip().lower()
        if user_input == "exit":
            print("До побачення! 👋")
            break

        prediction = predict_next_word(user_input, final_model, n)
        if prediction:
            print(f"🤖 Прогнозоване слово: {prediction}")
        else:
            print("❌ Немає прогнозу для цього контексту.")