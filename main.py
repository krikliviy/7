from figures import *

def create_figure(figure_type, params):
    if figure_type == "Triangle":
        return Triangle(*params)
    elif figure_type == "Rectangle":
        return Rectangle(*params)
    elif figure_type == "Trapeze":
        return Trapeze(*params)
    elif figure_type == "Parallelogram":
        return Parallelogram(*params)
    elif figure_type == "Circle":
        return Circle(*params)
    elif figure_type == "Ball":
        return Ball(*params)
    elif figure_type == "TriangularPyramid":
        return TriangularPyramid(*params)
    elif figure_type == "QuadrangularPyramid":
        return QuadrangularPyramid(*params)
    elif figure_type == "RectangularParallelepiped":
        return RectangularParallelepiped(*params)
    elif figure_type == "Cone":
        return Cone(*params)
    elif figure_type == "TriangularPrism":
        return TriangularPrism(*params)
    else:
        raise ValueError(f"Неизвестный тип фигуры: {figure_type}")

def read_figures(filename):
    figures = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            figure_type = parts[0]
            params = [float(x) for x in parts[1:]]
            try:
                figure = create_figure(figure_type, params)
                figures.append(figure)
            except Exception as e:
                print(f"Ошибка при создании фигуры {figure_type}: {e}")
    return figures

def find_max_volume_figure(figures):
    if not figures:
        return None
    return max(figures, key=lambda x: x.volume())

def main():
    # Читаем фигуры из всех трех файлов
    all_figures = []
    for filename in ['input01.txt', 'input02.txt', 'input03.txt']:
        try:
            figures = read_figures(filename)
            all_figures.extend(figures)
        except Exception as e:
            print(f"Ошибка при чтении файла {filename}: {e}")
    
    # Находим фигуру с максимальным объемом
    max_figure = find_max_volume_figure(all_figures)
    
    if max_figure:
        print(f"Фигура с максимальным объемом: {max_figure.__class__.__name__}")
        print(f"Объем: {max_figure.volume()}")
    else:
        print("Не удалось найти фигуры")

if __name__ == "__main__":
    main() 
