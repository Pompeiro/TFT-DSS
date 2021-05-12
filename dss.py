# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:12:03 2021

@author: janusz
"""
import logging
import time
import tkinter as tk

import numpy as np
import pyautogui
from cv2 import cv2 as cv
from win32gui import GetForegroundWindow, GetWindowText

logging.basicConfig(level=logging.DEBUG)


LOAD_IMAGE = 0
# LOAD_IMAGE = 1
# ^ swap comment on LOAD_IMAGE to test in game
IMAGE_DEBUG_MODE = 1
IMAGE_DEBUG_MODE_FULLSCREEN = 0
X_FIRST_CHAMPION_CARD = 505
PADDING_BETWEEN_CHAMPION_CARDS = 14
W_CHAMPION_CARD = 175
CARDS_TO_BUY_AMOUNT = 5
Y_FIRST_CHAMPION_CARD = 865
H_CHAMPION_CARD = 135
LINE_TYPE = cv.LINE_4
MARKER_TYPE = cv.MARKER_CROSS
ORIGIN_LABEL_POSITION_COLUMN = 1
SHIFT_BETWEEN_ORIGINS = 6
CARDS_CENTER_LIST = [
    (592, 932),
    (781, 932),
    (970, 932),
    (1159, 932),
    (1348, 932),
]
BUY_XP_CENTER = (400, 925)
REFRESH_CENTER = (400, 995)

CROPPING_X_CHAMPIONS = 450
CROPPING_Y_CHAMPIONS = 1000
CROPPING_WIDTH_CHAMPIONS = 1000
CROPPING_HEIGHT_CHAMPIONS = 30

CROPPING_X_ROUND = 760
CROPPING_X_ROUND_FIRST = 820
CROPPING_Y_ROUND = 30
CROPPING_WIDTH_ROUND = 60
CROPPING_HEIGHT_ROUND = 40

CROPPING_X_GOLD = 820
CROPPING_Y_GOLD = 850
CROPPING_WIDTH_GOLD = 100
CROPPING_HEIGHT_GOLD = 40

screenshot = cv.imread("examples/windowed_pyauto_ss.jpg", cv.IMREAD_UNCHANGED)
crop_img = cv.imread("examples/windowed_pyauto_ss.jpg", cv.IMREAD_UNCHANGED)
ocr_results_champions = [
    ([[67, 5], [113, 5], [113, 21], [67, 21]], "Leona", 0.9666508436203003),
    ([[255, 5], [303, 5], [303, 23], [255, 23]], "Vayne", 0.995654284954071),
    ([[445, 5], [507, 5], [507, 21], [445, 21]], "Vladimir", 0.9939249753952026),
    ([[633, 5], [685, 5], [685, 21], [633, 21]], "Aatrox", 0.9471874833106995),
    ([[823, 5], [889, 5], [889, 21], [823, 21]], "Warwick", 0.9830108880996704),
]
sorted_champions_to_buy = ["Brand", "Leona", "Udyr", "Vayne", "Soraka"]

pyautogui.PAUSE = 0.02
pyautogui.FAILSAFE = False


def filling_list_with_counter_for_namedtuple(
    field_to_check,
    input_list,
    origin_list_,
    class_list_,
    origin_counters_,
    class_counters_,
    df_,
):
    """


    Parameters
    ----------
    field_to_check : {4:"origin_prim", 5:"origin_sec", 6:"class_prim",
                           7:"class_sec"}
    input_list : List with 4,5,6,7 field == field_to_check. The default is champion_info.

    Returns
    -------
    list_of_counters : List of GUI counters

    """
    logging.debug("Function filling_list_with_counter_for_namedtuple() called")
    field_to_check_2_string = {
        4: "origin_prim",
        5: "origin_sec",
        6: "class_prim",
        7: "class_sec",
    }
    field_to_check_2_check_list = {
        4: origin_list_,
        5: origin_list_,
        6: class_list_,
        7: class_list_,
    }
    field_to_check_2_check_list_string = {
        4: "origin_list",
        5: "origin_list",
        6: "class_list",
        7: "class_list",
    }
    field_to_check_2_counters_list = {
        4: origin_counters_,
        5: origin_counters_,
        6: class_counters_,
        7: class_counters_,
    }
    list_of_counters = [None] * len(df_.champion)
    for i, champ in enumerate(df_.champion):
        if input_list[i][field_to_check] == "None":
            logging.info("Champion name: %s, champion index = %d", champ, i)
            logging.info(
                "Field with index %d == 'NONE' filling None as %sCounter",
                field_to_check,
                field_to_check_2_string[field_to_check],
            )
            list_of_counters[i] = None
        else:
            logging.info("%s IS NOT 'NONE'", field_to_check_2_string[field_to_check])
            for j, class_or_origin in enumerate(
                field_to_check_2_check_list[field_to_check]
            ):
                if input_list[i][field_to_check] == class_or_origin:
                    logging.info("Champion name: %s, champion index = %d", champ, i)
                    logging.info(
                        "Found match in champion %s and %s for : %s",
                        field_to_check_2_string[field_to_check],
                        field_to_check_2_check_list_string[field_to_check],
                        class_or_origin,
                    )
                    logging.info(
                        "Filling %s counter: %s",
                        field_to_check_2_string[field_to_check],
                        field_to_check_2_counters_list[field_to_check][j],
                    )
                    list_of_counters[i] = field_to_check_2_counters_list[
                        field_to_check
                    ][j]
    logging.debug("Function filling_list_with_counter_for_namedtuple() end")
    return list_of_counters


def append_counters_to_input_list(
    input_list, origin_list_, class_list_, origin_counters_, class_counters_, df_
):
    """


    Parameters
    ----------
    input_list : Appending counters to list with fields like {4:"origin_prim",
    5:"origin_sec", 6:"class_prim", 7:"class_sec"}.

    Returns
    -------
    None.

    """

    logging.debug("Function filling_list_with_counter_for_namedtuple() called")

    counters_to_append = [4, 5, 6, 7]
    for j in counters_to_append:
        list_of_counters_to_append = filling_list_with_counter_for_namedtuple(
            j,
            input_list,
            origin_list_,
            class_list_,
            origin_counters_,
            class_counters_,
            df_,
        )
        for i, champ in enumerate(input_list):
            champ.append(list_of_counters_to_append[i])

    logging.debug("Function filling_list_with_counter_for_namedtuple() end")


def add(counter):
    """Adding one to counter"""
    logging.debug("Function add() called")

    logging.info("input = %d", counter.get())
    counter.set(counter.get() + 1)

    logging.info("after call = %d", counter.get())
    logging.debug("Function add() end")


def sub(counter):
    """Minus one to counter"""
    logging.debug("Function sub() called")

    logging.info("input = %d", counter.get())
    if counter.get() > 0:
        counter.set(counter.get() - 1)

    logging.info("after call = %d", counter.get())
    logging.debug("Function sub() end")


def imshow_fullscreen(window_name="img", image=[0]):
    """
    https://stackoverflow.com/questions/9446733/opencv-window-in-fullscreen-and-without-any-borders#comment97925305_53005272

    Parameters
    ----------
    image : openCV image matrix.
    window_name : string, name for hidden window. The default is "img".

    Returns
    -------
    None.

    """
    cv.namedWindow(window_name, cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty(window_name, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow(window_name, image)


def make_ss(
    IMAGE_DEBUG_MODE_=IMAGE_DEBUG_MODE,
    IMAGE_DEBUG_MODE_FULLSCREEN_=IMAGE_DEBUG_MODE_FULLSCREEN,
):
    """


    Parameters
    ----------
    IMAGE_DEBUG_MODE_ : 0 or 1, calls cv.imshow().
        The default is IMAGE_DEBUG_MODE.
    IMAGE_DEBUG_MODE_FULLSCREEN_ : 0 or 1, calls dss.imshow_fullscreen().
        The default is IMAGE_DEBUG_MODE_FULLSCREEN.

    Returns
    -------
    screenshot : screenshot of game.

    """
    logging.debug("Function make_ss() called")
    activate_window(mode="game", delay=0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    activate_window(mode="dss", delay=0.2)
    if IMAGE_DEBUG_MODE_:
        if not IMAGE_DEBUG_MODE_FULLSCREEN_:
            cv.imshow("make_ss() screenshot", screenshot)
        else:
            imshow_fullscreen(window_name="make_ss() screenshot", image=screenshot)
    logging.debug("Function make_ss() end")
    return screenshot


def update_curent_ss():
    """
    Updates global state current screenshot.

    Returns
    -------
    None.

    """
    global screenshot
    logging.debug("Function update_curent_ss() called")
    screenshot = make_ss(IMAGE_DEBUG_MODE_=1, IMAGE_DEBUG_MODE_FULLSCREEN_=0)
    logging.debug("Function update_curent_ss() end")


def crop_ss(
    screenshot_=screenshot,
    cropping_x=CROPPING_X_CHAMPIONS,
    cropping_y=CROPPING_Y_CHAMPIONS,
    cropping_width=CROPPING_WIDTH_CHAMPIONS,
    cropping_height=CROPPING_HEIGHT_CHAMPIONS,
    IMAGE_DEBUG_MODE_=IMAGE_DEBUG_MODE,
    IMAGE_DEBUG_MODE_FULLSCREEN_=IMAGE_DEBUG_MODE_FULLSCREEN,
):
    logging.debug("Function crop_ss() called")

    crop_img = screenshot_[
        cropping_y : cropping_y + cropping_height,
        cropping_x : cropping_x + cropping_width,
    ]
    if IMAGE_DEBUG_MODE_:
        if not IMAGE_DEBUG_MODE_FULLSCREEN_:
            cv.imshow("crop_ss() screenshot", screenshot_)
            cv.imshow("crop_ss() crop_img", crop_img)
        else:
            imshow_fullscreen(window_name="crop_ss() screenshot", image=screenshot_)
            cv.imshow("crop_ss() crop_img", crop_img)

    logging.debug("Function crop_ss() end")
    return crop_img


def update_curent_cropped_ss_with_champions():
    """
    Crops global state current screenshot.

    Returns
    -------
    None.

    """
    global crop_img
    logging.debug("Function update_curent_cropped_ss_with_champions() called")
    crop_img = crop_ss(screenshot_=screenshot)
    logging.debug("Function update_curent_cropped_ss_with_champions() end")


def ocr_on_cropped_img(cropped_ss_with_champion_card_names=None, reader_=None):
    """


    Parameters
    ----------
    cropped_ss_with_champion_card_names : for example if want to OCR card names then
    input there crop_img which can be updated by update_curent_cropped_ss_with_champions().

    Returns
    -------
    ocr_result :

    """
    logging.debug("Function ocr_on_cropped_img() called")

    ocr_result = reader_.readtext(cropped_ss_with_champion_card_names)
    logging.info("OCR results(return): %s", ocr_result)

    logging.debug("Function ocr_on_cropped_img() end")
    return ocr_result


def update_ocr_results_champions(reader_=None):
    global crop_img, ocr_results_champions
    logging.debug("Function update_ocr_results_champions() called")
    ocr_results_champions = ocr_on_cropped_img(
        cropped_ss_with_champion_card_names=crop_img, reader_=reader_
    )
    logging.debug("Function update_ocr_results_champions() end")


def sort_detected_champions_to_buy_by_position(
    ocr_results_sorted=None, champions_list_for_ocr_=None
):
    """
        Sorting input in order from left to right by placement on the screen
    (lowest width is first).Then filters out champion names, numbers(champions cost)
    are discarded.

    Parameters
    ----------
    ocr_results_sorted : Typical == ocr_results_champions which is global state.
    champions_list_for_ocr_ : Typical == champions_list_for_ocr.

    Returns
    -------
    sorted_champions_to_buy : List of champions that were found in input..

    """

    logging.debug("Function sort_detected_champions_to_buy_by_position() called")
    # sort from lowest width (left to right side)
    ocr_results_sorted = sorted(ocr_results_sorted, key=lambda x: x[0])
    sorted_champions_to_buy = []
    for text in ocr_results_sorted:
        for champ in champions_list_for_ocr_:
            if champ in text:  # filters champion names
                sorted_champions_to_buy.append(champ)
                logging.info(
                    "from for loop in sort_detected_champions_to_buy_by_position()"
                )
                logging.info("found %s", champ)
    logging.info("return in sort_detected_champions_to_buy_by_position()")
    logging.info("List of sorted champions to buy: %s", sorted_champions_to_buy)

    logging.debug("Function sort_detected_champions_to_buy_by_position() end")
    return sorted_champions_to_buy


def update_sorted_champions_to_buy(champions_list_for_ocr_=None):
    """
    Updates sorted_champions_to_buy global state.

    Parameters
    ----------
    champions_list_for_ocr_ : The default is None.

    Returns
    -------
    None.

    """
    global ocr_results_champions, sorted_champions_to_buy
    logging.debug("Function update_sorted_champions_to_buy() called")
    sorted_champions_to_buy = sort_detected_champions_to_buy_by_position(
        ocr_results_sorted=ocr_results_champions,
        champions_list_for_ocr_=champions_list_for_ocr_,
    )
    logging.debug("Function update_sorted_champions_to_buy() end")


def test(ocr_on_cropped_img, **kwargs):
    # https://stackoverflow.com/questions/6289646/python-function-as-a-function-argument
    return ocr_on_cropped_img(**kwargs)


def generate_list_of_champions_to_buy_this_turn(
    sort_detected_champions_to_buy_by_position, **kwargs
):
    list_of_champs_to_buy_this_turn = sort_detected_champions_to_buy_by_position(
        **kwargs
    )
    print(list_of_champs_to_buy_this_turn)
    return list_of_champs_to_buy_this_turn


# generate_list_of_champions_to_buy_this_turn(sort_detected_champions_to_buy_by_position, ocr_results_sorted=ocr_on_cropped_img(make_cropped_ss(LOAD_IMAGE_=1)[0], reader_=reader),champions_list_for_ocr_=champions_list_for_ocr)


def full_state_update_champions_ocr(reader_=None, champions_list_for_ocr_=None):
    """
    Updates sorted_champions_to_buy global variable.

    Parameters
    ----------
    reader_ : easyOCR reader. The default is None.
    champions_list_for_ocr_ : champions_list_for_ocr. The default is None.

    Returns
    -------
    None.

    """
    
    update_curent_ss()
    update_curent_cropped_ss_with_champions()
    update_ocr_results_champions(reader_=reader_)
    update_sorted_champions_to_buy(
        champions_list_for_ocr_=champions_list_for_ocr_
    )


def update_champions_to_buy_from_ocr_detection(
    sorted_champions_to_buy_,
    champions_list_for_ocr__,
    origin_champs_counters_to_buy_,
    reader_,
):
    """
    Add 1 to every champion to buy counter detected in ocr_result.
    champion to buy counters GLOBAL STATE CHANGE !!!!!!!!!!!!!!!!!!!!

    Returns
    -------
    None.

    """
    global sorted_champions_to_buy
    logging.debug("Function update_champions_to_buy_from_ocr_detection() called")
    full_state_update_champions_ocr(
        reader_=reader_, champions_list_for_ocr_=champions_list_for_ocr__
    )

    champs_to_buy_indexes = []
    for champ_to_buy in sorted_champions_to_buy:
        for i, champ in enumerate(champions_list_for_ocr__):
            if champ_to_buy == champ:
                logging.info(
                    "IF inside for loop in update_champions_to_buy_from_ocr_detection()"
                )
                logging.info("Index in champions_list_for_ocr that is detected: %d", i)
                logging.info("Champ name in this index: %s", champ)
                add(origin_champs_counters_to_buy_[i])
                champs_to_buy_indexes.append(i)
                break
    logging.info("Champions to buy indexes: %s", champs_to_buy_indexes)
    logging.debug("Function update_champions_to_buy_from_ocr_detection() end")
    return sorted_champions_to_buy, champs_to_buy_indexes


def calculate_card_position_on_screen(
    card_index,
    X_FIRST_CHAMPION_CARD_=X_FIRST_CHAMPION_CARD,
    PADDING_BETWEEN_CHAMPION_CARDS_=PADDING_BETWEEN_CHAMPION_CARDS,
    W_CHAMPION_CARD_=W_CHAMPION_CARD,
):
    """


    Parameters
    ----------
    card_index : simply from 0-4(first to fifth card)

    Returns
    -------
    x_card : x Position on the screen of the top left corner for card

    """
    logging.debug("Function calculate_card_position_on_screen() called")

    x_card = (
        X_FIRST_CHAMPION_CARD_
        + PADDING_BETWEEN_CHAMPION_CARDS_ * card_index
        + W_CHAMPION_CARD_ * card_index
    )
    logging.info("X coord of card with index= %d is: %s", card_index, x_card)
    logging.debug("Function calculate_card_position_on_screen() end")
    return x_card


def build_list_of_champion_cards_rectangles(
    CARDS_TO_BUY_AMOUNT_=CARDS_TO_BUY_AMOUNT,
    Y_FIRST_CHAMPION_CARD_=Y_FIRST_CHAMPION_CARD,
    W_CHAMPION_CARD_=W_CHAMPION_CARD,
    H_CHAMPION_CARD_=H_CHAMPION_CARD,
):
    """
    This function building list of card rectangles position on screen.

    Returns
    -------
    cards_rectangles : list of card rectangles position on screen

    """
    logging.debug("Function build_list_of_champion_cards_rectangles() called")

    cards_rectangles = [0] * CARDS_TO_BUY_AMOUNT_
    for i in range(0, CARDS_TO_BUY_AMOUNT_):
        x_current_champ_card = calculate_card_position_on_screen(i)
        top_left = (x_current_champ_card, Y_FIRST_CHAMPION_CARD_)
        bottom_right = (
            x_current_champ_card + W_CHAMPION_CARD_,
            Y_FIRST_CHAMPION_CARD_ + H_CHAMPION_CARD_,
        )
        center = (
            top_left[0] + W_CHAMPION_CARD_ // 2,
            top_left[1] + H_CHAMPION_CARD_ // 2,
        )
        # print("Type" ,type(center))
        cards_rectangles[i] = [top_left, bottom_right, center]
        logging.info(
            "Card rectangle = [top_left, bottom_right, center]: %s", cards_rectangles[i]
        )

    logging.debug("Function build_list_of_champion_cards_rectangles() end")
    return cards_rectangles


# https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
def draw_rectangles_show_points_show_buttons_reset_counters(
    rgb_colours_list_,
    sorted_champions_to_buy_,
    champions_list_for_ocr_,
    origin_champs_counters_to_buy_,
    reader_,
    champions_list_,
    tk_window,
    origin_champs_counters_,
    df_,
    origin_list_,
    origin_counters_,
    class_list_,
    class_counters_,
    mode="points",
    CARDS_TO_BUY_AMOUNT_=CARDS_TO_BUY_AMOUNT,
    LINE_TYPE_=LINE_TYPE,
    MARKER_TYPE_=MARKER_TYPE,
):
    """
    This function is making OCR detection on champion cards, and then draws by
    input mode like default points on screenshot.

    Parameters
    ----------
    rgb_colours_list_ : ["worst", "medium3", "medium2", "medium1", "best"]. list of RGB tuples.
    The default is rgb_colours_list.
    mode :  The default is "points". Also there are cross and rectangle.

    Returns
    -------
    None.

    """
    logging.debug(
        "Function draw_rectangles_show_points_show_buttons_reset_counters() called"
    )
    reset_counters_in_list(origin_champs_counters_to_buy_)
    (
        list_of_champs_to_buy_this_turn,
        index_list,
    ) = update_champions_to_buy_from_ocr_detection(
        sorted_champions_to_buy_=sorted_champions_to_buy_,
        champions_list_for_ocr__=champions_list_for_ocr_,
        origin_champs_counters_to_buy_=origin_champs_counters_to_buy_,
        reader_=reader_,
    )

    champions_to_buy_in_order_as_in_screen = list_of_champs_to_buy_this_turn
    champions_to_buy_points_and_position = show_nonzero_counters_with_points_from_ocr(
        tk_window,
        origin_champs_counters_,
        origin_champs_counters_to_buy_,
        champions_list_,
        df_,
        index_list,
        origin_list_,
        origin_counters_,
        class_list_,
        class_counters_,
    )

    champions_position_to_buy_ordered_by_screen = [
        champions_list_for_ocr_.index(i) for i in champions_to_buy_in_order_as_in_screen
    ]
    logging.info(
        "champions_position_to_buy_ordered_by_screen: %s",
        champions_position_to_buy_ordered_by_screen,
    )

    champions_to_buy_points = list(zip(*champions_to_buy_points_and_position))[0]
    champions_to_buy_position = list(zip(*champions_to_buy_points_and_position))[1]
    logging.info(
        "Points (in alphabetical by champ name order?): %s", champions_to_buy_points
    )
    logging.info(
        "Champions position (in alphabetical by champ name order?): %s",
        champions_to_buy_position,
    )
    sorted_champions_to_buy_points_and_position = sorted(
        champions_to_buy_points_and_position
    )
    logging.info(
        "Points and Champions position (in alphabetical by champ name order?): %s",
        sorted_champions_to_buy_points_and_position,
    )
    sorted_champions_to_buy_position = list(
        zip(*sorted_champions_to_buy_points_and_position)
    )[1]
    logging.info(
        "sorted_champions_to_buy_position in alphabetical order?: %s",
        sorted_champions_to_buy_position,
    )
    values_by_points_indexes_order_by_position_on_screen = [
        sorted_champions_to_buy_position.index(i)
        for i in champions_position_to_buy_ordered_by_screen
    ]
    logging.info(
        "values_by_points_indexes_order_by_position_on_screen 0 worst 4 best card: %s",
        values_by_points_indexes_order_by_position_on_screen,
    )
    cards_rectangles = build_list_of_champion_cards_rectangles()

    # at the end
    # values_by_points_indexes_order_by_position_on_screen contains champions
    # sorted by points from lowest(0) to highest(4)
    # and indexes represents champion placement on the screen

    if mode == "rectangle":
        for i in range(0, CARDS_TO_BUY_AMOUNT_):
            cv.rectangle(
                screenshot,
                cards_rectangles[i][0],
                cards_rectangles[i][1],
                color=rgb_colours_list_[
                    values_by_points_indexes_order_by_position_on_screen[i]
                ],
                lineType=LINE_TYPE_,
                thickness=2,
            )
        cv.imshow(
            "draw_rectangles_show_points_show_buttons_reset_counters()", screenshot
        )
    elif mode == "cross":
        for i in range(0, CARDS_TO_BUY_AMOUNT_):
            # Draw the center point
            cv.drawMarker(
                screenshot,
                cards_rectangles[i][2],
                color=rgb_colours_list_[
                    values_by_points_indexes_order_by_position_on_screen[i]
                ],
                markerType=MARKER_TYPE_,
                markerSize=40,
                thickness=2,
            )
        cv.imshow(
            "draw_rectangles_show_points_show_buttons_reset_counters()", screenshot
        )
    elif mode == "points":
        for i in range(0, CARDS_TO_BUY_AMOUNT_):
            # Draw the center point
            cv.putText(
                screenshot,
                "{:.3f}".format(
                    sorted_champions_to_buy_points_and_position[
                        values_by_points_indexes_order_by_position_on_screen[i]
                    ][0]
                ),
                cards_rectangles[i][2],
                cv.FONT_HERSHEY_SIMPLEX,
                0.6,
                rgb_colours_list_[
                    values_by_points_indexes_order_by_position_on_screen[i]
                ],
                2,
            )
        cv.imshow(
            "draw_rectangles_show_points_show_buttons_reset_counters()", screenshot
        )

    logging.debug(
        "Function draw_rectangles_show_points_show_buttons_reset_counters() end"
    )


def create_gui_counter_with_plus_minus(
    window_tk,
    origin_index,
    counter,
    shift_between_upside_downside,
    i=0,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """
    Creating counter with plus and minus buttons.

    Parameters
    ----------
    window_tk : tkinter window.
    origin_index : to organize origins in columns.
    counter : Name of counter.
    shift_between_upside_downside : Shift to place upside or downside.
    i : counter index. The default is 0 for adding single button without loop.
    SHIFT_BETWEEN_ORIGINS_ :  The default is SHIFT_BETWEEN_ORIGINS.

    Returns
    -------
    None.

    """
    tk.Entry(window_tk, textvariable=counter, width=2).grid(
        row=2 + i + shift_between_upside_downside,
        column=SHIFT_BETWEEN_ORIGINS_ * origin_index + 1,
    )
    tk.Button(window_tk, text="+", command=lambda counter=counter: add(counter),).grid(
        row=2 + i + shift_between_upside_downside,
        column=SHIFT_BETWEEN_ORIGINS_ * origin_index + 2,
    )
    tk.Button(window_tk, text="-", command=lambda counter=counter: sub(counter),).grid(
        row=2 + i + shift_between_upside_downside,
        column=SHIFT_BETWEEN_ORIGINS_ * origin_index + 3,
    )


def show_champions_from_origin(
    window_tk,
    origin_index,
    origin_champs_from_df_list_,
    origin_list_,
    champions_list_,
    shift_between_upside_downside,
    ORIGIN_LABEL_POSITION_COLUMN_=ORIGIN_LABEL_POSITION_COLUMN,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """Adding buttons and text labels for single origin.
    In: origin_index - its used to pickup origin from origin_list_,
    and place text on the window.
    origin_champs_from_df_list_  - list of champions in origin.
    champions_list_ - list of champions namedtuples.
    shift_between_upside_downside - placing on the window, UPSIDE is upper location,
    DOWNSIDE is lower location.

    """
    logging.debug("Function show_champions_from_origin() called")

    tk.Label(window_tk, text=origin_list_[origin_index]).grid(
        row=1 + shift_between_upside_downside,
        column=ORIGIN_LABEL_POSITION_COLUMN_ * SHIFT_BETWEEN_ORIGINS_ * origin_index,
    )

    for i, champ_name in enumerate(origin_champs_from_df_list_):
        tk.Label(window_tk, text=champ_name).grid(
            row=2 + i + shift_between_upside_downside,
            column=ORIGIN_LABEL_POSITION_COLUMN_
            * SHIFT_BETWEEN_ORIGINS_
            * origin_index,
        )
        for champ in champions_list_:
            if champ.name == champ_name:
                create_gui_counter_with_plus_minus(
                    window_tk=window_tk,
                    origin_index=origin_index,
                    counter=champ.ChampCounter,
                    shift_between_upside_downside=shift_between_upside_downside,
                    i=i,
                    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
                )
                break
    logging.debug("Function show_champions_from_origin() end")


def show_classes_or_origins(
    window_tk,
    origin_or_class_list,
    origin_or_class_counters_list,
    shift_between_upside_downside,
    origin_or_class_string,
    ORIGIN_LABEL_POSITION_COLUMN_=ORIGIN_LABEL_POSITION_COLUMN,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """Adding buttons and text labels for single origin.
    In: column_pos - its used to pickup origin from origin_list,
    and place text on the window.
    origin_or_class_list  - list of origin or class names.
    origin_or_class_counters_list - list counters for origin or class.
    shift_between_upside_downside - placing on the window, UPSIDE is upper location,
    DOWNSIDE is lower location.
    origin_or_class_string - Title above counters
    """
    logging.debug("Function show_classes_or_origins() called")
    column_pos = len(origin_or_class_list)
    tk.Label(window_tk, text=origin_or_class_string).grid(
        row=1 + shift_between_upside_downside,
        column=ORIGIN_LABEL_POSITION_COLUMN_ * SHIFT_BETWEEN_ORIGINS_ * column_pos,
    )

    for i, champ in enumerate(origin_or_class_list):
        tk.Label(window_tk, text=champ).grid(
            row=2 + i + shift_between_upside_downside,
            column=ORIGIN_LABEL_POSITION_COLUMN_ * SHIFT_BETWEEN_ORIGINS_ * column_pos,
        )

        create_gui_counter_with_plus_minus(
            window_tk=window_tk,
            origin_index=column_pos,
            counter=origin_or_class_counters_list[i],
            shift_between_upside_downside=shift_between_upside_downside,
            i=i,
            SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
        )
    logging.debug("Function show_classes_or_origins() end")


def reset_counters_in_list(origin_champs_counters_to_buy_):
    """Reset counters to 0, used when roll or new round starts.
    In: list1d by default its origin_champs_counters_to_buy."""
    logging.debug("Function reset_counters_in_list() called")

    for champ_counter in origin_champs_counters_to_buy_:
        champ_counter.set(0)

    delete_all_buttons()

    logging.debug("Function reset_counters_in_list() end")


def check_nonzero_counters(origin_champs_counters_to_buy_, champions_list_):
    """Check how much champion counters are nonzero.
    IF ladder to append repetitions to list.
    In: list1d by default its origin_champs_counters_to_buy.
    Out: position of counters in champions list that are nonzero"""
    logging.debug("Function check_nonzero_counters() called")

    nonzero_counters_list = []
    nonzero_counters_number_list = []
    for i, champ_counter in enumerate(origin_champs_counters_to_buy_):
        if champ_counter.get() >= 1:
            nonzero_counters_list.append(champ_counter)
            nonzero_counters_number_list.append(i)
            if champ_counter.get() >= 2:
                nonzero_counters_list.append(champ_counter)
                nonzero_counters_number_list.append(i)
                if champ_counter.get() >= 3:
                    nonzero_counters_list.append(champ_counter)
                    nonzero_counters_number_list.append(i)
                    if champ_counter.get() >= 4:
                        nonzero_counters_list.append(champ_counter)
                        nonzero_counters_number_list.append(i)
    logging.info("Nonzero counters list human readable: ")
    for champ_index in nonzero_counters_number_list:
        logging.info("%s", champions_list_[champ_index].name)
    logging.info("Nonzero counters indexes(return): %s", nonzero_counters_number_list)
    logging.info("This is nonzero Counter list: %s", nonzero_counters_list)

    logging.debug("Function check_nonzero_counters() end")
    return nonzero_counters_number_list


def show_nonzero_counters(
    tk_window,
    origin_champs_counters_,
    origin_champs_counters_to_buy_,
    champions_list_,
    df_,
    row_offset=0,
    CARDS_TO_BUY_AMOUNT_=CARDS_TO_BUY_AMOUNT,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """It shows up champions to buy that counters are nonzero, as a button.
    Created button will add one to champion pool counter, delete itself from window
    and sub one from counters champions that can be bought.
    In: row_offset by default = 0 for buttons row placement."""
    logging.debug("Function show_nonzero_counters() called")

    global button_calc_list
    button_calc_list = [0] * CARDS_TO_BUY_AMOUNT_
    champion_position_in_list_ordered_by_origin = check_nonzero_counters(
        origin_champs_counters_to_buy_, champions_list_
    )
    for i in range(0, len(champion_position_in_list_ordered_by_origin), 1):
        button_calc_list[i] = tk.Button(
            tk_window,
            text=(df_.champion[champion_position_in_list_ordered_by_origin[i]]),
            command=lambda i=i: [
                add(
                    origin_champs_counters_[
                        champion_position_in_list_ordered_by_origin[i]
                    ]
                ),
                delete_button(i),
                sub(
                    origin_champs_counters_to_buy_[
                        champion_position_in_list_ordered_by_origin[i]
                    ]
                ),
            ],
        )
        button_calc_list[i].grid(
            row=12 + row_offset, column=SHIFT_BETWEEN_ORIGINS_ * (i + 1)
        )

    logging.debug("Function show_nonzero_counters() end")


def activate_window(mode, delay=0.02):
    """


    Parameters
    ----------
    mode : "client" or "game"
    delay : Delay between actions. The default is 0.5.

    Returns
    -------
    None.

    """

    logging.debug("Function activate_window() called with passed: %s.", mode)
    logging.info("Current active window: %s", GetWindowText(GetForegroundWindow()))
    try:
        if mode == "client":
            window = pyautogui.getWindowsWithTitle("League of Legends")[0]
            window_text = "League of Legends"
        elif mode == "game":
            window = pyautogui.getWindowsWithTitle("League of Legends (TM) Client")[0]
            window_text = "League of Legends (TM) Client"
        elif mode == "dss":
            window = pyautogui.getWindowsWithTitle("TFTDSS")[0]
            window_text = "TFTDSS"
        if GetWindowText(GetForegroundWindow()) != window_text:
            logging.info("active window != desired window, window activation goes on")
            window.minimize()
            time.sleep(delay)
            window.restore()
            window.activate()
            time.sleep(delay)
    except IndexError:
        logging.error("Couldnt find window in mode: %s.", mode)
        raise

    logging.info("Current active window: %s", GetWindowText(GetForegroundWindow()))

    logging.debug("Function activate_window end.")


def buy_champ(location_index, CARDS_CENTER_LIST_=CARDS_CENTER_LIST):
    start = pyautogui.position()
    activate_window("game")
    pyautogui.moveTo(CARDS_CENTER_LIST_[location_index])
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    activate_window("dss")
    pyautogui.moveTo(start)


def refresh(REFRESH_CENTER_=REFRESH_CENTER):
    start = pyautogui.position()
    activate_window("game")
    pyautogui.moveTo(REFRESH_CENTER_)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    activate_window("dss")
    pyautogui.moveTo(start)
    time.sleep(0.1)


def buy_xp(BUY_XP_CENTER_=BUY_XP_CENTER):
    start = pyautogui.position()
    activate_window("game")
    pyautogui.moveTo(BUY_XP_CENTER)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    activate_window("dss")
    pyautogui.moveTo(start)


def show_nonzero_counters_from_ocr(
    tk_window,
    origin_champs_counters_,
    origin_champs_counters_to_buy_,
    champions_list_,
    df_,
    index_list,
    row_offset=0,
    CARDS_TO_BUY_AMOUNT_=CARDS_TO_BUY_AMOUNT,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """It shows up champions to buy that counters are nonzero, as a button.
    Created button will add one to champion pool counter, delete itself from window
    and sub one from counters champions that can be bought.
    In: row_offset by default = 0 for buttons row placement."""
    logging.debug("Function show_nonzero_counters_from_ocr() called")

    global button_calc_list
    button_calc_list = [0] * CARDS_TO_BUY_AMOUNT_
    champion_position_in_list_ordered_by_origin = index_list
    for i in range(0, len(champion_position_in_list_ordered_by_origin), 1):
        button_calc_list[i] = tk.Button(
            tk_window,
            text=(df_.champion[champion_position_in_list_ordered_by_origin[i]]),
            command=lambda i=i: [
                add(
                    origin_champs_counters_[
                        champion_position_in_list_ordered_by_origin[i]
                    ]
                ),
                delete_button(i),
                sub(
                    origin_champs_counters_to_buy_[
                        champion_position_in_list_ordered_by_origin[i]
                    ]
                ),
                buy_champ(i),
            ],
        )
        button_calc_list[i].grid(
            row=12 + row_offset, column=SHIFT_BETWEEN_ORIGINS_ * (i + 1)
        )

    logging.debug("Function show_nonzero_counters_from_ocr() end")


def show_points_for_nonzero_counters(
    tk_window,
    origin_champs_counters_to_buy_,
    champions_list_,
    df_,
    row_offset=2,
    show_mode=1,
    CARDS_TO_BUY_AMOUNT_=CARDS_TO_BUY_AMOUNT,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """It shows up champions POINTS to buy that counters are nonzero, as a text.
    Doesnt disappear currently, should be fixed.
    In: row_offset by default = 0 for buttons row placement."""
    logging.debug("Function show_points_for_nonzero_counters() called")

    global text_label_list
    points_for_champion_to_buy = [0] * CARDS_TO_BUY_AMOUNT_
    text_label_list = [0] * CARDS_TO_BUY_AMOUNT_
    champion_position_in_list_ordered_by_origin = check_nonzero_counters(
        origin_champs_counters_to_buy_, champions_list_
    )
    for i in range(0, len(champion_position_in_list_ordered_by_origin), 1):
        points_for_champion_to_buy[i] = (
            df_.points[champion_position_in_list_ordered_by_origin[i]]
            + additional_points_from_origin_combo(
                champion_position_in_list_ordered_by_origin[i], champions_list_
            )
            + additional_points_from_class_combo(
                champion_position_in_list_ordered_by_origin[i], champions_list_
            )
            + additional_points_from_champions_in_pool(
                champion_position_in_list_ordered_by_origin[i], champions_list_
            )
        )
        points_for_champion_to_buy[i] = round(points_for_champion_to_buy[i], 3)
        if show_mode:
            text_label_list[i] = tk.Label(tk_window, text=points_for_champion_to_buy[i])
            text_label_list[i].grid(
                row=12 + row_offset, column=SHIFT_BETWEEN_ORIGINS_ * (i + 1)
            )
    logging.info(
        "Points and champion_position_in_list_ordered_by_origin: %s",
        list(
            zip(
                points_for_champion_to_buy,
                champion_position_in_list_ordered_by_origin,
            )
        ),
    )
    human_readable_champions = []
    logging.info("Should be empty list: %s", human_readable_champions)
    for champ_index in champion_position_in_list_ordered_by_origin:
        human_readable_champions.append(champions_list_[champ_index].name)
    logging.info(
        "Should be filled with nonzero champions to buy: %s", human_readable_champions
    )

    logging.info(
        "Champions availbable to buy with calculated points list readable: %s",
        list(zip(points_for_champion_to_buy, human_readable_champions)),
    )

    logging.debug("Function show_points_for_nonzero_counters() end")
    return list(
        zip(points_for_champion_to_buy, champion_position_in_list_ordered_by_origin)
    )


def show_points_for_nonzero_counters_from_ocr(
    tk_window,
    origin_champs_counters_to_buy_,
    champions_list_,
    df_,
    index_list,
    row_offset=2,
    show_mode=1,
    CARDS_TO_BUY_AMOUNT_=CARDS_TO_BUY_AMOUNT,
    SHIFT_BETWEEN_ORIGINS_=SHIFT_BETWEEN_ORIGINS,
):
    """It shows up champions POINTS to buy that counters are nonzero, as a text.
    Doesnt disappear currently, should be fixed.
    In: row_offset by default = 0 for buttons row placement."""
    logging.debug("Function show_points_for_nonzero_counters_from_ocr() called")

    global text_label_list
    points_for_champion_to_buy = [0] * CARDS_TO_BUY_AMOUNT_
    text_label_list = [0] * CARDS_TO_BUY_AMOUNT_
    champion_position_in_list_ordered_by_origin = index_list
    for i in range(0, len(champion_position_in_list_ordered_by_origin), 1):
        points_for_champion_to_buy[i] = (
            df_.points[champion_position_in_list_ordered_by_origin[i]]
            + additional_points_from_origin_combo(
                champion_position_in_list_ordered_by_origin[i], champions_list_
            )
            + additional_points_from_class_combo(
                champion_position_in_list_ordered_by_origin[i], champions_list_
            )
            + additional_points_from_champions_in_pool(
                champion_position_in_list_ordered_by_origin[i], champions_list_
            )
        )
        points_for_champion_to_buy[i] = round(points_for_champion_to_buy[i], 3)
        if show_mode:
            text_label_list[i] = tk.Label(tk_window, text=points_for_champion_to_buy[i])
            text_label_list[i].grid(
                row=12 + row_offset, column=SHIFT_BETWEEN_ORIGINS_ * (i + 1)
            )
    logging.info(
        "Points and champion_position_in_list_ordered_by_origin: %s",
        list(
            zip(
                points_for_champion_to_buy,
                champion_position_in_list_ordered_by_origin,
            )
        ),
    )
    human_readable_champions = []
    logging.info("Should be empty list: %s", human_readable_champions)
    for champ_index in champion_position_in_list_ordered_by_origin:
        human_readable_champions.append(champions_list_[champ_index].name)
    logging.info(
        "Should be filled with nonzero champions to buy: %s", human_readable_champions
    )

    logging.info(
        "Champions availbable to buy with calculated points list readable: %s",
        list(zip(points_for_champion_to_buy, human_readable_champions)),
    )

    logging.debug("Function show_points_for_nonzero_counters_from_ocr() end")
    return list(
        zip(points_for_champion_to_buy, champion_position_in_list_ordered_by_origin)
    )


def show_nonzero_counters_with_points(
    tk_window,
    origin_champs_counters_,
    origin_champs_counters_to_buy_,
    champions_list_,
    df_,
    origin_list_,
    origin_counters_,
    class_list_,
    class_counters_,
):
    """First updates classes and origins to get points updated, then shows
    champions to buy as a buttons and their points as a text.
    In: row_offset_buttons by default 0 for buttons.
    row_offset_points by default 2 for points as a text."""
    logging.debug("Function show_nonzero_counters_with_points() called")

    update_classes_and_origins(
        origin_list_, champions_list_, origin_counters_, class_list_, class_counters_
    )
    show_nonzero_counters(
        tk_window,
        origin_champs_counters_,
        origin_champs_counters_to_buy_,
        champions_list_,
        df_,
    )
    points_with_position_zip = show_points_for_nonzero_counters(
        tk_window, origin_champs_counters_to_buy_, champions_list_, df_
    )

    logging.debug("Function show_nonzero_counters_with_points() end")
    return points_with_position_zip


def show_nonzero_counters_with_points_from_ocr(
    tk_window,
    origin_champs_counters_,
    origin_champs_counters_to_buy_,
    champions_list_,
    df_,
    index_list,
    origin_list_,
    origin_counters_,
    class_list_,
    class_counters_,
):
    """First updates classes and origins to get points updated, then shows
    champions to buy as a buttons and their points as a text.
    In: row_offset_buttons by default 0 for buttons.
    row_offset_points by default 2 for points as a text."""
    logging.debug("Function show_nonzero_counters_with_points_from_ocr() called")

    update_classes_and_origins(
        origin_list_, champions_list_, origin_counters_, class_list_, class_counters_
    )
    show_nonzero_counters_from_ocr(
        tk_window,
        origin_champs_counters_,
        origin_champs_counters_to_buy_,
        champions_list_,
        df_,
        index_list,
    )
    points_with_position_zip = show_points_for_nonzero_counters_from_ocr(
        tk_window,
        origin_champs_counters_to_buy_,
        champions_list_,
        df_,
        index_list,
    )

    logging.debug("Function show_nonzero_counters_with_points_from_ocr() end")
    return points_with_position_zip


def update_origins(origin_list_, champions_list_, origin_counters_):
    """Checks nonzero counters for champions in pool and updates origins by
    setting origin counters."""
    logging.debug("Function update_origins() called")

    origin_counters_value_list = [0] * len(origin_list_)
    for i, origin_ in enumerate(origin_list_):  # looping over counters for every origin
        logging.info("Current origin: %s", origin_)
        for (
            champ
        ) in (
            champions_list_
        ):  # for loop to assign how much champions are nonzero in origin
            if champ.ChampCounter.get() >= 1:
                logging.info("Current champ with counter >=1: %s", champ.name)
                if origin_ in (champ.origin_prim, champ.origin_sec):
                    logging.info(
                        "Current champ with counter >=1 match origin Prim or Sec \
                                 : %s or %s",
                        champ.origin_prim,
                        champ.origin_sec,
                    )
                    origin_counters_value_list[i] = origin_counters_value_list[i] + 1
        logging.info(
            "Number of nonzero champions in this origin: %s",
            origin_counters_value_list[i],
        )
        origin_counters_[i].set(origin_counters_value_list[i])

    logging.debug("Function update_origins() end")


def update_classes(class_list_, champions_list_, class_counters_):
    """Checks nonzero counters for champions in pool and updates classes by
    setting class counters."""
    logging.debug("Function update_classes() called")

    class_counters_value_list = [0] * len(class_list_)
    for i, class_ in enumerate(class_list_):  # looping over counters for every class
        logging.info("Current class: %s", class_)
        for (
            champ
        ) in (
            champions_list_
        ):  # for loop to assign how much champions are nonzero in class
            if champ.ChampCounter.get() >= 1:
                logging.info("Current champ with counter >=1: %s", champ.name)
                if class_ in (champ.class_prim, champ.class_sec):
                    logging.info(
                        "Current champ with counter >=1 match class Prim or Sec \
                                 : %s or %s",
                        champ.class_prim,
                        champ.class_sec,
                    )
                    class_counters_value_list[i] = class_counters_value_list[i] + 1
        logging.info(
            "Number of nonzero champions in this class = %s",
            class_counters_value_list[i],
        )
        class_counters_[i].set(class_counters_value_list[i])

    logging.debug("Function update_classes() end")


def update_classes_and_origins(
    origin_list_, champions_list_, origin_counters_, class_list_, class_counters_
):
    """Checks nonzero counters for champions in pool and updates classes and origins."""
    logging.debug("Function update_classes_and_origins() called")

    update_origins(origin_list_, champions_list_, origin_counters_)
    update_classes(class_list_, champions_list_, class_counters_)

    logging.debug("Function update_classes_and_origins() end")


def additional_points_from_origin_combo(champion_position, champions_list_):
    """Part of sum points, bonus from origin for specific champion.
    In: champion_position its just position of champion in list by primal
    champions to buy list.
    Out: Bonus points from origin."""
    logging.debug("Function additional_points_from_origin_combo() called")

    logging.info(
        "Calculating origin points for champ named: %s",
        champions_list_[champion_position].name,
    )
    bonus_points_from_origin = 0.2
    total_count = champions_list_[champion_position].OriginPrimCounter.get()
    logging.info("Origin primary counter = %d", total_count)
    if champions_list_[champion_position].origin_sec != "None":
        total_count = (
            champions_list_[champion_position].OriginSecCounter.get() + total_count
        )
        logging.info("Origin primary + secondary counter = %f", total_count)

    origin_bonus = total_count * bonus_points_from_origin
    logging.info("Bonus(return) = %f", origin_bonus)
    logging.debug("Function additional_points_from_origin_combo() end")
    return origin_bonus


def additional_points_from_class_combo(champion_position, champions_list_):
    """Part of sum points, bonus from class for specific champion.
    In: champion_position its just position of champion in list by primal
    champions to buy list.
    Out: Bonus points from class."""
    logging.debug("Function additional_points_from_class_combo() called")

    logging.info(
        "Calculating class points for champ named: %s ",
        champions_list_[champion_position].name,
    )
    bonus_points_from_class = 0.2
    total_count = champions_list_[champion_position].ClassPrimCounter.get()
    if champions_list_[champion_position].class_sec != "None":
        total_count = (
            champions_list_[champion_position].ClassSecCounter.get() + total_count
        )
        logging.info("Class primary + secondary counter = %f", total_count)

    class_bonus = total_count * bonus_points_from_class
    logging.info("Bonus(return) = %f", class_bonus)
    logging.debug("Function additional_points_from_class_combo() end")
    return class_bonus


def additional_points_from_champions_in_pool(champion_position, champions_list_):
    """Part of sum points, bonus from champion in pool.
    In: champion_position its just position of champion in list by primal
    champions to buy list.
    Out: Bonus points from champions that are already in pool."""
    logging.debug("Function additional_points_from_champions_in_pool() called")

    champion_pool_bonus = (
        champions_list_[champion_position].ChampCounter.get() - 1
    ) * 0.2
    logging.info(
        "champion_pool_bonus = %f for champ named: %s ",
        champion_pool_bonus,
        champions_list_[champion_position].name,
    )

    logging.debug("Function additional_points_from_champions_in_pool() end")
    return champion_pool_bonus


def delete_button(position):
    """Deleting buttons"""
    logging.debug("Function delete_button() called")

    button_calc_list[position].destroy()

    logging.debug("Function delete_button() end")


def delete_all_buttons():
    """
    Deleting all buttons.

    Returns
    -------
    None.

    """
    logging.debug("Function delete_all_buttons() called")
    try:
        for button in button_calc_list:
            if button != 0:
                button.destroy()
    except NameError:
        print("There are no buttons to destroy.")

    logging.debug("Function delete_all_buttons() end")
