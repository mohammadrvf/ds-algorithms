class Stack:
  def __init__(self,size):
    self.size=size;
    self.array=[0]*self.size;
    self.num = 0;
  def add_stack(self,value):
    if self.num >= self.size:
      print('stack is full');
      return;
    self.array[self.num] = value;
    self.num +=1;
  def pop_stack(self):
    if self.num <=0 :
      print('stack is empty');
      return None;
    self.num -=1;
    return self.array[self.num];
  def peek(self):
    if self.num <=0:
        print('stack is empty');
        return None;
    return self.array[self.num-1]
