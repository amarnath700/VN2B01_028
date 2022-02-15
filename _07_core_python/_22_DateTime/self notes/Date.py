"""
Python Dates
A date in Python is not a data type of its own,
but we can import a module named datetime to work with dates as date objects.
"""
import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

"""
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.
"""

x = datetime.datetime(2022, 2, 12)
print(x)

"""
Directive	Description	Example	Try it
%a	Weekday, short version	:Wed	
%A	Weekday, full version	:Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	:3	
%d	Day of month 01-31	:31	
%b	Month name, short version:	Dec	
%B	Month name, full version:	December	
%m	Month as a number 01-12	:12	
%y	Year, short version, without century	:18	
%Y	Year, full version	:2018	
%H	Hour 00-23	:17	
%I	Hour 00-12	:05	
%p	AM/PM	:PM	
%M	Minute 00-59	:41	
%S	Second 00-59	:08	
%f	Microsecond 000000-999999	:548513	
%z	UTC offset	:+0100	
%Z	Timezone	:CST	
%j	Day number of year 001-366	:365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	:Mon Dec 31 17:41:00 2018	
%C	Century	:20	
%x	Local version of date	:12/31/18	
%X	Local version of time	:17:41:00	
%%	A % character	:%	
%G	ISO 8601 year	:2018	
%u	ISO 8601 weekday (1-7):	1	
%V	ISO 8601 week number (01-53):	01	

"""

x = datetime.datetime.now()
print(x)
print("%a shows name of day shortcut: ", x.strftime("%a"))
print("%a shows name of day :", x.strftime("%A"))
print("%w shows week day no.(0-6) :", x.strftime("%w"))
print("%W shows week day no.(00-06) :", x.strftime("%W"))
print("%d shows month day no.(0-31) :", x.strftime("%d"))
print("%b shows month name :", x.strftime("%b"))
print("%B shows month fullname :", x.strftime("%B"))
print("%m shows month no.(00-12) :", x.strftime("%m"))
print("%y shows year shortcut :", x.strftime("%y"))
print("%W shows full Year :", x.strftime("%Y"))
print("%H shows hours(0-24) :", x.strftime("%H"))
print("%I shows hours(0-12) :", x.strftime("%I"))
print("%p shows hours(AM-PM) :", x.strftime("%p"))
print("%M shows minute(00-59) :", x.strftime("%M"))
print("%S shows Second(00-59) :", x.strftime("%S"))
print("%f shows Microseconds(000000-999999) :", x.strftime("%f"))
print("%z shows UTC offset :", x.strftime("%z"))
print("%Z shows TimeZone :", x.strftime("%Z"))
print("%j shows year days(0-366) :", x.strftime("%j"))
print("%U Week number of year, Sunday as the first day of week, 00-53 :", x.strftime("%U"))
print("%W Week number of year, Sunday as the first day of week, 00-53 :", x.strftime("%W"))


