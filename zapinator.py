"""Module for coming with zap baby"""

def zapinate(text, mood="happy"):
    """Function for zapinating a text.
    
    Arguments
    ---------
    text : str
        Text to be zapinated.
    mood : {"happy", "angry"}
        Mood of generic emoji.

    Returns
    -------
    zapinated_text : str
        Text after zapination, Unicode-encoded.     
    """
    return text

if __name__ == '__main__':
    # main function, for debugging. modify for release.
    text = "vem de zap, bebe"
    zapinated_text = zapinate(text)

    # save to simple html
    out_file = open("out.html", "w")
    out_file.write("<body>{}</body>".format(zapinated_text))