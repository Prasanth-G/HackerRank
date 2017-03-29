######XML 1- Find te Score
'''
Input (stdin)
11
<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>
Expected Output
8
'''
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    return len_child(root,node,len(node.attrib))

def len_child(root,node,s):
    if not len(list(node)):
        if root == node:
            return s
        return s+len(node.attrib)
    else:
        for child in node:
            s = len_child(root,child,s)
        return s

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

######2.XML2 - Find the Maximum Depth
'''
Input (stdin)
11
<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>
Expected Output
2
'''
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level = level + 1
    if not len(list(elem)):
        if level > maxdepth:
            maxdepth = level
    else:
        for child in elem:
            depth(child,level)
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
