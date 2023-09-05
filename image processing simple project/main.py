import subprocess


print('Welcom in Image Processing App')
print('---------------------------------')
print('[1]-Binary image')
print('[2]-create a matrix-Density picture')
print('[3]-Blur an image with a 2D convolution matrix')
print('[4]-Smoothing (Averaging) Filter Masks')
print('[5]-Order Statistic (Nonlinear) Filters')
print('[6]-Gaussian Noise')
print('[7]-Salt&Pepper Noise')


# Call File Function ---------------------------------
def call_file(fileName):
    cmd = fileName
    subprocess.Popen(cmd, shell=True)

# Chooes Option Function -----------------------------
def chooes_Option(opt):
    if opt == '1':
        call_file("python BinaryImage.py")
    elif opt == '2':
        call_file("python matrixDensity.py")
    elif opt == '3':
        call_file("python BlurImage.py")
    elif opt == '4':
        call_file("python SmoothingFilterMasks.py")
    elif opt == '5':
        call_file("python OrderStatistic.py")
    elif opt == '6':
        call_file("python GaussianNoise.py")
    elif opt == '7':
        call_file("python SaltPepperNoise.py")
    else:
        print("!You Have Enter Wrong Number Try Again...")


option = input('Enter an option:...')
chooes_Option(option)