该脚本仅用于口碑项目（或其他按需）。

更新步骤：
1/首先cd到该文件夹；
2/删除build、dist和egg-info文件
3/改变setup.py文件中的description及version，根据改动的大小来修改version号
3/更新使用：python setup.py sdist build
4/提交：twine upload dist/*
5/更新库：pip install --upgrade general_calculator_zsd -i https://pypi.python.org/simple

username:__token__
password:pypi-AgEIcHlwaS5vcmcCJGE1NzI3YTUxLTg5YTAtNDY2Yi04MmYzLTA5NDAwZWMxZjViNQACKlszLCIyY2FjYTU2Ni03YWEzLTRmYTctYTQ1OC05YTlmYzdiYzJjYTIiXQAABiBKp6N-jOHCYfxFYFu6WRdyGQEYDgXHk15B3zVVnsTXVw