import matplotlib.pyplot as py  
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.pyplot import figure
import os


class Utilities:

    @staticmethod
    def is_all_peds_finish(params):
        for ped_i in params.all_peds_ordered:
            if ped_i.status != "finished":
                return False            
        return True
   
    @staticmethod
    def plot_ped_image(ped_i, ax):
        path_pre = ""
        cwd = os.getcwd()
        if "DayuanTanPCS" in cwd:   
            path_pre = "img/"
        else:
            path_pre = "DayuanTanPCS/img/"

        image = py.imread(path_pre+"ped_lr_big.png")
        zoom = 0.1
        if ped_i.direction == "left2right" and ped_i.type == "ped":
            image = py.imread(path_pre+"ped_lr_big.png")
            zoom = 0.07 if ped_i.status == "moving" else 0.04
        elif ped_i.direction == "right2left" and ped_i.type == "ped":
            image = py.imread(path_pre+"ped_rl_big.png")
            zoom = 0.07 if ped_i.status == "moving" else 0.04
        elif ped_i.direction == "left2right" and ped_i.type == "wheelchair":
            image = py.imread(path_pre+"wheelchair_lr_big.png")
            zoom = 0.1
        elif ped_i.direction == "right2left" and ped_i.type == "wheelchair":
            image = py.imread(path_pre+"wheelchair_rl_big.png")
            zoom = 0.1
        elif ped_i.direction == "left2right" and ped_i.type == "crutches_user":
            image = py.imread(path_pre+"crutches_user_lr_big.png")
            zoom = 0.11 if ped_i.status == "moving" else 0.05
        elif ped_i.direction == "right2left" and ped_i.type == "crutches_user":
            image = py.imread(path_pre+"crutches_user_rl_big.png")
            zoom = 0.11 if ped_i.status == "moving" else 0.05
        elif ped_i.direction == "left2right" and ped_i.type == "child":
            image = py.imread(path_pre+"child_lr.png")
            zoom = 0.06 if ped_i.status == "moving" else 0.04
        elif ped_i.direction == "right2left" and ped_i.type == "child":
            image = py.imread(path_pre+"child_rl.png")
            zoom = 0.06 if ped_i.status == "moving" else 0.04
        elif ped_i.direction == "left2right" and ped_i.type == "elder":
            image = py.imread(path_pre+"elder_lr.png")
            zoom = 0.07 if ped_i.status == "moving" else 0.04
        elif ped_i.direction == "right2left" and ped_i.type == "elder":
            image = py.imread(path_pre+"elder_rl.png")
            zoom = 0.07 if ped_i.status == "moving" else 0.04
        
    
        im = OffsetImage(image, zoom=zoom)
        ab = AnnotationBbox(im, (ped_i.x, ped_i.y), xycoords='data', frameon=False, clip_on=False)
        ax.add_artist(ab)
        ax.autoscale()
    
    @staticmethod
    def plot_car_image(params, ax):
        path_pre = ""
        cwd = os.getcwd()
        if "DayuanTanPCS" in cwd:   
            path_pre = "img/"
        else:
            path_pre = "DayuanTanPCS/img/"

        image = py.imread(path_pre+"car_lr.png")
        zoom = 0.5
        im = OffsetImage(image, zoom=zoom)
        x = params.waiting_area_length + params.crosswalk_length/4
        y = params.crosswalk_width*2 
        ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False, clip_on=False)
        ax.add_artist(ab)
        ax.autoscale()
        image = py.imread(path_pre+"car_lr_45.png")
        zoom = 0.55
        im = OffsetImage(image, zoom=zoom)
        x = params.waiting_area_length + params.crosswalk_length/8
        y = 0-params.crosswalk_width 
        ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False, clip_on=False)
        ax.add_artist(ab)
        ax.autoscale()

        image = py.imread(path_pre+"car_rl.png")
        zoom = 0.5
        im = OffsetImage(image, zoom=zoom)
        x = params.waiting_area_length + params.crosswalk_length*3/4
        y = params.crosswalk_width*2 
        ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False, clip_on=False)
        ax.add_artist(ab)
        ax.autoscale()
        image = py.imread(path_pre+"car_rl_45.png")
        zoom = 0.5
        im = OffsetImage(image, zoom=zoom)
        x = params.waiting_area_length + params.crosswalk_length*7/8
        y = 0-params.crosswalk_width 
        ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False, clip_on=False)
        ax.add_artist(ab)
        ax.autoscale()

    @staticmethod
    def plot_positions(params, status):
        figure(figsize=( (params.waiting_area_length*2 + params.crosswalk_length + 300)/100  * params.global_plot_zoom, 11 * params.global_plot_zoom), dpi=80)
        ax = py.gca()

        # draw ped
        for ped_i in params.all_peds_lr_sorted_by_x:
            # draw dot
            # ax.plot(ped_i.x, ped_i.y, 'ro', clip_on=False)
            Utilities.plot_ped_image(ped_i, ax)
            # add circle
            if status == "standing":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_standing, color='b', fill=False, clip_on=False) )
            if status == "moving" and ped_i.status == "moving":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving_curr_step, color='b', fill=False, clip_on=False) )

        for ped_i in params.all_peds_rl_sorted_by_x:
            # draw dot
            # ax.plot(ped_i.x, ped_i.y, 'cs', clip_on=False)
            Utilities.plot_ped_image(ped_i, ax)
            # add circle
            if status == "standing":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_standing, color='g', fill=False, clip_on=False) )
            if status == "moving" and ped_i.status == "moving":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving_curr_step, color='g', fill=False, clip_on=False) )
            
        # draw car
        Utilities.plot_car_image(params, ax)

        # draw crosswalk area
        split_line_left_x = [params.waiting_area_length, params.waiting_area_length]
        split_line_left_y = [0, params.crosswalk_width]
        split_line_right_x = [params.waiting_area_length + params.crosswalk_length, params.waiting_area_length + params.crosswalk_length]
        split_line_right_y = [0, params.crosswalk_width]
        top_line_x = [params.waiting_area_length, params.waiting_area_length + params.crosswalk_length]
        top_line_y = [params.crosswalk_width, params.crosswalk_width]
        bottom_line_x = [params.waiting_area_length, params.waiting_area_length + params.crosswalk_length]
        bottom_line_y = [0, 0]
        py.plot(split_line_left_x, split_line_left_y, 'b-')
        py.plot(split_line_right_x, split_line_right_y, 'b-')
        py.plot(top_line_x, top_line_y, 'b-')
        py.plot(bottom_line_x, bottom_line_y, 'b-')

        # draw bound
        top_bound_x = [params.waiting_area_length, params.waiting_area_length + params.crosswalk_length]
        top_bound_y = [params.crosswalk_width + params.outside_margin_width, params.crosswalk_width + params.outside_margin_width]
        py.plot(top_bound_x, top_bound_y, 'b-')
        bottom_bound_x = [params.waiting_area_length, params.waiting_area_length + params.crosswalk_length]
        bottom_bound_y = [- params.outside_margin_width, - params.outside_margin_width]
        py.plot(bottom_bound_x, bottom_bound_y, 'b-')

        py.xlim([-100, params.total_length + 300])
        py.ylim([-600, params.crosswalk_width + 600])

        py.text(params.waiting_area_length - 200, params.crosswalk_width / 3, "Waiting\narea\non one\nside")
        py.text(params.waiting_area_length + params.crosswalk_length + 10, params.crosswalk_width / 3, "Waiting\narea\non another\nside")
        py.text(params.waiting_area_length + params.crosswalk_length/4, params.crosswalk_width / 2, "Crosswalk area. "+"Length: "+str(params.crosswalk_length)+" cm; Width: "+str(params.crosswalk_width)+" cm.")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width + 50, "Outside crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, -50, "Outside crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/4, params.crosswalk_width + 92, "Upper bound for pedestrian allowed area")
        py.text(params.waiting_area_length + params.crosswalk_length/4, -108, "Bottom bound for pedestrian allowed area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width + 200, "Further outside crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, -200, "Further outside crosswalk area")

        py.text(-350, 1100, "To next step, click the close or 'X' button of this 'Current Simulation Step' window.")
        # py.get_current_fig_manager().canvas.set_window_title('Current Simulation Step (Close for next step)')
        py.get_current_fig_manager().set_window_title('Current Simulation Step (Close for next step)')


        py.show()
