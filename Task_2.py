class Road:
  def __init__(self, length, width):
    self._length = length
    self._width = width

  def calculate(self, mass_asf, thickness):
    total = self._length * self._width * mass_asf * thickness
    print(f'Понадобится закупить {total // 1000} тонн асфальта')

road_params = list(map(int, input('Введите длину(м) и ширину(м) дороги через пробел:\n').split()))
road_66 = Road(road_params[0], road_params[1])

asf_params = list(map(int, input('Введите массу асфальта для покрытия 1 м^2 дороги слоем 1 см(кг) и толщину полотна(см) через пробел:\n').split()))
print()
road_66.calculate(asf_params[0], asf_params[1])