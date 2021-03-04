#!/usr/bin/env python3

import calendar
from jinja2 import Environment

template_str="""
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Calendar</title>
<script type = "text/javascript" src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js">
</script>
<script type = "text/javascript">
$(document).ready(function() {
food='&#x1F374;'
water='&#x224b;'
litterbox='<img src="shovel.svg" height="12"/>'
medicine='&#9877;'

addendum = '<br>'
addendum += food
addendum += water
addendum += litterbox
addendum += medicine
$("td.mon").append(addendum)
$("td.tue").append(addendum)
$("td.wed").append(addendum)
$("td.thu").append(addendum)
$("td.fri").append(addendum)
$("td.sat").append(addendum)
$("td.sun").append(addendum)
});
</script>
</head>

<style>
table, th, td {
  border: 1px solid black;
  padding: 10px;
}
</style>
<body>

{% for year, month in months %}
{{ calendar.formatmonth(year, month) }}
{% endfor %}

<br>&#x1F374; = food
<br>&#x224b; = water
<br><img src="shovel.svg" height="12"/> = litterbox
<br>&#9877; = medicine

</body>
</html>
"""

env = Environment()
template = env.from_string(template_str)

c=calendar.HTMLCalendar(calendar.SUNDAY)
print(template.render(
    calendar = c,
    months = [ (2021, 3) ]))
