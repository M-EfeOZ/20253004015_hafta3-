import functools

def say(func):
    """Fonksiyonun kaç kez çağrıldığını sayar."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        mevcut = getattr(wrapper, "cagri", 0)
        setattr(wrapper, "cagri", mevcut + 1)
        return func(*args, **kwargs)
    
    setattr(wrapper, "cagri", 0)
    return wrapper

def test_fib_sadece_say():
    @say
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    fib(20)
    assert getattr(fib, "cagri") == 21891

def test_fib_say_ustte_lru_altta():
    @say
    @functools.lru_cache(maxsize=None)
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    fib(20)
    assert getattr(fib, "cagri") == 39

def test_fib_lru_ustte_say_altta():
    @functools.lru_cache(maxsize=None)
    @say
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    fib(20)
    alt_fonksiyon = getattr(fib, "__wrapped__")
    assert getattr(alt_fonksiyon, "cagri") == 21