class Road:

    def __init__(self, road_len, road_wid):
        self._length = road_len
        self._width = road_wid

    def asphalt_calc(self, weight=25, road_thick=5):
        print(f'{(self._length * self._width * weight * road_thick) / 1000 } т.')


road_1 = Road(int(input()), int(input()))
road_1.asphalt_calc()
