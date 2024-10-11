def add():
  b = 10
  
  def add_inner(x):
    return b + x
  
  return add_inner

f = add()
print(f(2))