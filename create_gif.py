import imageio.v3 as iio


filenames = ['OSO.png', 'ososouls.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('oso.gif', images, duration = 500, loop = 0) 

