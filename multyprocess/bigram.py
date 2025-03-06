import os
from multiprocessing import Pool
from collections import defaultdict

file_list = [
    "Асинхронне програмування.md",
    "Багатопотоковість у пайтон.md",
    "Багатопроцесність та паралелізм.md",
    "Паралельні_обчислення_і_функціональне_програмування.md"
    ]


# ---------------------- 2. Читання файлів ----------------------
def read_file(filename):
    """Зчитує вміст текстового файлу."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().lower()  # Приводимо текст до нижнього регістру

# ---------------------- 3. Фаза Map: Розбиття тексту на біграми ----------------------
def map_function(text):
    """Розбиває текст на біграми (пари слів)."""
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    return [(bigram, 1) for bigram in bigrams]

# ---------------------- 4. Фаза Shuffle: Групування біграм ----------------------
def shuffle(mapped_data):
    """Групує біграми, щоб об’єднати однакові ключі."""
    grouped_data = defaultdict(list)
    for key, value in mapped_data:
        grouped_data[key].append(value)
    return grouped_data

# ---------------------- 5. Фаза Reduce: Підрахунок частот ----------------------
def reduce_function(key_values):
    """Обчислює суму частот для кожної біграми."""
    key, values = key_values
    return (key, sum(values))

# ---------------------- 6. Функція прогнозування наступного слова ----------------------
def predict_next_word(word, model):
    """Прогнозує наступне слово на основі частотного аналізу біграм."""
    candidates = {key[1]: count for key, count in model.items() if key[0] == word}
    if not candidates:
        return None
    return max(candidates, key=candidates.get)  # Найбільш вживане слово

# ---------------------- Головна функція ----------------------
if __name__ == "__main__":
    with Pool() as pool:
        texts = pool.map(read_file, file_list)  # Паралельне читання файлів
        mapped_results = pool.map(map_function, texts)  # Паралельна обробка тексту

    # Об’єднуємо всі біграми з різних процесів в один список
    flat_mapped = [pair for sublist in mapped_results for pair in sublist]

    # Фаза Shuffle: групуємо біграми
    shuffled = shuffle(flat_mapped)

    # Фаза Reduce: обчислюємо частоти біграм паралельно
    with Pool() as pool:
        reduced_results = pool.map(reduce_function, shuffled.items())

    # Перетворюємо список у словник
    final_model = dict(reduced_results)

    # ---------------------- CLI для користувача ----------------------
    print("📖 Simple CLI Chatbot using MapReduce")
    print("Type a word and get the most probable next word (type 'exit' to quit).")

    while True:
        user_input = input("\nEnter a word: ").strip().lower()
        if user_input == "exit":
            print("Goodbye! 👋")
            break

        prediction = predict_next_word(user_input, final_model)
        if prediction:
            print(f"🤖 Predicted next word: {prediction}")
        else:
            print("❌ No prediction available for this word.")