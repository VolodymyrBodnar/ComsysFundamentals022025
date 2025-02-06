- Розглянемо **основні поняття формалізації** та як вони пов'язані зі створенням компіляторів, а також процес створення формальних описів для мов програмування.
- Ознайомимося із ключовим інструментом для визначення синтаксису мов програмування — **формальними граматиками**.
- Дізнаємося про **нотацію**, яка допомагає описати синтаксис мов програмування.
- Розглянемо **основні функції та різновиди компіляторів**, дізнаємося, що таке **абстрактне синтаксичне дерево** (AST) та як воно використовується в компіляторах.
- Дослідимо **етапи процесу компіляції**.
- Створимо **інтерпретатор**: розглянемо лексичний та синтаксичний аналіз, а також реалізацію основних компонентів.
- Познайомимось з  **модулем `ast` мови програмування Python** та його використання для роботи з абстрактним синтаксичним деревом.



[Формальна граматика](https://uk.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D0%B3%D1%80%D0%B0%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8) є математичним механізмом для опису синтаксичних структур мови. Вона використовується для визначення того, які рядки є частиною мови і які структури можна утворити в рамках цієї мови. Формальні граматики є основним компонентом теорії формальних мов і широко використовуються в компіляторах та теорії обчислень.

**Термінальні символи** являють собою символи алфавіту $Т$, тоді як **нетермінальні символи** формують множину $N$ і використовуються на проміжних етапах породжувального процесу. **Початковий символ** _$\Sigma$_ — це нетермінальний символ, з якого виводяться всі рядки мови.



#### **Опис синтаксису мови та підходи до його формалізації**

Синтаксис мови програмування визначає допустимі конструкції та правила побудови виразів у цій мові. Опис синтаксису може бути складним через можливу нескінченну кількість допустимих речень. Існує два основних підходи до формалізації мови:

1. **Породжувальний опис мови** – заснований на алгоритмі, який може генерувати всі можливі коректні рядки певної мови. Якщо рядок допустимий у цій мові, алгоритм рано чи пізно його згенерує. Цей підхід використовується у визначенні формальних граматик.
    
2. **Аналітичний опис мови** – базується на алгоритмі, який отримує на вхід рядок і визначає, чи є він коректним. Такий підхід використовується при реалізації аналізаторів мови та компіляторів.
    

#### **Формальна граматика**

Формальна граматика є математичним механізмом для точного опису синтаксичних структур мови. Вона визначає набір правил, які встановлюють, які рядки належать мові.

Компоненти формальної граматики:

- **Термінальні символи (алфавіт T)** – кінцевий набір символів, що безпосередньо входять до складу коректних виразів мови.
- **Нетермінальні символи (множина N)** – допоміжні символи, які використовуються для побудови структур мови.
- **Початковий символ Σ** – спеціальний нетермінальний символ, із якого починається породження виразів мови.
- **Правила переписування** – визначають, як один набір символів може бути замінений іншим.

Формальні граматики використовуються для опису синтаксису мов програмування і є основним інструментом у розробці компіляторів.
### **Переписування у формальних граматиках**

Правила переписування визначають, як змінювати одну послідовність символів на іншу відповідно до граматики мови. Вони є основним механізмом породження синтаксичних конструкцій і використовуються під час аналізу та компіляції.

#### **Формальне визначення**

Кожне правило має вигляд:

```
A → α
```

де:

- `A` – **нетермінальний символ**, що підлягає заміні (наприклад, `<вираз>`).
- `α` – **послідовність термінальних і/або нетермінальних символів**, якою `A` може бути замінене.

Правила переписування застосовуються поетапно, поки всі нетермінальні символи не будуть замінені на термінальні, що утворює коректний рядок мови.

#### **Приклад правил переписування**

Розглянемо граматику арифметичних виразів:

1. **Основна структура виразів:**
    
    ```
    <вираз> → <терм> + <вираз> | <терм>
    ```
    
    Це означає, що вираз може складатися з терма, після якого йде `+` і ще один вираз, або бути просто термом.
    
2. **Терми:**
    
    ```
    <терм> → <фактор> * <терм> | <фактор>
    ```
    
    Терм може бути множенням фактора на терм або просто фактором.
    
3. **Фактори:**
    
    ```
    <фактор> → ( <вираз> ) | <число>
    ```
    
    Фактором може бути вираз у дужках або просто число.
    
4. **Числа (термінали):**
    
    ```
    <число> → 0 | 1 | 2 | ...
    ```
    
    `<число>` може бути будь-якою цифрою.
    

#### **Процес породження рядка мови**

Якщо ми хочемо отримати вираз `3 + 4 * 5`, то застосування правил виглядає так:

1. Початковий нетермінал:
    
    ```
    <вираз>
    ```
    
2. Використовуємо правило для `<вираз>`:
    
    ```
    <терм> + <вираз>
    ```
    
3. Замінюємо `<вираз>` на `<терм>`:
    
    ```
    <терм> + <терм>
    ```
    
4. Замінюємо `<терм>` (перший на `<фактор>`, другий за правилом множення):
    
    ```
    <фактор> + <фактор> * <терм>
    ```
    
5. Замінюємо `<фактор>` на числа:
    
    ```
    3 + 4 * 5
    ```
    

Тепер вираз містить лише термінальні символи, що означає його допустимість у мові.

#### **Контекстно-вільні граматики та правила переписування**

Правила переписування можуть бути **контекстно-вільними** (CFG, Context-Free Grammar), коли вони мають вигляд `A → α`, де `A` – один нетермінал, а `α` – довільна послідовність символів. У компіляторах саме контекстно-вільні граматики використовуються для опису синтаксису мов програмування.


Правила переписування визначають, як утворюються або аналізуються конструкції мови. Вони є основою породжувальних граматик, синтаксичних аналізаторів та роботи компіляторів.

### **Приклад для української мови**

Уявімо, що існує набір правил, які дозволяють правильно будувати речення українською мовою. Вони визначають, як можна замінювати одні слова або групи слів на інші, зберігаючи правильну структуру.

Розглянемо процес побудови простого речення за такими правилами:

1. **Речення → Підмет + Присудок**
    
    ```
    <Речення> → <Підмет> + <Присудок>
    ```
    
2. **Підмет → Іменник**
    
    ```
    <Підмет> → хлопчик
    ```
    
3. **Присудок → Дієслово + Доповнення**
    
    ```
    <Присудок> → <Дієслово> + <Доповнення>
    ```
    
4. **Дієслово → їсть**
    
    ```
    <Дієслово> → їсть
    ```
    
5. **Доповнення → Іменник**
    
    ```
    <Доповнення> → яблуко
    ```
    

Тепер, використовуючи ці правила, будуємо речення:

6. Початковий нетермінал:
    
    ```
    <Речення>
    ```
    
7. Застосовуємо перше правило:
    
    ```
    <Підмет> + <Присудок>
    ```
    
8. Замінюємо `<Підмет>`:
    
    ```
    хлопчик + <Присудок>
    ```
    
9. Замінюємо `<Присудок>`:
    
    ```
    хлопчик + <Дієслово> + <Доповнення>
    ```
    
10. Замінюємо `<Дієслово>`:
    
    ```
    хлопчик + їсть + <Доповнення>
    ```
    
11. Замінюємо `<Доповнення>`:
    
    ```
    хлопчик їсть яблуко
    ```
    

Отже, ми отримали правильне речення: **"Хлопчик їсть яблуко"**.

#### **Як це працює в компіляторах?**

Аналогічно, компілятори використовують правила переписування для перетворення вихідного коду у правильну форму. Наприклад, код:

```python
x = 5 + 3
```

можна побудувати за такими правилами:

12. **Присвоєння** → **Змінна = Вираз**
13. **Вираз** → **Число + Число**
14. **Число** → **5**
15. **Число** → **3**

У результаті компілятор правильно розпізнає код і перетворює його у виконувану форму.


#### **Нотації для опису синтаксису мов програмування**

Для зручного представлення синтаксичних структур використовуються спеціальні нотації, серед яких:

- **BNF (Backus-Naur Form)** – використовується для строгого математичного опису граматик мов програмування. Вона задає правила у вигляді: <вираз>::=<термінал>∣<нетермінал><оператор><вираз><вираз> ::= <термінал> | <нетермінал> <оператор> <вираз>
- **EBNF (Extended BNF)** – розширена форма BNF, що включає додаткові оператори, такі як `*` (повторення) та `[]` (необов’язкові елементи).

#### **Основні функції та різновиди компіляторів**

Компілятор – це програма, що перетворює вихідний код із однієї мови програмування в іншу (зазвичай у машинний код або проміжний код).

Основні етапи роботи компілятора:

16. **Лексичний аналіз** – розбиває текст програми на окремі лексеми (токени).
17. **Синтаксичний аналіз** – перевіряє відповідність послідовності токенів правилам граматики.
18. **Семантичний аналіз** – перевіряє коректність використання конструкцій мови.
19. **Генерація проміжного коду** – створює представлення коду у формі, що зручна для оптимізації.
20. **Оптимізація коду** – покращує швидкодію та зменшує використання ресурсів.
21. **Генерація кінцевого коду** – створює машинний код або байт-код для виконання.

Різновиди компіляторів:

- **Однопрохідні** – обробляють код за один прохід.
- **Багатопрохідні** – проходять код декілька разів для кращої оптимізації.
- **JIT-компілятори** – компілюють код у момент виконання.
- **Транспілери** – перетворюють код однієї мови програмування в код іншої мови.

#### **Абстрактне синтаксичне дерево (AST)**

AST (Abstract Syntax Tree) – це структура, яка представляє синтаксичну організацію програми у вигляді дерева, де кожен вузол відповідає конструкції мови.

Основні особливості AST:

- AST не містить непотрібних деталей, таких як коментарі або зайві дужки.
- Кожен вузол дерева представляє окремий елемент синтаксису.
- Використовується для подальшої трансформації та оптимізації коду.

AST є ключовим компонентом компіляторів та інтерпретаторів, оскільки дозволяє зручно обробляти код на більш високому рівні абстракції.
![[Pasted image 20250206184139.png]]
#### **Етапи процесу компіляції**

 **Аналіз вихідного коду**:
    - Лексичний аналіз: розбиття на токени.
    - Синтаксичний аналіз: побудова AST.
    - Семантичний аналіз: перевірка типів та логічної коректності.
    - 
**Трансформація коду**:
    - Оптимізація проміжного представлення.
    - Конвертація у внутрішнє представлення.
**Генерація машинного коду**:
    - Генерація інструкцій для виконання.
    - Оптимізація для ефективного виконання.



> **Приклад простого інтерпретатора**

Після теоретичних викладок розберемо крок за кроком практичний процес створення простого інтерпретатора для арифметичних виразів. Ми розділимо програму на кілька ключових компонентів: лексичний аналізатор `Lexer`, парсер (синтаксичний аналіз) `Parser`, інтерпретатор `Interpreter` і вузли абстрактного синтаксичного дерева `AST`. Інтерпретатор ми будемо використовувати замість генерації коду.


### Лексичний аналіз

На першому кроці ми визначаємо типи токенів і клас `Token`, який буде використовуватися лексичним аналізатором `Lexer` для створення токенів із вхідного рядка. Токени є основними будівельними блоками для лексичного аналізу.

Лексичний аналізатор — це перший компонент інтерпретатора. Його завдання — перетворити код на послідовність токенів. **Токени** — це маленькі структури, які представляють елементи вихідного коду, такі як ідентифікатори, ключові слова, числа, оператори та символи пунктуації.

```python
class TokenType:
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'  # Означає кінець вхідного файлу/рядка

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'
```



```python
class LexicalError(Exception):
    pass


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """ Переміщуємо 'вказівник' на наступний символ вхідного рядка """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Означає кінець введення
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """ Пропускаємо пробільні символи. """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """ Повертаємо ціле число, зібране з послідовності цифр. """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """ Лексичний аналізатор, що розбиває вхідний рядок на токени. """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')

            raise LexicalError('Помилка лексичного аналізу')

        return Token(TokenType.EOF, None)



def main():
    while True:
        try:
            text = input('Введіть вираз (або "exit" для виходу): ')
            if text.lower() == 'exit':
                print("Вихід із програми.")
                break
            lexer = Lexer(text)
            token = lexer.get_next_token()
            while token.type != TokenType.EOF:
                print(token)
                token = lexer.get_next_token()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
```


Лексичний аналізатор переглядає вхідний рядок і створює токени для кожного цілого числа й арифметичного оператора. Це перший важливий крок в аналізі тексту програми. Аналізатор ігнорує пробіли та розділяє текст на смислові одиниці — токени.



### Створення парсера (синтаксичний аналіз)

Наступний крок — створення парсера, який будує абстрактне синтаксичне дерево (AST) з послідовності токенів, наданих лексичним аналізатором. Парсер аналізує структуру токенів і визначає їхні відношення.

Спочатку визначимо базові класи для вузлів AST:


```python
class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
```


Класи `AST`, `BinOp` і `Num` є частиною реалізації абстрактного синтаксичного дерева, яке використовується в компіляторах та інтерпретаторах для представлення структури вихідного коду під час його аналізу.

Клас `AST` є базовим класом для всіх вузлів AST. Зазвичай він абстрактний і слугує батьківським класом для всіх конкретних типів вузлів дерева.

Клас `BinOp` (Binary Operation) представляє бінарну операцію в AST, таку як додавання або віднімання. Він містить три атрибути:

- `left` — лівий операнд операції (також є вузлом AST).
- `op` — токен, що представляє операцію (наприклад, токен для `+` або `-`).
- `right` — правий операнд операції (також є вузлом AST).

Об'єкт `BinOp` використовується для представлення виразів типу "_число операція число_" (наприклад, `"2 + 3"`).

Клас `Num` (Number) представляє числовий літерал в AST. Він містить токен, що відповідає числу, і його числове значення. Об'єкти цього класу використовуються для представлення чисел у виразах.

Коли наш парсер аналізує вираз, він будує AST, використовуючи ці класи для представлення різних елементів виразу. Наприклад, вираз `"2 + 3"` буде представлено у вигляді дерева з коренем `BinOp`, де `left` — це `Num` об'єкт із числом `2`, `op` — це токен для `+`, а `right` — це `Num` об'єкт із числом `3`.


```python
class ParsingError(Exception):
    pass


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParsingError('Помилка синтаксичного аналізу')

    def eat(self, token_type):
        """
        Порівнюємо поточний токен з очікуваним токеном і, якщо вони збігаються,
        'поглинаємо' його й переходимо до наступного токена.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        """ Парсер для 'term' правил граматики. У нашому випадку - це цілі числа."""
        token = self.current_token
        self.eat(TokenType.INTEGER)
        return Num(token)

    def expr(self):
        """ Парсер для арифметичних виразів. """
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

def print_ast(node, level=0):
    indent = '  ' * level
    if isinstance(node, Num):
        print(f"{indent}Num({node.value})")
    elif isinstance(node, BinOp):
        print(f"{indent}BinOp:")
        print(f"{indent}  left: ")
        print_ast(node.left, level + 2)
        print(f"{indent}  op: {node.op.type}")
        print(f"{indent}  right: ")
        print_ast(node.right, level + 2)
    else:
        print(f"{indent}Unknown node type: {type(node)}")
```



## Створення інтерпретатора

На цьому кроці ми створюємо інтерпретатор, який буде обходити AST (абстрактне синтаксичне дерево), створене парсером, і виконувати обчислення арифметичного виразу. Інтерпретатор відіграє роль аналога генератора коду в компіляторі, але замість створення машинного або проміжного коду він безпосередньо виконує обчислення, ґрунтуючись на структурі AST. До цього кроку в нас уже є класи Lexer і Parser, які генерують токени та будують AST відповідно.


```python
class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.expr()
        print_ast(tree)
        return self.visit(tree)

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'Немає методу visit_{type(node).__name__}')
```



# Повний код
```python
class LexicalError(Exception):
    pass


class ParsingError(Exception):
    pass


class TokenType:
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'  # Означає кінець вхідного рядка


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """ Переміщуємо 'вказівник' на наступний символ вхідного рядка """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Означає кінець введення
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """ Пропускаємо пробільні символи. """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """ Повертаємо ціле число, зібране з послідовності цифр. """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """ Лексичний аналізатор, що розбиває вхідний рядок на токени. """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')

            raise LexicalError('Помилка лексичного аналізу')

        return Token(TokenType.EOF, None)


class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParsingError('Помилка синтаксичного аналізу')

    def eat(self, token_type):
        """
        Порівнюємо поточний токен з очікуваним токеном і, якщо вони збігаються,
        'поглинаємо' його і переходимо до наступного токена.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        """ Парсер для 'term' правил граматики. У нашому випадку - це цілі числа."""
        token = self.current_token
        self.eat(TokenType.INTEGER)
        return Num(token)

    def expr(self):
        """ Парсер для арифметичних виразів. """
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node


def print_ast(node, level=0):
    indent = '  ' * level
    if isinstance(node, Num):
        print(f"{indent}Num({node.value})")
    elif isinstance(node, BinOp):
        print(f"{indent}BinOp:")
        print(f"{indent}  left: ")
        print_ast(node.left, level + 2)
        print(f"{indent}  op: {node.op.type}")
        print(f"{indent}  right: ")
        print_ast(node.right, level + 2)
    else:
        print(f"{indent}Unknown node type: {type(node)}")


class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.expr()
        return self.visit(tree)

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'Немає методу visit_{type(node).__name__}')


def main():
    while True:
        try:
            text = input('Введіть вираз (або "exit" для виходу): ')
            if text.lower() == 'exit':
                print("Вихід із програми.")
                break
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()
            print(result)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
```



### **Огляд модуля `ast` у Python**

Модуль `ast` (Abstract Syntax Tree) у Python дозволяє працювати з абстрактним синтаксичним деревом (AST), яке є структурованим представленням вихідного коду у вигляді дерева.



#### **Основні можливості модуля `ast`**

1. **Парсинг коду у AST**
    
    ```python
    import ast
    tree = ast.parse("x = 5 + 3")
    print(ast.dump(tree, indent=4))
    ```
    
    Це створює AST для виразу `x = 5 + 3`.
    
2. **Обхід дерева AST**  
    Використовується для аналізу структури коду.
    
    ```python
    class MyVisitor(ast.NodeVisitor):
        def visit_BinOp(self, node):
            print(f"Знайдено операцію: {type(node.op).__name__}")
            self.generic_visit(node)
    
    visitor = MyVisitor()
    visitor.visit(tree)
    ```
    
3. **Модифікація AST та генерація коду**  
    Використовується для автоматичних трансформацій коду.
    

#### **Де використовується `ast`?**

- Аналіз вихідного коду Python.
- Оптимізація коду перед виконанням.
- Автоматичне генерування коду.
- Написання лінтерів та інструментів аналізу коду.

## Приклад

```python
import ast


class ExtendedInterpreter(ast.NodeVisitor):
    def __init__(self):
        self.result = 0

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        elif isinstance(node.op, ast.Pow):
            return left ** right
        else:
            raise ValueError(f"Unsupported operation: {type(node.op)}")

    def visit_Num(self, node):
        return node.n

		def visit_UnaryOp(self, node):
		        operand = self.visit(node.operand)
		        if isinstance(node.op, ast.USub):
		            return -operand
		        elif isinstance(node.op, ast.UAdd):
		            return +operand
		        else:
		            raise ValueError(f"Unsupported unary operation: {type(node.op)}")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.UAdd):
            return +operand
        else:
            raise ValueError(f"Unsupported unary operation: {type(node.op)}")

    def interpret(self, code):
        tree = ast.parse(code)
        return self.visit(tree.body[0].value)


if __name__ == '__main__':

    # Тестування інтерпретатора
    interpreter = ExtendedInterpreter()
    print(interpreter.interpret("3 + 5 - 2"))  # Виведе: 6
    print(interpreter.interpret("3 * 5"))  # Виведе: 15
    print(interpreter.interpret("10 / 2"))  # Виведе: 5.0
    print(interpreter.interpret("2 ** 3 + 1 - 3"))  # Виведе: 6
    print(interpreter.interpret("-3 + 5"))  # Виведе: 2
```

