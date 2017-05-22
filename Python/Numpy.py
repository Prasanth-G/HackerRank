1.Arrays
import numpy
print(numpy.array(list(reversed( input().split() )), float))

2.Shape and Reshape
import numpy
print(numpy.reshape( numpy.array(input().split(), int), (3,3)))

3.Transpose and Flatten
import numpy
m,n = map(int, input().split())
mat = [input().split() for i in range(m)]
arr = numpy.array(mat, int)
print(numpy.transpose(arr), arr.flatten(), sep='\n')

4.Concatenate
import numpy
m, n, p = map(int, input().split())
mat_list = list(map(lambda x: [input().split() for i in range(x)], [m,n]))
print(numpy.concatenate(list(map(lambda x: numpy.array(x,int), mat_list))))

5.Zeros and Ones
import numpy
n = list(map(int, input().split()))
print(numpy.zeros(n, dtype=numpy.int))
print(numpy.ones(n, dtype=numpy.int))

6.Eye and Identity
import numpy
m, n = map(int, input().split())
print(numpy.eye(m,n,0))

7.Array Mathematics
import numpy
m, n = map(int, input().split())
A, B = map(lambda x: numpy.array(x,int),[[input().split() for i in range(m)] for i in range(2)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

8.Floor, ceil and Rint
import numpy
A = numpy.array(input().split(), float)
print(numpy.floor(A), numpy.ceil(A), numpy.rint(A), sep='\n')

9.Sum and Prod
import numpy
m, n = map(int, input().split())
l = numpy.array([input().split() for i in range(m)], int)
print(numpy.prod(numpy.sum(l,axis=0)))

10.Min and Max
import numpy
m, n = map(int, input().split())
l = numpy.array([input().split() for i in range(m)], int)
print(numpy.max(numpy.min(l, axis=1)))

11.Mean, var and std
import numpy
m, n = map(int, input().split())
l = numpy.array([input().split() for i in range(m)], int)
print(numpy.mean(l, axis=1))
print(numpy.var(l, axis=0))
print(numpy.std(l))

12.Dot and Cross
import numpy
n = int(input())
A, B = [numpy.array([input().split() for i in range(n)], int) for i in range(2)]
print(numpy.dot(A,B))

13.Inner and Outer
import numpy
A, B = [numpy.array(input().split(), int) for i in range(2)]
print(numpy.inner(A,B), numpy.outer(A,B), sep='\n')

14.Polynomials
import numpy
P = numpy.array(input().split(), float)
print(numpy.polyval(P, int(input())))

15.Linear Algebra
import numpy
A = numpy.array([input().split() for i in range(int(input()))], float)
print(numpy.linalg.det(A))