from colorama import init, Fore, Back, Style


print(Fore.RED + "Letters")                        # використовується для кольору літер
print(Back.WHITE + "Background")                   # використовується для кольору фону

print(Fore.Style.DIM + "Letters")      # використовується для мінімального обведення
print(Fore.RED + Style.NORMAL + "Letters")   # використовується для звичайного стилю літер
print(Fore.RED + Style.BRIGHT + "Letters")   # використовується для яскравого стилю літер


print(cr.ansi.clear_screen())        # використовується для очистки консолій


print(Fore.RED + Back.WHITE + "Sample Text" + Style.RESET)  # використовуэться для повернення налаштувань до завмовчування
print(Fore.Style.DIM + "Letters")          # використовується для мінімального обведення
print(Fore.BLUREDStyle.NORMAL + "Letters")   # використовується для звичайного стилю літер


text=colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)