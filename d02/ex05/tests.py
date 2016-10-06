# -*- coding: utf-8 -*-

from elem import Text
from elements import *

def old_test():
    assert (str(Html([
        Head(Title(Text("\"Hello ground!\""))),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})
        ])]))
    == """<html>
  <head>
    <title>
      "Hello ground!"
    </title>
  </head>
  <body>
    <h1>
      "Oh no, not again!"
    </h1>
    <img src="http://i.imgur.com/pfp3T.jpg" />
  </body>
</html>"""
            )
    print('Old Test : OK.')

def html_test():
    assert((str(Html())) == """<html></html>""")
    assert((str(Html(attr={'lang': 'en'}))) == """<html lang="en"></html>""")
    print("Html Test : OK.")


def test():
    html_test()
    old_test()


if __name__ == '__main__':
    try:
        test()
        print('Tests succeeded!')
    except AssertionError as e:
        traceback.print_exc()
        print(e)
        print('Tests failed!')
