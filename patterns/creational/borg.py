"""
*What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.

-----说明-----
Monostate pattern 单一状态模式
实现单例的行为，和只拥有一个类的实例不同
Borg模式拥有多个实例但是共享一个状态



*What does this example do?
To understand the implementation of this pattern in Python, it is
important to know that, in Python, instance attributes are stored in a
attribute dictionary called __dict__. Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.
In this example, the __shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
__shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is __shared_state), all other
attributes will also be shared.

-----说明-----
python中，实例属性都存储在__dict__中
通常每个实例都有自己的__dict__
Borg模式做了修改，使所有实例共享__dict__


*Where is the pattern used practically?
Sharing state is useful in applications like managing database connections:
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

-----说明-----
共享属性 在管理数据库连接方便有用

*References:
- https://fkromer.github.io/python-pattern-references/design/#singleton
- https://learning.oreilly.com/library/view/python-cookbook/0596001673/ch05s23.html
- http://www.aleax.it/5ep.html

*TL;DR
Provides singleton-like behavior sharing state between instances.
"""


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


def main():
    """
    >>> rm1 = YourBorg()
    >>> rm2 = YourBorg()

    >>> rm1.state = 'Idle'
    >>> rm2.state = 'Running'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Running
    >>> print('rm2: {0}'.format(rm2))
    rm2: Running

    # When the `state` attribute is modified from instance `rm2`,
    # the value of `state` in instance `rm1` also changes
    >>> rm2.state = 'Zombie'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie

    # Even though `rm1` and `rm2` share attributes, the instances are not the same
    >>> rm1 is rm2
    False

    # New instances also get the same shared state
    >>> rm3 = YourBorg()

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie
    >>> print('rm3: {0}'.format(rm3))
    rm3: Zombie

    # A new instance can explicitly change the state during creation
    >>> rm4 = YourBorg('Running')

    >>> print('rm4: {0}'.format(rm4))
    rm4: Running

    # Existing instances reflect that change as well
    >>> print('rm3: {0}'.format(rm3))
    rm3: Running
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
