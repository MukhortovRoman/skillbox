def calculate_vibrations(initial_amplitude, stop_amplitude):
    vibrations = 0
    amplitude = initial_amplitude
    while amplitude > stop_amplitude:
        amplitude *= 0.916
        vibrations += 1
    return vibrations

def main():
    initial_amplitude = float(input("Введите начальную амплитуду: "))
    stop_amplitude = float(input("Введите амплитуду остановки: "))
    vibrations = calculate_vibrations(initial_amplitude, stop_amplitude)
    print(f"Маятник считается остановившимся через {vibrations} колебаний")

main()
