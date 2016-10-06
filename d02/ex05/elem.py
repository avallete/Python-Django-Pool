# -*- coding: utf-8 -*-


class Text(str):

    def __str__(self):
        return str.__str__(self).replace('\n', "\n<br />\n")


class Elem(object):

    def __init__(self, tag="div", attr={}, content=None, tag_type='double'):
        if not isinstance(content, (Text, Elem, list, None.__class__)):
            raise self.ValidationError()
        if isinstance(content, list):
            for node in content:
                if not isinstance(node, (Text, Elem)):
                    raise self.ValidationError()
        self.type = tag_type
        self.indent_level = 0
        self.content = [content] if not isinstance(content, list) else content
        self.attr = attr
        self.tag = tag


    def generate_attr_html(self):
        attr_string = ""
        for key, value in self.attr.items():
            attr_string += """ %s=\"%s\"""" % (key, str(value))
        return attr_string

    def set_indent_level(self, elem):
        if isinstance(elem, Elem):
            elem.indent_level += 1
        if elem.content[0] and isinstance(elem.content[0], Elem):
            elem.set_indent_level(elem.content[0])

    def generate_content_html(self):
        html_content = ""
        for elem in self.content:
            if isinstance(elem, Elem):
                self.set_indent_level(elem)
            if elem:
                html_content += "\n  %s%s" % ("  " * self.indent_level, str(elem))
        return html_content

    def get_tag(self, mode):
        if self.type != 'double':
            return "%s<%s%s />" % ("  " * (self.indent_level - 1), self.tag, self.generate_attr_html())
        if mode == 'open':
            return "<%s%s>" % (self.tag, self.generate_attr_html())
        else:
            if self.generate_content_html():
                return "\n%s</%s>" % ("  " * self.indent_level, self.tag)
            else:
                return "</%s>" % self.tag

    def __str__(self):
        content_string = self.generate_content_html()
        if self.type == 'double':
            return "%s%s%s" % (self.get_tag('open'), content_string, self.get_tag('close'))
        else:
            return "%s%s" % (self.get_tag('open'), content_string)

    def add_content(self, new_content):
        if isinstance(new_content, (Elem, Text)):
            self.content.append(new_content)
        else:
            raise self.ValidationError()


    class ValidationError(Exception):

        def __init__(self):
            Exception.__init__(self, "Error in Elem content validation.")
