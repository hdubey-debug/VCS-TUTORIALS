# from manim import ( # type: ignore
#     Scene, Text, Underline, Create, Write, Arrow, Triangle, VGroup, Line, Brace,
#     BLUE_E, GREEN_E, RED_E, CurvedArrow, DEGREES, Paragraph, DrawBorderThenFill, RoundedRectangle,
#     SurroundingRectangle, Rectangle, DashedVMobject, GrowArrow, ORIGIN, UP, LEFT,DARK_BLUE,
#     RIGHT, DOWN, PI, BLACK, GrowFromCenter, FadeIn, GREEN, ORANGE, RED, BLUE, YELLOW, LIGHT_PINK,
#     WHITE, GREY, ITALIC, FadeOut, Square, Transform, LaggedStart, ReplacementTransform, MAROON_B, Arc,np, CubicBezier, MathTex, AddTextLetterByLetter,
#     BOLD, Dot
# )

# class NewColumnWiseFocusAnimation(Scene):

#     def construct(self):
#         # 1. Main Title
#         main_title_obj = Text("Narrative Alignment Score - Line Based", font_size=25).move_to(ORIGIN)
#         self.play(Write(main_title_obj)); self.wait(0.5)
#         self.play(main_title_obj.animate.to_edge(UP*0.1)); self.wait(0.5)
#         main_underline_obj = Underline(main_title_obj)
#         self.play(Create(main_underline_obj)); self.wait(0.5)

#         # 2. Define Heatmap Data, Parameters, and Helper Functions
#         cosine_values = [
#             [0.51, 0.28, 0.08, 0.07, 0.09, 0.16, 0.05, 0.50, 0.73],
#             [0.20, 0.24, 0.27, 0.09, 0.18, 0.15, 0.19, 0.21, 0.21],
#             [0.12, 0.15, 0.15, 0.17, 0.12, 0.58, 0.12, 0.21, 0.17],
#             [0.61, 0.37, 0.28, 0.19, 0.14, 0.35, 0.16, 0.86, 0.66],
#             [0.30, 0.30, 0.38, 0.18, 0.10, 0.22, 0.09, 0.19, 0.30],
#             [0.51, 0.34, 0.12, 0.06, 0.12, 0.19, 0.15, 0.52, 0.53],
#             [0.26, 0.27, 0.80, 0.24, 0.20, 0.19, 0.27, 0.23, 0.22],
#             [0.49, 0.87, 0.33, 0.27, 0.23, 0.29, 0.17, 0.34, 0.38],
#             [0.94, 0.47, 0.33, 0.17, 0.14, 0.38, 0.18, 0.62, 0.77],
#         ]
#         num_rows = 9; num_cols = 9
#         heatmap_width = 5.0; heatmap_height = 5.0
#         dx_unscaled = heatmap_width / num_cols
#         dy_unscaled = heatmap_height / num_rows
#         label_box_size = 0.40; label_font_size = 11; value_font_size = 12

#         def create_heatmap_display_standalone( 
#             anchor_point, map_title_text, y_axis_label_color, x_axis_label_color,
#             value_accessor_func, green_border_coords, show_red_diagonal=True ):
#             heatmap_grid_and_content = VGroup()
#             grid_origin_ref_dot = Dot(point=anchor_point, radius=0.0001, fill_opacity=0, stroke_opacity=0)
#             heatmap_grid_and_content.add(grid_origin_ref_dot)
            
#             ht_y_axis = Line(anchor_point, anchor_point + UP * heatmap_height, stroke_color=WHITE, stroke_width=1)
#             ht_x_axis = Line(anchor_point, anchor_point + RIGHT * heatmap_width, stroke_color=WHITE, stroke_width=1)
#             heatmap_grid_and_content.add(ht_y_axis, ht_x_axis)
            
#             # Grid lines ARE NOW ADDED
#             ht_grid_lines = VGroup()
#             for r_idx in range(num_rows + 1):
#                 y_l = anchor_point[1] + r_idx * dy_unscaled
#                 ht_grid_lines.add(Line([anchor_point[0], y_l, 0], [anchor_point[0] + heatmap_width, y_l, 0], stroke_color=WHITE, stroke_width=0.5))
#             for c_idx in range(num_cols + 1):
#                 x_l = anchor_point[0] + c_idx * dx_unscaled
#                 ht_grid_lines.add(Line([x_l, anchor_point[1], 0], [x_l, anchor_point[1] + heatmap_height, 0], stroke_color=WHITE, stroke_width=0.5))
#             heatmap_grid_and_content.add(ht_grid_lines) # <<-- RESTORED

#             ht_y_labels = VGroup()
#             for i in range(num_rows):
#                 y_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=y_axis_label_color, fill_opacity=.5, stroke_width=1)
#                 y_box.move_to(anchor_point + LEFT * (label_box_size/2 + 0.1) + UP * (i + .5) * dy_unscaled)
#                 y_text = Text(str(i + 1), font_size=label_font_size, color=WHITE).move_to(y_box.get_center())
#                 ht_y_labels.add(VGroup(y_box, y_text))
#             heatmap_grid_and_content.add(ht_y_labels)
#             ht_x_labels = VGroup()
#             for j in range(num_cols):
#                 x_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=x_axis_label_color, fill_opacity=.5, stroke_width=1)
#                 x_box.move_to(anchor_point + DOWN * (label_box_size/2 + 0.1) + RIGHT * (j + .5) * dx_unscaled)
#                 x_text = Text(str(j + 1), font_size=label_font_size, color=WHITE).move_to(x_box.get_center())
#                 ht_x_labels.add(VGroup(x_box, x_text))
#             heatmap_grid_and_content.add(ht_x_labels)
#             ht_cell_content_elements = VGroup()
#             for i_vis_row in range(num_rows): 
#                 for j_vis_col in range(num_cols): 
#                     cell_center_x = anchor_point[0] + (j_vis_col + 0.5) * dx_unscaled
#                     cell_center_y = anchor_point[1] + (i_vis_row + 0.5) * dy_unscaled
#                     cell_center = [cell_center_x, cell_center_y, 0]
#                     if show_red_diagonal and i_vis_row == j_vis_col:
#                         red_rect = Rectangle(width=dx_unscaled, height=dy_unscaled, color=RED, fill_color=RED, fill_opacity=0.3, stroke_width=0).move_to(cell_center)
#                         ht_cell_content_elements.add(red_rect)
#                     # Only add green border and number if coordinates are in the (filtered) green_border_coords
#                     if (i_vis_row, j_vis_col) in green_border_coords: 
#                         val = value_accessor_func(i_vis_row, j_vis_col)
#                         num_text = Text(f"{val:.2f}", font_size=value_font_size, color=WHITE).move_to(cell_center)
#                         ht_cell_content_elements.add(num_text)
#                         green_rect = Rectangle(width=dx_unscaled, height=dy_unscaled, color=GREEN, stroke_width=2.5, fill_opacity=0).move_to(cell_center)
#                         ht_cell_content_elements.add(green_rect)
#             heatmap_grid_and_content.add(ht_cell_content_elements)
#             ht_title = Text(map_title_text, font_size=18, color=WHITE, weight="BOLD")
#             ht_title.next_to(heatmap_grid_and_content, UP, buff=0.25)
#             return VGroup(ht_title, heatmap_grid_and_content)

#         left_heatmap_green_coords_new_anim = {
#             (0,0), (1,1), (2,2), (1,3), (1,4), (6,5), (2,6), (5,7), (8,8)
#             # Add any other cells that should initially have green borders and numbers
#         }
#         def left_value_accessor_new_anim(vis_row, vis_col): return cosine_values[8 - vis_row][vis_col]

#         # Define the coordinates for which initial green border and number should be REMOVED
#         coords_to_remove_initial_highlight = { 
#             (1,0), (2,1), (0,1), (1,2), (3,2), (6,5), (4,3), (2,3), (5,4), (3,4), 
#             (6,5), (4,5), (7,6), (5,6), (8,7), (6,7), (7,8)
#         }

#         # Filter the green coordinates that will be passed to the heatmap creation function
#         filtered_green_coords_for_left_heatmap = left_heatmap_green_coords_new_anim - coords_to_remove_initial_highlight

#         # 3. Create and Fade In the "Finding Column-Wise Best Match" Heatmap
#         column_wise_heatmap = create_heatmap_display_standalone(
#             anchor_point=ORIGIN, 
#             map_title_text="Finding Column-Wise Best Match",
#             y_axis_label_color=BLUE_E, x_axis_label_color=MAROON_B,
#             value_accessor_func=left_value_accessor_new_anim,
#             green_border_coords=filtered_green_coords_for_left_heatmap, # USE THE FILTERED SET HERE
#             show_red_diagonal=True
#         )
#         column_wise_heatmap.move_to(LEFT * 2.5 + DOWN * 0.5) 
        
#         self.play(FadeIn(column_wise_heatmap, shift=UP*0.5), run_time=1.5)
#         self.wait(0.5) # Adjusted wait, as yellow highlights are removed







        
















#         # --- YELLOW HIGHLIGHTS SECTION HAS BEEN REMOVED ---

#         # 5. T-Term Arrows Animation (Only arrows, no formula text)
#         t_arrows_group_new = VGroup()

#         def create_heatmap_arrow_new_anim(
#             on_heatmap_mobject, source_vis_coords, target_vis_coords, arrow_color=WHITE
#         ):
#             grid_origin_world = on_heatmap_mobject[1][0].get_center()
#             arrow_start_x = grid_origin_world[0] + (source_vis_coords[1] + 0.5) * dx_unscaled
#             arrow_start_y = grid_origin_world[1] + (source_vis_coords[0] + 1.0) * dy_unscaled 
#             arrow_start_point = np.array([arrow_start_x, arrow_start_y, 0])
#             arrow_end_x = grid_origin_world[0] + (target_vis_coords[1] + 0.5) * dx_unscaled
#             arrow_end_y = grid_origin_world[1] + (target_vis_coords[0] + 0.0) * dy_unscaled
#             arrow_end_point = np.array([arrow_end_x, arrow_end_y, 0])
#             return Arrow(
#                 start=arrow_start_point, end=arrow_end_point, color=arrow_color, buff=0.05, 
#                 stroke_width=5, tip_length=0.2,
#                 max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=10.0 )

#         # Arrow T4: (1,3) -> (3,3) (0-indexed visual from bottom-left)
#         arrow_T4_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (1,3), (3,3))
#         t_arrows_group_new.add(arrow_T4_new)
#         self.play(Create(arrow_T4_new), run_time=1.0); self.wait(0.3)

#         # Arrow T5: (1,4) -> (4,4)
#         arrow_T5_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (1,4), (4,4))
#         t_arrows_group_new.add(arrow_T5_new)
#         self.play(Create(arrow_T5_new), run_time=1.0); self.wait(0.3)

#         # # Arrow T6 (Curved): (6,5) to (5,5)
#         # grid_origin_cw_heatmap = column_wise_heatmap[1][0].get_center()
#         # arrow_T6_source_vis_coords_new = (6, 5) 
#         # arrow_T6_target_vis_coords_new = (5, 5)
#         # start_T6_x_new = grid_origin_cw_heatmap[0] + arrow_T6_source_vis_coords_new[1] * dx_unscaled 
#         # start_T6_y_new = grid_origin_cw_heatmap[1] + (arrow_T6_source_vis_coords_new[0] + 0.5) * dy_unscaled 
#         # arrow_T6_start_point_new = np.array([start_T6_x_new, start_T6_y_new, 0]) + LEFT * dx_unscaled*0.5 
#         # end_T6_x_new = grid_origin_cw_heatmap[0] + arrow_T6_target_vis_coords_new[1] * dx_unscaled 
#         # end_T6_y_new = grid_origin_cw_heatmap[1] + (arrow_T6_target_vis_coords_new[0] + 0.5) * dy_unscaled 
#         # arrow_T6_end_point_new = np.array([end_T6_x_new, end_T6_y_new, 0]) + RIGHT * dx_unscaled*0.5 
#         # arrow_T6_curved_new = CurvedArrow(
#         #     arrow_T6_start_point_new, arrow_T6_end_point_new, 
#         #     angle=PI/4, color=WHITE, stroke_width=5, tip_length=0.2 )
#         # t_arrows_group_new.add(arrow_T6_curved_new)
#         # self.play(Create(arrow_T6_curved_new), run_time=1.0); self.wait(0.3)

#         # Arrow T7: (2,6) -> (6,6)
#         arrow_T7_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (2,6), (6,6))
#         t_arrows_group_new.add(arrow_T7_new)
#         self.play(Create(arrow_T7_new), run_time=1.0); self.wait(0.3)
        
#         # Arrow T8: (5,7) -> (7,7)
#         arrow_T8_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (5,7), (7,7))
#         t_arrows_group_new.add(arrow_T8_new)
#         self.play(Create(arrow_T8_new), run_time=1.0); self.wait(0.3)
        
#         self.wait(2.0)


















from manim import ( # type: ignore
    Scene, Text, Underline, Create, Write, Arrow, Triangle, VGroup, Line, Brace,
    BLUE_E, GREEN_E, RED_E, CurvedArrow, DEGREES, Paragraph, DrawBorderThenFill, RoundedRectangle,
    SurroundingRectangle, Rectangle, DashedVMobject, GrowArrow, ORIGIN, UP, LEFT,DARK_BLUE,
    RIGHT, DOWN, PI, BLACK, GrowFromCenter, FadeIn, GREEN, ORANGE, RED, BLUE, YELLOW, LIGHT_PINK,
    WHITE, GREY, ITALIC, FadeOut, Square, Transform, LaggedStart, ReplacementTransform, MAROON_B, Arc,np, CubicBezier, MathTex, AddTextLetterByLetter,
    BOLD, Dot, Table # Ensure Table is imported
)

class NewColumnWiseFocusAnimation(Scene):

    def construct(self):
        # 1. Main Title
        # ... (your main title code remains the same) ...
        main_title_obj = Text("Narrative Alignment Score - Line Based", font_size=25).move_to(ORIGIN)
        self.play(Write(main_title_obj)); self.wait(0.5)
        self.play(main_title_obj.animate.to_edge(UP*0.1)); self.wait(0.5)
        main_underline_obj = Underline(main_title_obj)
        self.play(Create(main_underline_obj)); self.wait(0.5)

        # 2. Define Heatmap Data, Parameters, and Helper Functions
        # ... (cosine_values, num_rows, etc. - this part of your code is fine) ...
        cosine_values = [
            [0.51, 0.28, 0.08, 0.07, 0.09, 0.16, 0.05, 0.50, 0.73],
            [0.20, 0.24, 0.27, 0.09, 0.18, 0.15, 0.19, 0.21, 0.21],
            [0.12, 0.15, 0.15, 0.17, 0.12, 0.58, 0.12, 0.21, 0.17],
            [0.61, 0.37, 0.28, 0.19, 0.14, 0.35, 0.16, 0.86, 0.66],
            [0.30, 0.30, 0.38, 0.18, 0.10, 0.22, 0.09, 0.19, 0.30],
            [0.51, 0.34, 0.12, 0.06, 0.12, 0.19, 0.15, 0.52, 0.53],
            [0.26, 0.27, 0.80, 0.24, 0.20, 0.19, 0.27, 0.23, 0.22],
            [0.49, 0.87, 0.33, 0.27, 0.23, 0.29, 0.17, 0.34, 0.38],
            [0.94, 0.47, 0.33, 0.17, 0.14, 0.38, 0.18, 0.62, 0.77],
        ]
        num_rows = 9; num_cols = 9
        heatmap_width = 5.0; heatmap_height = 5.0
        dx_unscaled = heatmap_width / num_cols
        dy_unscaled = heatmap_height / num_rows
        label_box_size = 0.40; label_font_size = 11; value_font_size = 12

        def create_heatmap_display_standalone( 
            anchor_point, map_title_text, y_axis_label_color, x_axis_label_color,
            value_accessor_func, green_border_coords, show_red_diagonal=True ):
            heatmap_grid_and_content = VGroup()
            grid_origin_ref_dot = Dot(point=anchor_point, radius=0.0001, fill_opacity=0, stroke_opacity=0)
            heatmap_grid_and_content.add(grid_origin_ref_dot)
            ht_y_axis = Line(anchor_point, anchor_point + UP * heatmap_height, stroke_color=WHITE, stroke_width=1)
            ht_x_axis = Line(anchor_point, anchor_point + RIGHT * heatmap_width, stroke_color=WHITE, stroke_width=1)
            heatmap_grid_and_content.add(ht_y_axis, ht_x_axis)
            ht_grid_lines = VGroup()
            for r_idx in range(num_rows + 1):
                y_l = anchor_point[1] + r_idx * dy_unscaled
                ht_grid_lines.add(Line([anchor_point[0], y_l, 0], [anchor_point[0] + heatmap_width, y_l, 0], stroke_color=WHITE, stroke_width=0.5))
            for c_idx in range(num_cols + 1):
                x_l = anchor_point[0] + c_idx * dx_unscaled
                ht_grid_lines.add(Line([x_l, anchor_point[1], 0], [x_l, anchor_point[1] + heatmap_height, 0], stroke_color=WHITE, stroke_width=0.5))
            heatmap_grid_and_content.add(ht_grid_lines) 
            ht_y_labels = VGroup()
            for i in range(num_rows):
                y_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=y_axis_label_color, fill_opacity=.5, stroke_width=1)
                y_box.move_to(anchor_point + LEFT * (label_box_size/2 + 0.1) + UP * (i + .5) * dy_unscaled)
                y_text = Text(str(i + 1), font_size=label_font_size, color=WHITE).move_to(y_box.get_center())
                ht_y_labels.add(VGroup(y_box, y_text))
            heatmap_grid_and_content.add(ht_y_labels)
            ht_x_labels = VGroup()
            for j in range(num_cols):
                x_box = RoundedRectangle(width=label_box_size, height=label_box_size, corner_radius=0.04, color=WHITE, fill_color=x_axis_label_color, fill_opacity=.5, stroke_width=1)
                x_box.move_to(anchor_point + DOWN * (label_box_size/2 + 0.1) + RIGHT * (j + .5) * dx_unscaled)
                x_text = Text(str(j + 1), font_size=label_font_size, color=WHITE).move_to(x_box.get_center())
                ht_x_labels.add(VGroup(x_box, x_text))
            heatmap_grid_and_content.add(ht_x_labels)
            ht_cell_content_elements = VGroup()
            for i_vis_row in range(num_rows): 
                for j_vis_col in range(num_cols): 
                    cell_center_x = anchor_point[0] + (j_vis_col + 0.5) * dx_unscaled
                    cell_center_y = anchor_point[1] + (i_vis_row + 0.5) * dy_unscaled
                    cell_center = [cell_center_x, cell_center_y, 0]
                    if show_red_diagonal and i_vis_row == j_vis_col:
                        red_rect = Rectangle(width=dx_unscaled, height=dy_unscaled, color=RED, fill_color=RED, fill_opacity=0.3, stroke_width=0).move_to(cell_center)
                        ht_cell_content_elements.add(red_rect)
                    if (i_vis_row, j_vis_col) in green_border_coords: 
                        val = value_accessor_func(i_vis_row, j_vis_col)
                        num_text = Text(f"{val:.2f}", font_size=value_font_size, color=WHITE).move_to(cell_center)
                        ht_cell_content_elements.add(num_text)
                        green_rect = Rectangle(width=dx_unscaled, height=dy_unscaled, color=GREEN, stroke_width=2.5, fill_opacity=0).move_to(cell_center)
                        ht_cell_content_elements.add(green_rect)
            heatmap_grid_and_content.add(ht_cell_content_elements)
            ht_title = Text(map_title_text, font_size=18, color=WHITE, weight="BOLD")
            ht_title.next_to(heatmap_grid_and_content, UP, buff=0.25)
            return VGroup(ht_title, heatmap_grid_and_content)

        left_heatmap_green_coords_new_anim = {
            (0,0), (1,1), (2,2), (1,3), (1,4), (6,5), (2,6), (5,7), (8,8)
        }
        def left_value_accessor_new_anim(vis_row, vis_col): return cosine_values[8 - vis_row][vis_col]

        coords_to_remove_initial_highlight = { 
            (1,0), (2,1), (0,1), (1,2), (3,2), (4,3), (2,3), (5,4), (3,4), 
            (6,5), (4,5), (7,6), (5,6), (8,7), (6,7), (7,8)
        }
        filtered_green_coords_for_left_heatmap = left_heatmap_green_coords_new_anim - coords_to_remove_initial_highlight

        column_wise_heatmap = create_heatmap_display_standalone(
            anchor_point=ORIGIN, 
            map_title_text="Finding Column-Wise Best Match",
            y_axis_label_color=BLUE_E, x_axis_label_color=MAROON_B,
            value_accessor_func=left_value_accessor_new_anim,
            green_border_coords=filtered_green_coords_for_left_heatmap,
            show_red_diagonal=True
        )
        column_wise_heatmap.move_to(LEFT * 2.5 + DOWN * 0.5) 
        
        self.play(FadeIn(column_wise_heatmap, shift=UP*0.5), run_time=1.5)
        self.wait(0.5)

        # --- BEGIN: SEGMENT DETAILS TABLE ANIMATION ---
        
        table_title_text = "Segment Details:"
        headers_str = ["Seg", "Start (x,y)", "End (x,y)", "dx", "dy", "Threshold", "LCT Thresh", "Calculable", "Method", "Length"]
        data_row_s1_str = ["S1", "(1,1)", "(2,2)", "1.00", "1.00", "1.00", "2.00", "Yes", "Standard", "1.41"]
        data_row_s2_str = ["S2", "(2,2)", "(3,3)", "1.00", "1.00", "1.00", "2.00", "Yes", "Standard", "1.41"]
        table_note_text_str = "Note: Leeway Context Threshold (LCT) = 1 is applied to extend the valid range for segment calculations."

        table_font_size = 10 # Made smaller for fitting
        header_font_size = 11 # Made smaller
        title_font_size = 14  # Made smaller
        note_font_size = 9    # Made smaller
        table_h_buff = 0.15   # Reduced horizontal buffer
        table_v_buff = 0.15   # Reduced vertical buffer

        # Create Text mobjects for headers
        header_mobjects = [Text(h, font_size=header_font_size, weight=BOLD, font="Monospace") for h in headers_str]
        
        # Create Table with only headers initially
        # Pass the list of mobject lists to the Table
        segment_table = Table(
            [header_mobjects], # Data for the table (list of rows, where each row is a list of mobjects)
            line_config={"stroke_width": 1, "color": WHITE}, 
            v_buff=table_v_buff, 
            h_buff=table_h_buff,
            # Set cell alignment for better control if needed, e.g., JuggledScene
            # For auto-sizing, we ensure mobjects themselves have appropriate widths by font/content
        )
        
        outer_box = SurroundingRectangle(segment_table, buff=0.1, stroke_width=1.5, color=WHITE)
        
        table_title_mobj = Text(table_title_text, font_size=title_font_size, weight=BOLD)
        table_title_mobj.next_to(outer_box, UP, buff=0.2) 
        
        table_note_mobj = Text(table_note_text_str, font_size=note_font_size, slant=ITALIC)
        # Note will be positioned later

        # This VGroup will hold all parts of the table display as it's built
        full_table_display_vgroup = VGroup(table_title_mobj, outer_box, segment_table) 
        
        full_table_display_vgroup.next_to(column_wise_heatmap, RIGHT, buff=0.25) # Reduced buff
        # Align top of table display (title) with top of heatmap display (title)
        if column_wise_heatmap[0] and table_title_mobj: 
             full_table_display_vgroup.align_to(column_wise_heatmap[0], UP).shift(UP * (column_wise_heatmap[0].height / 2 - table_title_mobj.height/2))

        self.play(
            Write(table_title_mobj),
            Create(outer_box),
            Create(segment_table), # Creates table with headers and its internal lines
            run_time=2.0
        )
        self.wait(0.5)

        # Store created rows and lines to manage them within full_table_display_vgroup
        animated_table_rows_and_lines = VGroup() 

        # Animate Data Row S1
        s1_text_mobjects = [Text(str(item), font_size=table_font_size, font="Monospace") for item in data_row_s1_str]
        s1_row_vgroup = VGroup(*s1_text_mobjects).arrange_in_grid(rows=1, cols=len(s1_text_mobjects), buff=table_h_buff*2, col_alignments="c") # Approximate alignment

        # Position S1 row below the header row of segment_table
        # We need to align each cell of s1_row_vgroup with the center of each header cell column
        header_row_actual_mobjects = segment_table.get_entries_without_labels()[0]
        for i, s1_cell_mob in enumerate(s1_text_mobjects):
            if i < len(header_row_actual_mobjects):
                s1_cell_mob.align_to(header_row_actual_mobjects[i], RIGHT).shift(LEFT * header_row_actual_mobjects[i].width/2) # Align centers
                s1_cell_mob.align_to(header_row_actual_mobjects[i], LEFT) # Align x-centers with header cells
        
        s1_row_vgroup.next_to(segment_table.get_rows()[-1], DOWN, buff=table_v_buff)
        # Manually adjust x-positions if arrange_in_grid is not perfect for column alignment
        for i, cell_text_s1 in enumerate(s1_text_mobjects):
            header_cell_center_x = segment_table.get_columns()[i].get_center()[0]
            cell_text_s1.move_to(np.array([header_cell_center_x, s1_row_vgroup.get_center()[1],0]))


        s1_hline = Line(
            s1_row_vgroup.get_left() + DOWN * (s1_row_vgroup.height/2 + table_v_buff/2),
            s1_row_vgroup.get_right() + DOWN * (s1_row_vgroup.height/2 + table_v_buff/2),
            stroke_width=1, color=WHITE
        )
        # More precise line start/end based on outer_box
        s1_hline.put_start_and_end_on(
            outer_box.get_bottom() + LEFT * outer_box.width/2 + UP * s1_row_vgroup.height + UP*table_v_buff, # This Y is wrong.
            outer_box.get_bottom() + RIGHT * outer_box.width/2 + UP * s1_row_vgroup.height + UP*table_v_buff # This Y is wrong.
        )
        s1_hline.move_to(s1_row_vgroup.get_center() + DOWN*(s1_row_vgroup.height/2 + table_v_buff*0.5) )
        s1_hline.set_width(outer_box.width)


        self.play(
            LaggedStart(*[Write(mobj) for mobj in s1_text_mobjects]),
            Create(s1_hline),
            run_time=2
        )
        animated_table_rows_and_lines.add(s1_row_vgroup, s1_hline)
        self.wait(0.5)

        # Animate Data Row S2 and simultaneous line on heatmap
        s2_text_mobjects = [Text(str(item), font_size=table_font_size, font="Monospace") for item in data_row_s2_str]
        s2_row_vgroup = VGroup(*s2_text_mobjects).arrange_in_grid(rows=1, cols=len(s2_text_mobjects), buff=table_h_buff*2, col_alignments="c")
        s2_row_vgroup.next_to(s1_row_vgroup, DOWN, buff=table_v_buff)
        # Manually adjust x-positions
        for i, cell_text_s2 in enumerate(s2_text_mobjects):
            header_cell_center_x = segment_table.get_columns()[i].get_center()[0]
            cell_text_s2.move_to(np.array([header_cell_center_x, s2_row_vgroup.get_center()[1],0]))

        s2_hline = Line(
            s2_row_vgroup.get_left() + DOWN * (s2_row_vgroup.height/2 + table_v_buff/2),
            s2_row_vgroup.get_right() + DOWN * (s2_row_vgroup.height/2 + table_v_buff/2),
            stroke_width=1, color=WHITE
        )
        s2_hline.move_to(s2_row_vgroup.get_center() + DOWN*(s2_row_vgroup.height/2 + table_v_buff*0.5) )
        s2_hline.set_width(outer_box.width)


        grid_origin_cw_heatmap = column_wise_heatmap[1][0].get_center()
        r_start_line, c_start_line = 1, 1 
        line_start_x = grid_origin_cw_heatmap[0] + (c_start_line + 0.5) * dx_unscaled
        line_start_y = grid_origin_cw_heatmap[1] + r_start_line * dy_unscaled 
        start_point_heatmap = np.array([line_start_x, line_start_y, 0])

        r_end_line, c_end_line = 0, 1 
        line_end_x = grid_origin_cw_heatmap[0] + (c_end_line + 0.5) * dx_unscaled
        line_end_y = grid_origin_cw_heatmap[1] + (r_end_line + 0.5) * dy_unscaled 
        end_point_heatmap = np.array([line_end_x, line_end_y, 0])

        s2_line_on_heatmap = Line(start_point_heatmap, end_point_heatmap, color=ORANGE, stroke_width=3)

        self.play(
            LaggedStart(*[Write(mobj) for mobj in s2_text_mobjects]),
            Create(s2_hline),
            Create(s2_line_on_heatmap),
            run_time=2
        )
        animated_table_rows_and_lines.add(s2_row_vgroup, s2_hline)
        self.wait(1.0)
        
        # Add all animated rows and lines to the main table display VGroup for consistent management if needed later
        full_table_display.add(animated_table_rows_and_lines)

        table_note_mobj.next_to(outer_box, DOWN, buff=0.3).align_to(outer_box, LEFT)
        self.play(Write(table_note_mobj), run_time=1.5)
        self.wait(1.0)

        # --- END: SEGMENT DETAILS TABLE ANIMATION ---

        # 5. T-Term Arrows Animation (Only arrows, no formula text)
        # ... (rest of your T-Term arrow animation code) ...
        t_arrows_group_new = VGroup()

        def create_heatmap_arrow_new_anim(
            on_heatmap_mobject, source_vis_coords, target_vis_coords, arrow_color=WHITE
        ):
            grid_origin_world = on_heatmap_mobject[1][0].get_center()
            arrow_start_x = grid_origin_world[0] + (source_vis_coords[1] + 0.5) * dx_unscaled
            arrow_start_y = grid_origin_world[1] + (source_vis_coords[0] + 1.0) * dy_unscaled 
            arrow_start_point = np.array([arrow_start_x, arrow_start_y, 0])
            arrow_end_x = grid_origin_world[0] + (target_vis_coords[1] + 0.5) * dx_unscaled
            arrow_end_y = grid_origin_world[1] + (target_vis_coords[0] + 0.0) * dy_unscaled
            arrow_end_point = np.array([arrow_end_x, arrow_end_y, 0])
            return Arrow(
                start=arrow_start_point, end=arrow_end_point, color=arrow_color, buff=0.05, 
                stroke_width=5, tip_length=0.2,
                max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=10.0 )

        arrow_T4_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (1,3), (3,3))
        t_arrows_group_new.add(arrow_T4_new)
        self.play(Create(arrow_T4_new), run_time=1.0); self.wait(0.3)

        arrow_T5_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (1,4), (4,4))
        t_arrows_group_new.add(arrow_T5_new)
        self.play(Create(arrow_T5_new), run_time=1.0); self.wait(0.3)

        grid_origin_cw_heatmap = column_wise_heatmap[1][0].get_center()
        arrow_T6_source_vis_coords_new = (6, 5) 
        arrow_T6_target_vis_coords_new = (5, 5)
        start_T6_x_new = grid_origin_cw_heatmap[0] + arrow_T6_source_vis_coords_new[1] * dx_unscaled 
        start_T6_y_new = grid_origin_cw_heatmap[1] + (arrow_T6_source_vis_coords_new[0] + 0.5) * dy_unscaled 
        arrow_T6_start_point_new = np.array([start_T6_x_new, start_T6_y_new, 0]) + LEFT * dx_unscaled*0.5 
        end_T6_x_new = grid_origin_cw_heatmap[0] + arrow_T6_target_vis_coords_new[1] * dx_unscaled 
        end_T6_y_new = grid_origin_cw_heatmap[1] + (arrow_T6_target_vis_coords_new[0] + 0.5) * dy_unscaled 
        arrow_T6_end_point_new = np.array([end_T6_x_new, end_T6_y_new, 0]) + RIGHT * dx_unscaled*0.5 
        arrow_T6_curved_new = CurvedArrow(
            arrow_T6_start_point_new, arrow_T6_end_point_new, 
            angle=PI/4, color=WHITE, stroke_width=5, tip_length=0.2 )
        t_arrows_group_new.add(arrow_T6_curved_new)
        self.play(Create(arrow_T6_curved_new), run_time=1.0); self.wait(0.3)

        arrow_T7_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (2,6), (6,6))
        t_arrows_group_new.add(arrow_T7_new)
        self.play(Create(arrow_T7_new), run_time=1.0); self.wait(0.3)
        
        arrow_T8_new = create_heatmap_arrow_new_anim(column_wise_heatmap, (5,7), (7,7))
        t_arrows_group_new.add(arrow_T8_new)
        self.play(Create(arrow_T8_new), run_time=1.0); self.wait(0.3)
        
        self.wait(2.0)