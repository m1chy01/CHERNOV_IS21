# вариант 24. с начала суток прошло N секунд (N - целое). найти количество полных минут, прошедших с начала суток

try:
    N = int(input('секунды:'))
    m = N//60
    print(f'минуты: {m}')
except:
    print('нужно ввести целое число')