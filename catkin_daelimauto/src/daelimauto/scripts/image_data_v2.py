import cv2
import math
import numpy as np

# # ignore this function
# def nothing(x):
#     pass
# #====================

# Crop the image method
def region_of_interest(img, roi):
    vertices = np.array([roi], np.int32)
    mask = np.zeros_like(img)

    #channel_count = img.shape[2]
    #match_mask_color = (255,) * channel_count

    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
   

    # cv2.imshow('masking result', mask)

    # cv2.waitKey(1)

    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


# Using Canny find Edges method
def find_edges(img, h_min = 0, h_max = 0, s_min = 0, s_max = 0, v_min = 0, v_max = 0):
    height = img.shape[0]
    width = img.shape[1]

    # Setting ROI value
    # When you want to Change Detect Reach,
    # Change the below value
    roi = [
        (0, int(height*0.9)),
        (0, int(height*0.6)),
        (width, int(height*0.6)),
        (width, int(height*0.9))
    ]

    # Blur
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Change image channel to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_val = (h_min, s_min, v_min)
    high_val = (h_max, s_max, v_max)

    # cv2.imshow('hsv result', hsv)

    # cv2.waitKey(1)

    # Threshold
    mask = cv2.inRange(hsv, low_val, high_val)

    # cv2.imshow('masking result', mask)

    # cv2.waitKey(1)

    # Crop the image
    mask = region_of_interest(mask, roi)

    # cv2.imshow('masking roi result', mask)

    # cv2.waitKey(1)

    # find edges
    edges = cv2.Canny(mask, 75, 150)

    # cv2.imshow('edge result', edges)

    # cv2.waitKey(1)

    return edges


# after Canny & Hough Transform, find a line
def find_lines(image, lines):
    width = image.shape[1]

    # init list
    lane_lines = []

    left_fit = []
    right_fit = []

    # When you want to
    boundary = 2 / float(3)
    left_region_boundary = width * (1 - float(boundary))
    right_region_boundary = width * float(boundary)

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            # find a linear function
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope = fit[0]
            intercept = fit[1]

            if slope < 0:
                if x1 < left_region_boundary and x2 < left_region_boundary:
                    left_fit.append((slope, intercept))
            else:
                if x1 > right_region_boundary and x2 > right_region_boundary:
                    right_fit.append((slope, intercept))

    if len(left_fit) > 0:
        left_fir_average = np.average(left_fit, axis=0)
        lane_lines.append(make_points(image, left_fir_average))
    if len(right_fit) > 0:
        right_fit_average = np.average(right_fit, axis=0)
        lane_lines.append(make_points(image, right_fit_average))

    return lane_lines


def make_points(frame, line):
    height, width, _ = frame.shape
    slope, intercept = line
    y1 = height  # bottom of the frame
    y2 = int(y1 / float(2))  # make points from middle of the frame down

    # bound the coordinates within the frame
    if slope == 0: # for prevent inf value like => | n / 0 == inf |
        slope = 1
    x1 = max(-width, min(2 * width, int((y1 - intercept) / float(slope))))
    x2 = max(-width, min(2 * width, int((y2 - intercept) / float(slope))))

    return [[x1, y1, x2, y2]]


# Using Point before We calculated, Draw a line
def draw_line(image, lane_lines, current_theta):
    height = image.shape[0]
    width = image.shape[1]

    # When you want to change line length,
    # Change below base_y value
    # base_y, y1, y2 is a height
    if len(lane_lines) == 2:
        _, _, left_x2, _ = lane_lines[0][0]
        _, _, right_x2, _ = lane_lines[1][0]
        mid = int(width / float(2))

        base_x = int(left_x2 + right_x2) / 2 - float(mid)
        base_y = int(height / float(2))
        image, current_theta = display_base_line(image, current_theta, 2, base_x, base_y)
    elif len(lane_lines) == 1:
        x1, _, x2, _ = lane_lines[0][0]

        base_x = x2 - x1
        base_y = int(height / float(2))
        image, current_theta = display_base_line(image, current_theta, 1, base_x, base_y)
    else:
        base_x = width / float(2)
        base_y = int(height / float(2))
        image, current_theta = display_base_line(image, 0, 0, base_x, base_y)

    for line in lane_lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 7)

    return image, current_theta


# This method output is Degree Not radian
def display_base_line(image, current_theta, line_num, base_x, base_y):
    height = image.shape[0]
    width = image.shape[1]

    # angle_to_mid_deg is this method output
    angle_to_mid_radian = math.atan(base_x / float(base_y))

    # calculating degree about base_x & base_y
    angle_to_mid_deg = int(angle_to_mid_radian * 180 / float(3.14))
    angle_to_mid_deg = stabilize_angle(current_theta, angle_to_mid_deg, number_of_line=line_num)

    # the reason why i add 90 degree it is because of draw a middle(or center) line
    # We want how curved the road angle is in the center
    theta = angle_to_mid_deg + 90

    steering_angle_radian = theta / float(180) * float(3.14)

    x1 = int(width / float(2))
    y1 = height

    # prevent inf output
    if steering_angle_radian == 0:
        x2 = int(width / float(2))
    else:
        x2 = int(x1 - height * 2 / 3 / float(math.tan(steering_angle_radian)))

    y2 = int(height / float(2))

    result = np.zeros_like(image)
    cv2.line(result, (x1, y1), (x2, y2), (0, 255, 255), 4)
    result = cv2.addWeighted(image, 0.8, result, 1, 1)

    return result, angle_to_mid_deg


# Stablize for Car motor(or steering Damage)
def stabilize_angle(curr_theta, new_theta, number_of_line, max_twoLine_angle_offset=5, max_signleLine_angle_offset=5):
    if number_of_line == 2:
        max_angle_offset = max_twoLine_angle_offset
    elif number_of_line == 1:
        max_angle_offset = max_signleLine_angle_offset
    else: # no line detected go straight
        return 0

    angle_offset = new_theta - curr_theta

    if abs(angle_offset) > max_angle_offset:
        fixed_angle = int(curr_theta + float(max_angle_offset) * float(angle_offset) / abs(float(angle_offset)))
    else:
        fixed_angle = curr_theta

    if fixed_angle > 20:
        fixed_angle = 20
    elif fixed_angle < -20:
        fixed_angle = -20

    return fixed_angle


#  main method
#  please change the h,s,v value if you want custom
#  this module focus on black line(for test)
def line_detect(image, current_theta=0, h_min=0, h_max=30, s_min=0, s_max=30, v_min=195, v_max=215):
    height = image.shape[0]
    width = image.shape[1]

    # find edges
    edges = find_edges(image, h_min, h_max, s_min, s_max, v_min, v_max)
    #cv2.imshow('Canny', edges)

    #get the line and Coordinates
    lines = cv2.HoughLinesP(edges, 1, float(3.14)/float(180), 20, maxLineGap=50)
    # lines = cv2.HoughLines(edges, 1, float(3.14)/float(180), 100)


    if lines is not None:
        lane_lines = find_lines(image, lines=lines)
        if lane_lines is not None:
            image, current_theta = draw_line(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), current_theta=current_theta, lane_lines=lane_lines)

    if current_theta > 0:
        direction = 'Right'
    elif current_theta < 0:
        direction = 'Left'
    else:
        direction = 'Straight'
    image = cv2.putText(image, direction + ' ' + str(current_theta),
                        (int(height-200), int(width/float(2))),
                        cv2.FONT_HERSHEY_PLAIN,
                        3, (255,255,0))

    # Finally main method return a result Image & angle
    return image, current_theta, direction



def line_detection(image):
    
    current_theta = 0

    timer_to_sending_data = 0
  
        
    frame = cv2.resize(image, dsize=(1280, 720)) # 1280 720

 

    img, current_theta, direction = line_detect(frame)
    cv2.imshow('result', img)
    cv2.waitKey(1)
    # sending time calculating
    # if waitKey parameter is 50
    # then sending time is 50 * 20 = 1000ms
    # so if you want to change sending time
    # change bellow 'if' logic or change waitkey parameter
    # Recommend is change if logic
    if timer_to_sending_data%1 == 0:
        # if you want radian value
        # disable down comment and use it
        #steering_angle_radian = current_theta / float(180) * float(3.14)
        timer_to_sending_data = 0

    return current_theta


