#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#  Он задумывает два натуральных числа X и Y (X,Y ≤ 1000), а Катя должна их отгадать. 
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#  Помогите Кате отгадать задуманные Петей числа.

S = int(input("Значение суммы: "))
P = int(input("Значение произведения: "))
def searcing_numbers(sum,product):
    for i in range(sum):
        for j in range(product):
            if sum == i + j and product == i*j:
                return f"Загаданные значения равны {i} и {j}"
    return "такой комбинации чисел не существует"
print(searcing_numbers(S,P))
