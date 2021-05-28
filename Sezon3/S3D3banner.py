def banner_text(text,screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text,screen_width))
    
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)

banner_text("*",60)
banner_text("Heyyo Heyyo Heyyo Heyyo Heyyo Heyyo",60)
banner_text("Hello my friendo",60)
banner_text("asterix",60)
banner_text("*",60)