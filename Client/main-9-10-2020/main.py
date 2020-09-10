# CREATE Necessary Libraries and initialization variables
import sys
import os
import kivy
from kivy.app import App
from kivy.lang import Builder
from python_scripts import Accountview
from python_scripts import Alltime
from python_scripts import Calendarview
from python_scripts import Dropdown
from python_scripts import Sevenday
from python_scripts import Tasksgrid
from python_scripts import Todaylist

# MAIN
#   CREATE MainGrid (3 Cols and 1 Row) (main.kv)
#     CREATE MenuGrid (Within MainGrid, will be on left side of screen, consists of a scrollable widget and another grid layout) (main.kv) (main.py)
#       CREATE AccountViewWidget (Consists of AccountManagementWidget(will be a custom widget)) (accountview.kv) (Accountview.py)
#       CREATE DropDownGrid (2 drop down menus for quick access to other widgets) (dropdown.kv) (Dropdown.py)
#         CREATE DropDown1Grid (A drop down widget with however many rows as calendars that have been imported) (dropdown.kv) (Dropdown.py)
#         CREATE DropDown2Grid (A drop down widget with 3 rows and 1 column to allow for easy access to widgets below) (dropdown.kv) (Dropdown.py)
#           CREATE DropDown2Item1 (A button that pulls up a today item list with all calendar events for that day) (dropdown.kv) (Dropdown.py)
#           CREATE DropDown2Item2 (A button that pulls up a next 7 days item list with all calendar events for the next 7 days) (dropdown.kv) (Dropdown.py)
#           CREATE DropDown2Item3 (A button that pulls up any calendar items) (dropdown.kv) (Dropdown.py)
#     CREATE TasksGrid (Within MainGrid, it will be in the center of screen, consists of scrollable widget) (main.kv) (main.py)
#       CREATE TodayList (Will pull data from calendar that is saved for that client and show all tasks for the day) (todaylist.kv) (Todaylist.py)
#       CREATE SevenDayList (Will pull data from calendar that is saved for that client and show all tasks for the next 7 days) (sevenday.kv) (Sevenday.py)
#       CREATE AllTimeList (Will contain all events from calendar for that client) (alltime.kv) (Alltime.py)
#     CREATE CalenderGrid (Within MainGrid, it will be right side of screen, consists of a Calendar and a scrollable widget) (main.kv) (main.py)
#       CREATE CalenderView (A user interactive calender that allows the user to see what they have going on for a certain day) (calendarview.kv) (Calendarview.py)
#       CREATE CalendarViewList (The list of items that are on that day) (calendarview.kv) (Calendarview.py)
# END MAIN

# LOOP
#   IF (__name__ == "__main__") THEN
#     MAIN().run()
#   ENDIF
# END LOOP
