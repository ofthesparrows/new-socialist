import re

import markdown


class InterviewProcessorOld(markdown.blockprocessors.BlockProcessor):
    """Interview quote processor.
    
    ~A
    One paragraph here (left bar)
    
    Another paragraph here
    ~

    ~B>
    One paragraph here (right bar)
    
    Another paragraph here
    ~
    """
    #RE = re.compile(r'~(?P<author>[A-Z]{1,3})(?P<side>>?)\n(?P<')


INTERVIEW_RE = r'^~(?P<author>[A-Z]{1,3})(?P<number>[1-4]) '
class InterviewPattern(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        """
        ~A1 Text here (on the left, first colour)
        ~B2 Text here (on the left, second colour)
        ~C3 Text here (on the right, third colour)
        ~D4 Text here (on the right, fourth colour)
        """
        author = m.group('author')
        number = m.group('number')
        el = markdown.util.etree.Element('span')
        el_class = 'interview-quote author-' + number
        el.set('class', el_class)
        el.text = author
        return el


class InterviewExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['interview'] = InterviewPattern(INTERVIEW_RE, md)


def makeExtension(*args, **kwargs):
    return InterviewExtension(*args, **kwargs)
