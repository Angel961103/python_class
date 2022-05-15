from pycat.core import Window
from pycat.experimental import LdtkFile

w = Window()
ldtk = LdtkFile("test.ldtk")

ldtk.render_level(w, "Level_0", debug_tags=True)

for level in ldtk._data.levels:
    print(level.identifier)
    for layer in level.layer_instances:
        print(layer.identifier)
        int_grid_csy_2d = []
        row = layer.c_hei
        c = 0
        col = layer.c_wid
        grid = layer.int_grid_csv
        if grid:
            for i in range(row):
                row = []
                for j in range(col):
                    row.append(grid[c])
                    c += 1
                int_grid_csy_2d.append(row)
            for row in int_grid_csy_2d:
                print(*row)

w.run()