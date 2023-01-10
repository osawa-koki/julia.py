import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures

# 複素数を扱うために np.complex128 型を使用する
def julia(c, z, maxiter):
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

# ジュリア集合を描写する範囲を指定する
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
cx, cy = -0.8, 0.156

# ジュリア集合を計算するためのグリッドを作成する
xs = np.linspace(xmin, xmax, 1000)
ys = np.linspace(ymin, ymax, 1000)
zs = np.empty((len(xs), len(ys)))

with concurrent.futures.ThreadPoolExecutor() as executor:
    zs = list(executor.map(lambda z: julia(cx + cy*1j, z, 50), [(x + y*1j) for x in xs for y in ys]))

zs = np.array(zs).reshape((len(xs), len(ys)))

plt.imshow(zs.T, cmap='bone', extent=(xmin, xmax, ymin, ymax))
plt.savefig('julia.png')
