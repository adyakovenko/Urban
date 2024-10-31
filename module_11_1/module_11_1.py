import numpy
from matplotlib import pyplot as plt
from PIL import Image

# демонстрационный скрипт
# библиотеку numpy удобно использовать для преобразования Фурье.
# Про само преобразование Фурье расказывать долго и бессмысленно, т.к. есть источники получше
# Для демонстрации необходимо знать, что это преобразование переводит сигнал в частотную область, где с ним можно выполнять разные операции,
# используя странные математические формулы
# Ниже представлено свойство сдвига преобразования Фурье: в частотной области можно сдвинуть последовательность.

# входные параметры
nsmp = 10  # количество элементов массива (лучше не ставить слишком много, а то не видно будет)
k = 1.5  # насколько сдвигать

array = [numpy.random.random() for _ in range(nsmp)]  # массив рандомных чисел (взял numpy.random)
array_shifted_in_time = numpy.roll(array, numpy.round(k, 0))  # это сдвиг во временной области через numpy.roll

# сдвиг во временной области
array_spec = numpy.fft.rfft(array)  # считаем спектр (входная последовательность действительная, поэтому можем использовать rfft вместо fft для экономии места)
array_spec_shift = [numpy.exp(-1j * i * k / len(array) * 2 * numpy.pi) * array_spec[i] for i in range(len(array_spec))]  # умножаем на экспоненту, которая обеспечит сдвиг
array_shift = numpy.fft.irfft(array_spec_shift, len(array))  # возвращаемся обратно во временную область

# для рисования буду использовать matplotlib. Если с numpy я, возможно, замудрил, то тут комментарии не нужны.
plt.figure()
plt.title('Последовательности')
plt.plot(array, linewidth=3)
plt.plot(array_shifted_in_time, linewidth=3)
plt.plot(array_shift, linestyle='dashed')
plt.grid()
plt.xlabel('отсчёты')
plt.legend(['Начальная', 'Сдвинутая с помощью numpy.roll()', 'Сдвинутая с помощью numpy.fft'])
#plt.show()

# если поставить k=2, сдвиг будет на 2 отсчёта. и т.д.
# если поставить сдвиг на 1.5 отсчёта, то во времени мы сдвинуть так не сможем (там поэтому numpy.roll()), а вот во частотной области нас ничего не ограничивает
# в случае, если k не является целым числом, дискретная последовательность будет "переливаться" от одного отсчёта к другому


# другое полезное применение numpy - аппроксимация полиномами разной степени

x = numpy.arange(len(array))  # ось х для исходной последовательности
x_interpolated = numpy.arange(len(array) * 10) / 10  # увеличили кол-во отсчётов в 10 раз

polynom_1 = numpy.polyval(numpy.polyfit(x, array, 1), x_interpolated)
polynom_2 = numpy.polyval(numpy.polyfit(x, array, 2), x_interpolated)
polynom_3 = numpy.polyval(numpy.polyfit(x, array, 3), x_interpolated)

plt.figure()
plt.title('Массив и его аппроксимации полиномами')
plt.plot(x, array)
plt.plot(x_interpolated, polynom_1)
plt.plot(x_interpolated, polynom_2)
plt.plot(x_interpolated, polynom_3)
plt.xlim(x_interpolated[0], x_interpolated[-1])
plt.grid()
plt.legend(['исходная последовательность', 'аппроксимация прямой', 'аппроксимация параболой', 'аппроксимация полиномом 3 степени'])
name = 'image'
plt.savefig(f'{name}.png')  # matplotlib умеет сохранять картинки, что очень удобно, кстати
#plt.show()


# входная картинка готова, теперь можно посмотреть Pillow
Image.open(f'{name}.png').rotate(numpy.random.randint(10, 350), expand=1).convert('L').save(f'{name}_black_and_white.bmp', 'BMP')

# эту картинку я открыл, перевернул, сделал черно-белой и сохранил в другом формате.
# можно докопаться до неё и рассматривать как матрицу с цветами RGB и тем самым менять цвета, но кажется, я её помучил достаточно
