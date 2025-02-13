# URL API ПриватБанку для отримання курсу валют
API_URL="https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

# Виконання запиту до API та отримання курсу долара
response=$(curl -s "$API_URL")
# Перевірка чи отримано відповідь
if [[ -z "$response" ]]; then
echo "$(date '+%Y-%m-%d %H:%M:%S') - Не вдалося отримати дані від API"
exit 1
fi
# Витягнення курсу USD до UAH за допомогою jq
USD_RATE=$(echo "$response" | jq -r '.[] | select(.ccy=="USD") | .sale')
# Перевірка чи курс було отримано
if [[ -z "$USD_RATE" ]]; then
echo "$(date '+%Y-%m-%d %H:%M:%S') - Не вдалося знайти курс USD/UAH у відповіді API"
exit 1
fi
# Запис результату
echo "$(date '+%Y-%m-%d %H:%M:%S') - Поточний курс USD/UAH: $USD_RATE"
