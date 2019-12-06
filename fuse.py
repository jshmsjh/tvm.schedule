import tvm

n = tvm.var("n")
A = tvm.placeholder((n), name='A')
k = tvm.reduce_axis((0, n), name='k')

B = tvm.compute((1,), lambda i: tvm.sum(A[k], axis=k), name='B')

s = tvm.create_schedule(B.op)

ko, ki = s[B].split(B.op.reduce_axis[0], factor=32)

print(tvm.lower(s, [A, B], simple_mode=True))
print("---------cutting line---------")

s[B].fuse(ko, ki)

print(tvm.lower(s, [A, B], simple_mode=True))
exit(0)