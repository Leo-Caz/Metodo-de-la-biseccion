import math
from pathlib import Path
import matplotlib.pyplot as plt


def biseccion(f, a, b, TOL, N0=100):

    if a >= b:
        raise ValueError("Se necesita a < b")
    if TOL <= 0:
        raise ValueError("La tolerancia debe ser positiva")
    if not isinstance(N0, int) or N0 < 1:
        raise ValueError("N0 debe ser un entero positivo")

    FA = f(a)
    FB = f(b)
    if not math.isfinite(FA) or not math.isfinite(FB):
        raise ValueError("La funcion no esta definida en algun extremo")
    if FA == 0:
        return a, []
    if FB == 0:
        return b, []
    if FA * FB > 0:
        raise ValueError("No hay cambio de signo en [a,b]")

    historia = []
    i = 1
    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)
        if not math.isfinite(FP):
            raise ValueError("La funcion no esta definida en un punto medio")
        historia.append((a, b, p))


        if FP == 0 or (b - a) / 2 < TOL:
            return p, historia

        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    raise RuntimeError(f"El metodo fracaso despues de {N0} iteraciones")



def f1(x):
    return x**3 - x - 1


def polinomio(x):
    return x**3 - 7*x**2 + 14*x - 6


def f_seno(x):
    return x - 2*math.sin(x)


def f_tangente(x):
    return x - math.tan(x)


def f_exponencial(x):
    return x**2 - 1 - math.exp(1 - x**2)


def f_multiples(x):
    return (x + 3)*(x + 1)**2*x*(x - 1)**3*(x - 3)


def f_agua(h):
    return 10*(math.pi/2 - math.asin(h) - h*math.sqrt(1 - h**2)) - 12.4


def f_caida(t):
    return 300 - 24.525*t + 61.3125*(1 - math.exp(-0.4*t))



CARPETA = Path(__file__).resolve().parent


def graficar_seno(raiz):
    xs = [3*i/1000 for i in range(1001)]
    plt.figure(figsize=(8, 5))
    plt.plot(xs, xs, label="y = x")
    plt.plot(xs, [2*math.sin(x) for x in xs], label="y = 2 sen(x)")
    plt.scatter([raiz], [raiz], label=f"Raiz positiva: x = {raiz:.6f}", zorder=4)
    plt.xlabel("x (radianes)")
    plt.ylabel("y")
    plt.title("Interseccion de y = x y y = 2 sen(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(CARPETA / "grafica_seno.png", dpi=180)
    plt.close()


def graficar_tangente(raiz):
    plt.figure(figsize=(9, 5))
    xs = [5*i/2000 for i in range(2001)]
    plt.plot(xs, xs, label="y = x")


    asintotas = [math.pi/2, 3*math.pi/2]
    tramos = [(0, asintotas[0]-0.001),
              (asintotas[0]+0.001, asintotas[1]-0.001),
              (asintotas[1]+0.001, 5)]
    color_tangente = None
    for i, (inicio, fin) in enumerate(tramos):
        xx = [inicio + (fin - inicio)*j/1000 for j in range(1001)]
        yy = [math.tan(x) for x in xx]
        if i == 0:
            linea, = plt.plot(xx, yy, label="y = tan(x)")
            color_tangente = linea.get_color()
        else:
            plt.plot(xx, yy, color=color_tangente)

    for i, pos in enumerate(asintotas):
        plt.axvline(pos, linestyle="--", linewidth=1,
                    label="Asintotas" if i == 0 else None)

    plt.scatter([raiz], [raiz], s=65, zorder=5,
                label=f"Raiz positiva: x = {raiz:.6f}")
    plt.annotate(f"({raiz:.4f}, {raiz:.4f})", (raiz, raiz),
                 xytext=(3.35, 7), arrowprops={"arrowstyle": "->"})
    plt.xlim(0, 5)
    plt.ylim(-10, 10)
    plt.xlabel("x (radianes)")
    plt.ylabel("y")
    plt.title("Interseccion de y = x y y = tan(x)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc="lower left")
    plt.tight_layout()
    plt.savefig(CARPETA / "grafica_x_tanx.png", dpi=180)
    plt.close()


def graficar_exponencial(raiz):
    xs = [-2 + 2*i/1000 for i in range(1001)]
    plt.figure(figsize=(8, 5))
    plt.plot(xs, [x*x-1 for x in xs], label="y = x^2 - 1")
    plt.plot(xs, [math.exp(1-x*x) for x in xs], label="y = exp(1-x^2)")
    plt.scatter([raiz], [raiz*raiz-1], zorder=4,
                label=f"Raiz: x = {raiz:.6f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interseccion de las curvas exponenciales")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(CARPETA / "grafica_exponencial.png", dpi=180)
    plt.close()


