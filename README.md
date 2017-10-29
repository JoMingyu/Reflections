# Reflection
파이썬을 위한 리플렉션 라이브러리  
Way to list all the modules in a Python package

## How to use
### PyPI
~~~
pip install reflections
~~~
~~~
import reflections
import pkg_for_search

print(reflections.reflect(pkg_for_search, reflections.default_extractor))
~~~
reflections.reflect(target_pkg, extractor_func)

타겟 패키지와 reflections의 extractor 함수를 넘겨주면 됩니다. extractor 함수는 default, module, package가 있습니다.

리소스들은 튜플로 이루어진 리스트입니다. module과 package extractor의 경우 튜플은 (loader, module_name) 순으로, default extractor의 경우 튜플은 (loader, module_name, is_package) 순으로 이루어집니다.
