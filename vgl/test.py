def int_to_star(score):
    html_tag = ""

    filled_star = '<span class="glyphicon glyphicon-star" aria-hidden="true" ></span>'
    empty_star = '<span class="glyphicon glyphicon-star-empty" aria-hidden="true" ></span>'

    if score == 1:
        filled_no = 1
        empty_no = 4

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 2:
        filled_no = 2
        empty_no = 3

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 3:
        filled_no = 3
        empty_no = 2

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 4:
        filled_no = 4
        empty_no = 1

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 5:
        filled_no = 5
        empty_no = 0

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no

    return html_tag

print int_to_star(5)