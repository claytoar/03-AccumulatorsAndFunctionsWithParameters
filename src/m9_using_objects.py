"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Abi Clayton.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    center1 = rg.Point(100, 100)
    circle1 = rg.Circle(center1, 20)
    circle1.fill_color = 'blue'
    circle1.attach_to(window)

    center2 = rg.Point(300, 200)
    circle2 = rg.Circle(center2, 40)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------

    window2 = rg.RoseWindow()

    center1 = rg.Point(100, 150)
    circle = rg.Circle(center1, 15)
    circle.fill_color = 'blue'
    circle.attach_to(window2)

    left_corner = rg.Point(275, 75)
    right_corner = rg.Point(325, 150)
    rectangle = rg.Rectangle(left_corner, right_corner)
    rectangle.attach_to(window2)
    point1 = rectangle.get_center()

    window2.render()

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(circle.center.x)
    print(circle.center.y)

    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(point1)
    print(point1.x)
    print(point1.y)

    window2.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # Done: 4. Implement and test this function.

    window3 = rg.RoseWindow()

    start = rg.Point(100, 50)
    end = rg.Point(75, 150)
    line1 = rg.Line(start, end)
    line1.attach_to(window3)

    start2 = rg.Point(250, 100)
    end2 = rg.Point(350, 200)
    line2 = rg.Line(start2, end2)
    line2.thickness = 5
    line2.attach_to(window3)
    midpoint2 = line2.get_midpoint()

    window3.render()

    print(midpoint2)
    print(midpoint2.x)
    print(midpoint2.y)

    window3.close_on_mouse_click()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
