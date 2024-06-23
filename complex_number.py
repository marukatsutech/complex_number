# Complex number

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk


def show_data():
    global arrow_complex_a, txt_cx_a
    global arrow_complex_b, txt_cx_b
    global real_part_c, imaginary_part_c, complex_number_c
    global arrow_complex_c, txt_cx_c
    # Complex number A
    arrow_complex_a.set_data(dx=real_part_a, dy=imaginary_part_a)
    txt_cx_a.set_text("A(" + str(complex_number_a.real) + "," + str(complex_number_a.imag) + ")")
    txt_cx_a.set_position((complex_number_a.real, complex_number_a.imag))
    # Complex number B
    arrow_complex_b.set_data(dx=real_part_b, dy=imaginary_part_b)
    txt_cx_b.set_text("B(" + str(complex_number_b.real) + "," + str(complex_number_b.imag) + ")")
    txt_cx_b.set_position((complex_number_b.real, complex_number_b.imag))
    # Complex number C
    txt_op = "C("
    if var_op.get() == 0:
        complex_number_c = complex_number_a + complex_number_b
        txt_op = "C(=A+B)("
    elif var_op.get() == 1:
        complex_number_c = complex_number_a - complex_number_b
        txt_op = "C(=A-B)("
    elif var_op.get() == 2:
        complex_number_c = complex_number_a * complex_number_b
        txt_op = "C(=A*B)("
    elif var_op.get() == 3:
        complex_number_c = complex_number_a / complex_number_b
        txt_op = "C(=A/B)("
    real_part_c = complex_number_c.real
    imaginary_part_c = complex_number_c.imag
    arrow_complex_c.set_data(dx=real_part_c, dy=imaginary_part_c)
    txt_cx_c.set_text(txt_op + str(np.round(complex_number_c.real, 2)) + ","
                      + str(np.round(complex_number_c.imag, 2)) + ")")
    txt_cx_c.set_position((complex_number_c.real, complex_number_c.imag))

    '''
    print("complex number A:", complex_number_a)
    print("real, imag:", np.real(complex_number_a), np.imag(complex_number_a))
    print("real, imag:", complex_number_a.real, complex_number_a.imag)
    print("abs:", np.abs(complex_number_a))
    print("conj:", np.conj(complex_number_a))
    print("angle(rad):", np.angle(complex_number_a, deg=False))
    print("angle(deg):", np.angle(complex_number_a, deg=True))
    '''


def set_real_part_a(value):
    global real_part_a, complex_number_a
    global arrow_complex_a
    real_part_a = float(value)
    complex_number_a = complex(real_part_a, imaginary_part_a)
    show_data()


def set_imaginary_part_a(value):
    global imaginary_part_a, complex_number_a
    imaginary_part_a = float(value)
    complex_number_a = complex(real_part_a, imaginary_part_a)
    show_data()


def set_real_part_b(value):
    global real_part_b, complex_number_b
    real_part_b = float(value)
    complex_number_b = complex(real_part_b, imaginary_part_b)
    show_data()


def set_imaginary_part_b(value):
    global imaginary_part_b, complex_number_b
    imaginary_part_b = float(value)
    complex_number_b = complex(real_part_b, imaginary_part_b)
    show_data()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True
    # tx_step.set_text("Step=" + str(cnt))


def update(f):
    pass
    global cnt
    # global tx_step
    if is_play:
        # tx_step.set_text("Step=" + str(cnt))
        cnt += 1


# Global variables
# Animation control
cnt = 0
is_play = False

# Parameters
real_part_a = 0.
imaginary_part_a = 0.
complex_number_a = complex(real_part_a, imaginary_part_a)

real_part_b = 0.
imaginary_part_b = 0.
complex_number_b = complex(real_part_b, imaginary_part_b)

real_part_c = 0.
imaginary_part_c = 0.
complex_number_c = complex(real_part_c, imaginary_part_c)

'''
complex_90deg = complex(0., 1.)
theta_deg = 270.
theta = np.deg2rad(theta_deg)
complex_rot = complex(np.cos(theta), np.sin(theta))
complex_number_rotated = complex_number_a * complex_rot
'''

# Data array
range_x_min = -6.
range_x_max = 6.
range_y_min = -6.
range_y_max = 6.

# Generate figure and axes
title_ax0 = "Complex number"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max

fig = Figure()
ax0 = fig.add_subplot(111)
ax0.set_title(title_ax0)
ax0.set_xlabel("Real part")
ax0.set_ylabel("Imaginary part")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")
ax0.grid()
# ax0.invert_yaxis()


# Generate graphic items
# Counter text
# tx_step = ax0.text(x_min, y_max * 0.9, "Step=" + str(0))

# Value of complex number
txt_cx_a = ax0.text(complex_number_a.real, complex_number_a.imag, "A(" + str(complex_number_a.real) + ","
                    + str(complex_number_a.imag) + ")")
txt_cx_b = ax0.text(complex_number_b.real, complex_number_b.imag, "B(" + str(complex_number_b.real) + ","
                    + str(complex_number_b.imag) + ")")
txt_cx_c = ax0.text(complex_number_c.real, complex_number_c.imag, "C(" + str(complex_number_c.real) + ","
                    + str(complex_number_c.imag) + ")")

# Quiver
x, y = 0., 0.
dx, dy = 0., 0.
arrow_complex_a = ax0.arrow(x, y, dx, dy, head_width=0.2, ec='blue', color='blue', length_includes_head=True)
arrow_complex_b = ax0.arrow(x, y, dx, dy, head_width=0.2, ec='green', color='green', length_includes_head=True)
arrow_complex_c = ax0.arrow(x, y, dx, dy, head_width=0.2, ec='red', color='red', length_includes_head=True)

# Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Animation control
'''
# Frame
frm_ac = ttk.Labelframe(root, relief="ridge", text="Animation control", labelanchor="n", width=100)
frm_ac.pack(side='left', fill=tk.Y)
# Play and pause button
btn_pp = tk.Button(frm_ac, text="Play/Pause", command=lambda: switch())
btn_pp.pack()
'''

# Parameter setting
# Complex number A
frm_cx_a = ttk.Labelframe(root, relief="ridge", text="Complex number A", labelanchor="n")
frm_cx_a.pack(side='left', fill=tk.Y)

lbl_real_a = tk.Label(frm_cx_a, text="Real part:")
lbl_real_a.pack(side='left')
var_real_a = tk.StringVar(root)
var_real_a.set(str(real_part_a))
spn_real_a = tk.Spinbox(
    frm_cx_a, textvariable=var_real_a, format="%.1f", from_=-6., to=6., increment=0.5,
    command=lambda: set_real_part_a(var_real_a.get()), width=6
    )
spn_real_a.pack(side='left')

lbl_imaginary_a = tk.Label(frm_cx_a, text="Imaginary part:")
lbl_imaginary_a.pack(side='left')
var_imaginary_a = tk.StringVar(root)
var_imaginary_a.set(str(real_part_a))
spn_imaginary_a = tk.Spinbox(
    frm_cx_a, textvariable=var_imaginary_a, format="%.1f", from_=-6., to=6., increment=0.5,
    command=lambda: set_imaginary_part_a(var_imaginary_a.get()), width=6
    )
spn_imaginary_a.pack(side='left')

# Complex number B
frm_cx_b = ttk.Labelframe(root, relief="ridge", text="Complex number B", labelanchor="n")
frm_cx_b.pack(side='left', fill=tk.Y)

lbl_real_b = tk.Label(frm_cx_b, text="Real part:")
lbl_real_b.pack(side='left')
var_real_b = tk.StringVar(root)
var_real_b.set(str(real_part_b))
spn_real_b = tk.Spinbox(
    frm_cx_b, textvariable=var_real_b, format="%.1f", from_=-6., to=6., increment=0.5,
    command=lambda: set_real_part_b(var_real_b.get()), width=6
    )
spn_real_b.pack(side='left')

lbl_imaginary_b = tk.Label(frm_cx_b, text="Imaginary part:")
lbl_imaginary_b.pack(side='left')
var_imaginary_b = tk.StringVar(root)
var_imaginary_b.set(str(real_part_b))
spn_imaginary_b = tk.Spinbox(
    frm_cx_b, textvariable=var_imaginary_b, format="%.1f", from_=-6., to=6., increment=0.5,
    command=lambda: set_imaginary_part_b(var_imaginary_b.get()), width=6
    )
spn_imaginary_b.pack(side='left')

# Operation
frm_op = ttk.Labelframe(root, relief="ridge", text="Operation", labelanchor="n", width=100)
frm_op.pack(side='left')
var_op = tk.IntVar(value=0)
rdb0_op = tk.Radiobutton(frm_op, text="C = A + B", command=lambda: show_data(), variable=var_op, value=0)
rdb1_op = tk.Radiobutton(frm_op, text="C = A - B", command=lambda: show_data(), variable=var_op, value=1)
rdb2_op = tk.Radiobutton(frm_op, text="C = A * B", command=lambda: show_data(), variable=var_op, value=2)
rdb3_op = tk.Radiobutton(frm_op, text="C = A / B", command=lambda: show_data(), variable=var_op, value=3)
rdb0_op.pack(side='left')
rdb1_op.pack(side='left')
rdb2_op.pack(side='left')
rdb3_op.pack(side='left')

# Initialize data
pass

# Draw animation
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
root.mainloop()
