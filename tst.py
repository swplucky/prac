Keep in mind
about
breaking
the
loop
--------------------------------------------------------------------------------
ar = [2, 3, 4, 5]


def sum(ar):
    for i in ar:
        print(i, end=" ")


if __name__ == '__main__':
    sum(ar)
'''
Describing comment for function
'''
--------------------------------------------------------------------------


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(word_count('the quick brown fox jumps over the lazy dog.'))

-------------------------------------------------------------------------------------
>> > chr(97)
'a'
>> > ord('a')
97

Char
list
to
string
''.join(list1)
.tostring

sequence[start:stop:step]
List1.remove()
List.Pop
List.extend
List.Sort(reverse=True)
Add
element
to
top
List1[:0] = [6]

split
strip is trim

import random

print(random.randint(1, 101))
-----------------------------------------------------------------------------------------------
Shbang  # !/usr/bin/env python3

If
__name__ == "__main__"
This
name if called as script
returns
main else module
name and doesn
't execute function called

__ is


class private instance


Global
keyword
to
change
value
of
global variable

Slicing
fetching
certain
elements
of
list
-------------------------------------------------------------------------------
https: // realpython.com / python - range /
-------------------------------------------------------------------------------
dictionary
https: // www.pythonforbeginners.com / dictionary / how - to - use - dictionaries - in -python /
for key in dict:
    val = dict[key]
    print("%s" % (val))
------------------------------------------------------------------------------
merge
sort
https: // www.youtube.com / watch?v = TzeBrDU - JaY
------------------------------------------------------------------------------


def findWater(arr, n):
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0] * n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0] * n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

        # Fill right array
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

        # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


-----------------------------------------------------------------------------------


def reverse(s):
    return s[::-1]


-----------------------------------------------------------------------------------


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        else:
            raise Exception("I am done %s" % "ok")

    def print_tree(self):
        if self.root is not None:
            self._print(self.root)

    def _print(self, node):
        if node is not None:
            self._print(node.left)
            print(node.value)
            self._print(node.right)


tree = BST()
tree.insert(2)
tree.print_tree()

BST
delete
node
https: // www.youtube.com / watch?v = Zaf8EOVa72I

-----------------------------------------------------------------------------------------------


class Node:
    def __init__(self, value=None):
        self.value = value
        self.neighbours = []
        self.visited = False


class BFS():
    def search(self, node, svalue):
        qu = []
        qu.append(node)
        node.visited = True

        while qu:
            thisNode = qu.pop(0)  # popping zero thats why its qu
            if thisNode.value == svalue:
                return thisNode
            print("node value: %s" % thisNode.value, end=" ")
            for n in thisNode.neighbours:
                if not n.visited:
                    n.visited = True
                    qu.append(n)


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')

n1.neighbours.append(n2)
n1.neighbours.append(n3)
n2.neighbours.append(n4)

print("found it %s" % BFS().search(n1, 'C').value)

--------------------------------------------------------------------------------


class Node:
    def __init__(self, value=None):
        self.value = value
        self.neighbours = []
        self.visited = False


class DFS:
    def search(self, node, svalue):
        node.visited = True
        print("value here is: %s" % node.value)
        if node.value == svalue:
            return node
        for n in node.neighbours:
            if not n.visited:
                n.visited = True
                self.search(n, svalue)


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')

n1.neighbours.append(n2)
n1.neighbours.append(n3)
n2.neighbours.append(n4)

print("found it %s" % DFS().search(n1, 'C').value)

------------------------------------------------------------------------


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    left = [arr[i] for i in range(l, m + 1)]
    right = [arr[j] for j in range(m + 1, r + 1)]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r - 1) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [5, 3, 6, 8, 9]
mergeSort(arr, 0, len(arr) - 1)

print(arr)
-----------------------------------------------------------------------------------------


def issubset(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n - 1] > sum:
        issubset(arr, n - 1, sum)
    return issubset(arr, n - 1, sum) or issubset(arr, n - 1, sum - arr[n - 1])


arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(issubset(arr, len(arr), sum))

------------------------------------------------------------------------------------------


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


subset_sum([9, 8, 4], 13)
------------------------------------------------------------------------------------------
Overlap
search -


class booking:
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, n):
        if self.root is None:
            self.root = n
        else:
            self._insert(n, self.root)

    def _insert(self, new, old):
        if new.fr < old.fr:
            if old.left is None:
                old.left = new
            else:
                self._insert(new, old.left)
        elif new.fr > old.fr:
            if old.right is None:
                old.right = new
            else:
                self._insert(new, old.right)
        else:
            return

    def doOverlap(self, x, y):
        if x is not None and y is not None:
            if y.fr <= x.to and x.fr <= y.to:
                return True
            return False

    def search(self, node, elem):
        if node is None:
            return
        if self.doOverlap(node, elem):
            return node
        return self.search(node.left, elem) or self.search(node.right, elem)


if __name__ == "__main__":
    t = BST()
    n1 = booking(1, 4)
    n2 = booking(5, 6)
    n3 = booking(6, 7)
    n4 = booking(5, 8)
    arr = [n1, n2, n3, n4]
    t.insert(n1)
    for i in range(1, len(arr)):
        x = t.search(t.root, arr[i])
        if x is not None:
            print("%s,%s -> %s,%s" % (arr[i].fr, arr[i].to, x.fr, x.to))
        t.insert(arr[i])

-----------------------------------------------------------------------------------------------
test_str = "GeeksforGeeks"
all_freq = {}

for i in test_str:

    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "

      - ----------------------------------------------------------------------------------------------


def isPalindrome(str):  # Run loop from 0 to len/2

    for i in range(0, len(str) / 2):
        if str[i] != str[len(str) - i - 1]:
            return False

    return True


-----------------------------------------------------------------------------------------------


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


-----------------------------------------------------------------------------------------------
https: // www.geeksforgeeks.org / find - k - bookings - possible - given - arrival - departure - times /
using
tuple
instead
of


class
    -----------------------------------------------------------------------------------------------


https: // www.geeksforgeeks.org / check - whether - an - array - is -subarray - of - another - array /
-----------------------------------------------------------------------------------------------
https: // www.geeksforgeeks.org / find - the - missing - number /

-----------------------------------------------------------------------------------------------

% python
import xml.etree.ElementTree as ET
from pyspark.sql.types import ArrayType, StringType
from pyspark.sql.functions import udf, col


def parseXml(xml):
    myroot = ET.fromstring(xml)
    result = []
    for x in myroot.findall('visitor'):
        visitor = []
        visitor.append(x.attrib['sex'])
        visitor.append(x.attrib['age'])
        visitor.append(x.attrib['id'])
        result.append(visitor)
    return result


parseUDF = udf(lambda z: parseXml(z), ArrayType(ArrayType(StringType())))

df = spark.read.json("/tmp/births-with-visitor-data.json")
parseDf = df.withColumn("parsedVisitor", parseUDF(col("visitors"))).selectExpr("sid",
                                                                               "explode(parsedVisitor) as Visitor_Dimension").selectExpr(
    "sid", "Visitor_Dimension[0] as sex", "Visitor_Dimension[1] as age", "Visitor_Dimension[2] as id")
parseDf.createOrReplaceTempView("Vistor_Dimension")
display(parseDf)

-------------------------------------------------------------------------------------------------
https: // www.geeksforgeeks.org / sum - n - digit - numbers - divisible - given - number /

Two
digit
numbers
max = 10 * (M - 1)
------------------------------------------------------------------------------------------------









