from logging import currentframe
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line, Polygon

def draw_start_shape(context: AppContext):
    context.canvas.delete("all")
    x_s = [50, 100, 150, 200, 300, 400, 450, 600]
    y_s = [50, 120, 200, 310, 410, 500, 110, 600]
    id = context.canvas.create_polygon(x_s[0], y_s[0], x_s[1], y_s[1],x_s[2], y_s[2],x_s[3], y_s[3],x_s[4], y_s[4],x_s[5], y_s[5],x_s[6], y_s[6], x_s[7], y_s[7], smooth="1", fill='', outline='red')
    id_1 = context.canvas.create_polygon(x_s[0], y_s[0], x_s[1], y_s[1],x_s[2], y_s[2],x_s[3], y_s[3],x_s[4], y_s[4],x_s[5], y_s[5],x_s[6], y_s[6], x_s[7], y_s[7], smooth="0", fill='', outline="black")
    polygon = Polygon(id, x_s, y_s)
    context.current_polygon = polygon
    context.smooth_polygon_id = id_1

def start_spline(event,context:AppContext):
    x_s = context.current_polygon.x_coordinates
    y_s = context.current_polygon.y_coordinates
    context.current_point_number = find_closest_point(x_s, y_s, event.x, event.y)

def on_changing_spline(event, context: AppContext):
    if context.current_polygon:
        new_x = event.x
        new_y = event.y
        context.current_polygon.update_point(new_x, new_y, context.current_point_number)
        x_s = context.current_polygon.x_coordinates
        y_s = context.current_polygon.y_coordinates
        context.canvas.coords(context.current_polygon.id, x_s[0], y_s[0], x_s[1], y_s[1],x_s[2], y_s[2],x_s[3], y_s[3],x_s[4], y_s[4],x_s[5], y_s[5],x_s[6], y_s[6], x_s[7], y_s[7])
        context.canvas.coords(context.smooth_polygon_id, x_s[0], y_s[0], x_s[1], y_s[1],x_s[2], y_s[2],x_s[3], y_s[3],x_s[4], y_s[4],x_s[5], y_s[5],x_s[6], y_s[6], x_s[7], y_s[7])

def changing_spline_finfished(event, context:AppContext):
    if context.current_point_number is not None:
        context.current_point_number = None

def erase_spline(context:AppContext):
    if (context.current_point_number is not None and context.current_polygon is not None):
        context.canvas.delete(context.current_point_number)
        context.canvas.delete(context.current_polygon.id)
        context.current_polygon = None
        context.smooth_polygon_id = None
        context.current_point_number = None

def find_closest_point(x_s, y_s, target_x, target_y):
    for i in range(8):
        if ((target_x < x_s[i] + 10 and target_x > x_s[i] - 10) and (target_y < y_s[i] + 10 and target_y > y_s[i] - 10)):
            return i
    return -1
